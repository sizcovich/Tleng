from parser_exceptions import SemanticException

figures = { 'redonda' : 1., 'blanca' : 2., 'negra' : 4., 'corchea' : 8., 'semicorchea' : 16., 'fusa' : 32., 'semifusa' : 64. }

class Song(object):
    def __init__(self, tempo, time_signature, voices):
        if len(voices) > 16:
            raise SemanticException("No se pueden declarar mas de 16 voces.")

        if len(voices) == 0:
            raise SemanticException("Debe declararse al menos 1 voz.")
        
        for voice in voices:
            for bar in voice.get_bar_definitions():
                if bar.relative_length() != time_signature.relative_length():
                    raise SemanticException("Un compas debe durar lo que se indico en el encabezado. Linea: {0}.".format(bar.line_num))

        self.tempo = tempo
        self.time_signature = time_signature        
        self.voices = voices

class Tempo(object):
    def __init__(self, figure, per_minute, line_num):    
        if per_minute < 1:
            raise SemanticException("El valor del tempo debe ser mayor a cero. Linea: {0}.".format(line_num))
            
        self.figure = figure
        self.per_minute = per_minute

class TimeSignature(object):
    def __init__(self, num_beats, beat_length, line_num):
        if num_beats < 1:
            raise SemanticException("El nominador de la indicacion de compas debe ser mayor a cero. Linea: {0}.".format(line_num))

        if beat_length not in figures.values():
            raise SemanticException("El denominador de la indicacion de compas debe indicar una figura valida. Linea: {0}.".format(line_num))
        
        self.num_beats = num_beats
        self.beat_length = beat_length

    def relative_length(self):
        return self.num_beats * (1. / self.beat_length)

class Voice(object):
    def __init__(self, instrument, content, line_num):
        self.instrument = instrument
        self.content = content
        self.line_num = line_num

    def get_bar_definitions(self):
        return [ bar for c in self.content for bar in c.get_bar_definitions() ]

    def get_bar_executions(self):
        return [ bar for c in self.content for bar in c.get_bar_executions() ]

class Bar(object):
    def __init__(self, content, line_num):
        self.content = content
        self.line_num = line_num

    def get_bar_definitions(self):
        return [ self ]

    def get_bar_executions(self):
        return [ self ]

    def relative_length(self):
        return sum(c.relative_length() for c in self.content)

class Repeat(object):
    def __init__(self, repetitions, content, line_num):
        if repetitions < 2:
            raise SemanticException("El valor de una repeticion debe ser al menos 2. Linea: {0}.".format(line_num))

        self.content = content
        self.repetitions = repetitions
        self.line_num = line_num

    def get_bar_definitions(self):
        return [ bar for c in self.content for bar in c.get_bar_definitions() ]

    def get_bar_executions(self):
        return [ bar for c in self.content for bar in c.get_bar_executions() ] * self.repetitions

class Note(object):
    def __init__(self, tone, octave, figure, line_num):
        if octave < 1 or octave > 9:
            raise SemanticException("La octava de una nota debe estar entre 1 y 9. Linea {0}.".format(line_num))
        
        self.tone = tone
        self.octave = octave
        self.figure = figure
        self.line_num = line_num

    def relative_length(self):
        return self.figure.relative_length()

class Silence(object):
    def __init__(self, figure, line_num):        
        self.figure = figure
        self.line_num = line_num

    def relative_length(self):
        return self.figure.relative_length()

class Figure(object):
    def __init__(self, name, line_num):     
        self.dotted = name.endswith('.')
        self.name = name.rstrip('.')
        self.line_num = line_num

    def relative_length(self):
        value = figures[self.name]
        return (1. / value) + (1. / (value * 2) if self.dotted else 0)