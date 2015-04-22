from intersectar import intersectar
from complementar import complementar

def igualar(automata1, automata2):
	# Si es vacio, el not de un Set da True.
	return not intersectar(automata1, complementar(automata2)).F