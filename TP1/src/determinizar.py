from sets import Set
import string
from automata import AutomataNoDet
from automata import AutomataDet
from collections import deque

def clausuraLambda(estado,automataNoDet):
	clausura = automataNoDet.Delta[estado]['lambda']
	clausura.add(estado)

	while True:
		estadosAgregar = Set([])
		for est in clausura:
			clausura2 = automataNoDet.Delta[est]['lambda']
			for est2 in clausura2:
				if not (est2 in clausura):
					estadosAgregar.add(est2)
		clausura = clausura|estadosAgregar
		if (len(estadosAgregar) == 0):
			return clausura

def mover(estados,simbolo,automataNoDet):
	moverPorSimbolo = Set([])
	clausura = Set([])
	for est in estados:
		estado = automataNoDet.Delta[est][simbolo]
		moverPorSimbolo = moverPorSimbolo|estado

	for a in moverPorSimbolo:
		aux3 = clausuraLambda(a,automataNoDet)
		clausura = clausura|aux3

	return clausura

def determinizar(automataNoDet):
	estadoInicial = automataNoDet.q0
	primerPaso = clausuraLambda(estadoInicial,automataNoDet)
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
				conjunto = mover(conjuntoACalcular,simbolo,automataNoDet)
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
						#agregarEstado(automataDet,conjunto)
						#setearArista(automataDet,conjuntoACalcular,simbolo,conjunto)
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
						#setearArista(automataDet,conjuntoACalcular,simbolo,conjunto)

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

def ejemplo():
	automata = AutomataNoDet("01")
	automata.agregarEstado('q0')
	automata.agregarEstado('q1')
	automata.agregarEstado('q2')
	automata.agregarEstado('q3')
	automata.agregarEstado('q4')
	
	automata.setearInicial('q0')
	automata.agregarArista('q0', 'lambda', 'q1')
	automata.agregarArista('q0', 'lambda', 'q2')
	automata.agregarArista('q1', '1', 'q1')
	automata.agregarArista('q1', '0', 'q1')
	automata.agregarArista('q1', '1', 'q3')
	automata.agregarArista('q2', '0', 'q2')
	automata.agregarArista('q2', '1', 'q4')
	automata.agregarArista('q2', 'lambda', 'q3')
	automata.agregarArista('q4', '1', 'q2')
	automata.agregarArista('q4', '0', 'q4')
	
	return automata