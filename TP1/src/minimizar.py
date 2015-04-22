from automata import AutomataDet
from sets import Set

def minimizar(automata):

	# Agrego el trampa para completar la funcion Delta
	if not 'qT' in automata.Q:
		automata.agregarEstado('qT')
	
	# Mando todos los que no esten definidos al trampa
	for estado in automata.Q:
		for simbolo in automata.Sigma:
			if not (simbolo in automata.Delta[estado]):				
				automata.Delta[estado][simbolo] = 'qT'
	
	ultimasClases = {}
	ejes = {}
	claseInicial = 'q1'
	clasesFinales = Set()
	
	for estado in automata.Q:
		if estado in automata.F:
			ultimasClases[estado] = 'q2'
		else:
			ultimasClases[estado] = 'q1'
	
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
		proximaClase = 1
		
		for estado in automata.Q:
			# convierto los valores de la tabla a un string
			# de la pinta "q1-q2-q2-q1" para poder hashear
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

def ejemplo():

	automata = AutomataDet("aso")
	automata.agregarEstado('q1')
	automata.agregarEstado('q2')
	automata.agregarEstado('q3')
	automata.agregarEstado('q4')
	automata.agregarEstado('q5')
	automata.agregarEstado('q6')
	automata.agregarEstado('q7')
	
	automata.setearInicial('q1')
	automata.setearArista('q1', 'o', 'q2')
	automata.setearArista('q1', 'a', 'q3')
	automata.setearArista('q2', 's', 'q4')
	automata.setearArista('q3', 's', 'q5')
	automata.setearArista('q4', 'a', 'q6')
	automata.setearArista('q5', 'a', 'q7')
	
	automata.agregarFinal('q6')
	automata.agregarFinal('q7')
	
	return automata
	
def ejemplo2():

	automata = AutomataDet("asobdET")
	automata.agregarEstado('q0')
	automata.agregarEstado('q1')
	automata.agregarEstado('q2')
	automata.agregarEstado('q3')
	
	automata.setearInicial('q0')
	automata.setearArista('q0', 'a', 'q1')
	automata.setearArista('q1', 'a', 'q2')
	automata.setearArista('q2', 'a', 'q3')
	automata.setearArista('q3', 'a', 'q1')		
	
	automata.agregarFinal('q0')
	automata.agregarFinal('q1')
	automata.agregarFinal('q2')
	automata.agregarFinal('q3')
	
	return automata