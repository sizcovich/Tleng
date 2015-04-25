# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeRegex
from determinizar import determinizar
from minimizar import minimizar
from serializar import exportarAArchivo

def afd_minimo(archivo_regex, archivo_automata, minimize):
	automata = importarDeRegex(archivo_regex)
	automata = determinizar(automata)
	if minimize:
		automata = minimizar(automata)
	exportarAArchivo(automata, archivo_automata)