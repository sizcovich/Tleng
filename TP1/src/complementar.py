from automata import AutomataDet
from minimizar import minimizar

def complementar(automata):
	nuevosFinales = automata.Q.copy()
	finales = automata.F.copy()
	#quito los estados finales del automata 
	for est in finales:
		automata.quitarFinal(est)
		nuevosFinales.remove(est)

	#agrego los nuevos estados finales
	for est in nuevosFinales:
		automata.agregarFinal(est)

	#minimizo
	return minimizar(automata)