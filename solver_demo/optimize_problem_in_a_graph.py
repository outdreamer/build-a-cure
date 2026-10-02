# 'Implement interface analysis', by 'defining/standardizing problems/solutions/optimizations to a graph structure', so that 'optimizations can be applied to a problem in a graph', until a 'solution in the graph is generated/identified'

""" High-level summary:
	1. creates a graph of the problem definition
	2. creates a solution_structure from the solution_definition (as in 'what structure the solution would look like if integrated into the graph')
	3. defines optimization components (like the 'graph definition of uniqueness', as in 'what structure uniqueness would look like if integrated into the graph')
	4. defines optimization structures (like a 'way to change a graph to optimize for uniqueness', as in 'what structures would increase the uniqueness in a graph')
	5. applies optimizations to the graph to increase/create those components in the graph (applies a 'uniqueness optimization' to 'increase uniqueness in the graph')
	6. checks if the applied optimizations created the solution_structure in the optimized graph
"""

""" example specifications to implement a 'uniqueness checking function', starting from the 'structural component of the definition of uniqueness (the count of a specific item in a set is 1)'
	- 'count of a specific item in a set is 1' # identify the specific structural component of the definition
	- 'count of "what item in what set" is 1' # identifying unspecified variables to specify constants for
	- 'count of "solution_item in this_list" is 1' # apply specific variable names
	- 'len("solution_item in this_list") == 1' # general syntax
	- 'len([item for item in list if item == solution_item]) == 1' # specific syntax
"""
import networkx as nx
from utils import get_nouns

# implement a structure as a 'standard' or 'dependency' graph
def generate_dependency_graphs(structure1, structure2):
	causal_keywords = ['cause', 'result', 'input', 'output', 'create', 'require', 'depend', 'effect']
	graph1, graph2 = nx.DiGraph(), nx.DiGraph() # directed/causal graph
	for sentence in structure1.split('. '):
		if len([cause_keyword for cause_keyword in cause_keywords if cause_keyword in sentence]) > 0:
			item1, item2 = get_nouns(sentence)
			graph1.add_nodes_from([item1, item2])
			graph1.add_edges_from([(item1, item2)])
	for sentence in structure2.split('. '):
		if len([cause_keyword for cause_keyword in cause_keywords if cause_keyword in sentence]) > 0:
			item1, item2 = get_nouns(sentence)
			graph2.add_nodes_from([item1, item2])
			graph2.add_edges_from([(item1, item2)])
	return graph1, graph2

def generate_standard_graphs(structure1, structure2):
	graph1, graph2 = nx.Graph(), nx.Graph() 
	for sentence in structure1.split('. '):
		item1, item2 = get_nouns(sentence)
		graph1.add_nodes_from([item1, item2])
		graph1.add_edges_from([(item1, item2)])
	for sentence in structure2.split('. '):
		item1, item2 = get_nouns(sentence)
		graph2.add_nodes_from([item1, item2])
		graph2.add_edges_from([(item1, item2)])
	return graph1, graph2

def dependency_graph_sequence_position_similarity(structure1, structure2):
	# check if the structures are similar in causality, by checking if their dependency graphs overlap
	graph1, graph2 = generate_dependency_graphs(structure1, structure2)
	# check each dependency graph for sequence/position similarity
	graph1_sequences = get_graph_sequences(graph1)
	graph2_sequences = get_graph_sequences(graph2)
	return identify_graph_overlap(graph1_sequences, graph2_sequences)

def general_variant_application_usage_similarity(structure1, structure2):
	# check if the structures are similar in intent, by checking if their graphs are 'general/specific variants' of each other
	# or check if the structures can be 'used for similar intents or applied similarly (have similar outputs)'
	graph1, graph2 = generate_standard_graphs(structure1, structure2)
	# check if either graph is a general variant/application/usage of the other graph
	# indicating one is an intent and the other is an implementation
	graph1_sequences = get_graph_sequences(graph1)
	graph2_sequences = get_graph_sequences(graph2)
	return identify_graph_generality(graph1, graph2, graph1_sequences, graph2_sequences)

def optimality_definition_component_similarity(structure1, structure2):
	# check if the structures are similar in optimality, by comparing their 'similarity to/overlap with/implementation of the graph of the definition of optimality'
	graph1, graph2 = generate_standard_graphs(structure1, structure2)
	# identify the overlap/general similarity of each graph to the 'graph of the definition of optimality'
	# check if the pair of graphs is 'similar in optimality (as in, similar in similarity to the optimality graph)'
	optimality_graph_sequences = get_graph_sequences(optimality_graph)
	graph1_sequences = get_graph_sequences(graph1)
	graph2_sequences = get_graph_sequences(graph2)
	graph1_optimality_similarity = (identify_graph_generality(graph1, optimality_graph, graph1_sequences, optimality_graph_sequences) + identify_graph_overlap(graph1_sequences, optimality_graph_sequences)) / 2
	graph2_optimality_similarity = (identify_graph_generality(graph2, optimality_graph, graph2_sequences, optimality_graph_sequences) + identify_graph_overlap(graph2_sequences, optimality_graph_sequences)) / 2
	return (graph1_optimality_similarity + graph2_optimality_similarity) / 2

def get_graph_sequences(graph):
	cutoff = 3
	all_paths = []
	for source in graph.nodes():
		for target in graph.nodes():
			paths = list(nx.all_simple_paths(graph, source=source, target=target, cutoff=cutoff))
			all_paths.extend(paths)
	return all_paths

def identify_graph_overlap(graph1_sequences, graph2_sequences):
	# check if one graph overlaps with the other graph
	# generate sequences of the graph and check the number of 'exact/similar sequences in common'
	# find intersection of the two graphs
	intersection = [item for item in graph1_sequences if item in graph2_sequences]
	return len(intersection) / len(graph1_sequences)

def get_general_node(node):
	# identify generality of a synonym, like 'does it (or its synonyms) have a greater number of synonyms than other synonyms'
	synonyms = get_synonyms(node)
	max_synonyms = 0
	general_synonym = None
	for syn in synonyms:
		sub_synonyms = get_synonyms(syn)
		if len(sub_synonyms) > max_synonyms:
			general_synonym = syn
			max_synonyms = len(sub_synonyms)
	return general_synonym if general_synonym is not None else node

def get_general_graph(graph):
	# requires a 'type graph' or a 'definition similarity graph'
	general_graph = nx.Graph()
	for node in graph.nodes():
		general_node = get_general_node(node)
		general_graph.add_nodes_from([general_node])
	for edge in graph.edges():
		general_node_0 = get_general_node(edge[0])
		general_node_1 = get_general_node(edge[1])
		general_graph.add_edges_from([(general_node_0, general_node_1)])
	return general_graph

def identify_graph_generality(graph1, graph2, graph1_sequences, graph2_sequences):
	# check if one graph is a generalization of the other graph
	# generate sequences of the graph, generate generalizations of the sequences
	# then check if the general sequences overlap with the sequences of the other graph
	general_graph1 = get_general_graph(graph1)
	general_graph2 = get_general_graph(graph2)
	general_graph1_sequences = get_graph_sequences(general_graph1)
	general_graph2_sequences = get_graph_sequences(general_graph2)
	overlap_similarity1 = identify_graph_overlap(general_graph1_sequences, graph2_sequences)
	overlap_similarity2 = identify_graph_overlap(graph1_sequences, general_graph2_sequences)
	overlap_similarity3 = identify_graph_overlap(general_graph1_sequences, general_graph2_sequences)
	overlap_similarity4 = identify_graph_overlap(graph1_sequences, graph2_sequences)
	return (overlap_similarity1 + overlap_similarity2 + overlap_similarity3 + overlap_similarity4) / 4

def identify_interface_similarity(structure1, structure2):	
	# iterate through a list of interface similarities, and check the pair of graphs for each interface similarity
	similarity_scores = []
	for similarity_type, similarity_function_name in interface_similarities.items():
		exec(similarity_function_name)
		similarity_score = similarity_function_name(structure1, structure2)
		if similarity_score > 0.1:
			similarity_scores.append(similarity_score)
	# to do: aggregate/weight the similarities by relevance
	return len(similarity_scores) / len(interface_similarities.keys())

def match(structure_to_match, structure_or_function):
	# iterates through a list of functions/structures, graphs them, and checks if any are 'interface similar' to the input structure_to_match
	# to do: check primarily for 'specification' by weighting the 'general_variant_application_usage_similarity' score more highly
	list_to_iterate = generated_public_functions if structure_or_function == 'function' else generated_public_structures
	scores = {}
	for item in list_to_iterate:
		# the similarities being checked include:
		# dependency_graph_sequence_position_similarity: checks if graph1 and graph2 have a 'high ratio of causal sequences in common'
		# general_variant_application_usage_similarity: checks whether graph1 is a 'general variant' of graph2 or vice versa
		# optimality_definition_component_similarity: checks which graph is 'more similar to the optimality graph' (which graph is more optimal)
		scores[item] = identify_interface_similarity(item, structure_to_match)
	top_match = None
	top_score = 0
	for f, s in scores.items():
		if s > top_score:
			top_score = s
			top_match = f
	return top_match

def run_code(function_name, *args, **kwargs):
	func = FUNCTION_REGISTRY.get(function_name)
	if callable(func):
		return func(*args, **kwargs)
	else:
		raise ValueError(f"Function '{function_name}' not found in registry.")

optimality_graph = [
	['uniqueness', 'required', 'important', 'direct', 'adjacent'], # components
	['uniqueness and required', 'important and adjacent'], # combinations/sequences/structures of components
	['uniqueness, applied to solve a general problem type, like conflict resolution'] # other optimization-specification structures like 'interactions with general problem types'
]
interface_similarities = {
	'causal': 'dependency_graph_sequence_position_similarity',
	'intent': 'general_variant_application_usage_similarity',
	'optimality': 'optimality_definition_component_similarity'
}

# to do: generate/identify graphs/functions
generated_public_structures = [] 
generated_public_functions = []

optimality_definition = ['uniqueness', 'directness']
graph_component_definition = {
	'uniqueness': 'only list in the graph list with this exact pair of elements in this exact sequence',
	'directness': 'there is a list in the graph list including the source/definition node in the list'
}

problem_definition = "the problem is 'a is directly connected to b' and 'b is directly connected to c' but there is no direct connection between 'a and c'"
solution_definition = "the graph has a direct connection between a and c"

# change 'concepts/definitions' into 'implementations/specifications' by changing them into 'similar functions/graphs'

# 1. change problem_definition into graph_of_problem_definition
#graph_of_problem_definition = match(problem_definition, 'structure')
graph_of_problem_definition = [['A','B'],['B','C']]
problem_graph = nx.Graph()
for sublist in graph_of_problem_definition:
	problem_graph.add_nodes_from(sublist)
	problem_graph.add_edges_from([(sublist[0], sublist[1])])

# 2. change solution_definition into solution_structure
#solution_structure = match(solution_definition, 'structure')
solution_structure = ['A','C']

# 3. change graph_component_definition (linguistic definitions of components) into code_statements (code defining each component in a graph structure)

#code_statements = match(graph_component_definition, 'function')

# only list in the graph list with this exact pair of elements in this exact sequence': 
def identify_uniqueness(graph, solution_structure):
	return len([item for item in graph.edges() if solution_structure[0] in item and solution_structure[1] in item]) == 1

# there is a sublist in the graph list including the source/definition node in the list': 
def identify_directness(graph, solution_structure):
	return len([item for item in graph.edges() if solution_structure[0] in item and solution_structure[1] in item]) > 0

# 4. change component (uniqueness) into optimizations (code implementing a uniqueness increase)

#optimizations = match(component, 'function')
def optimize_uniqueness(graph):
	new_graph = nx.Graph()
	for node in graph.nodes():
		if not new_graph.has_node(node):
			new_graph.add_nodes_from([node])
	for edge in graph.edges():
		if new_graph.has_node(edge[0]) and new_graph.has_node(edge[1]):
			new_graph.add_edge(edge[0], edge[1])
	return new_graph

def optimize_directness(graph):
	import random
	from itertools import combinations

	def identify_new_item(graph):
		pairs = [list(c) for c in combinations(graph.nodes(), 2)]
		new_item = random.choice(pairs)
		if not graph.has_edge(new_item[0], new_item[1]):
			return new_item
		return identify_new_item(graph)

	new_item = identify_new_item(graph)
	print('new_item', new_item)
	graph.add_edge(new_item[0], new_item[1])
	return graph

FUNCTION_REGISTRY = {
	"identify_uniqueness": identify_uniqueness,
	"identify_directness": identify_directness,
	"optimize_uniqueness": optimize_uniqueness,
	"optimize_directness": optimize_directness,
}

# 5. optimize the graph of the problem until it has the solution_structure
print('original nodes', problem_graph.nodes())
print('original edges', problem_graph.edges())

solution_found = False
for component in optimality_definition:
	print('checking/optimizing for component', component)
	application = run_code(f"identify_{component}", problem_graph, solution_structure)
	if application is False:
		# the graph_of_problem_definition doesnt already implement the solution structure
		# meaning the solution structure doesnt have this optimization component (such as 'uniqueness')
		# so apply optimizations to the graph and re-check for the solution_structure		
		problem_graph = run_code(f"optimize_{component}", problem_graph)
		print('optimized nodes', problem_graph.nodes())
		print('optimized edges', problem_graph.edges())
		optimized_application = run_code(f"identify_{component}", problem_graph, solution_structure)
		if optimized_application is not False:
			# 6. check if the optimized_graph now has the solution structure
			if solution_structure in problem_graph.edges():
				print('found_solution in optimized graph', problem_graph)
				solution_found = True
	else:
		print('graph', graph, 'already contains solution_structure', solution_structure)

if solution_found is False:
	print('no solution', solution_structure, 'found in optimized graph', problem_graph)