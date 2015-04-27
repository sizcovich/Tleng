from automata import AutomataDet
from sets import Set

def minimizar(automata):	
	# Mando todos los que no esten definidos al trampa
	agregarTrampa = False
	for estado in automata.Q:
		if Set(automata.Delta[estado].keys()) != automata.Sigma:
			agregarTrampa = True
			break

	if agregarTrampa:
		automata.agregarEstado('qT')
		for estado in automata.Q:		
			for simbolo in automata.Sigma:
				if not (simbolo in automata.Delta[estado]):
					automata.Delta[estado][simbolo] = 'qT'

	ultimasClases = {}
	ejes = {}
	claseInicial = 'q0'
	clasesFinales = Set()

	for estado in automata.Q:
		if estado in automata.F:
			ultimasClases[estado] = 'q1'
		else:
			ultimasClases[estado] = 'q0'

	while True:
		tabla = {}
		for estado in automata.Q:
			tabla[estado] = {}
			for simbolo in automata.Sigma:
				tabla[estado][simbolo] = ultimasClases[automata.Delta[estado][simbolo]]

		clases = {}
		ejes = {}
		clasesFinales = Set()

		mapeo = {}
		proximaClase = 0

		for estado in automata.Q:
			# convierto los valores de la tabla a un string
			# de la pinta "q0-q1-q2-q1" para poder hashear
			temp = ultimasClases[estado] + '-' + '-'.join(tabla[estado].values())

			if temp in mapeo:
				clases[estado] = mapeo[temp]
			else:
				nuevoEstado = 'q' + str(proximaClase)
				mapeo[temp] = nuevoEstado
				clases[estado] = nuevoEstado
				ejes[nuevoEstado] = tabla[estado]
				proximaClase += 1

			if automata.q0 == estado:
				claseInicial = mapeo[temp]

			if estado in automata.F:
				clasesFinales.add(mapeo[temp])

		if clases == ultimasClases:
			break

		ultimasClases = clases

	nuevo = AutomataDet(automata.Sigma)

	for estado in Set(ultimasClases.values()):
		nuevo.agregarEstado(estado)

	for estado in Set(ultimasClases.values()):		
		for simbolo in automata.Sigma:
			nuevo.setearArista(estado, simbolo, ejes[estado][simbolo])			

	nuevo.setearInicial(claseInicial)

	for clase in clasesFinales:
		nuevo.agregarFinal(clase)

	return nuevo