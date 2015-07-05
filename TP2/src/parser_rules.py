from lexer_rules import tokens, figures_inv
from expressions import *

class SemanticException(Exception):
    pass

def p_song_declaration(subexpressions):
    'song_declaration : tempo time_signature const_list'
    subexpressions[0] = Song(subexpressions[1], subexpressions[2], subexpressions[3])

def p_tempo(subexpressions):
    'tempo : NUMERAL TEMPO FIG NUM'
    figure_token = subexpressions[3]
    per_minute_token = subexpressions[4]

    if per_minute_token < 1:
        raise SemanticException("El valor del tempo debe ser mayor a cero.")
        
    subexpressions[0] = Tempo(figure_token, per_minute_token)

def p_time_signature(subexpressions):
    'time_signature : NUMERAL BAR NUM SLASH NUM'
    num_beats_token = subexpressions[3]
    beat_length_token = subexpressions[5]

    if num_beats_token < 1:
        raise SemanticException("El nominador de la indicacion de compas debe ser mayor a cero.")
    
    if beat_length_token not in figures_inv:
        raise SemanticException("El denominador de la indicacion de compas debe indicar una figura valida.")
        
    subexpressions[0] = TimeSignature(num_beats_token, beat_length_token)

def p_const_list_empty(subexpressions):
    'const_list :'
    subexpressions[0] = {}

def p_const_list_append(subexpressions):
    'const_list : CONST CONST_ID EQUALS NUM SEMICOLON const_list'
    id_token = subexpressions[2]
    num_token = subexpressions[4]
    sub_const_list = subexpressions[6]
    
    if id_token in sub_const_list:
        raise SemanticException("Se intento declarar la constante " + id_token + " mas de una vez .")
    
    sub_const_list[id_token] = num_token
    
    subexpressions[0] = sub_const_list
    
def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
