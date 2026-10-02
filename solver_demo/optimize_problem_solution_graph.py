# Optimize Problem/Solution Graph

# a script to 'generate a problem/solution graph' and 'identify suboptimalities of the graph' and 'generate optimizations of the graph'
# generate a set of problems/solutions, graph them by some similarity (like 'verb/noun/type/problem difference/structure similarity')
# then identify 'suboptimalities' like 'problems/solutions which are too similar (like having a causal similarity)' (problems/solutions are 'opposite' structures by definition, so they should be different in the graph)

import networkx as nx
from utils import get_synonyms

interface_structures = [
	'cause', 'change', 'definition', 'requirement', 'logic', 'concept', 'meaning', 'similarity', 'limit', 'variable', 
	'structure', 'function', 'intent', 'graph', 'connection', 'filter', 'reduction', 'expansion', 'set', 'sequence'
]

def compare(problems, solutions):
	problem_synonym_overlaps = {} # similarity scores for problem i and problem j
	for i, problemi in enumerate(problems):
		problemi_synonyms = get_synonyms(problemi)
		for j, problemj in enumerate(problems):
			problemj_synonyms = get_synonyms(problemj)
			if problemi != problemj:
				#print('problemi', problemi, problemi_synonyms)
				#print('problemj', problemj, problemj_synonyms)
				problem_synonym_overlaps['_'.join([str(i),str(j)])] = len([problemi_synonym for problemi_synonym in problemi_synonyms if problemi_synonym in problemj_synonyms]) / (len(problemi_synonyms) + len(problemj_synonyms) / 2)
	solution_synonym_overlaps = {} # similarity scores for solution i and solution j
	for i, solutioni in enumerate(solutions):
		solutioni_synonyms = get_synonyms(solutioni)
		for j, solutionj in enumerate(solutions):
			solutionj_synonyms = get_synonyms(solutionj)
			if solutioni != solutionj:
				solution_synonym_overlaps['_'.join([str(i),str(j)])] = len([solutioni_synonym for solutioni_synonym in solutioni_synonyms if solutioni_synonym in solutionj_synonyms]) / (len(solutioni_synonyms) + len(solutionj_synonyms) / 2)
	problem_solution_synonym_overlaps = {} # similarity scores for problem i and solution j
	for i, problemi in enumerate(problems):
		problemi_synonyms = get_synonyms(problemi)
		for j, solutionj in enumerate(solutions):
			solutionj_synonyms = get_synonyms(solutionj)
			if problemi != solutionj:
				problem_solution_synonym_overlaps['_'.join([str(i),str(j)])] = len([problemi_synonym for problemi_synonym in problemi_synonyms if problemi_synonym in solutionj_synonyms]) / (len(problemi_synonyms) + len(problemj_synonyms) / 2)
	return problem_synonym_overlaps, solution_synonym_overlaps, problem_solution_synonym_overlaps

def generate_graph(ai_problems, ai_solutions):
	# currently determining cause by a 'high ratio of synonyms'
	# to do: add a real causal identification function, like 'identifying inputs that are similar in synonym to outputs'
	problem_similarities, solution_similarities, problem_solution_similarities = compare(ai_problems, ai_solutions)
	graph = nx.DiGraph() # directed/causal graph
	graph.add_nodes_from(ai_problems)
	graph.add_nodes_from(ai_solutions)
	for i_j, ratio in problem_similarities.items():
		i, j = int(i_j.split('_')[0]), int(i_j.split('_')[1])
		if ratio > 0.1:
			graph.add_edges_from([(ai_problems[i], ai_problems[j])])
	for i_j, ratio in solution_similarities.items():
		i, j = int(i_j.split('_')[0]), int(i_j.split('_')[1])
		if ratio > 0.1:
			graph.add_edges_from([(ai_solutions[i], ai_solutions[j])])
	for i_j, ratio in problem_solution_similarities.items():
		i, j = int(i_j.split('_')[0]), int(i_j.split('_')[1])
		if ratio > 0.1:
			graph.add_edges_from([(ai_problems[i], ai_solutions[j])])
	return graph

def get_cause(graph_node, graph):
	# identify the first causal node of the graph_node in the directed graph
	try:
	    predecessors = list(graph.predecessors(graph_node))
	    #print(f"Predecessors of {graph_node}: {predecessors}")
	    if len(predecessors) > 0:
		    return predecessors[0]
	except nx.NetworkXError as e:
	    print(f"Error: {e}")
	return False 

def get_interface(definition):
	for interface in interface_structures:
		if interface in definition:
			return interface
	return False

def identify_suboptimalities(graph):
	# identify where problems are similar to solutions, similar in a simple/irrelevant structure like "similar cause/requirement" rather than "relevant impact/interaction"
	# like 'identify an ai_problem that has a similar cause as an ai_solution'
	graph_suboptimalities = {}
	for ai_problem in ai_problems:
		for ai_solution in ai_solutions:
			for suboptimality_definition in suboptimality_definitions:
				interface = get_interface(suboptimality_definition) # returns 'cause'
				if 'equal' in suboptimality_definition:
					# meaning 'check if the first causal graph node of ai_problem is the same first causal graph node of ai_solution'
					if run_code(f"get_{interface}", ai_problem, graph) == run_code(f"get_{interface}", ai_solution, graph):
						graph_suboptimalities[suboptimality_definition] = [ai_problem, ai_solution]
				else:
					if run_code(f"get_{interface}", ai_problem, graph) != run_code(f"get_{interface}", ai_solution, graph):
						graph_suboptimalities[suboptimality_definition] = [ai_problem, ai_solution]
	return graph_suboptimalities

def standardize(structure, interface_vocabulary):
	# compare 'standardize' to 'match' function in optimize_problem_in_a_graph ('match' finds specifying/implementing functions of an input structure by comparing their graphs')
	# function to specify a structure to some interface, using the interface_vocabulary
	# creates a graph of interface_vocabulary, then checks if 'structure' is similar to any terms/structures in that vocabulary/graph, then changes 'structure' to the 'similar term/structure in the vocabulary/graph'
	return False

def run_code(function_name, *args, **kwargs):
	func = FUNCTION_REGISTRY.get(function_name)
	if callable(func):
		return func(*args, **kwargs)
	else:
		raise ValueError(f"Function '{function_name}' not found in registry.")

def apply_optimization1(graph, problem, solution): 
	problem_causal_node = get_cause(problem, graph)
	solution_causal_node = get_cause(solution, graph)
	other_problem_nodes = [node for node in graph if node not in [problem_causal_node, solution_causal_node, problem, solution] and node in ai_solutions]
	graph.add_edges_from([(solution, other_problem_nodes[0])])
	if graph.has_edge(solution, solution_causal_node):
		graph.remove_edge(solution, solution_causal_node)

def apply_optimizations(graph, suboptimalities):
	optimizations = ['differentiate problems and solutions, in a relevant structure to differentiate, like "interaction/intent/usage/requirement/cause"']
	graph_optimizations = ['differentiate a problem node and a solution node, if they have the same first causal node, like by adding nodes in between to either the problem node or solution node']
	structural_graph_optimizations = ['add a causal node to the problem node or solution node']
	code_graph_optimizations = ['apply_optimization1']

	# to do: fill out vocabulary graphs so that 'similar terms' (like the above optimization specifications) can be identified across vocabularies
	graph_interface_vocabulary = []
	structural_graph_interface_vocabulary = []
	code_graph_interface_vocabulary = []

	for suboptimality, problem_solution in suboptimalities.items():
		for i, optimization in enumerate(optimizations):
			# apply a relevant difference to problems/solutions that are 'irrelevantly similar in cause/requirement' to make problems/solutions more clearly different
			#graph_optimization = standardize(optimization, graph_interface_vocabulary)
			graph_optimization = graph_optimizations[i]
			#structural_graph_optimization = standardize(graph_optimization, structural_graph_interface_vocabulary)
			structural_graph_optimization = structural_graph_optimizations[i]
			#code_graph_optimization = standardize(structural_graph_optimization, code_graph_interface_vocabulary)
			code_graph_optimization = code_graph_optimizations[i]
			problem = problem_solution[0]
			solution = problem_solution[1]
			run_code(code_graph_optimization, graph, problem, solution) # add node in between the solution and the causal node, to distance it from the causal node as the problem node
	return graph

FUNCTION_REGISTRY = {
	"apply_optimization1": apply_optimization1,
	"get_cause": get_cause
}
suboptimality_definitions = ['equal_problem_solution_cause'] 
ai_problems = ['vanishing gradient problem', 'optimization plateaus', 'lack of good data', 'over-fitting', 'lack of interpretability']
ai_solutions = ['weight initialization', 'optimizing the definition of optimality', 'gathering more data', 'regularization', 'integrating interface structure graphs in models for interpretability']
graph = generate_graph(ai_problems, ai_solutions)
print('\ngraph: \n\tnodes', graph.nodes(), '\n\tedges', graph.edges())
suboptimalities = identify_suboptimalities(graph)
optimized_graph = apply_optimizations(graph, suboptimalities)
print('\noptimized_graph: \n\tnodes', optimized_graph.nodes(), '\n\tedges', optimized_graph.edges())

# now there is a new edge, bc the optimization function 'apply_optimization1' adds an edge between a solution node and another solution node, 
# to differentiate it more from the problem node that it shares a predecessor with, 
# thereby 'applying a difference between problem/solution nodes'