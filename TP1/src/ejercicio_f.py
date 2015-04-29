# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from algoritmos import equivalencia

def equivalentes(archivo_automata_in1, archivo_automata_in2):
	automata1 = importarDeArchivo(archivo_automata_in1)
	automata2 = importarDeArchivo(archivo_automata_in2)

	if equivalencia(automata1, automata2):
		print("TRUE")
	else:
		print("FALSE")