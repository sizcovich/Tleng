from automata import AutomataDet
from sets import Set

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

def Minimizar(automata):
	clases = {}
	
	for estado in automata.Q:
		if estado in automata.F:
			clases[estado] = 2
		else:
			clases[estado] = 1
	
	while True:
		for simbolo in automata.Sigma:
			