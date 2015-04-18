from sets import Set
import string

class AutomataDet(object):
	def __init__(self):
		self.Q = { 'qT' }
		self.Sigma = set(string.letters + string.digits + "[,:;.?!()\"\'\\&-]" + " " + "\t")
		self.F = Set([])
		self.q0 = 'qT'
		self.Delta = { 'qT' : {}}
		for simbolo in self.Sigma:
			self.Delta['qT'][simbolo] = 'qT'
	
	def agregarEstado(estado):
		if estado in self.Q
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
		
class AutomataNoDet(object):
	def __init__(self):
		self.Q = { 'qT' }
		self.Sigma = set(string.letters + string.digits + "[,:;.?!()\"\'\\&-]" + " " + "\t")
		self.F = Set([])
		self.q0 = 'qT'
		self.Delta = { 'qT' : {}}
		for simbolo in self.Sigma:
			self.Delta['qT'][simbolo] = {}
			
	def agregarEstado(estado):
		if (estado in self.Q)
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