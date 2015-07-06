from lexer_rules import tokens, figures_inv
from expressions import *
from parser_exceptions import SemanticException

constants = {}
time_signature = None

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
    
    time_signature = TimeSignature(num_beats_token, beat_length_token)   
    subexpressions[0] = time_signature

def p_const_dict_empty(subexpressions):
    'const_dict :'
    constants = {}
    subexpressions[0] = {}

def p_const_dict_append(subexpressions):
    'const_dict : CONST CONST_ID EQUALS NUM SEMICOLON const_dict'
    id_token = subexpressions[2]
    num_token = subexpressions[4]
       
    if id_token in constants:
        raise SemanticException("Se intento declarar la constante " + id_token + " mas de una vez.")
    
    constants[id_token] = num_token

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
    
    sub_voice_list.append(VoiceHeader(voice_num, voice))
    
    subexpressions[0] = sub_voice_list
    
def p_num_or_const_id_from_num(subexpressions):
    'num_or_const_id : NUM'
    subexpressions[0] = subexpressions[1]

def p_num_or_const_id_from_const_id(subexpressions):
    'num_or_const_id : CONST_ID'
    const_id = subexpressions[1]
    if const_id not in constants:
        raise SemanticException("Uso de constante no declarada. Valor: " + const_id + ". Linea: " + subexpressions.lineno(1) + ". ")
            
    subexpressions[0] = constants[const_id]

def p_voice_non_empty(subexpressions):
    'voice : bar_or_repeat'
    subexpressions[0] = subexpressions[1]

def p_voice_list(subexpressions):
    'voice : voice voice'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_bar_or_repeat_from_bar(subexpressions):
    'bar_or_repeat: BAR LBRACE bar_content RBRACE'
    subexpressions[0] = Bar(subexpressions[3])
    
def p_bar_content_from_note(subexpressions):
    'bar_content : NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON'
    octave_value = subexpressions[5]    
    if octave_value < 1 or octave_value > 9
        raise SemanticException("La octava de una nota debe estar entre 1 y 9. Valor: " + octave_value + ". Linea: " + subexpressions.lineno(5) + ". ")
    
    subexpressions[0] = [ Note(subexpressions[3], octave_value, subexpressions[7]) ]

def p_bar_content_from_silence(subexpressions):
    'bar_content : SILENCE LPAREN FIG RPAREN SEMICOLON'
    subexpressions[0] = [ Silence(subexpressions[3]) ]

def p_bar_content_list(subexpressions):
    'bar_content : bar_content bar_content'
    subexpressions[0] = subexpressions[1] + subexpressions[2]
    
def p_error(token):
    message = "[Syntax error]"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
