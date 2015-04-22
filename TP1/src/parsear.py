from automata import *

def importarDeRegex(archivo_regex):
	return AutomataNoDet("")

def importarDeArchivo(archivo_automata):
	try:
		Q = archivo_automata.readline().strip('\n').split('\t')
		Sigma = archivo_automata.readline().strip('\n').split('\t')
		q0 = archivo_automata.readline().strip('\n')
		F = archivo_automata.readline().strip('\n').split('\t')
		
		automata = AutomataDet(Sigma)
		
		for estado in Q:
			automata.agregarEstado(estado)
		
		automata.setearInicial(q0)
		
		for estado in F:
			automata.agregarFinal(estado)
		
		for eje in archivo_automata:
			separado = eje.strip('\n').split('\t')
			automata.setearArista(separado[0], separado[1], separado[2])
		
		return automata
	except:
		sys.exit("El archivo de automata no sigue el formato esperado.")