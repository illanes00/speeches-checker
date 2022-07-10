import re

TITLE_PATTERN = "<span id=.main_ltTitulo.>!text</span>"

def get_title(text):
    rgx = re.compile(TITLE_PATTERN)
    matches = []
    for match in rgx.finditer(text):
        matches.append(match.group('text'))
    return matches
