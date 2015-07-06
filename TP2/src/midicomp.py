import lexer_rules
import parser_rules

from sys import argv, exit, stdout

from ply.lex import lex
from ply.yacc import yacc


def dump_song(song, output_file):
    output_file.write('tempo: %d %d\n' % (song.tempo.figure, song.tempo.per_minute))
    output_file.write('ts: %d/%d\n' % (song.time_signature.num_beats, song.time_signature.beat_length))

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

    song = parser.parse(text, lexer)

    if (len(argv) == 3):
        output_file = open(argv[2], "w")
        dump_song(song, output_file)
        output_file.close()
    else:
        dump_song(song, stdout)