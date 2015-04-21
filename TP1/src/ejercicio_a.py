# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeRegex
from serializar import exportarAArchivo
#from determinizar import determinizar
from minimizar import minimizar
from determinizar import determinizar

def afd_minimo(archivo_regex, archivo_automata):
	automata = importarDeRegex(archivo_regex)
	automata = determinizar(automata)
	automata = minimizar(automata)
	exportarAArchivo(automata, archivo_automata)	