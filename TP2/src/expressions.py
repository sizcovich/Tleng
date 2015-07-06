from lexer_rules import figures_inv
from parser_exceptions import SemanticException, ProgrammingException

class Song(object):
    def __init__(self, tempo, time_signature, constants, voices):
        self.tempo = tempo
        self.time_signature = time_signature
        self.constants = constants
        self.voices = voices

class Tempo(object):
    def __init__(self, figure, per_minute):
        self.figure = figure
        self.per_minute = per_minute

class TimeSignature(object):
    def __init__(self, num_beats, beat_length):
        self.num_beats = num_beats
        self.beat_length = beat_length

    def relative_length(self):
        return (1. / self.beat_length) * self.num_beats

class VoiceHeader(object):
    def __init__(self, instrument, content):
        self.instrument = instrument
        self.content = content

class Bar(object):
    def __init__(self, content):
        self.content = content

    def relative_length(self):
        return sum(c.relative_length() for c in self.content)

class Note(object):
    def __init__(self, tone, octave, length):
        self.tone = tone
        self.octave = octave
        self.length = length

    def relative_length(self):
        return 1. / self.length

class Silence(object):
    def __init__(self, length):        
        self.length = length

    def relative_length(self):
        return 1. / self.length

class Figure(object):
    