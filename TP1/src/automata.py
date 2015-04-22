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
			
	def removerFinal(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento remover de los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.remove(estado)
		
	def setearArista(self, estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento poner una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento poner una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento poner una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo] = estado2
		
	def removerEstado(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento sacar el estado '%s', no existente en el automata." % estado)
			
		if len(self.Q) == 1:
			sys.exit("Se intento sacar el estado '%s', pero es el unico estado en el automata." % estado)
		
		for estado2 in self.Q:
			if estado2 == estado:
				continue
				
			for simbolo in self.Sigma:
				if self.Delta[estado2][simbolo] == estado:
					sys.exit("Se intento sacar el estado '%s', pero existen estados que llegan a el mismo." % estado)
		
		self.Q.remove(estado)
		self.Delta.pop(estado)
		
		if self.q0 == estado:
			self.q0 = iter(self.Q).next()
		
	def acepta(self, cadena):
		estadoActual = 	self.q0;		
		for simbolo in cadena:
			if not (simbolo in self.Delta[estadoActual]):
				return False;
			estadoActual = self.Delta[estadoActual][simbolo];
			
		if estadoActual in self.F:
			return True;
			
		return False;
	
class AutomataNoDet(object):
	def __init__(self, sigma = None):
		self.Q = Set([])
		self.Sigma = Set(sigma)			
		self.Sigma.add('lambda')		
		self.F = Set(sigma)
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
			
	def removerFinal(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento remover de los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.remove(estado)
		
	def agregarArista(self, estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento agregar una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento agregar una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento agregar una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo].add(estado2)
		
	def removerArista(self, estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento remover una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento poner una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento poner una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo].remove(estado2)
		
	def removerEstado(self, estado):
		if not (estado in self.Q):
			sys.exit("Se intento sacar el estado '%s', no existente en el automata." % estado)
			
		if len(self.Q) == 1:
			sys.exit("Se intento sacar el estado '%s', pero es el unico estado en el automata." % estado)
		
		for estado2 in self.Q:
			if estado2 == estado:
				continue
				
			for simbolo in self.Sigma:
				if estado in self.Delta[estado2][simbolo]:
					sys.exit("Se intento sacar el estado '%s', pero existen estados que llegan a el mismo." % estado)
		
		self.Q.remove(estado)
		self.Delta.pop(estado)
		
		if self.q0 == estado:
			self.q0 = iter(self.Q).next()