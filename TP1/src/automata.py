from sets import Set
import string
import sys

class AutomataDet(object):
	def __init__(self, sigma):
		self.Q = Set([])
		self.Sigma = Set(sigma)		
		self.F = Set([])
		self.q0 = None
		self.Delta = { }

	def setearInicial(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento seleccionar como estado inicial el estado '%s', no existente en el automata." % estado)

		self.q0 = estado

	def agregarEstado(self, estado):
		if estado in self.Q:
			sys.exit("Se intento agregar el estado '%s' ya existente en el automata." % estado)

		self.Q.add(estado)
		self.Delta[estado] = {}

	def agregarFinal(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento agregar a los estados finales el estado '%s', no existente en el automata." % estado)

		self.F.add(estado)

	def quitarFinal(self, estado):
		if not (estado in self.F):
			sys.exit("Se intento quitar de los estados finales el estado '%s', el cual no pertenecia a dicho conjunto." % estado)

		self.F.remove(estado)

	def setearArista(self, estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento poner una arista desde el estado '%s', no existente en el automata." % estado1)

		if not (simbolo in self.Sigma):
			sys.exit("Se intento poner una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)

		if not (estado2 in self.Q):
			sys.exit("Se intento poner una arista hacia el estado '%s', no existente en el automata." % estado2)

		self.Delta[estado1][simbolo] = estado2
		
	def toString(self):
		if self.q0 is None:
			sys.exit("El automata no tiene definido un estado inicial.")
		
		res = '\t'.join(self.Q) + '\n'
		res += '\t'.join(['\\t' if s == '\t' else s for s in self.Sigma]) + '\n'
		res += self.q0 + '\n'
		res += '\t'.join(self.F) + '\n'

		for estado in self.Q:
			for rel in self.Delta[estado]:
				res += '%s\t%s\t%s\n' % (estado, rel if rel != '\t' else '\\t', self.Delta[estado][rel])

		return res

	def acepta(self, cadena):
		if self.q0 is None:
			sys.exit("El automata no tiene definido un estado inicial.")
		estadoActual = 	self.q0;		
		for simbolo in cadena:
			if not (simbolo in self.Delta[estadoActual]):
				return False;
			estadoActual = self.Delta[estadoActual][simbolo];

		if estadoActual in self.F:
			return True;

		return False;

class AutomataNoDet(object):
	def __init__(self, sigma):
		self.Q = Set([])
		self.Sigma = Set(sigma)
		self.Sigma.add('lambda')		
		self.F = Set([])
		self.q0 = None
		self.Delta = { }

	def setearInicial(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento seleccionar como estado inicial el estado '%s', no existente en el automata." % estado)

		self.q0 = estado

	def agregarEstado(self, estado):
		if (estado in self.Q):
			sys.exit("Se intento agregar el estado '%s' ya existente en el automata." % estado)

		self.Q.add(estado)
		self.Delta[estado] = {}
		for simbolo in self.Sigma:
			self.Delta[estado][simbolo] = Set()

	def agregarFinal(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento agregar a los estados finales el estado '%s', no existente en el automata." % estado)

		self.F.add(estado)

	def agregarArista(self, estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento agregar una arista desde el estado '%s', no existente en el automata." % estado1)

		if not (simbolo in self.Sigma):
			sys.exit("Se intento agregar una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)

		if not (estado2 in self.Q):
			sys.exit("Se intento agregar una arista hacia el estado '%s', no existente en el automata." % estado2)

		self.Delta[estado1][simbolo].add(estado2)
		
	def toString(self):
		if self.q0 is None:
			sys.exit("El automata no tiene definido un estado inicial.")
		
		res = '\t'.join(self.Q) + '\n'
		res += '\t'.join(['\\t' if s == '\t' else s for s in self.Sigma]) + '\n'
		res += self.q0 + '\n'
		res += '\t'.join(self.F) + '\n'

		for estado in self.Q:
			for rel in self.Delta[estado]:
				res += '%s\t%s\t%s\n' % (estado, rel if rel != '\t' else '\\t', str(list(self.Delta[estado][rel])))

		return res		