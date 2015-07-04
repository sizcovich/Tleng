tokens = [
   'TEMPO',
   'BAR',
   'VOICE',
   'REPEAT',
   'NOTE',
   'ALTERATION',
   'SILENCE',
   'FIGURE',
   'TONE',
   'NUMBER',   
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

figures = set(['redonda', 'blanca', 'negra', 'corchea', 'semicorchea', 'fusa', 'semifusa'])
tones = set(['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do+', 're+', 'fa+', 'sol+', 'la+', 're-', 'mi-', 'sol-', 'la-', 'si-'])

def t_NUMBER(token):
    r"[0-9][0-9]*"
    token.value = int(token.value)
    return token
   
def t_CONST_ID(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*"
    if token.value == 'tempo':
        token.type = 'TEMPO'
    elif token.value in figures:
        token.type = 'FIGURE'
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
   
def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

t_ALTERATION = r"\+|\-"  

t_NUMERAL = r"\#"
t_SLASH = r"/"
t_EQUALS = r"="
t_SEMICOLON = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","

t_ignore_comments = r"//(.*?)\r?\n"
t_ignore = " \t"

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
