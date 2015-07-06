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

figures = set(['redonda.', 'redonda', 'blanca.', 'blanca', 'negra.', 'negra', 'corchea.', 'corchea', 'semicorchea.', 'semicorchea', 'fusa.', 'fusa', 'semifusa.', 'semifusa' ])
tones = set(['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do+', 're+', 'fa+', 'sol+', 'la+', 're-', 'mi-', 'sol-', 'la-', 'si-'])

def t_NUM(token):
    r"[0-9][0-9]*"
    token.value = int(token.value)
    return token

def t_TONE_WITH_ALTERATION(token):
    r"[a-z][a-z]*(\+|\-)"
    if token.value in tones:
        token.type = 'TONE'
        return token
    else:
        t_error(token)

def t_FIG_WITH_DOT(token):
    r"[a-z][a-z]*(\.)"
    if token.value in figures:
        token.type = 'FIG'
        token.value = token.value
        return token
    else:    
        t_error(token)

def t_CONST_ID(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*"
    if token.value == 'tempo':
        token.type = 'TEMPO'
    elif token.value in figures:
        token.type = 'FIG'
        token.value = token.value
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
    message = "Fin inesperado de archivo."
    if token is not None:
        # Sacado de la doc de PLY como obtener la columna
        input = token.lexer.lexdata
        last_cr = input.rfind('\n', 0, token.lexpos)
        if last_cr < 0:
            last_cr = 0    
        col = token.lexpos - last_cr
        message = "Valor no esperado: \"{0}\". Linea: {1}. Posicion: {2}.".format(token.value, token.lineno, col)
    raise SyntacticException(message)