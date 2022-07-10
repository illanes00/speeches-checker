from tabnanny import verbose
import requests
import const
from requests.exceptions import HTTPError
from classes import Speech
from bs4 import BeautifulSoup
import threading
import time




def download_speech(id):
    try:
        url = const.SPEECHES_URL.format(id)
        reply = requests.get(url)
        reply.encoding = "UTF-8"
        if reply.status_code == 200:
            return reply.text
        return None

    except HTTPError as http_err:
        print(f'[ERROR HTTP]: {http_err}')

    except Exception as err:
        print(f'[ERROR]: {err}')


def get_speech(id):

    speech_html = download_speech(id)

    if speech_html is None:
        return None

    speech_lxml = BeautifulSoup(speech_html, 'lxml')

    title = speech_lxml.find(id="main_ltTitulo").string.strip()
    title = title.replace(',', '')
    
    text = speech_lxml.find(id="main_ltContenido").getText()
    
    if text is None or text == '':
        return None
    
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace(';', '')
    text = text.replace('\n', '')
    text_r = repr(text)
    text = text_r.replace("\\r\\xa0\\r", " ")
    
    #text = text_r.replace(r"\r\xa0", "")
    #text = text_r.replace(r"\r", " ")
    text = text.lower()
    text = text[:-7]
    text = text.replace("'", '')
    text = text.replace("\"", '')
    
    
    date = speech_lxml.find(id="main_ltFEcha").string.strip()
    date = date.split(" ")
    date = ";".join(date)

    url = const.SPEECHES_URL.format(id)

    speech = Speech(id, title, date, url, text)
    return speech


def save_speeches(file, speech_list):

    with open(file, 'w', encoding="UTF-8") as f:
        for speech in speech_list:
            f.write(speech.to_csv())


if __name__ == "__main__":

    
    speeches = []
    threads = []
    
    for id in range(71541, const.LAST_SPEECH_ID + 1):
        t = threading.Thread(target=get_speech, args=(id,))
        t.daemon = True
        threads.append(t)
        print(f"[INFO]: Appending Thread N°{id}")

    n_thread = 0
    for t in threads:
        t.start()
        time.sleep(0.5)
        print(f"[INFO]: Starting Thread N°{n_thread}")
        n_thread += 1

    count = 0
    for t in threads:
        count += 1
        print(f"[INFO]: Getting speech N°{count}")
        speech = t.join()
        if speech is not None:
            speeches.append(speech)
            print(f"[INFO]: Speech N°{count} downloaded")
                
    save_speeches(const.SPEECHES_FILE, speeches)