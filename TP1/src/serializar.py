from sets import Set

def exportarAArchivo(automata, archivo_automata):
	archivo_automata.write('\t'.join(automata.Q) + '\n')
	archivo_automata.write('\t'.join(automata.Sigma) + '\n')
	archivo_automata.write(automata.q0 + '\n')
	archivo_automata.write('\t'.join(automata.F) + '\n')
	
	for estado in automata.Q:
		for rel in automata.Delta[estado]:
			archivo_automata.write('%s\t%s\t%s\n' % (estado, rel, automata.Delta[estado][rel]))

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
			archivo_dot.write("%s -> %s [label=\"%s\"]\n" % (estado, estado2, ", ".join(ejes[estado2])))
	
	archivo_dot.write("}\n")