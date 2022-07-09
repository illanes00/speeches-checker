import re

TITLE_PATTERN = "<span id=.main_ltTitulo.>!text</span>"

PATRON_1 = "^(# )!texto{[^\n]+}($|\n)"
PATRON_2 = "##(#)? !texto{[^\n]+}($|\n)"
PATRON_3 = "<img src='!texto{[^\n ]+}' alt>"
PATRON_4 = "```!texto{[^\n ]+}\n!codigo{[^`]+}```"
PATRON_5 = "\* \[[Xx]\] !texto{[^\n]+}($|\n)"
PATRON_6 = "(^|\n)!texto{[^\n]*\[[^\n]+\]\(!link{[^\n ]+}\)[^\n]*}($|\n)"

# CONSULTA 1
def get_title(text):
    rgx = re.compile(TITLE_PATTERN)
    matches = []
    for match in rgx.finditer(text):
        matches.append(match.group('text'))
    return matches

# CONSULTA 2
def consulta_2(texto, patron):
    rgx = re.compile(patron)
    listado = []
    for match in rgx.finditer(texto):
        diccionario = {"contenido": match.group('texto'),
                       "posicion": match.span('texto')
                       }
        listado.append(diccionario)
    return listado


# CONSULTA 3
def consulta_3(texto, patron):
    rgx = re.compile(patron)
    listado = []
    for match in rgx.finditer(texto):
        diccionario = {"contenido": match.group('texto'),
                       "posicion": match.span('texto')
                       }
        listado.append(diccionario)
    return listado


# CONSULTA 4
def consulta_4(texto, patron):
    rgx = re.compile(patron)
    listado = []
    for match in rgx.finditer(texto):
        diccionario = {"contenido": match.group('texto'),
                       "posicion": match.span('codigo')
                       }
        listado.append(diccionario)
    return listado


# CONSULTA 5
def consulta_5(texto, patron):
    rgx = re.compile(patron)
    listado = []
    for match in rgx.finditer(texto):
        diccionario = {"contenido": match.group('texto'),
                       "posicion": match.span('texto')
                       }
        listado.append(diccionario)
    return listado


# CONSULTA 6
def consulta_6(texto, patron):
    rgx = re.compile(patron)
    listado = []
    for match in rgx.finditer(texto):
        diccionario = {"contenido": match.group('texto'),
                       "posicion": match.span('link')
                       }
        listado.append(diccionario)
    return listado