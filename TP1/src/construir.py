from automata import AutomataNoDet

def construirBase(simbolo):
	automata = AutomataNoDet(simbolo)
	
	automata.agregarEstado('q0')
	automata.agregarEstado('q1')
	
	automata.setearInicial('q0')
	automata.agregarFinal('q1')
	
	automata.agregarArista('q0', simbolo, 'q1')

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

	return renombrarEstados(nuevo)

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

	return renombrarEstados(nuevo)

def construirStar(automata):
	nuevo = construirPlus(automata)

	for estado in automata.Q:
		nuevo.agregarArista(nuevo.q0, 'lambda', estado)

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

	return renombrarEstados(nuevo)

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

	return automata

def renombrarEstados(automata):
	nuevo = AutomataNoDet(automata.Sigma)
	
	nuevo.agregarEstado('q0')
	
	nuevo.setearInicial('q0')

	mapeo = { automata.q0 : 'q0' }
	i = len(automata.Q) - 1

	for estado in automata.F:
		nuevoEstado = 'q' + str(i)
		nuevo.agregarEstado(nuevoEstado)
		nuevo.agregarFinal(nuevoEstado)
		mapeo[estado] = nuevoEstado		
		i -= 1

	i = 1

	for estado in automata.Q:
		if estado != automata.q0 and not estado in automata.F:
			nuevoEstado = 'q' + str(i)
			nuevo.agregarEstado(nuevoEstado)
			mapeo[estado] = nuevoEstado			
			i += 1

	for estado in automata.Q:		
		for simbolo in automata.Delta[estado]:
			for estado2 in automata.Delta[estado][simbolo]:			
				nuevo.agregarArista(mapeo[estado], simbolo, mapeo[estado2])

	return nuevo