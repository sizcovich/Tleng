# -*- coding: utf-8 -*- 
#!/usr/bin/python

from parsear import importarDeArchivo

def pertenece_al_lenguaje(archivo_automata, cadena):
	automata = importarDeArchivo(archivo_automata)

	if automata.acepta(cadena):
		print("TRUE")
	else:
		print("FALSE")