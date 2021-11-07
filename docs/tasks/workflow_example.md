'''
- to do list
	- add functions & definitions to do the following:
		- find('attributes') # as a way of finding attributes to describe a structure
		- find('differences') # as a way of finding attributes that vary between structures
			- find('similarities') # as a way of finding attributes that vary minimally between structures
		- find('connections') # as a way of finding a route between structures
		- apply('change', 'difference.type') # as a way of creating a difference in a structure in one of its attributes/functions
	- add an example of creating the 'interface definitions' from a normal definition
	- add an example of implementing a solution automation workflow (like 'apply changes to see what works') in a 'neural network' solution format (to the problem of 'find a solution-finding method for the "find a prediction function" problem')
	- add an example of structuring a default set of interface structures as a network as a grpah database to run queries on
'''

problem_definition = 'find a block in the set of blocks that has "three corners"'

''' 
the solution_automation_workflows data structure stores workflows & their summaries & implementation steps
{
	'workflow1': {
		'workflow1_version1_summary': {
			'workflow1_version1_step1',
			'workflow1_version1_step2'
		},
		'workflow1_version2_summary': {
			'workflow1_version2_step1',
			'workflow1_version2_step2'
		}
	}
}

- so an implementation of 'workflow1' might have functions corresponding to the steps in a particular version of the workflow, given its summary
- given that the steps correspond to functions required to implement the workflow, this data structure can act like a standard 'abstract interface' as defined using software terms (meaning 'a list of functions to implement an object')
'''

solution_automation_workflows = {
	'trial_and_error': {
		'test every possible solution until a solution is found that fulfills the solution metrics': [
			'iterate through all possible solutions',
			'test a solution',
			'stop when a solution is found that fulfills the solution metrics',
			'return current solution'
		],
		'test every possible solution until it is determined which solution out of all possible solutions fulfills the solution metrics the most optimally': [
			'initialize the best solution at zero value (indicating it is the worst possible solution fulfillment)',
			'iterate through all possible solutions',
			'test a solution',
			'test whether the current solution is better than the previous best solution at fulfilling solution metrics',
			'update the best solution to the current solution if its better than the previous best solution at fulfilling solution metrics',
			'stop when all solutions have been tested',
			'return the best solution'
		]
	}
	'break_problem_into_sub_problems_and_merge_sub_solutions': {
		'identify sequence of problems leading to the original problem': [
			'identify problem causes (the input causal sequence of a problem)',
			'identify problem cause sequence',
			'solve problem cause (a 'problem cause' is also a 'problem')',
			'update impact of a solution on other problems and problem causes',
			'test if a problem is solved by solving one of the causal problems in its input causal sequence',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		],
		'identify 'equalizing' sub-problems building the original problem': [
			'identify 'connection' structures required to convert problem into solution (equalize the problem with the solution)',
			'identify equalizing functions that would connect the problem & solution (functions that would convert one state into a state similar to another state)',
			'apply equalizing functions to connect the problem/solution',
			'test if the equalizing functions solves the problem (connects the problem & solution)',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		],
		'identify 'connection' sub-problems building the original problem': [
			'identify 'connection' structures required to convert problem into solution (equalize the problem with the solution)',
			'identify connection functions that would connect the problem & solution (functions that would find 'connection' structures like 'input-output sequences')',
			'apply connection functions to connect the problem/solution',
			'test if the connection functions solves the problem (connects the problem & solution)',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		],
		'identify 'interaction' sub-problems building the original problem': [
			'identify 'connection' structures required to convert problem into solution (equalize the problem with the solution)',
			'identify interaction functions that would connect the problem & solution (functions that would find 'interactive' structures like 'input-output sequences')',
			'apply interaction functions to connect the problem/solution',
			'test if the interaction functions solves the problem (connects the problem & solution)',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		],
		'identify 'difference' sub-problems building the original problem': [
			'identify 'difference' problem structure between problem & solution',
			'identify functions that remove or reduce the difference between problem & solution',
			'apply functions to remove/reduce differences to the difference between problem & solution',
			'test if reducing/removing the difference solves the problem (fulfills the solution metrics)',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		],
		'identify 'missing information' sub-problems building the original problem': [
			'identify 'missing information' problem structure preventing the solution',
			'identify functions that can find information',
			'apply functions that can find information to find the missing information',
			'test if the missing information solves the problem (fulfills the solution metrics)',
			'if the problem is solved by a solution (the solution metrics are fulfilled, possibly determined by whether the problem/solution are connected, which is a problem-solving intent), return that solution'
		]
	}
}

def identify_problem_attributes_functions(problem_definition):
	''' 
		- attributes like the problem type are useful for querying for existing solutions to that type or otherwise filtering possible solutions 
		- functions of a problem like 'causes_other_problems' or 'prevents_other_problems' are useful to identify as inputs to workflows such as 'identify other problems to solve, given that its suboptimal to solve the original problem itself because it also prevents another problem, so instead solve the problems caused by the original problem'
	'''
	problem = {'attributes': {}, 'functions': {}}
	problem['attributes'] = {
		'types': {
			'primary_types': ['solution space-filtering problem'],
			'general_types': [
				'missing_information of optimal state (filtered solution space having size one, including the optimal solution, or the first solution metric-fulfilling solution found) & how to find optimal state (solution-space filtering function)', 
				'difference between problem/solution state or problem/solution space',
				'"solution space-filtering" function-finding problem',
				'"solution requirement-invalidating" function-finding problem'
			]
		}
	}
	return problem

def identify_problem_space(problem_definition, problem):
	''' 
		- the problem space is the 'system where the problem exists' 
		- for an example problem like 'find the block having this attribute (having three corners)', the problem space is:
			- the system where it's not obvious (not trivial to solve) which block has that attribute, so the answer must be calculated
			- this could be a system such as the 'tetris game', where each possible & optimal position of a block must be calculated because it's not immediately obvious which positions are possible & which position is best
			- some functions would make the answer obvious (trivial to solve), so if a problem space is updated to have those functions, the problem is solved (or trivially solved) and other problems would be focused on (or would be caused by the added functions or other changes)
				- if you hacked your tetris game app to include a function to 'automatically find the best position for a block', the problem space would change, and new problems like 'finding the best optimization metric' and 'finding the best solution-finding function' would become the problems to focus on, which would not be trivial to solve in that updated problem space, and would involve new functions like 'abstract a function' to abstract the existing function of 'finding the best position for a block' to 'finding the best solution for a problem' in order to solve the new problems like 'finding the best solution-finding function'
			- an example of a system where the answer would be obvious is where there is one possible solution (indicating a 'requirement to use that solution', rather than a 'problem of filtering possible solutions') - in all other situations, the answer must be calculated, such as by comparing possible alternative solutions given that there are multiple possible solutions
	'''
	problem_space = [
		'it is required to find a block having a particular attribute value (such as block_corner_count = three)',
		'it is possible for blocks & corners to exist and possible for a block to have a corner and it is possible for a straight line to be a side/boundary structure of a block',
		'blocks are defined as "closed shapes having lines with different angles as possible boundaries" and corners are defined as "angles created by two lines with different angles representing boundaries/sides of a shape"'
		'it is possible for blocks to vary on the attribute of the solution metric (block_corner_count)',
		'it is not obvious which block fulfills the solution metric, given a set of blocks (there is more than one possible solution)',
		'it is required to test which block fulfills the solution metric (find the block_corner_count of a block)',
		'functions like count_corners_of_block, identify_closed_shape, identify_straight_line, identify_shape_sides, identify_blocks (meaning blocks are differentiable), and iterate_blocks are possible to build and may already exist', 
	]
	return problem_space

def find_entities(structure):
	''' this function just excludes functions and finds nouns '''
	structure = 'sets of two endpoint-connected lines with different angles'
	# the 'set' structure acts like a function to create a 'group of inputs'
	entities = ['two endpoint-connected lines with different angles']
	return entities

def find(substructure, structure):
	''' 
		- given a structure like 'structures that can build a block with three corners', find the substructure in that structure, such as 'structures' 
	'''
	identified_functions = identify_functions(structure)
	identified_functions = {
		'build': {
			'input': 'structure',
			'output': 'block with three corners'
		}
	}
	definitions = {
		'build': {
			'input': ['structures'],
			'output': ['combinations of structures']
		}
	}
	// given that the definition of 'build' we retrieved involves 'combining structures', we can inject an interim subfunction connecting inputs/outputs of the specific function
	updated_functions = apply_definition(definitions, identified_functions)
	updated_functions = {
		'build': {
			'input': 'structure',
			'subfunction': 'combinations of structures',
			'output': 'block with three corners'
		}
	}
	// given that we have the output ('solution metric fulfilling solution'), 
	// and we want the input (structures that can create the 'solution metric fulfilling solution'), 
	// and the reverse of the subfunction is 'subsets of structures', 
	// we can apply the subfunction in reverse to the output, to identify the input (structures that, when combined, build the output)

	// in the apply() function, the map parameter connects the function with the params
	apply_reverse_subfunction = apply(function='reverse', map={'reverse': 'input-output sequence'}, params=['combinations of structures'])
	apply_reverse_subfunction = 'subsets of structures'
	interim_input = apply(function=apply_reverse_subfunction, map={'structures': 'block with three corners'}, params=['block with three corners']) 
	// apply the 'reverse subfunction' ('subsets of structures') to the 'output' ('block with three corners'), where the 'structures' in the 'subsets of structures' refers to the 'block with three corners'
	interim_input = 'subsets of "block with three corners"'
	updated_applied_functions = {
		'build': {
			'input': 'structure',
			'interim_input_1': 'subsets of "block with three corners"',
			'subfunction': 'combinations of structures',
			'output': 'block with three corners'
		}
	}
	''' - now we've gone through this conversion sequence of the output so far, to find the input structures that can build the output:
			'block with three corners'
			'structures to build "block with three corners"'
			'combination of "structures" to build "block with three corners"'
			'combination of "subset of block with three corners" to build "block with three corners"'
		- now we need to use definitions to substitute specific structures that qualify as 'subsets of the "block with three corners"'
	'''
	specific_subsets = apply(function='define', map={}, params=['subsets of "block with three corners"']) 
	specific_subsets = {
		'block with three corners': [
			'closed shape with three corners', 
			# apply 'closed shape' definition to substitute specific structures of ' gap-less overlap-less endpoint-connected lines of count greater than two'
			'gap-less overlap-less endpoint-connected lines of count greater than two and with three corners', 
			# apply corners definition to substitute specific structures of 'two endpoint-connected lines with different angles'
			'gap-less overlap-less endpoint-connected lines of count greater than two and with three (two endpoint-connected lines with different angles)'
		]
	}
	''' - now we've gone through this conversion sequence of the output so far, to find the input structures that can build the output:
			'block with three corners'
			'structures to build "block with three corners"'
			'combination of "structures" to build "block with three corners"'
			'combination of "subset of block with three corners" to build "block with three corners"'
			'combination of "gap-less overlap-less endpoint-connected lines of count greater than two with three (two endpoint-connected lines with different angles)" to build "block with three corners"'
		- now that we have found specific structures that can be combined to create the output structure, the find() function is complete
		- meaning we have found the 'substructures' (specific structures of 'block' and 'corner' definitions) that are in the input 'structure' ('block with three corners')
		- now we'll apply the 'find_entities' function to find the components ('two endpoint-connected lines', 'gap-less overlap-less endpoint-connected lines of count greater than two') of the specified reversed subset version of the output used to find components of the output
		- if we wanted to take it farther to the most core structures, we could continue applying specifications given definitions of these component structures, to identify the substructures of 'lines', 'connections', 'endpoints', 'gaps', 'overlaps' in these substructures
	'''
	return find_entities(specific_subsets[structure][-1])

def apply_interface(structure, interface):
	'''
	- applying the 'core' interface to the problem_definition 'find blocks with three corners in a set of blocks' would result in the 'core interface' standardized_problem_definition:
		- 'find closed shapes having at least three sets of two endpoint-connected lines with different angles'
	- because structures like 'endpoint-connected lines with different angles' and 'sets' can be used to build structures like 'closed shapes with a set of three corners' (a 'block having three corners')
	'''
	interfaces = ['core', 'structure', 'intent', 'cause']
	if interface in interfaces:
		separated_structure = separate_structure_by_function(structure)
		function = 'find' // separated_structure['function']
		original_input = '' // separated_structure['input']
		standardized_input = ''
		original_output = 'block with three corners' // separated_structure['output']
		standardized_output = ''
		interface_concept_definition = get_definition(interface)
		interface_concept_definition = 'structures that can build a structure' 
		// definition of the 'core' interface concept includes 'components', as in 'structures that can build a structure'
		component_structures = find('structures', 'structures that can build ' + original_output) 
		// find the specific 'structures' in 'structures that can build "block with three corners"' given definitions
		component_structures = ['gap-less overlap-less endpoint-connected lines of count greater than two', 'two endpoint-connected lines with different angles']
		standardized_output = component_structures
		standardized_structure = structure.replace(original_input, standardized_input) if standardized_input != '' else structure
		standardized_structure = standardized_structure.replace(original_output, standardized_output) if standardized_output != '' else standardized_structure
		return standardized_structure
	return False

def standardize_problem_to_interface(problem_definition, interface):
	'''
	standardizing the problem to an interface will make it more obvious which structures are involved in the problem & which structures can solve it
	example: '"finding the inputs of a structure" will make the problem of "finding the structure" easier to solve when applying the "break problem into sub-problems" workflow'	
	'''
	standardized_problem_definition = apply_interface(problem_definition, interface)
	standardized_problem_definition = 'find (gap-less overlap-less endpoint-connected lines of count greater than two) with three (two endpoint-connected lines with different angles)'
	return standardized_problem_definition

def identify_solution_space(problem_definition, problem_space, problem):
	''' 
		- the solution space is the set of possible solutions, 
			which is a subset of all the possible interactions allowed by the problem space, 
			so the problem space can be converted into the solution space by applying a subset filter 
	'''
	solution_space = [
		'set of closed shapes having at least three sets of two endpoint-connected lines with different angles (blocks with three corners)'
	]
	return solution_space

def identify_solution_space_filters(problem_definition, problem_space, problem):
	'''
		- a solution space can be filtered by:
			- functions specific to that solution space:
				- there may be some line that intersects with blocks in a way that identifies corners of blocks in a way that can filter out blocks to test, and a function deriving this line can act like a solution space-filtering function
				- there may be a more efficient solution metric than 'counting blocks' that can filter out blocks to test with the more computationally heavy solution metric test, such as 'deriving the shape of possible solution blocks (triangle, square) and possible non-solution blocks (lines with different angles, unclosed shapes)' and 'filtering out blocks similar to non-solution blocks (blocks similar to lines with different angles or unclosed shapes)', then applying the 'three-corner' solution metric test to the filtered set of blocks that are not similar to non-solution blocks
			- general filtering functions
				- there may be a general filtering function that can be applied across problems to filter solution spaces in general, like:
					- separate solution space into clusters of similar blocks, identify the type of each cluster, and apply the solution metric test to the cluster type rather than each individual solution in the cluster (if the clustering algorithm is less computationally heavy than the solution metric test applied to each possible solution)
						- in general, filtering functions can be ruled out by which involve more operations than a standard or less optimal workflow like 'trial & error' (applying the solution metric test to each possible solution in the solution space), in various common cases (the average case & other representative cases)
					- identify the attributes by which possible solutions vary (solution differences/variables), and identify attributes that are likelier or required to create the optimal solution
						- solution variables include shape, shape closure, side shape, side count, & number of corners
						- 'two connected sides of a closed shape that are lines with different angles (corners)' is a solution variable that is required to identify the optimal solution (having a 'specific count of corners')
	'''
	solution_space_filters = [
		'separate solutions into clusters by most differentiating solution variables',
	]
	return solution_space_filters

def identify_solution_metrics(standardized_problem_definition, problem_space, problem):
	''' 
		- the solution metric is the test applied to determine 
			- if a solution is better than another solution
			- if a solution is optimal in the sense that its the first solution found that fulfills the solution metric 
			- if a solution is optimal in the sense that its the best solution of all solutions, having either logically filtered out or individually tested all other possible solutions
	'''
	solution_metrics = [
		'closed shape having at least three sets of two endpoint-connected lines with different angles'
	]
	return solution_metrics

def apply_solution_metric(solution):
	return False

def apply_solution_space_filter(solution_space, solution_space_filter):
	return filtered_solution_space

def filter_solution_space(problem_definition, problem_space, problem, solution_space, solution_space_filters, solution_metrics):
	solutions = []
	filtered_solution_space = solution_space
	// filter the solution space if possible
	for solution_space_filter in solution_space_filters:
		filtered_solution_space = apply_solution_space_filter(solution_space, solution_space_filter)
	// apply test to each possible solution in the filtered (or original) solution space
	for possible_solution in filtered_solution_space:
		solution = apply_solution_metric(possible_solution)
		if solution:
			solutions.append(solution)
	solutions = ['triangular blocks in solution space', 'square blocks in solution space']
	return solutions

// apply these functions to fulfill workflows involving the problem-solving intent of 'filter the solution space'

// apply the 'core' interface to the 'problem', to implement the 'break problem into sub-problems' workflow (since finding core structures like 'inputs/components' of a structure makes finding the structure easier to solve)
standardized_problem_definition = standardize_problem_to_interface(problem_definition, 'core')

// apply standard problem/solution information-finding functions inherent to most or all workflows
problem = identify_problem_attributes_functions(standardized_problem_definition)
problem_space = identify_problem_space(standardized_problem_definition, problem)
solution_space = identify_solution_space(standardized_problem_definition, problem_space, problem)
solution_space_filters = identify_solution_space_filters(standardized_problem_definition, problem_space, problem)
solution_metrics = identify_solution_metrics(standardized_problem_definition, problem_space, problem)

// given that we have the 'problem' object with the problem attributes like 'type' and problem functions, we can apply functions to fulfill problem-solving intents like 'find existing solutions for the problem type' or 'find causal problems to solve instead of the original problem'

// fulfill the problem-solving intent of 'filter the solution space', given that we have identified the solution space filters & solution metric required to call this function
// filtering the solution space involves applying the 'core' structures found as a solution metric tests to each possible solution
// by applying the 'core' interface & then filtering solutions, we are now filtering solutions to 'find combinations of subset components like three corners and closed shapes' instead of 'find blocks with three corners'
// this essentially applies a 'merge sub-solutions' operation of the 'break a problem into sub-problems & merge sub-solutions' workflow, finding the 'merged components' (combinations of three corners & closed shapes) that are required to find 'solutions to the original problem'
solutions = filter_solution_space(problem_definition, problem_space, problem, solution_space, solution_space_filters, solution_metrics)

// the application of these problem/solution functions should equate to the steps of the workflow, in terms of functionality (input/output similarities)
// alternatively, specific functions to implement the specific steps of the workflow can be generated with an interface query, rather than using general problem/solution functions like functions for a particular problem-solving intent

'''
- additional processing can be done to optimize the process followed to:
	- optimize generating the solution (the set of queries & functions applied) once the process (or associated structures like the 'specific state sequence') to generate it using this workflow is known
	- to compare this workflow's solution(s) with solution(s) produced by other workflows 
'''