# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from serializar import exportarAArchivo
from construirDet import construirComplemento
from algoritmos import minimizar

def complemento(archivo_automata_in, archivo_automata_out):
	automata = importarDeArchivo(archivo_automata_in)
	complemento = minimizar(construirComplemento(automata))
	exportarAArchivo(complemento, archivo_automata_out)