# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from serializar import exportarAArchivo
from construirDet import construirInterseccion, renombrarEstados
from algoritmos import minimizar

def interseccion(archivo_automata_in1, archivo_automata_in2, archivo_automata_out):
	automata1 = importarDeArchivo(archivo_automata_in1)
	automata2 = importarDeArchivo(archivo_automata_in2)
	interseccion = intersectar(automata1, automata2)
	exportarAArchivo(interseccion, archivo_automata_out)
	
def intersectar(automata1, automata2):
	return renombrarEstados(minimizar(construirInterseccion(automata1, automata2)))