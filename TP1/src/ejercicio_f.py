# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from igualar import igualar

def equivalentes(archivo_automata_in1, archivo_automata_in2):

	automata1 = importarDeArchivo(archivo_automata_in1)
	automata2 = importarDeArchivo(archivo_automata_in2)
	
	if igualar(automata1, automata2):
		print("TRUE")
	else:
		print("FALSE")