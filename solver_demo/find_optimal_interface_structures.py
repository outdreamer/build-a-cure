# Generate and Filter 'Structures of Interface Structures' for 'Optimality'

# a script to 1. 'generate interface structure combinations' and 2. 'filter those combinations using the definition of relevance/optimality'
# like how a 'generated interface structure' like:
# 'specify the definition/requirement/intent' and 'connect problem/solution definition' are optimal, 
# bc they optimize the 'implement' function

# similarly, apply interface analysis iterations to a useful degree:
# 'identify interface structures like errors/limits/optimizations of a structure'
# and apply interface analysis iteratively to identify 'emergent structures' like 'emergent problems/solutions' in the 'generated structures of the structure'

import networkx as nx
from itertools import combinations
from utils import get_synonyms

problems = ['problem', 'limit', 'error', 'conflict', 'inferior', 'different', 'useless', 'meaningless', 'irrelevant']
solutions = ['optimal', 'solution', 'target', 'goal', 'objective', 'intent', 'useful', 'meaningful', 'relevant']
interface_structures = [
	'cause', 'change', 'definition', 'requirement', 'logic', 'concept', 'meaning', 'similarity', 'limit', 'variable', 
	'structure', 'function', 'intent', 'graph', 'connection', 'filter', 'reduction', 'expansion', 'set', 'sequence'
]

def is_similar(structure, combination_of_interface_structures):
	structure_synonyms = get_synonyms(structure)
	combination_synonyms = get_synonyms(' of '.join(combination_of_interface_structures))
	similar_ratio = len([ss for ss in structure_synonyms if ss in combination_synonyms]) / len(structure_synonyms)
	return True if similar_ratio > 0.3 else False

def is_solution(combination_of_interface_structures):
	similar_to_solutions = []
	for s in solutions:
		if is_similar(s, combination_of_interface_structures):
			similar_to_solutions.append(s)
	ratio = len(similar_to_solutions) / len(solutions)
	#print('solution ratio', ratio, combination_of_interface_structures)
	return True if ratio > 0.1 else False

def is_problem(combination_of_interface_structures):
	similar_to_problems = []
	for p in problems:
		if is_similar(p, combination_of_interface_structures):
			similar_to_problems.append(p)
	ratio = len(similar_to_problems) / len(problems)
	#print('problem ratio', ratio, combination_of_interface_structures)
	return True if ratio > 0.1 else False

def is_path_more_optimal(graph, old_path, new_path):
	old_path_source = old_path.split(' ')[0]
	old_path_target = old_path.split(' ')[-1]
	new_path_source = new_path.split(' ')[0]
	new_path_target = new_path.split(' ')[-1]
	old_paths = list(nx.all_simple_paths(graph, source=old_path_source, target=old_path_target, cutoff=15))
	new_paths = list(nx.all_simple_paths(graph, source=new_path_source, target=new_path_target, cutoff=15))
	shortest_new_path = 15
	for path in new_paths:
		if len(path) < shortest_new_path:
			shortest_new_path = len(path)
	shortest_old_path = 15
	for path in old_paths:
		if len(path) < shortest_old_path:
			shortest_old_path = len(path)
	if shortest_new_path < shortest_old_path:
		return True
	return False

if __name__ == '__main__':

	# currently checking for synonym similarity with problem/solution keywords
	# to do: add 'additive logic' like to check for 'double negatives'

	# use a reduced list for the demo
	interface_structures = interface_structures[0:5]
	combinations_of_interface_structures = [list(c) for r in range(len(interface_structures)+1) for c in combinations(interface_structures, r)]
	for c in combinations_of_interface_structures:
		if len(c) > 2:
			if is_solution(c) is True or is_problem(c) is False:
				print('identified solution interface structure:', ' of '.join(c))
			elif is_solution(c) is False or is_problem(c) is True:
				print('identified problem interface structure:', ' of '.join(c))

	# example of 'additive relevance' implementation, using a generated interface structure combination (like those generated above, stored in combinations_of_interface_structures)
	generated_structure = 'limit of a limit of a problem'
	print('generated structure:', generated_structure)
	problem_points, solution_points = 0, 0
	if 'limit of a problem' in generated_structure:
		solution_points += 1
	if 'limit of a limit of a problem' in generated_structure:
		problem_points += 1
	if 'problem' in generated_structure:
		problem_points += 1
	if solution_points > problem_points:
		print('the generated structure is a solution', 'problem score', problem_points, 'solution score', solution_points)
	else:
		print('the generated structure is a problem', 'problem score', problem_points, 'solution score', solution_points)

	# example of 'identifying an optimization' implementation (check if a 'generated structure' has an 'optimization-implementing' structure (like a 'more direct path on a graph')
	implementation_definition = 'apply examples of a structure, to trivially change existing structures, until the code is runnable'
	generated_implementation_definition = 'specify the definition of a structure, until its interactive with existing functions'
	graph = nx.Graph()
	for definition in [implementation_definition, generated_implementation_definition]:
		words = definition.split(' ')
		for word in words:
			graph.add_node(word)
		# Add edges between consecutive words
		for i in range(len(words) - 1):
			graph.add_edge(words[i], words[i + 1])
	more_optimal = is_path_more_optimal(graph, implementation_definition, generated_implementation_definition)
	print('is new path more optimal than old path?', more_optimal)