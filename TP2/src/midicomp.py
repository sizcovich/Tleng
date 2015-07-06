import lexer_rules
import parser_rules
import parser_exceptions

from sys import argv, exit, stdout

from ply.lex import lex
from ply.yacc import yacc


def dump_song(song, output_file):
    output_file.write('tempo: %s %d\n' % (song.tempo.figure.name, song.tempo.per_minute))
    output_file.write('ts: %d/%d\n' % (song.time_signature.num_beats, song.time_signature.beat_length))
    output_file.write('ts: %d/%d\n' % (song.time_signature.num_beats, song.time_signature.beat_length))
    i = 1
    for voice in song.voices:        
        output_file.write('voice %d: instrument %d. bars: %d\n' % (i, voice.instrument, len(voice.get_bar_executions())))
        i = i + 1

if __name__ == "__main__":
    if len(argv) != 2 and len(argv) != 3:
        print "Parametros invalidos."
        print "Uso:"
        print "  parser.py archivo_entrada [archivo_salida]"
        exit()

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)
        
    try:
        song = parser.parse(text, lexer)
        if (len(argv) == 3):
            output_file = open(argv[2], "w")
            dump_song(song, output_file)
            output_file.close()
        else:
            dump_song(song, stdout)
    except parser_exceptions.SemanticException as exception:
        print "[Semantic error]: " + str(exception)
    except parser_exceptions.SyntacticException as exception:
        print "[Syntax error]:  " + str(exception)