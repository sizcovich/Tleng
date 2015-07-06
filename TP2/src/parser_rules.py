from lexer_rules import tokens
from parser_exceptions import *
from expressions import *

constants = None

def p_song_declaration(subexpressions):
    'song_declaration : tempo time_signature const_dict voice_list'
    subexpressions[0] = Song(subexpressions[1], subexpressions[2], subexpressions[4])

def p_tempo(subexpressions):
    'tempo : NUMERAL TEMPO FIG NUM'
    subexpressions[0] = Tempo(Figure(subexpressions[3], subexpressions.lineno(1)), subexpressions[4], subexpressions.lineno(1))

def p_time_signature(subexpressions):
    'time_signature : NUMERAL BAR NUM SLASH NUM'
    subexpressions[0] = TimeSignature(subexpressions[3], subexpressions[5], subexpressions.lineno(1))    

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
    subexpressions[0] = [ subexpressions[1] ]

def p_voice_content_append(subexpressions):
    'voice_content : bar_or_repeat voice_content'
    subexpressions[0] = [ subexpressions[1] ] + subexpressions[2]
    
def p_bar_or_repeat_from_bar(subexpressions):
    'bar_or_repeat : BAR LBRACE bar_content RBRACE'
    subexpressions[0] = Bar(subexpressions[3], subexpressions.lineno(1))
    
def p_bar_or_repeat_from_repeat(subexpressions):
    'bar_or_repeat : REPEAT LPAREN num_or_const_id RPAREN LBRACE voice_content RBRACE'
    subexpressions[0] = Repeat(subexpressions[3], subexpressions[6], subexpressions.lineno(1))

def p_bar_content_from_note(subexpressions):
    'bar_content : NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON'
    subexpressions[0] = [ Note(subexpressions[3], subexpressions[5], Figure(subexpressions[7], subexpressions.lineno(1)), subexpressions.lineno(1)) ]

def p_bar_content_from_silence(subexpressions):
    'bar_content : SILENCE LPAREN FIG RPAREN SEMICOLON'
    subexpressions[0] = [ Silence(Figure(subexpressions[3], subexpressions.lineno(1)), subexpressions.lineno(1)) ]

def p_bar_content_append_note(subexpressions):
    'bar_content : NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON bar_content'
    subexpressions[0] = [ Note(subexpressions[3], subexpressions[5], Figure(subexpressions[7], subexpressions.lineno(1)), subexpressions.lineno(1)) ] + subexpressions[10]

def p_bar_content_append_silence(subexpressions):
    'bar_content : SILENCE LPAREN FIG RPAREN SEMICOLON bar_content'
    subexpressions[0] = [ Silence(Figure(subexpressions[3], subexpressions.lineno(1)), subexpressions.lineno(1)) ] + subexpressions[6]    
    
def p_error(token):
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