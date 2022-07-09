class Speech:
    
    def __init__(self, ID, title, date, url, text):
        self.ID = ID
        self.title = title
        self.date = date
        self.url = url
        self.text = text
        
    def __str__(self):
        return f"{self.url}\nID:{self.ID} - {self.title}\n{self.date}\n{self.text}"
    
    def to_csv(self):
        return f"{self.url},{self.ID},{self.title},{self.date},{self.text}\n"