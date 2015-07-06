from lexer_rules import tokens
from parser_exceptions import *
from expressions import *

constants = None
time_signature = None

def p_song_declaration(subexpressions):
    'song_declaration : tempo time_signature const_dict voice_list'
    subexpressions[0] = Song(subexpressions[1], subexpressions[2], subexpressions[4])

def p_tempo(subexpressions):
    'tempo : NUMERAL TEMPO FIG NUM'
    subexpressions[0] = Tempo(Figure(subexpressions[3]), subexpressions[4], subexpressions.lineno(1))

def p_time_signature(subexpressions):
    'time_signature : NUMERAL BAR NUM SLASH NUM'
    global time_signature
    time_signature = TimeSignature(subexpressions[3], subexpressions[5], subexpressions.lineno(1))    
    subexpressions[0] = time_signature

def p_const_dict_empty(subexpressions):
    'const_dict :'
    global constants
    constants = {}

def p_const_dict_append(subexpressions):
    'const_dict : CONST CONST_ID EQUALS NUM SEMICOLON const_dict'
    id_token = subexpressions[2]
    num_token = subexpressions[4]
    
    if id_token in constants:        
        raise SemanticException("Se intento declarar la constante \"{0}\" mas de una vez. Linea: {1}.".format(id_token, subexpressions.lineno(1)))
    
    constants[id_token] = num_token

def p_voice_list_empty(subexpressions):
    'voice_list :'
    subexpressions[0] = []

def p_voice_list_append(subexpressions):
    'voice_list : VOICE LPAREN num_or_const_id RPAREN LBRACE voice_content RBRACE voice_list'
    subexpressions[0] = [ Voice(subexpressions[3], subexpressions[6], subexpressions.lineno(1)) ] + subexpressions[8]

def p_num_or_const_id_from_num(subexpressions):
    'num_or_const_id : NUM'
    subexpressions[0] = subexpressions[1]

def p_num_or_const_id_from_const_id(subexpressions):
    'num_or_const_id : CONST_ID'
    const_id = subexpressions[1]

    if const_id not in constants:
        raise SemanticException("Se intento usar la constante \"{0}\" que no fue declarada. Linea: {1}.".format(const_id, subexpressions.lineno(1)))
            
    subexpressions[0] = constants[const_id]

def p_voice_content_non_empty(subexpressions):
    'voice_content : bar_or_repeat'
    subexpressions[0] = subexpressions[1]

def p_voice_content_list(subexpressions):
    'voice_content : voice_content voice_content'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_bar_or_repeat_from_bar(subexpressions):
    'bar_or_repeat : BAR LBRACE bar_content RBRACE'
    bar = Bar(subexpressions[3], subexpressions.lineno(1))
    
    if bar.relative_length() != time_signature.relative_length():
        raise SemanticException("Un compas debe durar lo que se indico en el encabezado. Linea: {0}.".format(subexpressions.lineno(1)))
    
    subexpressions[0] = [ bar ]
    
def p_bar_or_repeat_from_repeat(subexpressions):
    'bar_or_repeat : REPEAT LPAREN num_or_const_id RPAREN LBRACE voice_content RBRACE'
    
    repetitions = subexpressions[3]
        
    if repetitions < 2:
        raise SemanticException("El valor de una repeticion debe ser al menos 2. Linea: {0}.".format(subexpressions.lineno(1)))
    
    subexpressions[0] = subexpressions[6] * repetitions

def p_bar_content_from_note(subexpressions):
    'bar_content : NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON'
    octave_value = subexpressions[5]
        
    subexpressions[0] = [ Note(subexpressions[3], octave_value, Figure(subexpressions[7]), subexpressions.lineno(1)) ]

def p_bar_content_from_silence(subexpressions):
    'bar_content : SILENCE LPAREN FIG RPAREN SEMICOLON'
    subexpressions[0] = [ Silence(Figure(subexpressions[3]), subexpressions.lineno(1)) ]

def p_bar_content_list(subexpressions):
    'bar_content : bar_content bar_content'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_error(token):
    message = "Valor no esperado: \"{0}\". Linea: {1}. Posicion: {2}.".format(token.value, token.lineno, token.lexpos)    
    raise SyntacticException(message)