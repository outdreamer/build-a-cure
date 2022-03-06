# these are core functions that should be using the fewest functions possible in their implementation strategy
# for example, formatting all functions in terms of the 'similarity/difference' interface 
# to use as many existing functions that identify, find, apply, build similarities/differences as possible
# and reduce the need to write other functions, given the availability of similarity-finding and differentiating
# functions.

# these functions are organized by their similarity to each other, such as how 'identify' is a variant of the 'find' function

def find(substructure, structure, find_type, output_filters={'output_count'=1}):
	''' 
	- find()
		1. looks for a substructure in a structure
	- meaning its:
		- 'checking for similarities between the structures, applying changes as needed 
	 		to find those similarities & the degree of similarity'
	- find has variants like: filter/select, identify, sort
	'''
	# apply change of 'multiple/unit' to the 'find output count' variable as find_type
	if output_filters:
		if 'solution_metric' in output_filters:
			solutions = apply(apply_structure='test', apply_params=output_filters['solution_metric'], to_structure=[substructure, structure])
		if 'output_count' in output_filters:
			if output_filters['output_count'] == 1:
				''' reduce the possible matches to one '''
				solutions = filter(substructure, structure, output_filters)
			else:
				''' reduce the possible matches '''
				solutions = filter(substructure, structure, output_filters)
	return matches

def filter(substructure, structure, output_filters):
	''' this should reduce the matches of substructure that fulfill the output_filters found in the structure
	- filter()
		1. finds the possibilities in structure that could be substructure
		2. iterates through the possibilities
		3. applies default similarity tests or other solution metric tests specified in output_filters to reduce the possibilities
	'''
	return possibilities

def identify():
	''' this should return an exact match or one match '''

def sort():
	''' this should apply a sequence to the inputs '''

def break():
	''' this should break a structure into substructures '''

def build(target_structure, available_structures, output_filters):
	''' 
	- build() 
		1. looks for existing useful (similar) components
		2. then looks for an assembly method
			to assemble those components to create the target_structure
	- meaning its:
		- 'checking for similarities in available structures, interim structures, and the target structure'
		- once it finds similarities in available structures, interim/adjacent structures, and the target structure,
			it then looks for a method to apply those similarities in a sequence of build steps to create the target structure
	- build has variants like: combine, stack, group, merge, integrate
	'''
	combinations = combine(available_structures)
	# 1. find useful similar components
	similar_combinations = filter('similarity', combinations)
	# 2. find sequence determined by these similarities
	sequentially_similar_combinations = apply(apply_structure='similarity sequence', to_structure=similar_combinations)
	# if filtering is required (like output one solution instead of multiple, or apply a solution metric test), apply those filters
	assemblies = apply(apply_structure='filter', apply_params=output_filters, to_structure=sequentially_similar_combinations)
	return assemblies

def combine():

def stack():

def group():

def aggregate():

def merge():

def integrate():

def apply(apply_structure, apply_params, to_structure, apply_output_filters):
	'''
	- apply() (change)
		1. looks for relevant attributes/functions (like 'direction' or 'change direction') of the object to alter (like 'vector') 
			that would accept the applied attribute like ('random') as input or be changed by applied function (like 'randomize')
			- if there is a known way to inject the attribute 'random' to any relevant attribute/function of the 'vector' (like the 'direction' attribute)
				this function applies that attribute to the relevant attribute/function and returns the altered version of the to_structure
			- this requires finding relevant attributes/functions which are relevant in their interactivity, as one can be an input to another
			- then applying the input to those relevant attributes/functions
		2. apply apply_structure to relevant attributes/functions of to_structure
	- apply can be used to implement a 'change' function (apply a function that changes another structure, like a variable)
	'''
	return altered_structure

def format(structure, output_filters):
	apply(apply_structure='change', apply_params=structure['format'], to_structure=structure, output_filters)

def standardize(equalize_attribute, structure):
	''' this should apply a similarity or equivalence to the structure in the attributes to equalize '''

def compare():
	''' this should return differences between inputs '''

def derive(structure, attributes, functions, output_filters):
	'''
	- derive() (predict, guess)
		is similar to find/build in its usage intents, but differs in that it:
		fulfills their functionality without the same info they require (using adjacent info),
		trying to predict/guess missing info
		- find() a solution would iterate through known possible structures & apply a test
		- build() a solution would iterate through combinations & apply a test
		- derive() a solution would try to construct a solution by applying changes to 'solution-adjacent info' (like 'solution requirements')
			- first applying combinations of solution requirements to find 'limit structures' or 'base structures' that can act like a template or interface, 
				to fill with approximate or otherwise guessed values derived by applying changes to these limit/base template/interface structures
		- for example, to find a route connecting two points:
			- find could list all possible routes, iterate through them, and test each one
			- derive would not have the info of 'all possible routes', but would try to derive it with adjacent info 
				- adjacent info could be definitions, solution components, or solution requirements,	
					as well as adjacent applied changes to those definitions/components/requirements
				- apply the definition of a route to get a 'route template'
				- apply variables to get different routes fulfilling this template
				- find a route-filtering/testing function that can filter/test routes for a metric
			- derive might not return a possible route, whereas find would if one route was a possible solution
			- derive might instead return a solution-finding method that would reduce the solution space to some degree, 
				if it lacks the info to construct a possible solution from adjacent info
	'''

''' these functions are called by the above functions '''

def equalize(source, target, equivalence_metric, function_metric):
	''' this function should:
		1. compare the inputs 
		2. return the attributes/functions that are similar according to the equivalence_metric
		3. or return the functions required to equalize the input source & target, according to some function metric 
	this function has variants like: 'connect' 
	'''

def differentiate(source, target, difference_metric, function_metric:
	''' this function should:
		1. compare the inputs
		2. return the attributes/functions that are different according to the difference_metric
		3. or return the functions required to differentiate the input source & target, according to some function metric
	'''

def organize(substructures, structure, output_filters):
	''' this function changes substructure positions in a structure to fulfill some metric '''

def meaning():
	''' this function applies a substructure like a 'function' (like a sentence) to a structure like a 'system' (like a language)
		to determine how the function fits in that system (how it interacts with other sentences, words, idioms)
		returning those interactions as the meaning of the subtructure in the system structure
	'''
	return interactions

def optimize(structure, metric):
	''' this function improves the input structure on some metric '''

''' to do: 

	- identify the network of these functions where apply/find/build/derive are function hubs to reduce function requirements

'''

def find_document_matches(input_keywords):
	''' the solution to 'optimize' this problem should:
		1. identify optimization structures like 'reduce steps of the function'
		3. move the find_synonyms() function to outside the loop '''
	possible_documents = get_possible_documents()
	possible_matches = []
	for document in possible_documents:
		synonyms = find_synonyms()
		input_keywords = input_keywords + synonyms
		count = [key for key in input_keywords if key in document]
		if count > 0:
			possible_matches.append(document)
	return possible_matches
	
def solve_problem(problem_statement):
	verb = get_verb(problem_statement)
	if verb in available_functions:
		apply(apply_structure=verb, to_structure=problem_statement)
	else:
		# iterate through workflows, generate new workflows, apply workflows, etc
		interface_query = design_interface_query(problem_statement)

def design_interface_query(problem_statement, solution_automation_workflow):
	''' this function generates output like the example query below for the sorting algorithm test_problem,
		where the query implements the specified workflow '''


available_resources = get_resources() # fetches available definitions, available functions, etc
test_problem = 'optimize the function find_document_matches() on metric of "function steps required"'
solve_problem(test_problem)

test_problem = 'find a more generalizable "sorting algorithm" than existing "sorting algorithms"'
default_interface_query = 'analyze problem/solution and format problem/solution to fulfill requirements of solution_automation_workflow and implement solution_automation_workflow'
solution_automation_workflow = 'apply differences to certainty structures to fulfill the "connect problem/solution" problem-solving intent, using the "filter and test solutions" problem-solving intent wherever multiple solutions are identified'
problem_solving_intent = 'connect problem/solution'
default_problem_solving_intent = 'filter and test solutions'

# interface query:

	# fulfill problem_solving_intent ('connect problem/solution') by applying method specified ('apply differences to certainty structures') in solution automation workflow to problem statement test_problem
		
		# analyze problem and solution from problem_statement (test_problem)
		problem = describe(problem=test_problem)
		problem = {
			'format': 'sorting_algorithm'
		}
		solution = describe(solution=test_problem)
		solution = {
			'format': 'sorting_algorithm',
			'requirements': [
				'solution generalizability is higher than average existing solution generalizability'
			],
			'definitions': {
				'generalizability': 'successfully applicable to multiple very different sorting problem examples, "generalizability" increasing with the number of very different sorting problem examples'
			}
		}

		# fulfill requirements of solution_automation_workflow

			# get required inputs of solution_automation_workflow
			inputs = find('inputs', solution_automation_workflow)
			inputs = [requirement('required_problem_format == "connect the difference between problem and solution state"')]
		
			# format problem in the format of a 'connect the difference between problem and solution state'
			problem_state = 'existing sorting_algorithms are suboptimal in generalizability'
			solution_state = 'new sorting_algorithms are more optimal in generalizability than (are different from) existing sorting_algorithms'
			required_problem format = 'change "existing sorting_algorithms" into "new sorting_algorithms that are more optimal in generalizability"'

			formatted_test_problem = 'apply differences to certainty structures like known solutions (sorting algorithms)' to connect the known solutions with the solution requirement of a 'more generalizable sorting algorithm'
				# find structures of certainty of problem (current/input/existing) state, to apply as input to solution automation workflow
					# find known structures, including 'existing solutions' (sorting_algorithm examples), known interface structures like 'variables' of those 'solutions' and known definitions of problem/solution structures like 'sorting algorithms'

						known_structures = {}
						# apply definition interface
							known_structures['definitions'] = [find('definition', 'sorting_algorithm')]
							known_structures['definitions'] = ['function that changes the "order" attribute of a set']
						# apply 'example' structure from information interface 
							known_structures['examples'] = find('examples', 'sorting_algorithm')
						# apply problem_solving_intent to find any known solution structures
							
							known_structures['solutions'] = find('difference', known_structures)
								
							# find known differences in known structures
								# find change structures of certainty structures
									# apply 'variable' structure from change interface
										variables_known_structures = find('variables', known_structures['examples'])
								
							# apply difference types to known structures to convert them into possible solution structures

								# find new differences from known structures to apply difference_type = 'unique maximal differences from known structures'
									# apply change structures to find new differences from known structures
										# apply variables to (variables of known structures)
										different_from_known_structures = apply('change', attributes='maximally different unique', variables_known_structures)
										# with this set of possible solutions, apply default_problem_solving_intent
											# filter by solution format definition (sorting_algorithm definition of 'function that changes the "order" attribute of a set')
											filtered_different_from_known_structures = apply('filter', )
											# test if filtered_different_from_known_structures are optimally different from known structures
											solutions_filtered_different_from_known_structures = apply('filter', 
												solutions_filtered_different_from_known_structures, 
												condition='higher generalizability score than that of known_structures["examples"]')
								
								# find patterns in known structures to apply difference_type = 'differences in patterns of known structures'
									patterns_in_known_structures = apply('pattern', known_structures)
									# apply changes to patterns without violating the pattern's core attributes
									different_from_patterns_in_known_structures = apply('change', attributes='non-violating change', patterns_in_known_structures)
									# with this set of possible solutions, apply default_problem_solving_intent
										# filter by solution format definition (sorting_algorithm definition of 'function that changes the "order" attribute of a set')
										# test if filtered_different_from_patterns_in_known_structures are optimally different from known structures
										solution_filtered_different_from_patterns_in_known_structures = apply('filter', 
											solution_filtered_different_from_patterns_in_known_structures, 
											condition='higher generalizability score than that of known_structures["examples"]')
								
								# find unused differences in known structures to apply difference_type = 'unused known difference of known structures'
									# apply combinations of variable values of known structures
										combinations = apply('combine', variables_known_structures.values)
										# filter out combinations which are in known structures
											unused_combinations = filter(combinations, condition="in known_structures['examples']")
											# with this set of possible solutions, apply default_problem_solving_intent
												# filter by solution format definition (sorting_algorithm definition of 'function that changes the "order" attribute of a set')
												# test if filtered_unused_combinations are optimally different from known structures
												solution_unused_combinations = apply('filter', 
													filtered_unused_combinations, 
													condition='higher generalizability score than that of known_structures["examples"]')
