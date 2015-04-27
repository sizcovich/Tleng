# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from serializar import exportarAArchivo
from construirDet import construirComplemento
from minimizar import minimizar

def complemento(archivo_automata_in, archivo_automata_out):
	automata = importarDeArchivo(archivo_automata_in)
	complemento = complementar(automata)
	exportarAArchivo(complemento, archivo_automata_out)

def complementar(automata):	
	return minimizar(construirComplemento(automata))