from parser_exceptions import SyntacticException

tokens = [
   'TEMPO',
   'BAR',
   'VOICE',
   'REPEAT',
   'NOTE',
   'SILENCE',
   'FIG',
   'TONE',
   'NUM',   
   'CONST',
   'CONST_ID',
   'NUMERAL',
   'SLASH',
   'EQUALS',
   'SEMICOLON',
   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'COMMA',
]

# relativizo la duracion de las figuras a la negra, por costumbre
figures = { 'redonda.' : 6, 'redonda' : 4., 'blanca.' : 3., 'blanca' : 2., 'negra.' : 1.5, 'negra' : 1., 'corchea.' : 0.75, 'corchea' : 0.5, 'semicorchea.' : 0.375, 'semicorchea' : 0.25, 'fusa.' : 0.1875, 'fusa' : 0.125, 'semifusa.' : 0.09375, 'semifusa' : 0.0625 }
tones = set(['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do+', 're+', 'fa+', 'sol+', 'la+', 're-', 'mi-', 'sol-', 'la-', 'si-'])

def t_NUM(token):
    r"[0-9][0-9]*"
    token.value = int(token.value)
    return token

def t_TONE_WITH_ALTERATION(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*(\+|\-)"
    if token.value in tones:
        token.type = 'TONE'
        return token
    else:
        t_error(token)

def t_FIG_WITH_DOT(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*(\.)"
    if token.value in figures:
        token.type = 'FIG'
        token.value = Figure(figures[token.value])
        return token
    else:    
        t_error(token)

def t_CONST_ID(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*"
    if token.value == 'tempo':
        token.type = 'TEMPO'
    elif token.value in figures:
        token.type = 'FIG'
        token.value = Figure(figures[token.value])
    elif token.value in tones:
        token.type = 'TONE'
    elif token.value == 'compas':
        token.type = 'BAR'
    elif token.value == 'voz':
        token.type = 'VOICE'
    elif token.value == 'repetir':
        token.type = 'REPEAT'
    elif token.value == 'const':
        token.type = 'CONST'
    elif token.value == 'nota':
        token.type = 'NOTE'
    elif token.value == 'silencio':
        token.type = 'SILENCE'

    return token

def t_IGNORE_COMMENTS(token):
    r"//(.*?)\r?\n"
    token.lexer.lineno += 1
    
def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

t_NUMERAL = r"\#"
t_SLASH = r"/"
t_EQUALS = r"="
t_SEMICOLON = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","


t_ignore = " \t"

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise SyntacticException(message)
