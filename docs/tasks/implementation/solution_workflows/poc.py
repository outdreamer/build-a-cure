'''
Terms:
- objects: a data set, function set, attribute set, class definition, type hierarchy
- attribute value: value held by the attribute like True/False
- attribute property: conceptual metadata property of the attribute like unique, identifier, static, etc
- decisions:
  - choosing to execute one section of code over another; 
  - for example a conditional statement, design patterns, emergent usage/behavior 
    of user/system, bugs, assumptions, & possible input values are decisions since
    they may result in calling different code
- relationship types: sub-type, causal factor, cooperating equal, different version
- strategy: rule used to make decisions, possibly for a particular context
- solution: strategy implemented for a particular context & problem type

Abstract functions to code:
1. identify an attribute of an object (lookup definition of attribute, create logical tests based on definition)
2. identify & list all attributes of an object (database table fields)
3. identify & list all rules related to an object (entries in 'functions' database field)
4. determine if an attribute is new or fits into an existing attribute & whether its an ancestor or descendant of other attributes
5. add an attribute to a list of attributes of an object (add column to table)
6. identify all possible values of an attribute (alphanumeric, numbers, a value from a list)
7. identify all rules defining the list of possible values of an attribute (max length, string data type, contains limited characters)
8. identify all possible properties of an attribute (static/regularly changed, required, unique, identifier, causal, determines other attributes)
9. identify attribute/rule/type/object relationship rules (attribute A is used to calculate how attribute B should be updated or deleted)
10. identify rank/priority of attributes used to make decisions like classification in entity group, identification of unique entity
11. classify a field as a particular type (by category or data format or other identifying or deciding attribute having multiple possible values)
12. build a class definition 
  - retrieve any known rules describing the object's interactions
  - build a list of probable attributes which could be inherited from type ancestors or shared with other objects interacted with in rules
  - retrieve the type hierarchy position based on attribute/rule similarity to ancestors/descendants
  - filter possible attributes by which attributes can be used to identify it, which will be tagged with the 'required' property
    - identifying attributes are those that maximize variance
  - retrieve the values for these attributes required to qualify as an instance of the class
  - assemble attribute-identification functions for each attribute if not already in database table 'functions'
  - derive any additional interaction rules to describe interactions with other objects (if interaction data is available)
13. convert data from one format to another
  csv/graph to database, csv to graph/functions, functions to patterns/objects, log to csv/database
14. identify data relevant to the same object
15. prioritize which version takes precedence over other versions (updated more recently, better design, etc)
16. determine intent (of data, function, design, convention, protocol, decision, change)
17. identify a change that should be entered into the 'functions' table as:
  - a 'conversion' function type, which converts from one usable format to another
  - a granular 'operation' function type doing a single operation on an input
18. identify a pattern 
  to store in the 'functions' table as a 'pattern' function type
19. identify which operation or combination of operations can convert one object into another
  to know which linking changes to look for when trying to connect two objects
20. derive a relationship using list of possible operation sets that convert an object into another or explain their interaction rules
  - identify if one object is a sub-type, causal factor, cooperating equal, different version, etc of the other object
21. identify if a relationship fits into an existing network or if it contradicts a relationship in the network
22.identify if a strategy is a good fit to compress a problem & addresses its causal metrics without causing bigger problems
23. compare two input objects & return a list of similarities & differences,
   as well as possible inferred similarities based on network position with probability,
   and a list of ordered functions to convert one object into the other
   - raw % difference between attribute values & attribute properties
   - weight of attribute value differences based on attribute priority
   - create attribute-rule network graph for each object & calculate raw degree of difference
   - identify equivalent attributes & weight degree of difference between them & their corresponding relationships across graphs
   - check equivalence of composite scores
24. identify minimum information needed to make a decision (identify required inputs to make the right decision 100% of the time)
25. identify operations to attain minimum required information (generate required inputs for decision)
26. optimize code (spot inefficiencies in code & fix them automatically, like redundant conditions)
27. identify field usage/query requirements in UI, request data, & code base
  ex: 'code commonly queries by name field so create a separate index for that'
'''

'''
- example of automating solution of & finding/deriving insight paths for a basic calculation
'''

def apply_solution_automation_workflow(workflow_metadata):
  '''
    - applies logic from solution automation workflow workflow1
      - create function connecting input/output format

    - apply_solution_automation_workflow calls the logic associated with workflow1, including the function implementing the 'workflow intents', like 'connect problem input & ssolution output':
      
      - apply_structure('function.connecting', workflow_objects['standardized_problem_statement'], workflow_objects['solution_output_format']) 

          - answers the question:
            - 'given input resources of workflow_objects['interface_functions'] & the problem formatted as a difference between input/output format'
              - 'how can convesrsions be applied to connect input/output format'
              
          - executes logic:
            - identifies interim formats connecting problem & solution formats (interface query)
                - identify steps to connect input variable value & output variable value
                  - identify steps to connect input exercise type units & output exercise type units
                    - standardize exercise types to one exercise type
                    - I. identify input/output format value (energy units) associated with proxy variable (standardized exercise type unit, a)
                    - II. convert standardized input exercise type format value (a = 5/13 energy units) to the output exercise type format value (b = 5/13 energy units)
                    - III. apply output exercise type format value to unsolved solution output variable x (x = 6 * 10/13 energy units)

            - applies interim formats to connect problem input & solution output
              - generated logic from solution automation workflow could look like this:
                - to connect solution output & problem input, build functions to resolve sub-differences by:
                  1. connecting exercise type 1 & 2
                  2. standardizing to units of the same exercise type
                  3. connecting new value of problem input energy units after standardizing to units of an exercise type & the original value of solution output units

      - apply methods to connect problem input & solution output

        - find function connecting problem input & solution output in original equation set by standardizing to interim interfaces (variables a, b, & x)

          - apply standardization & connecting (equalizing) methods to solve for interim format sequence connecting problem & solution formats:
            I. find a in energy unit format
            II. find b in a format
            III. find x in b format

            - query sequence for interim format sequence (a, b, x) created with missing info logic (a in terms of energy units, b in terms of a, x in terms of b)
              
              I. find a in energy unit format:
                - find energy units for a (1 unit of exercise type 1)
                  - query: reduce original equation to variable a by applying a standardization method connecting function of b & a
                        
                        1. identify standardization structure (path)
                          - standardization to equate problem input & solution output requires either:
                            - A. converting minutes at speed 1 to minutes at speed 2 or vice versa (converting to speed 2 requires fewer operations)
                              - find connecting function of speed 2 b & speed 1 a energy units
                                  - connecting function:
                                    - energy units of speed 2 b = x * energy units of speed 1 a
                                    - b = xa
                              - if none found, use default numerical connecting function
                                  - connecting function:
                                    - energy units of speed 2 b = 2 * energy units of speed 1 a
                                    - b = 2a
                            - B. converting energy units used to a minute/speed unit or vice versa (converting to exercise type unit requires fewer operations without losing required info)

                        2. apply standardization connecting function of method A: energy units of speed 2 & speed 1 (b = 2a)
                          - original function
                            - 5 energy units = 5 units of type 2 exercise + 3 units of type 1 exercise
                            - 5 energy units = 5 minutes * speed 2 + 3 minutes * speed 1
                          - apply variable labels to units with coefficients
                            - a = minute of type 1 exercise
                            - b = minute of type 2 exercise
                            - 5 energy units = 5b + 3a
                            - 5 energy units = 5 * 2 * a + 3 * a = 13 * a 
                            - 5 energy units = 13a = 13 units of exercise type 1 (speed 1)
                            - a = 5/13 energy units
                            - 1 unit of exercise type 1 (speed 1) = 5/13 energy units

              II. find b from a:
                - find energy units for b (1 unit of exercise type 2) in terms of a
                  - query: convert value for that variable to value for solution output format (b)
                        - find energy units for unit of exercise type 2
                          - apply standardization connecting function of method A: energy usage of speed 2 & speed 1 (b = 2a) 
                          - how many energy units does a unit of each exercise type use?
                            - one unit of exercise type 1 (speed 1) uses 5/13 energy units
                            - two units of exercise type 1 (speed 1) uses 10/13 energy units
                            - one unit of exercise type 2 (speed 2) uses 10/13 energy units
                            - b = 10/13 energy units

              III. find x number of energy units from b:
                - find x energy units of 6 units of exercise type 2
                  - query: apply energy units/per unit of an exercise type to find energy units for 6 minutes of type b exercise
                    - x energy units used = 6 minutes * speed 2
                    - x = 6 units of exercise type 2 (speed 2) = 6 * 10/13 = 60/13 energy units

  '''

  # inherit available functions from interface analysis function table in database, and/or pull dynamically from queries of code data sources, to use later when connecting interim formats
  workflow_objects['interface_functions'] = {
    'math': ['add', 'subtract', 'multiply', 'divide'], 
    'structure': ['direct/pivot', 'combine', 'merge', 'break', 'reduce', 'convert', 'fill', 'fit', 'match', 'map', 'filter', 'identify', 'connect', 'subset'],
    'system': ['optimize', 'equalize', 'differentiate', 'assume = apply(condition/input)'],
    'core': ['find', 'build', 'derive', 'apply'],
    'interface': ['change', 'depend (cause)', 'prioritize (intent)', 'structure', 'communicate (info)', 'abstract', 'systematize', 'possibilize/empower (potential)', 'standardize (core)', 'typify', 'functionalize', 'objectify', 'describe (metadata/attributes)', 'define (certainty)', 'randomize (uncertainty)', 'connect/organize (interface)']
  }

  workflow_objects['standardized_problem_statement'] = standardize_problem_statement(problem_statement)
  workflow_objects['standardized_problem_statement'] = 'find energy units for 6 minutes at exercise type 2, assuming 5 energy units for 5 minutes at exercise type 2 & 3 minutes at exercise type 1'

  # I. apply function interface to get variables, constants & functions
  workflow_objects = apply_interface('function', problem_statement)

  # II. apply structure interface to get variable structures
  workflow_objects = apply_interface('structure', problem=problem_statement, workflow_objects)

  # III. apply info.problem interface to get problem metadata
  workflow_objects = apply_interface('info.problem', problem=problem_statement)

  # IV. connect problem input & solution output # params = [problem_input_format, solution_output_format]
  apply_structure('function.connecting', params = [workflow_objects['problem_input_format'], workflow_objects['solution_output_format']])
  
  return workflow_objects

def apply_structure(structure, params):
  '''
  - params = [problem_input_format, solution_output_format]
  - position params in logic generated for applying this structure
  '''
  structure = find_structure(structure) # returns 'function.connecting' logic & metadata
  if structure.type == 'function':
    map_params_to_function(params)
    test, test_params = get_test(structure, params) # given structure & params, how do you test if structure application worked
    test = ["if test_params[0] == test_params[1]"]
    test_params = [workflow_objects['current_position'], workflow_objects['target_position']]
    apply_function(structure, params)
    passed = apply_test(test, test_params)
    if passed:
      # produces output of 'connecting' function, workflow_objects['functions']['workflow_intents']['connect']['output']['connecting_structures']
      return workflow_objects
  return False

def apply_test(test, test_params):
  # workflow_objects['current_position'] should now equal the solution output format, where the original equation has been converted into a value for x
  for line in test:
    output = execute(line)
    if output > 0:
      return False
  return True

def apply_workflow_logic(problem_statement, workflow_logic):
  # 'difference_logic' from workflow definition
  input_workflow_logic_to_apply = [insight_path]
  output_workflow_logic_to_apply = {
    1: 'break into sub-problems',
    2: 'identify interim formats, given sub-problems',
    3: 'identify sub-problem (and therefore interim format & sub-solution) structure (like a sequence)',
    4: 'solve sub-problems in structure (sequence)',
    5: 'merge the sub-solution (merge = "apply to previous state", since the structure is a sequence)',
    6: 'apply solution metric filter to sub-solution',
    7: 'if sub-solution fulfills solution metric, continue with next sub-problem'
  }
  return output_workflow_logic_to_apply

def find_subsolution(subproblem):

def apply_solution(apply_function, solution, problem):
  ''' function_name = merge_subsolution '''
    for function_name in filters:
      if function_name in globals():
        function = getattr(function_name, globals())
        function(solution, problem)

def merge_subsolution(subsolution, subproblem):

def apply_solution_metric_filters(filters, target_structure, current_structure):
  ''' function_name = check_merged_subsolution '''
    for function_name in filters:
      if function_name in globals():
        function = getattr(function_name, globals())
        function(structure)

def check_merged_subsolution(solution_target_position, current_position):
  ''' check progress compared to previous current position '''
  if solution_target_position == current_position:
    return True 

def get_formats(input_structure):
  formats = [structure for item in input_structure.split(' ') if hasattr(item, 'structure')]
  return formats

def identify_organizing_structure(function_name, subproblems, problem, solution):
  structure = None
  if function_name == 'connect':
    structure = 'sequence'
  return structure

def apply_function(function_name, params):
  '''
  - apply_function('connect', params=[problem_input_format, solution_output_format]):
  '''
  output_workflow_logic_to_apply = apply_workflow_logic(workflow_objects['problem_statement'], workflows['workflow1']['logic'][selected_format + '_logic'])
  for step_number in sorted(output_workflow_logic_to_apply.keys()):
    apply_function(output_workflow_logic_to_apply[step_number])
    # step 1: break into sub-problems (using workflow['logic']['difference_logic'] from workflow definition)
    subproblems = [
      'find differences causing problems', # ['difference between original & target position' = 'core problem structure'], 
      'find solutions resolving differences', 
      'combine solutions'
    ]
    # step 2: identify interim formats from subproblems
    interim_formats = []
    for subproblem in subproblems:
      sub_formats = get_formats(subproblem)
      interim_formats.append(sub_formats)
    interim_formats = [['differences'], ['solutions'], ['combined_solutions']]
    # step 3: identify sub-problem structure (sequence)
    organizing_subproblem_structure = identify_organizing_structure(function_name, subproblems, problem, solution)
    solution_output_format = params[1]
    for i, subproblem in enumerate(workflow_objects['connecting_structures']['sub-problems']):
      subsolution = workflow_objects['connecting_structures']['sub-solutions'][i]
      interim_format = workflow_objects['connecting_structures']['interim_formats'][i]
      # step 4: solve subproblem
      subsolution = find_subsolution(subproblem)
      # step 5: apply the subsolution, using a function to apply it like 'merge_subsolution'
      workflow_objects['current_position'] = apply_solution('merge_subsolution', subsolution, subproblem)
      # step 6: check if new current position had a difference between problem/solution resolved (if it made progress toward the goal), by applying solution metric filters
      progress = apply_solution_metric_filters(solution_output_format, workflow_objects['current_position']) # solution_output_format
      # step 7: continue solving sub-problems if solution metric made progresss
      if not progress:
        return False

  # workflow objects now contains output of connecting function for this solution automation workflow (break problem into subproblems, solve sub-problems, merge sub-solutions)
  workflow_objects['functions']['workflow_intents']['connect']['output']['connecting_structures'] = {
    'sub-problems': [
      'difference in problem input formats exercise type 1 & 2',
      'difference in problem input & solution output from exercise type unit (one minute of exercise type)',
      'difference in energy units of problem input & solution output'
    ],
    'sub-solutions': [ # steps to resolve sub-optimal differences, or sub-problems
      'convert problem input energy units at exercise type 1 to problem input energy units at exercise type 2',
      'convert problem input energy units at exercise type to energy units of an exercise type unit (one minute of an exercise type)',
      'convert problem input energy units at exercise type unit to solution output energy units of same exercise type unit'
    ],
    'interim_formats': [
      'original_equation_in_terms_of_b': 'standardized_problem_statement formatted with exercise type 1 standardized to exercise type 2 (requiring fewer conversions than the opposite)', # (apply 'b = 2a')
      'b_in_terms_of_a': 'standardized_problem_statement formatted with energy units per unit (minute) of exercise type 2 found', # (found value of a)
      'x_in_terms_of_b': 'standardized_problem_statement formatted with energy units per unit (minute) of exercise type 2 applied to problem input & solution output' # (apply value of a to find solution output x)
    ],
    'interim_variables': [
      'function connecting exercise type 1 unit (a) and exercise type 2 unit (b)',
      'function connecting energy units and exercise type 1 unit (a)',
      'function connecting x energy units of 6b and 5 energy units of 5b and 3a'
    ],
    'states': [] # states after each interim format is applied, progressing toward solution output
  }
  return workflow_objects

def apply_interface(interface_name, problem_statement):
  if interface_name == 'function':
    workflow_objects['variables'] = get_variables(problem_statement)
    workflow_objects['variables'] = ['energy units', 'speed', 'minutes']
    workflow_objects['functions'] = get_functions(problem_statement)
    workflow_objects['functions'] = ['find', 'use', 'assume']

  elif interface_name == 'structure':
    workflow_objects['variable_structures'] = {
      'variable_combinations': {
        'variable_standards': [
          'energy units per minute', 
          'energy units per minute at a speed', 
          'energy units per minute of an exercise type', 
          'minutes at a speed', 
          'minutes of an exercise type'
        ],
        'variable_connecting_functions': [
          '5 energy units = 5 minutes at speed 2 & 3 minutes at speed 1',
          'x energy units = 6 minutes at speed 2'
        ],
        'variable_functions': [
          'speed acts like a type variable (exercise at speed 2 uses energy at a different rate) except when converting between types, when it acts like a numerical spectrum variable'
        ],
      },
      'unknown_variables': ['energy units for 6 minutes at speed 2'],
      'adjacent_variables': [
        'unit': ['time unit (minute)', 'exercise unit', 'energy unit', 'exercise type unit']
        'type': ['exercise type', 'exercise type unit']
      ],
      'similar_variables': {
        'interchangeable_variables': {},
        'proxy_variables': {
          'exercise type unit': 'time unit (minute) of exercise at a speed'
        },
      },
      'common_variables': {
        'input_output': [
          'energy unit',
          'minutes',
          'speed',
          'exercise type', 
          'exercise type unit'
        ]
      },
      'required_variables': {
        'equalizing_intent': workflow_objects['variable_structures']['common_variables']
      },
      'variable_components': ['unit', 'time', 'rate']
    }
    # variable_connecting_functions could include a given default function of 'energy units at speed 2 = 2 * energy units at speed 1' if the problem statement includes that, and will include it later when we apply a connecting insight path
    workflow_objects['variable_structures']['common_variables'].extend(workflow_objects['variable_structures']['variable_combinations']['variable_standards'])
    
  elif interface_name == 'info.problem':
    workflow_objects['problem_input_format'] = 'energy units'
    # this problem type format is adjacent to the workflow we'll use, which breaks the statement into sub-problems
    workflow_objects['problem_types'] = {
      1: 'connect input/output values of same/related variables & format',
        2: 'identify & reduce differences (variables) causing problem',
          3: 'identify & reduce variables by standardizing',
            4: 'identify common useful standard in input & output formats & standardize to that standard',
            5: 'connect related variables to reduce variables by standardizing',
              6: 'connect related variables by identifying components in common & conversion functions to connect common components & other components'
      7: 'connect standardized input/output values of same variables & format'
    } 
    workflow_objects['solution_output_format'] = 'x number of energy units for 6 units of exercise type 2'
    workflow_objects['solution_metric_filters'] = {
      'formats': ['energy units'],
      'values': ['6 minutes', 'speed 2']
    }

  return workflow_objects

def find_relevant_workflow(problem_statement):

  ''' 
  - metadata for this workflow:
    - the interface metadata (intents, functions, insights) can be derived from the definition or pulled from the database of 'insight' functions
    - the logic can be generated by the definition & insights driving this workflow
  '''
  workflow1 = {
    'definition': 'break problem into sub-problems, find sub-solutions, merge sub-solutions to create solutions',
    'insights': [
      'problems are a sub-optimal state by some metric',
      'structures of sub-optimality require a change of some type to create optimal structures',
      'the change can be in many formats, like adding a function or reducing a difference, based on the original/adjacent/possible problem/solution formats & how those can be connected',
      'problems can be formatted as various structures, like imbalances such as 1, a lack of structure (missing info, lack of functionality, too much variation (variables that should be constants, differences that should be similarities)), or 2, too much structure (limits, barriers, definitions)',
      'core problem structures include limit, barrier, info gap, difference, distance'
      'solutions can be formatted as the opposite of the problem structure',
      'core solution structures include functions like empower, reduce, fill, similarize, connect'
      'problems can be formatted by applying any core problem structures',
      'when formatted using the difference core problem structure, differences between origin/target cause the problem',
      'if differences between origin/target cause the problem, the solution is a standard applied to input/output (creating a similarity), so the created similarity can be used to connect them'
    ],  
    'logic': {
      'difference_logic': [
        'find differences causing problems', # ['difference between original & target position' = 'core problem structure'], 
        'find solutions resolving differences', 
        'combine solutions'
      ],
      'function_logic': [
        'find functionality (or lack of) causing problems', # ['lack of conversion function', 'lack of standardization function', 'lack of equalizing function']
        'find functions that can build that functionality', ['replace', 'subset', 'multiply', 'check']
        'apply functions to build that functionality',
        'apply built functions to resolve problem'
      ],
      'definition_logic': [
        'find definitions causing problems', # ['definition of difference between problem & solution', 'definition of problem', 'definition of solution']
        'find alternate definitions that dont cause problems, or find definition metadata that doesnt cause problems & derive definition', # 'solution': 'difference in value & format compared to problem value & format'
        'apply found/derived alternate definitions that dont cause definition problems'
      ],
      'distance_logic': [
        'find positions causing problems', # ['source position', 'target position']
        'find functions to move from source to target',
        'find order of functions to move from source to target',
        'apply filters to function sequences between source & target'
      ],
      'info_gap_logic': [
        'find info gaps causing problems', # ['info gap of connection between a & b', 'info gap of how to apply structures like 'combine' to standardize variables', 'info gap of solution output energy unit number'] and other applications of build/derive/find/filter/identify/select functions
        'find order of info gaps to fill', 
        'find/generate/derive info to fill info gaps in correct order'
      ],
      'limit_logic': [
        'find limits causing problems', # ['limit of variables to capture info', 'limit of variables to be converted into each other', 'limit of variable structures to be equated']
        'find functions with power to invalidate limits', 
        'find order of limits to invalidate',
        'apply functions to invalidate limits in correct order'
      ],
      'barrier_logic': [
        'find barriers causing problems', #['specialization', 'differences']
        'find functions to resolve barriers', # ['abstract', 'tunnel', 'move', 'traverse']
        'select function to resolve barriers',
        'find types of functions to apply to barrier types for selected function', # ['abstract to compress', 'abstract to standardize']
        'apply functions to resolve barriers'
      ]
    },
    'components': ['problem', 'subproblem', 'subsolution', 'solution'],
    'intents': {
      'core_intents': ['break', 'find', 'merge', 'filter'],
      'workflow_intents': [
        "connect(workflow_objects['problem_input_format'], workflow_objects['solution_output_format'])"
      ]
    },
    'functions': {
      'core_intents': {
        'break': 'isolate(differences_causing_problem)', # isolate the differences between origin & target states causing the original problem
        'find': 'fit(problem_difference, solution_conversion)', # fit/match the problem's causative difference with a solution converting that difference into a non-problematic structure
        'merge': 'combine(subsolutions, solution)', # find a combination function that allows combination of subsolutions into the solution,
        'filter': 'filter(combined_subsolutions, solution_metric_filters, solution)', # adjust combinations of subsolutions until they match the solution output format, based on solution metric filters
      },
      'interim_intents': {
        'convert': workflow_objects['interface_functions'] # interim intents connect core & workflow intents
      },
      'workflow_intents': {
        'connect': {
          'connect': 'connect(problem, solution)', # apply structures to create a connecting function between input & output to fulfill the 'merge' intent of the solution automation workflow)'
          'output': None
        }
      }
    }
  }
  return workflow1

def standardize_problem_statement(problem_statement):
  '''
    # the following would be reduced by a typical language compression function, removing unnecessary words & converting rare to common words without losing info
    # reduced_problem_statement = 'find energy units for 6 minutes at speed 2, assuming 5 energy units for 5 minutes at speed 2 & 3 minutes at speed 1'
    - this function applies similarities & other optimizations useful for simplifying & standardizing the problem statement, like replacing rare terms with more common terms & removing unnecessary terms where possible
      - applies variable structures in order to standardize the problem statement
        - variable structures like important variables, isolated variable components, variables that can be combined, variables that are interchangeable, variables that are adjacent, as in n conversions away from other variables (like core/unit variables)
      - can identify/apply that: 
        - 'minutes at a speed' is not a useful standard bc speed relies on time & time is already embedded in the minute count, so it should isolate these inputs
        - speed 1 & 2 are values of the important variable to relate for 'standardization' intent
        - variables that are both proxy variables of input/output formats and variable in common for input/output
          - proxy variables of input/output format (energy usage) include exercise type units
          - variables in common for problem input (5 = 5b + 3a) & solution output (x = 6b) include exercise type units
        - can apply that 'exercise type unit' is the most useful way to format the 'minutes of an exercise type' or 'minutes at a speed' variable structures
          - bc the variables of minutes & exercise type don't add info useful for finding energy units at a different number of minutes & a related/equal exercise type/speed, 
            so its safe to compress/abstract them into one combined variable 'exercise type 1 unit' 
            (rather than a variable structure of a 'variable given/applied to another variable' like 'minute of exercise type 1', or 'minute at speed 1')
  '''
  for vstandard in workflow_objects['variable_structures']['variable_combinations']['variable_standards']:
    # convert the problem according to a variable standard to achieve some useful intent for connection/equalization, like simplification
    converted = convert_problem_statement(problem_statement, vstandard)
    # apply some filter to select most useful variable standard
    if workflow_objects['solution_output_format'] in converted and len(converted) < len(problem_statement):
      workflow_objects['standardized_problem_statement']

def apply_in_parallel(workflows):
  # apply_in_parallel executes workflows across threads if there are more than one
  for workflow in workflows:
    workflow_objects = apply_solution_automation_workflow(workflow)
    if workflow_objects:
      interface_objects['workflows'][workflow['definition']] = workflow_objects

def solve(problem_statement):
  # select & apply solution automation workflow
  workflows = interface_objects['workflows'] if 'workflows' in interface_objects['workflows'] or len(interface_objects['workflows']) == 0 else find_relevant_workflow(problem_statement)
  if workflows:
    apply_in_parallel(workflows)

interface_objects = {'workflows': {}}
problem_statement = 'find energy units used for 6 minutes at speed 2, assuming energy usage of 5 energy units for session of 5 minutes at speed 2 & 3 minutes at speed 1'
solve(problem_statement)

'''
  - apply other insight path structures (before/after/with/in general call to apply_structure('function.connecting')) to generate other workflows
    - derive insight paths used by applying insight paths that are also solution automation workflows & check that they can also solve the problem

  - alternate versions of interface query above (steps 1 - 4)
    
    - apply insight path 'change the problem to a more solvable problem' (which is also a solution automation workflow) to generate the insight path:
      - apply structure & change interface
        - standardize to variables that fulfill both categories first if possible:
          - identify proxy variables & equate those instead of original variables
          - identify variables that problem input & solution output formats have in common
    
    - apply insight path 'connect formats using structures of efficiency & interaction (such as standards, commonness, fit, adjacence, & similarity)' (which is also a solution automation workflow if applied to problem/solution formats) to generate the insight path:
      - apply structure & system interface 
        - identify interim formats by applying standardizing operations to input/output formats
          - standardize to common unit
          - find function to convert common unit to solution output format unit
          - apply conversion function to unsolved functions once standardized
'''