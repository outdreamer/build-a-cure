'''
- ideally the program would pull definitions of these verbs, which use a common core function set, and the common core function set would be explicitly defined
- the common core function set would be irreducible functions like find/build/derive/apply
	- whose definitions involve core code operations like 'iterate', 'assign', 'test'
	- which are so fundamental that all other functions can be built from them
- all functions that can be defined as functions of the common core function set would not have explicit function definitions
	- they would just be the result of an apply(definition=function_verb), which would return the function implementation of that verb, using functions of the common core function set
'''

definition = {
	'set': 'multiple items of the same type',
	'subset': 'set of positions in a field of all possible attribute combinations of attributes of structure, not equal to the position of the structure in the field',
	'prediction function': 'combine coefficients, exponents and variables to create output variables', # math definition route
	'function': 'apply a set of change sequences/networks/trees to inputs', # 'changes' applied in a 'function' can be assignments, copies, conversions, additions/reductions, changes in position (return a value), etc
	'find': 'list all subsets of structure that are equal to or similar to substructure'
}

def get(item_type, identifier):
	if item_type in globals():
		# its been loaded from configuration json
		if identifier in item_type:
			return item_type[identifier]
	return None

def general_function_template(function_verb, function_params, function_params_verb):

	# find words in the structure which are 'structures'
	function_verb = 'find'
	function_params = ['substructure', 'structure']
	function_params_verb = 'in'
	function_string = function_verb + function_params_verb.join(function_params)

	# currently this function is configured to convert to the 'structure' interface, then to the 'function' interface

	# 1. the 'structure' interface is used to fulfill the workflow step 'break problem into sub-problems'
	# this is to find 'component' structures like 'term interactions', once standardized to the 'structure' interface
	# the results of applying the 'structure' interface are used to identify structures of components of the function (like term definitions)

	# 2. the 'function' interface is used to fulfill the workflow step:
	# 'merge sub-problem solutions (structural term definitions as function components) into the solution (function)'

	# then the 'function' interface is applied, to merge these structures of components into a function

	# bc its designed to generate code fulfilling the input function indicated by function_verb, function_params, and function_params_verb
	# this code should use common core structures to implement the function, so the structure interface is applied first

	for interface in ['structure', 'function']:

		if interface == 'structure':

			# define unknown terms
			terms = {}

			for item in function_params:
				unknown_terms = find('words', params=item, output_filters=['structure']) # get words which are 'structures' like 'functions' or 'objects'
				for unknown_term in unknown_terms:
					terms[unknown_term] = get('definition', unknown_term, output_filters=[interface]) # get the 'structure' interface definition route
			
			# for 'find', terms would have keys: ['list', 'subset', 'structure', 'all', 'equal', 'similar', 'substructure']

			# get core component 'clause' of the input function_string
			core_component = get('core component', function_string)
			core_component = 'clause'

			# get term interactions
			term_interactions = {}
			for term, definition in terms.items():
				definition_clauses = get(core_component, definition) # get the clauses in the definition
				for definition_clause in definition_clauses:
					words = definition_clause.split(' ')
					term_position = words.index(term)
					adjacent_term_positions = [term_position - 1, term_position + 1]
					words_in_definition = [w for w in get('word', definition) if w != term]
					# words in definition are either functions or objects
					objects_in_definition = [w for w in words_in_definition if type(w) == 'object']
					functions_in_definition = [w for w in words_in_definition if type(w) == 'function']
					interaction_function = [f for f in functions_in_definition if words.index(f) in adjacent_term_positions]
					interaction_function_position = words.index(interaction_function)
					term_interactions[term] = {interaction_function: [w for w in words if words.index(w) not in [term_position, interaction_function_position]]}
			
			# for 'find', term_interactions would be:
			term_interactions = {
				'structure': ['subsets of structure', 'all subsets of structure', 'list all subsets of structure'],
				'subset': ['subsets of structure', 'all subsets of structure', 'list all subsets of structure', 'subsets equal to substructure', 'subsets similar to substructure', 'subsets equal or similar to substructure'],
				'list': ['list all subsets of structure', 'list all subsets of structure equal or similar to substructure'],
				'all': ['all subsets of structure', 'list all subsets of structure'],
				'equal': ['subsets equal to substructure', 'subsets equal or similar to substructure'],
				'similar': ['subsets similar to substructure', 'subsets equal or similar to substructure'],
				'substructure': ['subsets equal to substructure', 'subsets similar to substructure', 'subsets equal or similar to substructure']
			}

			# apply terms once defined

			# for example, to apply the 'list' definition to the term_interactions, use the term_interactions of 'list' to fulfill the 'list' definition
			# if list is defined as 'combine x until a set containing these structures exists', apply that definition to the relevant term_interaction 'list all subsets of structure'
			# combine 'all subsets of structure' until a set containing these structures exists, as 'all subsets of structure' are the inputs (x value) of the 'list' function
			# applying the other relevant term interaction results in 'combine "all subsets of structure equal or similar to substructure" until a set containing these structures exists'

			structured_component_interactions = {k: v for k, v in term_interactions.items()}
			for term, interaction in term_interactions.items():
				term = 'list'
				term_definition = terms[term]
				term_definition = 'combine x until a set containing these structures exists'
				for k, v in structured_component_interactions.items():
					if term in v:
						v = 'list all subsets of structure'
						val_without_term = v.replace(term, '')
						val_without_term = 'all subsets of structure' # 'list' is removed from this interaction				
						new_val = term_definition.replace('x', val_without_term)
						new_val = 'combine "all subsets of structure" until a set containing these structures exists'
						structured_component_interactions[k] = new_val

			# once applied, the interactions in structured_component_interactions should be using none of the key terms of term_interactions
			# but rather should be using the more specific structures theyve been replaced with

			# this version of the input in structured_component_interactions is far more similar to the actual runnable code version 
			# than the original input, which is 'find substructure in structure'

			# this process can be repeated iteratively, applying layers of definition routes
			# above we applied a 'structure' definition route of the definition of each term in the input
			# additional iterations of this process could apply a 'logic' or 'math' definition route to further similarize the input state to runnable code

		if interface == 'function':

			# standardize the structured_component_interactions until its in a function format

			# once the state only uses functions which are already defined in a programming language (split, reverse, for)
			# this function can return that version of the input, which is the function code of the input

			# merge structured_component_interactions to convert the original input to use the structures in structured_component_interactions

			function_string = 'find substructure in structure'
			# function_string = merge(structured_component_interactions, function_string)
			function_string = function_string
			for word in function_string.split(' '):
				if word in structured_component_interactions:
					function_string.replace(word, structured_component_interactions[word])

	return function_string

def merge(inputs, original_structure):
	''' this function applies a merge strategy, like:
		- combines and replaces inputs according to the original structure 
			(like merging structured_component_interactions according to the input 'find substructure in structure')
	'''

def find(substructure, structure):
	'''
	- what this function does is convert the above definition for 'find' into specific code structures like iterations/conditions
		- the below code 'infers' some of the required operations to fulfill the above definition of 'find'
		- for example, the generated code 'infers' that in order to fulfill explicit defined intents like:
			'check substructure for equivalence/similarity with a subset of structure'
		- this 'inference' is built in to the program
			- as 'retrieving a definition for any unknown terms' is a default behavior when encountering unknown terms
		- the definition of 'substructure' is required
		- a subset-identifying function is required to find possible subsets to check
	'''
	# substructure could be an item in a set (like a 'function' in a 'set of functions'), where structure is a set
	# substructure's definition provides the test to filter out non-matching structures

	general_function_template(function_verb='find', function_params=['substructure', 'structure'], function_params_verb='in')

	# the definition of a function is a 'set of change sequences/networks/trees applied to inputs'
	subsets_of_structure = get('combinations of core components of x', x=structure)
	# subsets could be a piece/component of the structure that is an identifiable object
	# such as a function in a set of functions
	equal_matches = []
	approximate_matches = []
	non_matches = []
	for subset in subsets_of_structure:
		if subset == substructure:
			# found a matching structure
			return subset
		else:
			# test for various definitions of either structure for approximate matching


def build(structure, available_substructures):
	# structure could be a 'function', where available_substructures could be a set of components/inputs/functions capable of building the 'function'


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
	- 'apply' compared to 'combine'
		- if structures are additive (combinable), it means they can interact by coordinating their changes (their changes are isolatable and compounding, not creating other value types by default but resulting in the same value type)
	    - if structures are multiplicative (applicable), it means they can interact by applying one change as an input to the other's attributes (multiply x by y means to apply x, y number of times, or in other words, create x with attribute 'count' value of y)
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

def break(structure_to_break, output_filters):
	'''
		standard function name: 'get components'
		similar to filter, break reduces the inputs, but into components, rather than subsets, 
		where output_filters specifies some component type 
		- notes
			- these structural functions like break/filter/reduce are basically a definition of the structure of these verbs, 
			so they can be called in the 'apply' function as a function structure to apply, 
			or the 'find' function as a function substructure to search for in another function structure
	'''


def define(structure):
	'''
	- some structures cant be reduced to another definition, for example, like 'input', 
		which if it's reduced to another structure like 'triggers' or 'requirements' or 'assumptions', 
		changes its definition so it cant be used to cover the other structures it refers to
	- to do: 
		- add fetching of definition_routes as well as the primary definition to this function
			or the find() implementation when pulling a definition, given the usefulness of definition_routes for find()
	'''
	# defs are default core structure definitions
	defs = {
		'fulfill': 'equate inputs/outputs', # an interface query that implements/fulfills a workflow is equal to that workflow in its specified inputs/outputs (problem/solution)
		'core': 'find complete set of components that combine to form input',
		'break': 'find components of input',
		'reduce': 'find fewer variables of input',
		'expand': 'find more variables of input',
		'filter': 'find subset of input set',
		'find': 'find output_filter substructure in input structure',
		'cause': 'build output fulfilling output_filter',
		'apply': 'build change',
		'build': 'find combinations of structures until input exists',
		'exist':  'find identifier of input',
		'connect': 'find input-output structures', # like (sequence, network, etc of functions, changes, requirements, filters, or input/output mappings)'
	}
	return defs[structure] if structure in defs else None

def apply_interface(structure, interfaces):
	if not interfaces or len(interfaces) == 0:
		interfaces = find('list', 'interface')
		interfaces = ['cause', 'change']
	interface_structures = {}
	for interface in interfaces:
		interface_structures[interface] = {}
		definition_routes = find('definition_routes', interface)
		# for example, 'cause' definition is 'triggers of a structure', triggers such as inputs, intents, contexts or other structures requiring that structure, etc
		definition_routes = ['input of structure', 'systems requiring structure', 'intents that use structure']
		for definition_route in definition_routes:
			definition_route = 'input of structure'
			interface_structures[interface][definition_route] = {}
			definition_structures = find('structure', definition_route)
			definition_structures = ['input', 'structure']
			for definition_structure in definition_structures:
				definition_structure = 'input'
				if definition_structure != 'structure':
					# if 'input' != 'structure':
					this_interface_route_structures_in_structure = find(definition_structure, structure) # find 'input' of 'structure'
					# this should match all structures related to structure that match the 'input' definition, such as 'a variable used as input to a function'
					this_interface_route_structures_in_structure = ['structure_input_variables']
					interface_structures[interface][definition_route][definition_structure] = this_interface_route_structures_in_structure
					# this stores the 'definition structure' and the 'matching structure of that definition structure in structure' as a dict
					# similar to storing a 'network' as a set of 'connected node pairs'
					# so that these structures of structure which match this 'definition route' can be related in a 'network' form
	return interface_structures

def change(structure, changes):
	'''
		1. first apply similar logic as find('difference') if changes is not populated
		2. then apply each found difference type to the input structure

		- notes 
			- build, find, change, derive should all have multiple strategies applied
				- for example, build should apply multiple 'build' strategies, such as:
					-  multiple 'merge', 'combine', 'connect', and 'integrate' variants
				- similarly, 'change' should apply multiple 'change' strategies, such as:
					- 'multiple combinations of changes', 'multiple sequences of changes', 'multiple combinations of sequences of changes'
				- 'find' should apply multiple 'find' strategies, like 'find substructure based on a matching threshold ratio'
	'''
	changed_structures = []
	if not changes:
		definition = find('definition', 'change')
		definition_routes = find('definition_routes', 'change')
		definition_routes = ['differences output by applying variables', 'differences output by applying functions']
		for definition_route in definition_routes:
			definition_structures = find('structures', definition_route)
			definition_structures = ['variables', 'output', 'apply', 'differences']
			for definition_structure in definition_structures:
				possible_structures = find(definition_structure)
				possible_structures = ['possible unique structures (as anything unique can create a new difference type)', 'variables of unique structures', 'function inputs', 'function outputs'] # examples of 'variable' structures
				if len(possible_structures) > 0:
					changes.extend(possible_structures)
	if len(changes) > 0:
		for change in changes:
			changed_structure = apply('change', structure)
			if changed_structure != structure:
				changed_structures.append(changed_structure)
			# applying a change amounts to retrieving the change definition, finding change structures, then iterating through each change
			# on each iteration, finding the attributes/functions of the structure which can be changed by the change
			# for example, if the structure is a network, applying a change like a 'position' variable could mean:
			# 'changing position of nodes' or 'changing position of functions' or 'changing position of the network'
			# because the 'nodes', 'functions', and 'network' are structures that have a position attribute, so their position can be changed
			# as another example, changing the 'power' of the structure could mean:
			# 'changing the inputs', 'changing the outputs', 'changing the functionality', 'changing the controlling hub nodes', 'changing the determining variables of the network'
			# since the 'inputs/outputs', 'functionality', 'hub nodes', and 'determining variables' are all structures of power (that control other structures)
	return changed_structures

def find(substructure, structure):
	similarity_threshold_ratio = 0.5
	# ratio of matching attributes/functions to total attributes/functions used to find sufficiently similar substructures
	# get all possible substructures in the structure as the solution space to filter
	substructures = find('substructure', structure)
	# apply interface structures to substructures to get adjacent distortions and related structures of substructures
	for interface in interfaces:
		interface_substructures = apply_interface(interface, substructures)
		substructures.extend(interface_substructures)
	scores = {}
	max_substructure_score = {}
	# iterate through substructures, comparing to substructure by each combination of attributes/functions
	for possible_substructure in substructures:
		# get all combinations of attributes/functions
		combination_possible_substructure = find('combination', possible_substructure['attributes'] + possible_substructure['functions'])
		combination_substructure = find('combination', substructure['attributes'] + substructure['functions'])
		common_combinations = find('duplicate', combination_possible_substructure + combination_substructure)
		this_threshold_ratio = len(common_combinations) / len(combination_substructure)
		if this_threshold_ratio >= similarity_threshold_ratio:
			scores[possible_substructure] = common_combinations
			if max_substructure_score:
				if len(common_combinations) > [val for val in max_substructure_score.values()][0]:
					max_substructure_score[possible_substructure] = len(common_combinations)
			else:
				max_substructure_score[possible_substructure] = len(common_combinations)
	print('all matches found')
	for struct, score in scores.items():
		print('structure', struct, 'score', score)
	if max_substructure_score:
		print('substructure with most matches found', max_substructure_score)
		return [key for key in max_substructure_score.keys()][0]
	return False

def design_interface_query(problem_statement, solution_automation_workflow, intent):
	''' 
	- this function generates output like the example query below for the sorting algorithm test_problem,
		where the query implements the specified workflow

	1. break the given intent (or the intent of the workflow or problem statement) into sub-intents, matched to 'info required to solve the problem'

	2. then find/build/derive functions that can fulfill each sub-intent
		- if functions are already indexed by intent, this can be a simple 'find' query to find structures of existing functions that fulfill the specified intent
			- for example, 'find functions that when a structure (like a input-output sequence) is applied to the functions, the functions fulfill the intent in a relevant (like "adjacent") way, (like "connect the inputs/outputs of the intent")'
			- an 'input-output sequence' is useful for intents like 'connect inputs/outputs' ('connect inputs (problem or independent variables) with outputs (solution or dependent variable)')

	- notes
		each function should have a solution using 'find', 'build', 'derive', and 'apply' as interchangeable alternate implementation verbs
	'''

	if intent:
		intent_sub_intents = apply('break', intent, output_filters='clauses')
	else:
		problem_sub_intents = apply('break', problem_statement, output_filters='clauses')
		workflow_sub_intents = apply('break', solution_automation_workflow, output_filters='clauses')
	# the sub intents should correspond to 'info required to solve the problem'

	break_function_applied = find('difference', input_structure=[break_input, break_output])
	merge_function = apply(structure='opposite', input_structure=break_function_applied)
	merged_solution_of_sub_intents = apply('merge', structure=merge_function, structure_inputs=sub_intent_solutions)


available_resources = get_resources() # fetches available definitions, available functions, etc
test_problem = 'optimize the function find_document_matches() on metric of "function steps required"'
solve_problem(test_problem)

test_problem = 'find a more generalizable "sorting algorithm" than existing "sorting algorithms"' # 'search algorithms'
default_interface_query = 'analyze problem/solution and format problem/solution to fulfill requirements of solution_automation_workflow and implement solution_automation_workflow'
solution_automation_workflow = 'apply differences to certainty structures to fulfill the "connect problem/solution" problem-solving intent, using the "filter and test solutions" problem-solving intent wherever multiple solutions are identified'
problem_solving_intent = 'connect problem/solution'
default_problem_solving_intent = 'filter and test solutions'

# example interface query:

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



def filter(structure, solution_metric_filter):
	'''
		- example attributes of solution ('test function') structures:
			solution_metric_filter = 'is a sorting algorithm' = 'is a function that changes order of a set'
			solution_metric_filter = 'is more generalizable than an existing sorting_algorithm'
	'''
	if 'solution_metric_filter' not in globals():
		solution_metric_filter = derive(structure='function', None, attribute=solution_metric_filter)

def derive(structure_type, example_structure_with_attribute, attribute):
	''' 
		this function derives a structure of the specified type like a 'function' that can be applied to the input_structure (like a "change sequence") and has the specified attribute, like a 'determines generalizability of a "change sequence"'
		- for example, derive a 'test function' that 'tests if a structure like the example input_structure example_structure_with_attribute (like a "change sequence") has the attribute "changes the order attribute of a set"'
		- example structure_type
			- structure_type = 'test function'
		- example example_structure_with_attribute, which can be None or can include an example of an input to the structure_type, like follows
			- sequence of sorting algorithm function steps like:
				[
					'reverse', 'sort_alphabetical', 'sort_numerical', 'sort_descending', 
					'determine attribute value to sort by', 'determine position to sort at', 
					'determine position assigning logic once attribute value is found', 
					'determine iteration logic to apply, given a starting position'
				]
		- example attributes of solution ('test function') structures:
			solution_metric_filter = 'is a sorting algorithm' = 'is a function that changes order of a set'
			solution_metric_filter = 'is more generalizable than an existing sorting_algorithm'
		- this function finds a route to 'connect' the example_structure_with_attribute ('change sequence') with the attribute 'determines generalizability of the change sequence' in the form of the structure_type ('function')
		- the 'derive' function applies 'changes' to 'certainty structures' to derive connections between the 'structures to connect'
		- for example, 'deriving' a prediction function applies 'changes' to the 'certainty structures' (input variables, output variables) to derive connections ('coefficients', 'exponents', 'operators') between the 'structures to connect' (input and output variables of the prediction function), having incomplete information about those connections (as the certainty structure of the 'data set' is, by definition of the 'prediction function' problem, necessarily 'incomplete', otherwise a prediction function wouldnt be necessary to find and the original data set could act like a mapping table rather than requiring a function)
	'''
	derived = apply('test', structure, attribute)
	return derived

def apply(structure, input_structure, output_filter, definitions):
	''' 
		structure = 'test'
		input_structure = 'example_sorting_algorithm' # an example sorting_algorithm, as a list, tree, etc of function steps
		output_filter = 'is more generalizable than an existing sorting_algorithm'

		apply('test', 'sorting_algorithm', 'is more generalizable than an existing sorting_algorithm')
	'''

	for keyword, value in definitions.items():
		output_filter = output_filter.replace(keyword, value)
	objects = get_primary_nouns(output_filter)
	objects = ['function']
	verb = get_primary_verb(output_filter)
	verb = 'is'
	operator = get_operator_for_verb(verb) # 'is' becomes '=='

	# this is a test
	if structure == 'test':

		# get the default definition of the structure 'test', which is 'check if x is y'
		# derive & apply logic implementing the definition of the structure

		# this is an equivalence test (check identity or equivalence/similarity/difference of object/attribute/function)
		if verb == 'is':

			attribute_test = output_filter[output_filter.index(verb):]

			has_sub_conditions = find('conditions', attribute_test)
			if has_sub_conditions:

				# if attribute_test is complicated, has many sub-conditions of the test, or is not translated to a particular interface
				# simplify it or translate it to a useful interface like the structure interface, and apply these sub-tests iteratively

				object_definitions = find('definition', objects) # find 'function' definition
				object_definitions = {'function': 'structure (like a "network", "tree", "set", or "sequence") of isolated logical structures (like "changes") to change units (like "inputs/variables")'}

				iterated_conditions = find(structure='sequential_combinations of conditions', attribute_test)
				iterated_conditions = [
					'function', 
					'function that changes order',
					'function that changes order of a set'
				]
				iterated_variable_conditions = apply('variables', iterated_conditions)
				iterated_variable_conditions = [
					'function', 
					'function that changes order',
					'function that changes order of (a) set',
					'function that changes order of (different) sets',
					'function that changes order of (any) set'
				]
				for statement in iterated_variable_conditions:
					
					# check if structure is equal to the structure specified in the attribute
					structure_passed = apply(structure=operator, input_structure=input_structure, output_filter=statement, definitions=object_definitions) 
					
					# apply('is', 'example_sorting_algorithm', 'function that changes order')

					if not structure_passed:
						print('test failed', statement)

			else:
				structure_passed = apply(structure=operator, input_structure=input_structure, output_filter=attribute_test)

def is(attribute, base_structure, alternate_structure):
	''' 
		attribute = 'similar', out of options ['equal', 'different', 'opposite', 'similar']
		base_structure = 'example_sorting_algorithm' (formatted as a sequence of changes)
		alternate_structure = 'function that changes order' # 'sorting_algorithm definition'
	'''

	# to do: order by those which are most filterable first

	comparison = {
		'structure_type': {}, 
		'structure_definition': {}, 
		'example_structures': {}, 
		'example_structure_variables': {}, 'structure_variables': {}, 
		'example_inputs_outputs': {}, 'example_input_output_differences': {}
	}

	# apply various differences to the structures to get more metrics to compare them
	for structure in [base_structure, alternate_structure]:

		comparison['structure_type'][structure].append(find('type', base_structure)) # 'function')
		comparison['structure_definition'][structure].append(find('definition', base_structure)) # definition of 'sorting_algorithm'
			
		comparison['example_structures'][structure].append(find('examples', base_structure)) # [reverse(), sort_alphabetically(), divide_and_conquer()]
			
		# variables of sorting algorithms like 'reverse()', 'sort_alphabetically()', etc, like 'starting position', 'position change logic', the 'descending' definition that is applicable to numbers/letters, etc
		comparison['example_structure_variables'][structure].append(find('variables', comparison['example_structures'])) 
		comparison['structure_variables'][structure].append(find('variables', base_structure)) # variables of the input sorting_algorithms
			
		comparison['example_inputs_outputs'][structure].append(find(['inputs', 'outputs'], base_structure)) # ('acb', 'abc')
		comparison['example_input_output_differences'][structure].append(find('changes', params=[base_structure['inputs'], base_structure['outputs']])) # ['order']

	if attribute == 'equal':

	elif attribute == 'difference': 

	elif attribute == 'opposite':

	elif attribute == 'similar':

		# apply comparison of the differences to determine similarity on each metric, like:

		# 'does the base function respond to the alternate function's example inputs/outputs the same way, to produce the same input/output differences'
		# 'does the base function 'change the order of the input set', as specified in the alternate_structure of the 'sorting algorithm definition'
