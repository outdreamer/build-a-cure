from utils import *

def get_concept_metadata(concept_name):
	concepts = get_data('concepts.json')
	if concepts:
		if concept_name in concepts:
			concept = concepts[concept_name]
			''' get definition for concept '''
			definitions = get_data('definition_routes.json')
			if definitions:
				if concept_name in definitions:
					concept['definitions'] = definitions[concept_name]
			if 'functions' not in concept:
				concept['functions'] = []
			functions = get_data('functions.json')
			if functions:
				if concept_name in functions['interface_functions']['concept_functions']:
					concept['functions'].extend(functions['interface_functions']['concept_functions'][concept_name])
				rules = get_data('system_logic_rules.json')
				if rules:
					if concept_name in ' '.join(rules.keys()):
						for key, val in rules.items():
							if concept_name in key:
								if type(val) == list:
									concept['functions'].extend(val)
				concept_functions = find_functions_in_dict(functions, [], search_term)
				if concept_functions:
					concept['functions'].extend(concept_functions)
			return concept
	''' to do: make call to define concept if no definition is found '''
	return False

def get_function_metadata(fdef, delimiter):
	function_items = fdef.split(delimiter)
	if len(function_items) > 0:
		function = function_items[1].replace('):', '').split('(')
		if len(function) > 1:
			function_name = function[0]
			syntax_function_name = ''.join(['def ', function_name, '('])
			function_params = function[1].replace(' ','').split(',')
			function_code = []
			start_adding = False
			function_path = ''.join([function_items[0], '.py'])
			if os.path.exists(function_path):
				code = get_data(function_path)
				if code:
					for line in code.split('\n'):
						if syntax_function_name in line:
							start_adding = True
						else:
							if start_adding:
								if 'def ' in line:
									start_adding = False
								else:
									''' to do: add filter for comments '''
									function_code.append(line)
				function_def = {'name': function_name, 'params': function_params, 'code': function_code}
				return function_def
	return False

def get_problem_metadata(problem_def_path):
	print('function::get_problem_metadata')
	'''
		1. Identify problem metadata
			- problem type
			- default/original problem type (position on problem type network)
			- adjacent problem types
			- component problem types
			- related problem types
			- combination problem types

			- problem structure
				- space (output dimensions to measure solutions)
				- structure (gap/limit/force/conflict/intersection)

			- problem attributes
				- interfaces (dimensions that frame or highlight variable value change rules)
	'''
	''' to do: add metadata id functions '''
	problem_metadata_path = 'workflow1_problem_metadata.json'
	problem_metadata = get_data(problem_metadata_path)
	if problem_metadata:
		return problem_metadata
	problem_def = get_data(problem_def_path)
	if problem_def:
		return problem_def
	return False