# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from construirDet import construirComplemento, construirInterseccion
from algoritmos import minimizar, noAceptaNingunaCadena

def equivalentes(archivo_automata_in1, archivo_automata_in2):
	automata1 = importarDeArchivo(archivo_automata_in1)
	automata2 = importarDeArchivo(archivo_automata_in2)

	if igualar(automata1, automata2):
		print("TRUE")
	else:
		print("FALSE")
		
def igualar(automata1, automata2):	
	return noAceptaNingunaCadena(minimizar(construirInterseccion(automata1, construirComplemento(automata2))))