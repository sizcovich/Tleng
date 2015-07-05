from lexer_rules import tokens, figures_inv
from expressions import *
from parser_exceptions import SemanticException

def p_song_declaration(subexpressions):
    'song_declaration : tempo time_signature const_dict voice_list'
    subexpressions[0] = Song(subexpressions[1], subexpressions[2], subexpressions[3], subexpressions[4])

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

def p_const_dict_empty(subexpressions):
    'const_dict :'
    subexpressions[0] = {}

def p_const_dict_append(subexpressions):
    'const_dict : CONST CONST_ID EQUALS NUM SEMICOLON const_dict'
    id_token = subexpressions[2]
    num_token = subexpressions[4]
    sub_const_dict = subexpressions[6]
    
    if id_token in sub_const_dict:
        raise SemanticException("Se intento declarar la constante " + id_token + " mas de una vez.")
    
    sub_const_dict[id_token] = num_token
    
    subexpressions[0] = sub_const_dict

def p_voice_list_empty(subexpressions):
    'voice_list :'
    subexpressions[0] = []

def p_voice_list_append(subexpressions):
    'voice_list : VOICE LPAREN num_or_const_id RPAREN LBRACE voice RBRACE voice_list'
    voice_num = subexpressions[3]
    voice = subexpressions[6]
    sub_voice_list = subexpressions[8]
    
    if len(sub_voice_list) == 16:
        raise SemanticException("No se pueden declarar mas de 16 voces.")
    
    sub_voice_list.append(Voice(voice_num, voice))
    
    subexpressions[0] = sub_voice_list
    
def p_num_or_const_id_from_num(subexpressions):
    'num_or_const_id : NUM'
    subexpressions[0] = NumOrConstantFromNum(subexpressions[1])

def p_num_or_const_id_from_const_id(subexpressions):
    'num_or_const_id : CONST_ID'
    subexpressions[0] = NumOrConstantFromConstant(subexpressions[1])

def p_voice(subexpressions):
    'voice : '
    subexpressions[0] = "CONTENIDO VOZ"

    
def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
