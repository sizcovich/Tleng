from automata import AutomataDet
# A AND B = ¬(¬A U ¬B)
def intersectar(automata1, automata2):
	nuevo = AutomataDet(automata1 | automata2)
	automata1Negado = construirComplemento(automata1)
	automata2Negado = construirComplemento(automata2)

	nuevo = union(automata1Negado, automata2Negado)
	
	nuevo = construirComplemento(nuevo)

	return minimizar(nuevo)

def union(automat1, automata2):
	for estado_aut1 in automata1.Q:
 		for estado_aut2 in automata2.Q:
 			nuevo.agregarEstado(estado_aut1 + estado_aut2)
 			if estado_aut1 in automata1.F || estado_aut2 in automata2.F
 				nuevo.agregarFinal(estado_aut1 + estado_aut2)

 	nuevo.setearInicial(automata1.q0 + automata2.q0)

	for estado1 in automata1.Q:
		for estado2 in automata2.Q:
			for simbolo in automata1.Delta[estado1]:
				if simbolo in automata2.Delta[estado2]:
					nuevo.setearArista(estado1 + estado2, simbolo, automata1.Delta[estado1][simbolo] + automata2.Delta[estado2][simbolo])

	return renombrarEstados(nuevo)