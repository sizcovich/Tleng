import lexer_rules
import parser_rules
import parser_exceptions
from translation import generate_output

from sys import argv, exit, stdout
from ply.lex import lex
from ply.yacc import yacc

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
    parser = yacc(debug=0,module=parser_rules)
        
    try:
        song = parser.parse(text, lexer)
        if (len(argv) == 3):
            output_file = open(argv[2], "w")
            generate_output(song, output_file)
            output_file.close()
        else:
            generate_output(song, stdout)
    except parser_exceptions.SemanticException as exception:
        print "Error de validacion: " + str(exception)
    except parser_exceptions.SyntacticException as exception:
        print "Error de sintaxis: " + str(exception)