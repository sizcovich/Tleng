from ejercicio_a import afd_minimo
from ejercicio_b import pertenece_al_lenguaje
from ejercicio_c import grafo
from ejercicio_d import interseccion
from ejercicio_e import complemento
from ejercicio_f import equivalentes
from AFD import archivo_para_leer
from automata import AutomataDet
from construirDet import construirInterseccion
from algoritmos import minimizar
from algoritmos import equivalencia
from construirDet import construirComplemento

if __name__ == "__main__":

########################### test ejercicio_a ########################### 	
	#python AFD.py -leng ejemplo4.in -aut salida.out
	#devuelve error por que el OR deberia tener un 2 y no un 1

	#python AFD.py -leng ejemplo1.in -aut automata1.in
	#genera correctamente el automata1.in

########################### test ejercicio_b ########################### 	

	archivo_automata = archivo_para_leer('automata1.in')
	
	cadena = 'def' #cadena valida
	pertenece_al_lenguaje(archivo_automata, cadena) # imprime True
	
	cadena = 'simbolosinexistentes' #con simbolos que no existen
	pertenece_al_lenguaje(archivo_automata, cadena) # imprime False
	
	cadena = 'aaa' #sin estado final
	pertenece_al_lenguaje(archivo_automata, cadena) # imprime False
	
########################### test ejercicio_d ########################### 	

	automata1 = AutomataDet("ab")
	automata1.agregarEstado('q0')
	automata1.agregarEstado('q1')
	automata1.agregarEstado('q2')
	automata1.setearInicial('q0')
	automata1.agregarFinal('q1')
	automata1.setearArista('q0', 'b', 'q1')
	automata1.setearArista('q0', 'a', 'q2')
	
	interseccion = minimizar(construirInterseccion(automata1, automata1))
	print equivalencia(automata1,interseccion)

	automata2 = AutomataDet("ab")
	automata2.agregarEstado('q0')
	automata2.agregarEstado('q1')
	automata2.agregarEstado('q2')
	automata2.setearInicial('q0')
	automata2.agregarFinal('q1')
	automata2.setearArista('q0', 'b', 'q1')
	automata2.setearArista('q0', 'a', 'q2')
	automata2.setearArista('q1', 'a', 'q2')

	interseccion = minimizar(construirInterseccion(automata1, automata2))
	print equivalencia(automata1,interseccion)

	automata3 = AutomataDet("ab")
	automata3.agregarEstado('q0')
	automata3.agregarEstado('q1')
	automata3.setearInicial('q0')
	automata3.agregarFinal('q1')
	automata3.setearArista('q0', 'a', 'q1')

	automata4 = AutomataDet("ab")
	automata4.agregarEstado('q0')
	automata4.agregarEstado('q1')
	automata4.agregarEstado('q2')
	automata4.setearInicial('q0')
	automata4.agregarFinal('q1')

	interseccion = minimizar(construirInterseccion(automata1, automata3))
	print equivalencia(automata4,interseccion)

########################### test ejercicio_e ########################### 	

	automata1 = AutomataDet("ab")
	automata1.agregarEstado('q0')
	automata1.agregarEstado('q1')
	automata1.agregarEstado('q2')
	automata1.setearInicial('q0')
	automata1.agregarFinal('q1')
	automata1.setearArista('q0', 'b', 'q1')
	automata1.setearArista('q0', 'a', 'q2')
	
	complemento = minimizar(construirComplemento(automata1))
	cadena = 'b' #cadena valida en automata1
	print (automata1.acepta(cadena) == True)
	print (complemento.acepta(cadena) == False)

	cadena = 'a' #cadena invalida en automata1
	print (automata1.acepta(cadena) == False)
	print (complemento.acepta(cadena) == True)