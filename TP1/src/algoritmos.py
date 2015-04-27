from automata import *
import string
from collections import deque

def clausuraLambda(estado, automataNoDet):
	clausura = automataNoDet.Delta[estado]['lambda']
	clausura.add(estado)

	while True:
		estadosAgregar = Set([])

		for est in clausura:
			clausura2 = automataNoDet.Delta[est]['lambda']

			for est2 in clausura2:
				if not (est2 in clausura):
					estadosAgregar.add(est2)

		clausura = clausura | estadosAgregar

		if (len(estadosAgregar) == 0):
			return clausura

def mover(estados, simbolo, automataNoDet):
	moverPorSimbolo = Set([])
	clausura = Set([])

	for est in estados:
		estado = automataNoDet.Delta[est][simbolo]
		moverPorSimbolo = moverPorSimbolo | estado

	for a in moverPorSimbolo:
		aux3 = clausuraLambda(a, automataNoDet)
		clausura = clausura | aux3

	return clausura

def determinizar(automataNoDet):
	estadoInicial = automataNoDet.q0
	primerPaso = clausuraLambda(estadoInicial, automataNoDet)
	valoresExistentes = Set([]) 
	valoresExistentes.add(primerPaso)

	i = 1

	estados = { }
	estados[0] = primerPaso

	aristas = { }
	aristas[0] = { }

	valoresACalcular = deque([])
	valoresACalcular.append(primerPaso)
	while not (len(valoresACalcular) == 0):
		conjuntoACalcular = valoresACalcular.pop()

		for simbolo in automataNoDet.Sigma:
			if not (simbolo == 'lambda'):
				conjunto = Set([])	
				conjunto = mover(conjuntoACalcular, simbolo, automataNoDet)

				if conjunto:
					if not (conjunto in valoresExistentes):
						valoresExistentes.add(conjunto)
						valoresACalcular.append(conjunto)

						estados[i] = conjunto #agrego un estado

						for j in range(len(estados)):  #agrego la arista
							if estados[j] == conjuntoACalcular:
								aristas[j][i] = Set([simbolo])
								aristas[i] = { }
								break

						i = i + 1						
					else:
						k = 0

						for m in range(len(estados)):
							if estados[m] == conjunto:
								k = m
								break

						for j in range(len(estados)):
							if estados[j] == conjuntoACalcular:
								if not (k in aristas[j]):
									aristas[j][k] = Set([simbolo])
								else:
									aristas[j][k].add(simbolo)
								break

	automataDet = AutomataDet(automataNoDet.Sigma - Set(['lambda']))

	#agrego estados
	for i in range(len(estados)):
		nuevoEstado = 'q' + str(i)
		automataDet.agregarEstado(nuevoEstado)

	automataDet.setearInicial('q0')

	#agrego aristas
	for i in range(len(estados)):
		for j in range(len(estados)):
			if j in aristas[i]:
				for est in aristas[i][j]:
					if est != 'lambda':
						est1 = 'q' + str(i)
						est2 = 'q' + str(j)
						automataDet.setearArista(est1,est,est2)

	#agrego estados finales
	for conj in valoresExistentes:
		for est in conj:
			if est in automataNoDet.F:
				for m in range(len(estados)):
						if estados[m] == conj:
							est1 = 'q' + str(m)
							automataDet.agregarFinal(est1)
							break

	return automataDet

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
	
def noAceptaNingunaCadena(automata):
	return True