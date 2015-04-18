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
			
class AutomataNoDet(object):
	def __init__(self):
		self.Q = { 'qT' }
		self.Sigma = set(string.letters + string.digits + "[,:;.?!()\"\'\\&-]" + " " + "\t")
		self.F = Set([])
		self.q0 = 'qT'
		self.Delta = { 'qT' : {}}
		for simbolo in self.Sigma:
			self.Delta['qT'][simbolo] = { 'qT' }