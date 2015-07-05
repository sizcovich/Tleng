from lexer_rules import figures_inv

class Song(object):
    def __init__(self, tempo, time_signature, constants):
        self.tempo = tempo
        self.time_signature = time_signature
        self.constants = constants
        
    def name(self):
        return "Song"

    def children(self):
        return [self.tempo, self.time_signature] + [Const(k, v) for k,v in self.constants.items()]

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