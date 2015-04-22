# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from serializar import exportarADot

def grafo(archivo_automata, archivo_dot):

	automata = importarDeArchivo(archivo_automata)
	exportarADot(automata, archivo_dot)