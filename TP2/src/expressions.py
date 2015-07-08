from parser_exceptions import SemanticException

figures = { 'redonda' : 1, 'blanca' : 2, 'negra' : 4, 'corchea' : 8, 'semicorchea' : 16, 'fusa' : 32, 'semifusa' : 64 }
american = { 'do' : 'c', 're' : 'd', 'mi' : 'e', 'fa' : 'f', 'sol' : 'g', 'la' : 'a', 'si' : 'b', 'do+' : 'c+', 're+' : 'd+', 'fa+' : 'f+', 'sol+' : 'g+', 'la+' : 'a+', 're-' : 'd-', 'mi-' : 'e-', 'sol-' : 'g-', 'la-' : 'a-', 'si-' : 'b-' }

class Song(object):
    def __init__(self, tempo, time_signature, voices):
        if len(voices) > 16:
            raise SemanticException("No se pueden declarar mas de 16 voces.")

        if len(voices) == 0:
            raise SemanticException("Debe declararse al menos 1 voz.")
        
        for voice in voices:
            for bar in voice.get_bar_definitions():
                if bar.relative_length() > time_signature.relative_length():
                    raise SemanticException("El compas tiene tiempos de mas. Linea: {0}.".format(bar.line_num))
                elif bar.relative_length() < time_signature.relative_length():
                    raise SemanticException("El compas tiene tiempos de menos. Linea: {0}.".format(bar.line_num))

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
    def __init__(self, beats_per_bar, beat_length, line_num):
        if beats_per_bar < 1:
            raise SemanticException("La cantidad de pulsos por compas debe ser mayor a cero. Linea: {0}.".format(line_num))

        if beat_length not in figures.values():
            raise SemanticException("La duracion de cada pulso debe indicar una figura valida. Linea: {0}.".format(line_num))

        self.beats_per_bar = beats_per_bar
        self.beat_length = beat_length

    def relative_length(self):
        return self.beats_per_bar * (1. / self.beat_length)

class Voice(object):
    def __init__(self, instrument, content, line_num):
        if instrument > 127:
            raise SemanticException("Numero instrumento fuera del rango [0, 127]. Linea: {0}.".format(line_num))

        if len(content) == 0:
            raise SemanticException("Una voz debe tener al menos un compas. Linea: {0}.".format(line_num))

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
            raise SemanticException("Cantidad de repeticiones debe ser al menos 2. Linea: {0}.".format(line_num))

        if len(content) == 0:
            raise SemanticException("Declaracion de repetir con cuerpo vacio. Linea: {0}.".format(line_num))
        
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
            raise SemanticException("Octava fuera del rango [1, 9]. Linea {0}.".format(line_num))
        
        self.tone = tone
        self.octave = octave
        self.figure = figure
        self.line_num = line_num

    def relative_length(self):
        return self.figure.relative_length()

    def american_tone_with_octave(self):
        return american[self.tone] + str(self.octave)

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
        self.value = figures[self.name]
        self.line_num = line_num

    def relative_length(self):        
        return (1. / self.value) + (1. / (self.value * 2) if self.dotted else 0)
        
    def clicks(self, clicks_per_beat, beat_length):
        return ((384 * beat_length) / self.value) + ((384 * beat_length) / (self.value * 2) if self.dotted else 0)