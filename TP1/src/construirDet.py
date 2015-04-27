from automata import AutomataDet
from sets import Set

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
	return AutomataDet("")
	
def renombrarEstados(automata):
	nuevo = AutomataDet(automata.Sigma)

	nuevo.agregarEstado('q0')
	nuevo.setearInicial('q0')

	mapeo = { automata.q0 : 'q0' }
	i = len(automata.Q) - 1

	for estado in automata.F:
		if estado == automata.q0:
			nuevo.agregarFinal('q0')
		else:		
			nuevoEstado = 'q' + str(i)			
			nuevo.agregarEstado(nuevoEstado)
			nuevo.agregarFinal(nuevoEstado)
			mapeo[estado] = nuevoEstado		
			i -= 1

	i = 1
	
	for estado in automata.Q:
		if estado != automata.q0 and not estado in automata.F:
			nuevoEstado = 'q' + str(i)			
			nuevo.agregarEstado(nuevoEstado)
			mapeo[estado] = nuevoEstado			
			i += 1

	for estado in automata.Q:		
		for simbolo in automata.Delta[estado]:
			nuevo.setearArista(mapeo[estado], simbolo, mapeo[automata.Delta[estado][simbolo]])

	return nuevo