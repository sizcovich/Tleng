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
   'COMMA'
]

figures = { 'redonda' : 1, 'blanca' : 2, 'negra' : 4, 'corchea' : 8, 'semicorchea' : 16, 'fusa' : 32, 'semifusa' : 64 }
figures_inv = { v: k for k, v in figures.items() }
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
        raise Exception(token.value + "no es una altura reconocida.")

def t_CONST_ID(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*"
    if token.value == 'tempo':
        token.type = 'TEMPO'
    elif token.value in figures:
        token.type = 'FIG'
        token.value = figures[token.value]
    elif token.value in tones:
        token.type = 'TONE'
    elif token.value == 'compas':
        token.type = 'BAR'
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
    raise Exception(message)
