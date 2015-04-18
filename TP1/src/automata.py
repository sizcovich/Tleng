from sets import Set
import string

class AutomataDet(object):
	def __init__(self, sigma = None):
		self.Q = { 'qT' }
		if sigma is None:
			self.Sigma = Set(string.letters + string.digits + "[,:;.?!()\"\'\\&-]" + " " + "\t")
		else:
			self.Sigma = Set(sigma)
		
		self.F = Set([])
		self.q0 = 'qT'
		self.Delta = { 'qT' : {}}
		for simbolo in self.Sigma:
			self.Delta['qT'][simbolo] = 'qT'
	
	def setearInicial(estado):
		if not (estado in self.Q):
			sys.exit("Se intento seleccionar como estado inicial el estado '%s', no existente en el automata." % estado)
			
		self.q0 = estado
	
	def agregarEstado(estado):
		if estado in self.Q:
			sys.exit("Se intento agregar el estado '%s' ya existente en el automata." % estado)
		
		self.Q.add(estado)
		for simbolo in self.Sigma:
			self.Delta[estado][simbolo] = 'qT'
			
	def agregarFinal(estado):
		if not (estado in self.Q):
			sys.exit("Se intento agregar a los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.add(estado)
			
	def removerFinal(estado):
		if not (estado in self.Q):
			sys.exit("Se intento remover de los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.remove(estado)
		
	def setearArista(estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento poner una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento poner una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento poner una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo] = estado2
		
class AutomataNoDet(object):
	def __init__(self, sigma = None):
		self.Q = { 'qT' }
		if sigma is None:
			self.Sigma = Set(string.letters + string.digits + "[,:;.?!()\"\'\\&-]" + " " + "\t")			
		else:
			self.Sigma = Set(sigma)
			
		self.Sigma.add('lambda')
		
		self.F = Set(sigma)
		self.q0 = 'qT'
		self.Delta = { 'qT' : {}}
		for simbolo in self.Sigma:
			self.Delta['qT'][simbolo] = {}
			
	def setearInicial(estado):
		if not (estado in self.Q):
			sys.exit("Se intento seleccionar como estado inicial el estado '%s', no existente en el automata." % estado)
			
		self.q0 = estado	
			
	def agregarEstado(estado):
		if (estado in self.Q):
			sys.exit("Se intento agregar el estado '%s' ya existente en el automata." % estado)
		
		self.Q.add(estado)
		for simbolo in self.Sigma:
			self.Delta[estado][simbolo] = {}
			
	def agregarFinal(estado):
		if not (estado in self.Q):
			sys.exit("Se intento agregar a los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.add(estado)
			
	def removerFinal(estado):
		if not (estado in self.Q):
			sys.exit("Se intento remover de los estados finales el estado '%s', no existente en el automata." % estado)
			
		self.F.remove(estado)
		
	def agregarArista(estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento agregar una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento agregar una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento agregar una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo].add(estado2)
		
	def removerArista(estado1, simbolo, estado2):
		if not (estado1 in self.Q):
			sys.exit("Se intento remover una arista desde el estado '%s', no existente en el automata." % estado1)
			
		if not (simbolo in self.Sigma):
			sys.exit("Se intento poner una arista con el simbolo '%s', no existente en el alfabeto." % simbolo)
			
		if not (estado2 in self.Q):
			sys.exit("Se intento poner una arista hacia el estado '%s', no existente en el automata." % estado2)
		
		self.Delta[estado1][simbolo].remove(estado2)