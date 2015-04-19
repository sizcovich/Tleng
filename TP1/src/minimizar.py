from automata import AutomataDet
from sets import Set

def minimizar(automata):
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
			# de la pinta "q1-q2-q2-q1" para poder hashear
			temp = ultimasClases[estado] + '-' + '-'.join(tabla[estado])
			
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
		
	nuevo.removerEstado('qT')

	return nuevo