from automata import *
import logging

def importarDeRegex(archivo_regex):
	try:		
		line = archivo_regex.readline().strip('\n').strip('\t')
		
		if not line:
			sys.exit("El archivo de expresion regular finalizo antes de lo esperado.")

		if '{CONCAT}' in line:
			children = int(line.strip('{CONCAT}'))
			if children < 2:
				sys.exit("El archivo de expresion regular no sigue el formato esperado.")
			
			automata = importarDeRegex(archivo_regex)

			for i in xrange(1,children):
				automata2 = importarDeRegex(archivo_regex)
				automata = construirConcat(automata, automata2)

			return automata

		elif '{OR}' in line:
			children = int(line.strip('{OR}'))

			if children < 2:
				sys.exit("El archivo de expresion regular no sigue el formato esperado.")

			automata = importarDeRegex(archivo_regex)

			for i in xrange(1,children):
				automata2 = importarDeRegex(archivo_regex)
				automata = construirOr(automata, automata2)

			return automata

		elif '{STAR}' in line:
			automata = importarDeRegex(archivo_regex)

			return construirStar(automata)

		elif '{PLUS}' in line:
			automata = importarDeRegex(archivo_regex)

			return construirPlus(automata)

		elif '{OPT}' in line:
			automata = importarDeRegex(archivo_regex)

			return construirOpt(automata)

		elif line == '\\t':
			return construirBase('\t')

		elif len(line) == 1: 
			return construirBase(line)

		else:
			sys.exit("El archivo de expresion regular no sigue el formato esperado.")

	except Exception as ex:
		logging.exception("Something awful happened!")
		sys.exit("El archivo de expresion regular no sigue el formato esperado.")

def importarDeArchivo(archivo_automata):
	try:
		Q = archivo_automata.readline().strip('\n').split('\t')		
		Sigma = ['\t' if s == '\\t' else s for s in archivo_automata.readline().strip('\n').split('\t')]
		q0 = archivo_automata.readline().strip('\n')
		F = archivo_automata.readline().strip('\n').split('\t')
		
		automata = AutomataDet(Sigma)

		for estado in Q:
			automata.agregarEstado(estado)

		automata.setearInicial(q0)

		for estado in F:
			if estado:
				automata.agregarFinal(estado)

		for eje in archivo_automata:			
			separado = ['\t' if s == '\\t' else s for s in eje.strip('\n').split('\t')]
			automata.setearArista(separado[0], separado[1], separado[2])

		return automata
	except Exception,e:
		print(e)
		sys.exit("El archivo de automata no sigue el formato esperado.")
		
def construirBase(simbolo):
	automata = AutomataNoDet(simbolo)
	
	automata.agregarEstado('q0')
	automata.agregarEstado('qf')
	
	automata.setearInicial('q0')
	automata.agregarFinal('qf')
	
	automata.agregarArista('q0', simbolo, 'qf')

	return automata

def construirConcat(automata1, automata2):
	nuevo = AutomataNoDet(automata1.Sigma | automata2.Sigma)
	
	for estado in automata1.Q:
		nuevo.agregarEstado(estado + '-1')

	for estado in automata2.Q:
		nuevo.agregarEstado(estado + '-2')

	nuevo.setearInicial(automata1.q0 + '-1')
		
	for estado in automata1.F:
		nuevo.agregarArista(estado + '-1', 'lambda', automata2.q0 + '-2')

	for estado in automata2.F:
		nuevo.agregarFinal(estado + '-2')

	for estado in automata1.Q:
		for simbolo in automata1.Sigma:
			for estado2 in automata1.Delta[estado][simbolo]:
				nuevo.agregarArista(estado + '-1', simbolo, estado2 + '-1')

	for estado in automata2.Q:
		for simbolo in automata2.Sigma:
			for estado2 in automata2.Delta[estado][simbolo]:
				nuevo.agregarArista(estado + '-2', simbolo, estado2 + '-2')

	return nuevo

def construirOr(automata1, automata2):
	nuevo = AutomataNoDet(automata1.Sigma | automata2.Sigma)

	nuevo.agregarEstado('q0')
	nuevo.agregarEstado('qf')

	nuevo.setearInicial('q0')
	nuevo.agregarFinal('qf')

	for estado in automata1.Q:
		nuevo.agregarEstado(estado + '-1')

	for estado in automata2.Q:
		nuevo.agregarEstado(estado + '-2')

	nuevo.agregarArista('q0', 'lambda', automata1.q0 + '-1')
	nuevo.agregarArista('q0', 'lambda', automata2.q0 + '-2')

	for estado in automata1.F:
		nuevo.agregarArista(estado + '-1', 'lambda', 'qf')

	for estado in automata2.F:
		nuevo.agregarArista(estado + '-2', 'lambda', 'qf')

	for estado in automata1.Q:
		for simbolo in automata1.Sigma:
			for estado2 in automata1.Delta[estado][simbolo]:
				nuevo.agregarArista(estado + '-1', simbolo, estado2 + '-1')

	for estado in automata2.Q:
		for simbolo in automata2.Sigma:
			for estado2 in automata2.Delta[estado][simbolo]:
				nuevo.agregarArista(estado + '-2', simbolo, estado2 + '-2')

	return nuevo

def construirStar(automata):
	nuevo = construirPlus(automata)	
	nuevo.agregarArista('q0', 'lambda', 'qf')

	return nuevo

def construirPlus(automata):
	nuevo = AutomataNoDet(automata.Sigma)

	nuevo.agregarEstado('q0')
	nuevo.agregarEstado('qf')

	nuevo.setearInicial('q0')
	nuevo.agregarFinal('qf')

	for estado in automata.Q:
		nuevo.agregarEstado(estado + '-1')

	nuevo.agregarArista('q0', 'lambda', automata.q0 + '-1')

	for estado in automata.F:
		nuevo.agregarArista(estado + '-1', 'lambda', 'qf')
		nuevo.agregarArista(estado + '-1', 'lambda', automata.q0 + '-1')

	for estado in automata.Q:
		for simbolo in automata.Sigma:
			for estado2 in automata.Delta[estado][simbolo]:
				nuevo.agregarArista(estado + '-1', simbolo, estado2 + '-1')

	return nuevo

def construirOpt(automata):
	nuevo = AutomataNoDet(automata.Sigma)

	for estado in automata.Q:
		nuevo.agregarEstado(estado)

	nuevo.setearInicial(automata.q0)
	
	for estado in automata.F:
		nuevo.agregarFinal(estado)
		nuevo.agregarArista(nuevo.q0, 'lambda', estado)
		
	for estado in automata.Q:
		for simbolo in automata.Sigma:
			for estado2 in automata.Delta[estado][simbolo]:
				nuevo.agregarArista(estado, simbolo, estado2)