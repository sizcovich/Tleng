from lexer_rules import figures_inv
from parser_exceptions import SemanticException, ProgrammingException

class Song(object):
    def __init__(self, tempo, time_signature, constants, voices):
        self.tempo = tempo
        self.time_signature = time_signature
        self.constants = constants
        self.voices = voices
        
        for voice in voices:
            voice.set_constants(constants)
        
    def name(self):
        return "Song"

    def children(self):
        return [self.tempo, self.time_signature] + [Const(k, v) for k,v in self.constants.items()] + self.voices

class Tempo(object):
    def __init__(self, figure, per_minute):
        self.figure = figure
        self.per_minute = per_minute;

    def name(self):
        return "Tempo: " + figures_inv[self.figure] + " " + str(self.per_minute)

    def children(self):
        return []

class TimeSignature(object):
    def __init__(self, figure, per_minute):
        self.figure = figure
        self.per_minute = per_minute;

    def name(self):
        return "TimeSignature: " + figures_inv[self.figure] + " " + str(self.per_minute)

    def children(self):
        return []

class Const(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value;

    def name(self):
        return "const " + self.key + " = " + str(self.value)

    def children(self):
        return []

class NumOrConstantFromNum(object):
    def __init__(self, num):        
        self.value = num;

    def set_constants(self, constants_dict):
        pass

    def get_value(self):
        return self.value

    def name(self):
        return "num " str(self.value)

    def children(self):
        return []
        
class NumOrConstantFromConstant(object):
    def __init__(self, constant_id):
        self.constant_id = constant_id;
        self.value = None

    def set_constants(self, constants_dict):
        if self.constant_id not in constants_dict:
            raise SemanticException("Uso de constante " + self.constant_id + " no declarada.")

        self.value = constants_dict[self.constant_id]

    def get_value(self):
        if self.value is None:
            raise ProgrammingException("Use el value de una constante antes de setearle el diccionario de constantes.")

        return self.value

    def name(self):
        return "const " + self.constant_id + " = " + str(self.value)

    def children(self):
        return []
        
class Voice(object):
    def __init__(self, instrument, content):
        self.instrument = instrument
        self.content = content

    def set_constants(self, constants_dict):
        self.instrument.set_constants(constants_dict)

    def name(self):
        return "voice " + str(self.instrument.get_value())

    def children(self):
        return [self.instrument]