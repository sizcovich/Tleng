# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo
from complementar import complementar
from serializar import exportarAArchivo

def complemento(archivo_automata_in, archivo_automata_out):

	automata = importarDeArchivo(archivo_automata_in)
	complemento = complementar(automata)
	exportarAArchivo(complemento, archivo_automata_out)