from automata import *
from sets import Set
from collections import deque

def clausuraLambda(estado, automataNoDet):

	clausura = automataNoDet.Delta[estado]['lambda']
	clausura.add(estado)

	while True:
		estadosaAAgregar = Set([])
		
		for est in clausura:			
			for est2 in automataNoDet.Delta[est]['lambda']:
				if not (est2 in clausura):
					estadosaAAgregar.add(est2)
					
		if not estadosaAAgregar:
			return clausura
			
		clausura.update(estadosaAAgregar)

def mover(estados, simbolo, automataNoDet):

	moverPorSimbolo = Set([])
	clausura = Set([])
	
	for est in estados:		
		moverPorSimbolo.update(automataNoDet.Delta[est][simbolo])

	for simb in moverPorSimbolo:
		clausura.update(clausuraLambda(simb, automataNoDet))
	
	return clausura

def determinizar(automataNoDet):

	estadoInicial = automataNoDet.q0
	primerPaso = clausuraLambda(estadoInicial, automataNoDet)

	valoresExistentes = Set([primerPaso])
	
	i = 1

	estados = { 0 : primerPaso  }
	aristas = { 0 : {} }	

	valoresACalcular = deque([primerPaso])
		
	while not valoresACalcular:
		conjuntoACalcular = valoresACalcular.pop()
		
		for simbolo in automataNoDet.Sigma - Set(['lambda']):
			conjunto = mover(conjuntoACalcular,simbolo,automataNoDet)
			
			if not (conjunto in valoresExistentes):
				#agrego un estado
				valoresExistentes.add(conjunto)
				valoresACalcular.append(conjunto)
				
				estados[i] = conjunto
				
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
	
	automataDet = AutomataDet(automataNoDet.Sigma)

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
					est1 = 'q' + str(i)
					est2 = 'q' + str(j)
					automataDet.setearArista(est1, est, est2)

	#agrego estados finales
	for conj in valoresExistentes:
		for est in conj:
			if est in automataNoDet.F:
				for m in range(len(estados)):
						if estados[m] == conj:
							est1 = 'q' + str(i)
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