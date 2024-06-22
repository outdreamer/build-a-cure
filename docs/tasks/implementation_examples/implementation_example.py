import itertools


'''

- to do

	- add properties to objects (graph.connect, structure1.interface_variable)

'''

# 1. identify relevant structures which are connectible bc of an abstract similarity (like 'intents/structures')

# identify interface_variables
interface_variables = ['position', 'structure', 'size']

# identify useful problem-solving intents
useful_intents = ['identify new variables', 'identify new interface']

# identify interface structures that can describe interactions/connections between useful structures and useful intents and which can be used to generate new useful structures
interface_structures = ['overlap', 'adjacency']

# identify graphs that can connect interface structures
graphs = ['2-d graphs of concepts involving comparisons like volatility (involving a comparison of extreme adjacent changes/unpredictability)', '2-d concept graph like volatility compared to variation', 'system layer graph', 'abstract concept definition connection network', 'abstract-specific concept network']

# identify useful structures which still have value (the most useful recent graphs/networks identified)
useful_structures = ['abstract similarities', 'similarity sequences', 'abstract-specific sequences', 'relevance definitions']
useful_structures.extend(graphs)

# 2. apply interface structures to generate new useful structures
new_generated_useful_structures = list(itertools.combinations(useful_structures.extend(interface_structures), 5))


# 3. iterate through abstract similarity item 1 (useful intents)

for intent in useful_intents:

	# 4. iterate abstract similarity item 2 (new_generated_useful_structure)

	for new_generated_useful_structure in new_generated_useful_structures:

		# 5. iterate connection structures (interface structures)

		for interface_structure in interface_structures:

			# 6. check if this interface structure can connect this new generated useful structure and this useful intent on some graph

			connecting_graph = connect(intent, new_generated_useful_structure, interface_structure)

			if connecting_graph:
				# if there is a graph where this is connectible using this structure
				# that means we identified a new generated useful structure that fulfills this intent (to some degree
				# depending on the interface variables of their connection)

'''
- another algorithm would be;
	'apply interface structures to useful intents to generate new intents, 
	identify if these intents are connectible to existing useful structures (like relevance definitions), 
	to identify if these intents are useful'

- this fulfills the general problem-solving intent 'identify new variation' 
	with new specific intents (identify new useful intents, identify new useful structures) 
	using specific useful structures like 'abstract similarities' (like 'intent/structure')
	to match required variation (new directions) in structures that can provide it (new intents)

'''

def connect(structure1, structure2, connection_structure):

	# iterate through graphs to identify a graph where this connection_structure can connect this structure set

	for graph in graphs:
		
		applied = apply(structure1, connection_structure, graph)
		
		# once the connection_structure is applied, check for an equivalence/similarity (like in its position)

		if equals_or_similar(applied, structure2):
		
			# this connection_structure can create structure2 (in some way, like its position), from structure1, on this graph
			return graph

    return False


def apply(structure1, connection_structure, graph):

	# identify the combine/addition/connection operation on this graph and apply it
	combined = run(graph.connect, structure1, connection_structure, graph)

	return combined

def equals_or_similar(structure1, structure2):

	for interface_variable in interface_variables:

		# if structure1 and structure2 have a similarity in interface_variables like 'position' or 'structure'
		if similarity(structure1, structure2, interface_variable):

			return True

	return False

def similarity(structure1, structure2, interface_variable):

	# determine the variable like position of structure1/2
	structure1_interface_variable = structure1.interface_variable
	structure2_interface_variable = structure2.interface_variable

	if (structure1_interface_variable/structure2_interface_variable) > 0.5 and (structure1_interface_variable/structure2_interface_variable) < 1.5:
		return True

	return False