from sets import Set

def exportarAArchivo(automata, archivo_automata):
	archivo_automata.write(automata.toString())	

def exportarADot(automata, archivo_dot):
	archivo_dot.write("strict digraph {\n")
	archivo_dot.write("rankdir=LR;\n")
	archivo_dot.write("node [shape = none, label = \"\", width = 0, height = 0]; qd;\n")
	archivo_dot.write("node [label = \"\N\", width = 0.5, height = 0.5];\n")
	archivo_dot.write("node [shape = doublecircle]; %s;\n" % " ".join(automata.F))
	archivo_dot.write("node [shape = circle];\n")
	archivo_dot.write("qd -> %s\n" % automata.q0)

	for estado in automata.Q:
		ejes = {}
		for rel in automata.Delta[estado]:
			estado2 = automata.Delta[estado][rel]
			if estado2 in ejes:
				ejes[estado2].add(rel)
			else:
				ejes[estado2] = Set(rel)

		for estado2 in ejes:
			archivo_dot.write("%s -> %s [label=\"%s\"]\n" % (estado, estado2, ", ".join(['\\\\t' if s == '\t' else s for s in ejes[estado2]])))

	archivo_dot.write("}\n")