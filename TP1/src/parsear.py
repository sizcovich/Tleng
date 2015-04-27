from construirNoDet import *
from automata import AutomataDet

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
	except:
		sys.exit("El archivo de automata no sigue el formato esperado.")