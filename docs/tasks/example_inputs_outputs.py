# find the relevant interactions (and the useful structures of these interactions) in the input system variable interactions, after finding the causal structures in the input system
input_system_variables = ['teeth enamel thickness', 'nail length', 'acid intake', 'vinegar intake']
structure_interface_structures = ['none', 'low', 'medium', 'high']
input_system = ['high acid intake': 'teeth enamel thickness reduction', 'nail length reduction': 'high vinegar intake']
causal_interface_structures = ['1-degree causal input/output connection', 'causal loop']
function_interface_structures = ['repeat', 'reduce']

causal_structures = apply('cause', type='interface', input=input_system, output='standard')
causal_structures = {
	'1-degree causal input/output connection': [
		'high acid intake': 'teeth enamel thickness reduction', 
		'high vinegar intake': 'nail length reduction'
	],
}

function_structures = apply('function', type='interface', input=input_system, output='standard')
function_structures = {
	'repeat': {'high -> reduce': 'variable connection structure between both input pairs'},
	'reduce': {'acid intake': ['teeth enamel thickness', 'nail length']}
}

structural_interface_structures = apply('structure', type='interface', input=[function_structures, causal_structures], output='cross-interface')
structural_interface_structures = {
	'structural_similarity': {
		'high x intake': 'y length reduction'
	},
	'variable_function_combinations': {
		'teeth enamel thickness reduce high acid intake', 'teeth enamel thickness reduce acid decomposition', 'teeth enamel thickness reduce nail length', # ...
	}
}

possible_structures = apply('potential-cause', type='interface', input=structural_interface_structures, output=['alternate', 'core causal structures', 'indirect inference (without requirement of possibility)'])
possible_structures = {
	'possible_causal_structures': {
		'alternate': ['(vinegar-to-acid decomposition or acid output) as higher adjacency cause than vinegar'],
			# could either of the input 1-degree variable causal function components be equivalent in some way (could acid equal vinegar, could nail equal enamel)
		'causal_loop': ['output of teeth enamel thickness is input of nail length or vice versa', 'prior acid intake (worsens or enables) acid function impact']
	}
}

useful_structures = apply('meaning', type='interface', input=[structural_interface_structures, possible_structures], output='standard')
useful_structures = {
	'components': ['vinegar.acid'],
	'relevant': [
		'variables': [['teeth enamel', 'nail length'], ['acid intake', 'nail length'], ['acid intake', 'teeth enamel']], 
			# teeth and nails are related somehow, and both are related to acid
		'derived_variables': [['high acid intake', 'exterior barrier and functional tissue length reduction'], ['low acid intake', 'no impact on exterior barrier and functional tissue length reduction']], 
			# what variables might exist, how might they interact with these variables
		'functions': [['vinegar.acid', 'reduce'], ['vinegar.acid', 'reduce vinegar to acid'], ['teeth enamel/nail length', 'reduce length'], ['teeth enamel/nail length', 'reduce barrier or functional tissue length']],
			# what functions can be identified
		'external interaction functions': [['(teeth enamel component or nail component) as input (or similarity to input) of (acid or acid components or acid functions)']]
			# what interaction functions might exist with other components other than these variables
	]
}