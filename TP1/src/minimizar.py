from automata import AutomataDet
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
	
	return automata

def Minimizar(automata):
	clases = {}
	clases[1] =  filter(lambda q : not (q in automata.F), automata.Q)
	clases[2] =  automata.F