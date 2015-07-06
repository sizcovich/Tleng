import lexer_rules
from sys import argv, stdout
from ply.lex import lex

def dump_tokens(lexer, output_file):
    token = lexer.token()
    
    for token in lexer:
        output_file.write("type: " + token.type)
        output_file.write(" - value: " + str(token.value))
        output_file.write(" - line: " + str(token.lineno))
        output_file.write(" - position: " + str(token.lexpos))
        output_file.write("\n")

if __name__ == "__main__":
    if len(argv) != 2 and len(argv) != 3:
        print "Parametros invalidos."
        print "Uso:"
        print "  lexer.py archivo_entrada [archivo_salida]"
        exit()

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules)

    lexer.input(text)

    if (len(argv) == 3):
        output_file = open(argv[2], "w")
        dump_tokens(lexer, output_file)
        output_file.close()
    else:
        dump_tokens(lexer, stdout)
