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
