
'''
- to do:
	- select implementation options of functions
		- implement a subset of functions that can be used to generate the others & store generated functions as combinations of implemented functions
			- 'core interaction functions': implement only core interaction functions, and write all functions as combinations of core functions
			- 'common functions': implement only common functions that can be used to create all other functions, define function requirements as combinations of implemented functions
		- write functions as a cmobination of math functions
			- example:
				- the 'filter' function described below would be structured as:
					- a sequence of objects in 3-d space, where:
						- one dimension is used to depict the sequence in order
						- another dimension is used to depict the sequence items' differences
						- a third dimension is used to depict the result of a test applied to each item
							- where the test is a template/scaffold structure and the inner shape allows for fitting a value derived from each sequence item
					- this structure would allow input/output value convergence sequences to be depicted as well, 
						from input sequence items, to items with conditional logic applied after test results, to updated value store, to final solution output value, with each step in the sequence
					- the test structure could be as simple as a loop or pipe that a value must be able to pass through, or a threshold value that a value must be able to cross over
						- for example, filtering a database table by a specified value means any passing values must fit a structure that only allows equal values to the specified value
					
			- how to translate the function into a set of math operations:
				- determine structures that match & can hold function components based on function/attribute/component similarities/equivalences, without any contradicting structures invalidating use of that structure, and without unnecessary structures
				- example query for a sequence:
					- 'find a structure that can hold a set of items that has an order, so that only one item of the structure is stored at each position of the structure (one y value for each x value), 
						that preserves the original order of the structure'
						- this implies a set of points that could be used to draw a line, which is an acceptable structure to use for the 'sequence' structure
						- this does not enforce which y-value is used for each item position in the sequence, so the y-value can be assigned to the value of each item
						- this structure has the advantage of allowing parallel sequences to be depicted, to show valuable info about differences between the original & parallel sequences
						- by changing x variable value (indicating position in sequence) & aligning the x-value with positions in parallel sequences, we can identify other useful info like 'patterns of differences' in the sequence
					
					- 'find a filter test structure that will not allow incorrect values, according to the input filter_test_structure (such as 'even' values)'
						- this can have many different structures, such as:
							- whole solution space (trial & error): computing a sequence of non-even numbers and checking if a value is a member in that sequence
							- generative: deriving a generative function of even values and checking if the value can be generated with that function
							- definition: deriving a test function of even values, based on a useful/adjacent definition of even (integer, having a remainder of zero when divided by 2) and applying that as the implementation of the filter test
							- pattern: deriving a function to test an attribute of even numbers based on their patterns (integer, having ones digit is in 0, 2, 4, 6, or 8)
							- opposite: deriving a test function of non-even values and applying the opposite of that as a filter

					- once you apply these two structure queries, you have:
						- a sequence structure (a set of points that can be joined to form a line) and 
						- a test structure (a check if the number is an integer and if the ones digit is even)
					- all thats missing at this point is the structure of the variable to store the updated value, and the break condition structure if there is one provided to the filter function config

					- at this point, we have math structures providing components of the filter function - we need to connect them according to the function's definition
						- the filter function definition includes interaction rules between components like:
							- iterate through (sequence) & (apply test to [each individual item])
						- to connect the sequence structure (set of points) & the test structure (check if value has a decimal and if the value's ones digit is in the set of (0,2,4,6,8)), we apply this rule to the structures of components in the definition:
							- iterate through the (set of points) and (check if [each point's] ones digit value is in the set (0,2,4,6,8) and if the value has a decimal)

					- so to identify the math structures that correspond with a function:
						- pull the function's definition, which has interaction rules like the above: 
							- 'filter' function definition interaction rule: 
								- iterate through (sequence) & (apply test to [each individual item in sequence])
						- identify structures in the function definition:
							- iterate
							- sequence
							- apply
							- test
							- individual item
						- query for structures matching these components
							- 'set of points having position on x-axis and value on y-axis' for a sequence
						- assemble structures found according to original interaction rules of the function's definition:
							- iterate through (sequence)
								- iterate through ('set of points having position on x-axis and value on y-axis')
						- test for structures that contradict the intent of the original function definition structures, or have any unnecessary structures beyond the definition, which is sub-optimal even if errors are immediately foreseeable

					- other advantages to this approach:
						- generating the function becomes a query of similar math structures, which have more definition/structure than other interfaces, allowing fewer ambiguities & other errors (given the structures in the 'filter' definition)
							- this query can be a query of differences between the original filter function query & the new custom filter function query

	- abstract workflows in apply() based on common components
	- adjust workflows in apply() based on variables of each structure, stored in apply() params variable
		- 'combine' has many possible combination_types
	- add support for other structures to apply
		- function
			- applies the function specified in params as a function of apply() inputs
		- attribute
			- applies the attribute specified in params to apply() inputs
		- structure
			- applies the structure (which may be a function or attribute) to apply() inputs
			- structure types
				- cross-interface structures like 'function_sequence'
				- core structures
				- core functions
	- format each function definition in terms of 'apply' function calls() wherever possible for organization & streamlining
	- fill in function logic with calls to other functions
	- identify which core functions are necessary to implement other required functions
	- identify which functions are possible to build given these core functions
	- identify if intended usage cases are covered by variables & function calls in function definitions

	- create index of function types:

		- function interface interaction types
			- functions
			- conditions
				- check input variable
				- check variable state
			- assignments
				- changes/updates
				- equivalences
					- copies
			- operators
			- iterations
			- triggers (inputs/outputs like return statements)
				- inputs
				- outputs
					- return statements

		- interface component interactions
			- insight paths
				- solution automation workflows
			- interaction level interactions
			- cross-interface interactions
			- useful concepts like interactivity

		- structure interface interaction types
		
- functions to build

	- apply logic/definitions

		- apply 

			- find
				- apply 'filter' structure
					- apply filters necessary to identify
				- apply 'test' structure
					- apply definitions of output (pass/fail) status to check for a component (like an interaction attribute, like 'equivalence' or 'requirement')
					- tests differ from normal filters in that they may involve generating/fetching values to test where none are provided, like an experiment

			- build
				- fill structure
					- apply definitions to build/fill/combine/connect a structure according to the definition (template) & available resources
			
			- change
				- apply a component definition (like a structure such as a sequence, an object like a definition or a function like 'inject') to another
					- apply structures
					- apply attributes
					- apply functions
						- change a structure
						- convert between formats
							- format input component as a:
								- system
								- generative/determinine function
								- network
									- causal network
									- function network
									- variable network
								- variable
									- formatting 'lyrics' as a variable (a standard variable like a datetime or multi-option field) would amount to:
										- creating a predictive/generative function allowing a variable value selection from configurable options as sub-parameters to the prediction function
'''

def generate_possible_structures(input, output_format):
	# identify all structures of input given item metadata, formats, interaction level, etc

def pull_definition(keyword):
	# in the returned definition, the object that is not 'input' is assumed to be the output unless otherwise specified
	# like if the defined item 'component' is specified in the definition logic
	definition = ['set(item) == input'] 
	# set(item) is the 'output' being defined, as in the 'components' of the input
	return definition

def generate_structure(structure, inputs):
	#definition_filter = 'unit'
	#test = generate_structure(structure='test', inputs=definition_filter)
	#test = 'len([possibility for possibility in generate_possible_structures(items) if possibility == items]) > 0'

def define(keyword):
	keyword = 'component.type == core'
	definitions = {}
	for item in [keyword].split_by_all_delimiters():
		definitions[item] = pull_definition(item)
		'''
		if item == 'component':
			definitions[item] = ['set(item) == input'] # set(item) is the 'output' being defined, as in the 'components' of the input
		if item == 'type':
			definitions[item] = pull_definition(item)
			definitions[item] = ['input in set.name'] # set.name is the 'output' being defined, as in the 'type' of the input
		if item == 'core':
			definitions[item] = pull_definition(item)
			definitions[item] = ['input = apply(standard_ops, inputs=core_inputs)'] 
		if item == 'combination':
			definitions[item] = ['all possible sets including items']
		'''
		# the input is created by calling the 'apply' function on the 'output' being defined, meaning the core items of the input
		# standard_operations is a global variable, referencing a list of core standard basic interaction functions like add/combine/connect 
		# ['unit', 'isolatable', 'unique', 'generative', 'common']
	#now organize these definitions so they make sense in the original format 'component.type == core'
	function_version = 'component.type == core'
	# target output definition of 'merge' function:
	# 'type of set(items) that can build input and is equal to input' == 'core' #, so that items are members of "core" set'
	applied_definition = apply(structure='definition', inputs=[definitions, function_version])
	# call standardize to make objects as equivalent as possible for intents like 'compare'/'merge'
	standardized_definition = apply(structure='standard', inputs=applied_definition)
	# call merge to organize definitions into a final definition of 'core_component_combinations'
	merged_definition = apply(structure='merge', standardized_definition)
	merged_definition = 'set(items) that create & equal input is a set in the "core" set'
	return merged_definition
	# now we have a definition of 'core_component_combinations' by applying the definitions of each item in the keyword to define 
	# & organizing those definitions so they interact

	# another alternative workflow is as follows
	# below, in the apply() function, 
	# we reverse-engineered the filtering logic by injecting definitions to the formatted function_logic definition,
	# to create a filtering function that could identify structures matching a definition 
	# here, we are implementing the apply() function by first generating structure possibilities in all_item_structures 
	# and applying a 'filter' structure to them in the form of test_logic for definition structures to find structures fulfilling the definition
	# (like applying test logic for 'unit' and 'generative' structures of the 'core' definition)
	all_possible_definition_structures = set()
	for keyword in keywords: # 'core', 'component', 'combination'
		definitions = pull_definition(keyword)
		possible_definition_structures = apply(structure='filter', inputs=original_items, params=definitions)
		all_possible_definition_structures.add(possible_definition_structures)
	# merge the definition structures so they create a final definition
	merged_definition_structures = apply(structure='merge', inputs=all_possible_definition_structures)
	return merged_definition_structures

def apply(structure, inputs, input_format, output_format, metrics, logic, params):
	'''
	- apply is always changing the input structure with some core interaction function, like:
		- filtering
		- reducing
		- connecting
		- filling
		- creating
		- deriving
		- formatting
		- organizing

	- apply() function, which implements: 
		- an interface query containing:
			- a standard solution automation workflow:
				- 'determine differences between input/output & reduce differences'

	- constant logic of the apply() function

		- validate:
			- validating initial checks that the inputs can interact in the requested structure
				- check if the input structure (filter) can be applied to the inputs given the input format
				- check if the input structure (filter) can be applied in the structure given in the logic/conditions
				- check if the logic/conditions contain only inputs supplied/available to the function
				- check if inputs can be converted into outputs given the output format
				- check if inputs can be converted into outputs using the logic/conditions
				- check if selected logic complies with the input structure (filter) structure definition, according to requirements from that structure's definition:
					- a 'filter' structure would have:
						- required logic:
							- a test function embedded in the iteration that the input structure (or some adjacent iterable structure of it, like its components) can be an input to
							- an iteration to apply the test to each item in input
						- optional logic according to the 'filter' structure requirements:
							- iteration variables (like 'break/continue conditions')
							- test variables (like 'equivalence operators')
						- variable logic that varies by the input structure & params:
							- which structure of the input is iterated
							- multiple tests based on conditions

		- define:
			- pulling definitions of params and deriving definitions from a standard set where a definition is missing
			- standardization of definitions of params 

		- connect:
			- connect inputs/outputs
				- determining structure of changes required to convert input into output
				- converting required changes into a standard structure, like a function structure
				- iterating through this standard structure, generating calls to apply() to generate its components (like functions)

			- this is where custom logic often occurs at some point in the connection sequence, in the form of a function interface defined for the structure, 
				(like the traditional software definition of a 'function interface', meaning a 'list of required functions')
				like how 'filter' function interface has defined required functions:
				- iterate through items
				- test each item in iteration in each iteration
				- update value based on test in each iteration
					- possibly breaking & skipping to return on some value
				- return updated value
			- the connection sequence between inputs like a list of items & a test to filter with, and the output of a value based on these tests & the items 
				will look like the above 'filter' function interface once generated by an interface query, possibly with more detail and different variables, like:
					- whether to break once a test passes/fails
					- whether to apply multiple or alternate tests or other test structures
			- the connection sequence specifically may be implemented as:
				- original problem inputs: 
					- list of items
					- filter test structure
					- logic to execute if test has a particular output
					- break condition
				- original state of output in sequence:
					- the value of the variable that is updated in the loop, if there is one, is instantiated with a default value
				- original state of input in sequence: 
					- list of items
				- operation to convert input state (list of items) to state (individual item) that coordinates with other input (test)
					- apply 'iteration' to convert 'list of items' into an 'individual item', which is the input of the 'filter test structure'
				- new state of input in sequence:
					- individual item
				- operation to convert input state (individual item) to state (boolean) that coordinates with output state (variable value to update)
					- apply 'test' to individual item to get the output of the test (usually a boolean)
				- new state of input in sequence
					- boolean
				- operation to connect input state to output state
					- apply logic to create updated value once test is determined to pass, which may be a simple assignment of the updated value to the boolean, to the value, or adding the value to a list
				- new state of output in sequence
					- boolean flag variable set, variable set to individual item value or version of it created by conditional logic, or variable containing a value set passing the test
				- operation to connect current input state & current output state to final output state (returned value)
					- break condition test application, if specified
				- new state of output in sequence:
					- once the break condition is encountered or the loop exits, the new state in the sequence is the updated variable value that was updated by conditional logic in the iteration, 
						if there is a variable updated according to a condition that was fulfilled in the iteration, otherwise the variable value is its original default value it was instantiated with
					- solution output is the updated value, if a value based on the list items content is returned and no break condition was specified or reached, 
						where the output value is based on list items content (like a boolean based on whether a value is found, or the value itself, or a list of all values fulfilling the test filter structure)
			
			- a particular filter function implementation may differ in the connection structure, which may have multiple possible outputs & output paths, taking the form of a tree/network instead of a sequence

			- input/output connection structure:
				- the inputs & outputs run in parallel in this function, since the output is usually initialized at the beginning before the function logic based on inputs starts in a 'filter' function
				- the inputs also interact laterally with the outputs according to conditional logic (run according to a test application) and any break condition specified

		- apply:
			- apply connections between inputs/outputs
				- executing the calls to apply() that would generate the components of the standard structure to translate inputs to outputs

	- variable logic of the apply() function:

		- formatting applied to the input before the changes
		- how the changes to the input are determined
		- how the changes to the input are done
			- what function is used to apply a change required in the input/output required change structure
				- whether a prioritized function is passed in params
			- whether those functions are found/derived/generated
		- structure-specific variables stored in params
	'''
	#structure = 'combination(components.type=core)'
	#inputs = [['1','2','3'], ['4','5','6']]
	outputs = set() # returns input structures matching the structure

	'''
	- each structure can have its own associated apply() workflow, which can be generated or defined but generally follow the pattern
		- standardize according to differences between input_format & structure requirements
		- define undefined keywords
		- apply logic if given, otherwise derive logic:
			- derive/generate possibilities of the structure applied to inputs
				- identify correct total structure definition (definition of 'core components' as 'set of items that can create/equal the input')
					- generate possibilities from that definition
				- identify input structures matching individual structure keyword definitions & merge to match total structure to generate possibilities
			- derive & apply filter/test to reduce possibilities 
		- apply metrics if given
		- format filtered possibilities by output_format
		- return formatted filtered possibilities
	'''

	#standard_structure = format_input()
	#1. format input structure into a standard structure (like a structure of functions such as a function network) to apply to the input
	
	#function_definition for structure = 'combination(components.type=core)':
	function_definitions = ['find components with type=core', 'combine output of previous function', 'return combinations from previous function']
	#function_definition for structure = 'filter':
	function_definitions = ['iterate through filters', 'apply filter to update input', 'return filtered input']
	
	#standard_structure(inputs)
	#2. apply structure to inputs, by iterating through functions in function_definition according to its structure:

	if structure == 'definition':

		#applied_definition = apply_definitions(item_definitions, standardized_function_version): 
		#apply_definitions has logic like:
		#	- replace keywords with definitions 
		#	- create placeholder variables (like 'core_inputs') to organize variables according to definition 
		for defined_item, item_definitions in definitions.items():
			function_version = function_version.replace(defined_item, item_definitions)
			#for example, replace 'component' with 'set(item) == input'
		definition_states = [
			'type' 							'of set(items) = input' 		== 'core'
			'input in set.name' 			'of set(items) = input' 		== 'core'
			'input in set.name' 			'of set(items) = input' 		== 'input = apply(standard_ops, inputs=core_inputs)'
		]
		return definition_states[-1]

	elif structure == 'merge':
		# call merge to organize definitions into a final definition of 'core_component_combinations'
		merged_definition = merge(standardized_definition)
		# merge has logic like:
		#merged_unit = join(field1, field2)
		#for example, join 'set(items) equal input' with 'core_inputs create input' to create 'set(items) that create & equal input'
		equivalence_to_replace_with, rules_with_equivalence = get_common_items(definition)
		new_definition = []
		for definition_item in definition:
			for equivalent_rule in rules_with_equivalence:
				# inject the standardized definition, the first item returned, in place of the others
				definition_item.replace(equivalent_rule, equivalence_to_replace_with)
			new_definition.append(definition_item)
		definition_states = [
			'set(items) equal input' 				'is a member of set.name'		== 'core_inputs create input'
			'set(items) that create & equal input'  'is a member of set.name' 		== 'core'
			'set(items) that create & equal input'  'is a member of the "core" set of sets' # meaning it fulfills 'core' type tests
			'set(items) that create & equal input is a set in the "core" set'
		]
		# now we know what structure to look for when looking for 'core component combinations' (a set that can create and equal the input)
		# in order for this condition to be true, the core set has to be an 'ordered list of items' (in order to be able to equal & create the input)
		# so this applies a very specific definition of 'core component combinations' as an example
		return definition_states[-1]

	elif structure == 'standard':
		# standardize(applied_definition): 
		#- standardize logic:
		#	- detects & replaces equivalent keywords ('core_inputs' = 'set(items)')
		#	- detects & replaces equivalent operators & words ('=' = 'equal')
		#	- simplifies functions ('input = apply(standard_ops, inputs=core_inputs)' = 'core_inputs create input')
		# converting to plain language may be unnecessary but its more readable
		definition_states = [
			'input in set.name' 			'of set(items) = input' 		== 'input = apply(standard_ops, inputs=core_inputs)'
			'set(items) = input' 			'is a member of set.name'		== 'core_inputs create input'
			'set(items) equal input' 		'is a member of set.name'		== 'core_inputs create input'
			'set(items) equal input' 		'is a member of set.name'		== 'set(items) create input'
		]
		return definition_states[-1]

	elif structure == 'filter':
		matching_structures = set()
		#- function_definition = 'iterate through filters'
		for filter_item in metrics:
			#- function_definition = 'apply filter to update input'
			# identify all structures of items given item metadata, formats, interaction level, etc in the same format as the input (a set)
			# given that the input is a set, we know the generative formats (another set, a set of sets, a function that outputs a set)
			# we dont know which specific items in those formats created from the inputs can generate a set 
			# fulfilling a definition of 'core component' unless we:
			#	- try many combinations of items to see if they can generate a set
			#	- format the definition as a structures of available functions, and select specific versions of those functions to apply
			filter_item = 'unit'
			test = generate_structure(structure='test', inputs=filter_item)
			test = 'len([possibility for possibility in generate_possible_structures(items) if possibility == items]) > 0'
			# outputs a condition to test if an item set in item_structures is equal to items
			# an item is a unit of a set if it can be combined to equal the set
			# generate_possible_structures() is a function that allows any set of attributes/components/functions of the input
			#if the original_inputs is found in the combinations of generated_possible_structures, that structure is a core set of the original_inputs
			generated_possible_structures = [
				['1', '2', '3'],
				['integer', 'even', 'odd'],
				['sequence(n + 1)']
			]
			passed_test = apply(structure='test', logic=test, inputs=[items], outputs='possibility')
			if passed_test:
				# this component fulfills the definition, so add it to the list of output components 
				matching_structures.add(passed_test)
				break	
		#- function_definition = 'return filtered input'
		return matching_structures

	elif structure == 'function_sequence':
		core_component_combinations = set()
		for function in function_definitions:
			#- function_definition = 'find components with type=core'
			core_components = apply(structure='components', metrics='type=core', input=inputs)
			#- function_definition = 'combine output' 
			# output refers to output of previous function, if function_logic is an ordered sequence, and any input functions if not
			core_component_combinations = apply(structure='combine', inputs=core_components)
			''' now we combine the output of 'find components with type core' to generate the final output, which is core_component_combinations '''
			#- function_definition = 'output combinations from previous function'
		return core_component_combinations

	elif structure == 'components':
		core_components = set()
		''' to find components with type 'core':
			1. define any undefined keywords in the function_definition
				- standardized_undefined_keywords = standardize any undefined keywords in function 'find components with type=core' 
				- standardized_undefined_keywords = 'component.type=core'
				- item_definitions = pull_definitions(items in standardized_undefined_keywords)
				- definition = apply_definition(item_definitions, standardized_undefined_keywords)
				- definition = standardize(definition)
				- merged_function_definition = merge(definition)
			2. apply the new merged_function_definition to the input, once merged with definitions of previously undefined keywords
				- core_components = apply('filter', params=merged_definition, original_items) 
					#core_components equal the original_items input in this very specific case, 
					#	applying a specific definition of 'core' & 'component' that happen to have an overlap structure
				- core_components = [['1','2','3'], ['4','5','6']]
		'''
		return core_components

	elif structure == 'combine':
		#1. define any undefined keywords in the function_definition
		#	- function_definition = 'combine(core_components)'
		#	- merged_function_definition = 'generate all possible sets of core_components'
		#2. apply the new merged_function_definition to the input
		all_combinations = set()
		for i in range(0, len(inputs)):
			core_component_combinations = itertools.permutations(inputs, i)
			all_combinations.update(core_component_combinations)
		return all_combinations

	return False


def identify(input_structure, filter_structure):
	# identify any changes necessary to make filters in filter_structure applicable to input_structure, then execute those changes
	differences_in_input_structure_filter_pairs = apply(
		structure='filter', 
		input=[input_structure, filter_structure.input, filter_structure], 
		input_format=['structure', 'input', 'structure'],
		logic=['for item2, item1 in map(filter_structure, input_structure), output.append(diff(item1, item2.input)) if item1 != item2.input'], 
		# inputs in the input_structure are checked for equivalence with filter_structure inputs, according to 'filter_structure' structure (like its sequence)
		outputs=[set(list(input_structure.x, filter_structure.input.x))], # 'x' indicates any matching structures from inputs that fulfill filter conditions
		output_format='item_sets_from_lists' # like 'pairs' having one item from each list
	)

def test(item1, item2, condition):
	'''
	- finds out if item1 and item2 fulfill the condition involving their potential interaction rule
		- if the interaction_rule applies, or if the condition is true
	- may involve simulating the interaction, or finding out what info to request & requesting that info, in order to test the interaction rule
	'''

def connect(item1, item2):
	#- connect item1 and item2 

def reduce(input, metrics):
	#- reduce variables/components/differences or other metrics of input, given metrics to reduce

def derive(input, output, prioritized_interaction_functions):
	#- derive the output from the input
	#- using whatever generative/connecting or other core interaction functions are available, or prioritized_interaction_functions if specified

def filter(input, filters):
	#- filter the input by the specified filters

def find(structure, input):
	#- find the specified structure in the input

def define(input):
	'''
	- defines input according to any structures that are found to be equal in some way, like:
		- filters indicating what it is not or requirements
		- interaction functions that arent contradicted
	'''

def combine(item1, item2, metrics, combination_type):
	#combines input items in a structure that can contain them, fulfilling metrics if given, according to the specified combination_type

def predict(output, input, prioritized_methods):
	#predicts output given input, applying prioritized_methods if given

def decompose(input, interaction_level): # core, specific
	#breaks input into components on specified interaction_level

def build(output, output_format, input, input_format):
	#builds output using input

def change(input, using_process, fulfilling_metric):
	#applies changes to input using a process or fulfilling a metric

def fill(structure, input):
	#applies input to fill structure

def merge(item1, item2):
	#merges items from input sets where differences can be captured by adding variables to merged item

def organize(items, structure, metrics):
	#positions items in the structure, according to coooperative/fitting structures, outputting every possible organization that fulfills metrics

def compare(item1, item2):
	#identifies comparable items forming a set having one item from each list 
	#compares those pairs, adding differences to output

def distinct(item1, item2):
	# gets distinct items that are in one set but not the other

def equalize(item1, item2):
	# changes input items until they are equal, returning list of operations applied

def diff(obj1=item1, obj2=item2, diff_types):
	'''
	- diff(item1, item2) function:
		- assumes we are convert item1 into item2
		- does a comparison between the two inputs, so that the differences between them indicate the changes necessary to convert one to the other
		- diff(image, video) would output the list of steps ['multiple images in a sequence'] to convert an image to a video
	'''
	required_changes = set()
	all_differences = {}
	all_difference_components = set()
	all_distinct = {}
	all_distinct_components = set()

	item1_def = pull_definition(item1)
	item2_def = pull_definition(item2)
	objects, attributes, functions = pull_definition(item1):
	o2, a2, f2 = pull_definition(item2)

	# iterate through difference types & get differences of that type between inputs
	diff_type_function_map = {
		'distinct': 'missing', # diff type 'distinct' maps to error type 'missing', with solution functions like 'create'
		'compare': 'unequal' # diff type 'compare' maps to error type 'unequal', with solution functions like 'equalize', 'balance' or 'distribute'
	}

	diff_types = get_all_diff_types() if 'all' in diff_types else diff_types 
	for diff_type in diff_types:

		# get distinct items from each set
		for pair_type, set_pair in ['objects': [objects, o2], 'attributes': [attributes, a2], 'functions': [functions, f2]]:
			distinct_items = apply_function(diff_type, set_pair[0], set_pair[1])
			#distinct_items = set('objects', 'found', 'only', 'in', 'one', 'input')
			#different_items = set('differences', 'between', 'comparable', 'objects')
			if pair_type not in all_distinct:
				all_distinct[pair_type] = set()
			all_distinct[pair_type].update(distinct_items)
			all_distinct_components.update(distinct_items)

		for difference in all_distinct_components:
			# find solutions for diff_type = 'distinct' having associated error_type 'missing'
			changes_found = find_solutions(diff_type_function_map[diff_type], difference)
			if changes_found:
				required_changes.update(changes_found)

	if required_changes:
		return required_changes
	return False

	change_structures = apply(
		structure='connect', 
		input=unequal_input_structure_filter_pairs,
		input_format='item_sets_from_lists',
		logic=['iterate_through_input', 'apply_logic'], # 'logic' being applied is the 'connect' structure, acting like a symbol indicating input logic
		outputs=[connecting_change_sets_for_input_pairs],
		output_format=['structure_of_change_sets'] 
		# a list of change sets is created first, then the list items are connected in a structure that makes sense (such as by connecting interactive inputs/outputs)
	)
	changed_input = apply_function('change', change_structure, input_to_change)
	for individual_filter in filter_structure:
		apply_structure('filter', logic=individual_filter, inputs=changed_input)

def convert(input, input_format, output_format):
	'''
	- identify structure of structures that fulfill a core interaction function between input_format and output_format 
		- identify_fulfilling_structure(structure='sequence', core_interaction_function='connect', params=[input_format, output_format])
			apply_structure('filter')
	- once structure sequence is identified, determine changes necessary to convert between each sequence pair 
	- once change sequence between structure sequence is identified, identify which calls to apply_* will make those changes
	- once the required apply_* function calls are identified, execute those calls
	'''

def apply_component(component_type, component_to_apply, componet_to_apply_to):
	#'component' can mean a function like 'change', attribute like 'usefulness', structure like 'sequence', object like 'definition' or 'interface'
	#applies 'component_to_apply' to 'component_to_apply_to'


''' example of apply_structure() is apply('core_component_combination', items)'''
original_items = [['1','2','3'], ['4','5','6']]
#apply core combination combinations of original items to get combinations like ['1','2','3'], ['1', '2'], ['1', '4'], etc
core_component_combinations = apply(structure='combination(components.type=core)', input=original_items)
#by calling apply() on a function structure, we are deriving/finding/generating & executing the logic 
#to retrieve the output core_component_combinations from the input original_items
