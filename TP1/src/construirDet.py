from automata import AutomataDet
from sets import Set
from collections import deque

def construirComplemento(automata):
	nuevo = AutomataDet(automata.Sigma)

	for estado in automata.Q:
		nuevo.agregarEstado(estado)

		if not estado in automata.F:
			nuevo.agregarFinal(estado)

	# Mando todos los que no esten definidos al trampa
	agregarTrampa = False
	for estado in automata.Q:
		if Set(automata.Delta[estado].keys()) != automata.Sigma:
			agregarTrampa = True
			break

	if agregarTrampa:
		nuevo.agregarEstado('qT')
		nuevo.agregarFinal('qT')

	nuevo.setearInicial(automata.q0)

	for estado in nuevo.Q:
		for simbolo in nuevo.Sigma:
			if estado != 'qT' and simbolo in automata.Delta[estado]:
					nuevo.setearArista(estado, simbolo, automata.Delta[estado][simbolo])
			else:
				nuevo.Delta[estado][simbolo] = 'qT'

	return renombrarEstados(nuevo)

def construirInterseccion(automata1, automata2):
	nuevo = AutomataDet(automata1 | automata2)
	automata1Negado = construirComplemento(automata1)
	automata2Negado = construirComplemento(automata2)

	nuevo = construirUnion(automata1Negado, automata2Negado)
	
	nuevo = construirComplemento(nuevo)

	return nuevo

def construirUnion(automata1, automata2):
	for estado_aut1 in automata1.Q:
 		for estado_aut2 in automata2.Q:
 			nuevo.agregarEstado(estado_aut1 + estado_aut2)

 			if (estado_aut1 in automata1.F) or (estado_aut2 in automata2.F):
 				nuevo.agregarFinal(estado_aut1 + estado_aut2)

 	nuevo.setearInicial(automata1.q0 + automata2.q0)

	for estado1 in automata1.Q:
		for estado2 in automata2.Q:
			for simbolo in automata1.Delta[estado1]:
				if simbolo in automata2.Delta[estado2]:
					nuevo.setearArista(estado1 + estado2, simbolo, automata1.Delta[estado1][simbolo] + automata2.Delta[estado2][simbolo])

	return renombrarEstados(nuevo)
	
def renombrarEstados(automata):
	nuevo = AutomataDet(automata.Sigma)

	visitados = Set()
	queue = deque()

	i = 0
	mapeo = { }

	queue.append(automata.q0)

	for inicial in automata.Q:
		if inicial not in visitados:
			queue.append(inicial)

		while queue:
			estado = queue.popleft()

			nuevoEstado = 'q' + str(i)
			nuevo.agregarEstado(nuevoEstado)

			if estado == automata.q0:
				nuevo.setearInicial(nuevoEstado)

			if estado in automata.F:
				nuevo.agregarFinal(nuevoEstado)

			mapeo[estado] = nuevoEstado
			i += 1

			visitados.add(estado)

			for simbolo in automata.Delta[estado]:
				vecino = automata.Delta[estado][simbolo]

				if not vecino in visitados:
					queue.append(vecino)

	for estado in automata.Q:		
		for simbolo in automata.Delta[estado]:
			nuevo.setearArista(mapeo[estado], simbolo, mapeo[automata.Delta[estado][simbolo]])

	return nuevo