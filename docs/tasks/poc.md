'''
- example of finding/deriving insight paths for a basic calculation
'''

problem_statement = 'find energy units used for 6 minutes at speed 2, assuming energy usage of 5 energy units (per session of 5 minutes at speed 2 & 3 minutes at speed 1)'

def get_problem_metadata(problem_statement):
  '''
    1. apply function interface
      - get variables
      - get variable structures
    2. apply information (problem/solution interface)
    3. apply standardization

  '''
  interface_objects = {}

  # I. apply function interface
  interface_objects = apply_interfaces(['function'], problem_statement, interface_objects)
  interface_objects['variables'] = get_variables(problem_statement, interface_objects)
  interface_objects['functions'] = get_functions(problem_statement, interface_objects)
  interface_objects['variables'] = ['energy units', 'speed', 'minutes']
  interface_objects['functions'] = ['find', 'use', 'assume']
  
  # II. apply structure interface
  interface_objects = apply_interfaces(['structure'], problem=problem_statement, interface_objects)
  interface_objects['variable_structures'] = {
    'variable_combinations': {
      'variable_standards': ['energy units per minute', 'energy units per minute at a speed', 'energy units per minute of an exercise type', 'minutes at a speed', 'minutes of an exercise type']
    },
    'variable_functions': [
      'speed acts like a type variable (exercise at speed 2 uses energy at a different rate) except when converting between types, when it acts like a numerical spectrum variable'
    ],
    'adjacent_variables': [
      'unit': ['time unit (minute)', 'exercise unit', 'energy unit', 'exercise type unit']
      'type': ['exercise type', 'exercise type unit']
    ],
    'proxy_variables': [
      'exercise type unit'
    ],
    'common_variables': [
      'energy unit',
      'minutes',
      'speed',
      'exercise type', 
      'exercise type unit'
    ],
    'variable_connecting_functions': [
      '5 energy units = 5 minutes at speed 2 & 3 minutes at speed 1',
      'x energy units = 6 minutes at speed 2'
    ]
  }
  # variable_connecting_functions can include a given default function of 'energy units used at speed 2 = 2 * energy units used at speed 1'
  interface_objects['variable_structures']['common_variables'].extend(interface_objects['variable_structures']['variable_combinations']['variable_standards'])
  
  # III. apply info.problem interface
  interface_objects = apply_interfaces(['problem'], problem=problem_statement, interface_objects)
  interface_objects['problem_input_format'] = 'energy units used'
  interface_objects['problem_types'] = {
    1: 'connect different input/output values of same or related variables and same format',
    2: 'standardize to as few variables as possible',
    3: 'identify common standards to input & output formats',
    4: 'identify connecting function between related variables to standardize to as few variables as possible',
    5: 'connect standardized different input/output values of same variables and same format'
  }
  interface_objects['solution'] = 'energy units used for 6 minutes at speed 2'
  interface_objects['solution_output_format'] = 'energy units used for 6 minutes at speed 2'
  interface_objects['standardized_problem_statement'] = standardize_problem_statement(problem_statement, interface_objects)

  '''
  def standardize_problem_statement(problem_statement, interface_objects):
    - identifies that 'minutes at a speed' is not a useful standard bc speed relies on time & time is already embedded in the minute count, so it should isolate these inputs
    - identifies that speed 1 & 2 are values of the important variable to relate for 'standardization' intent
    - identify proxy variables of input/output format (energy usage): exercise type units
    - identify variables in common for problem input (5 = 5b + 3a) & solution output (x = 6b): exercise type units
    - identify variables that are both proxy variables of input/output formats and variable in common for input/output
    - identifies that 'exercise type unit' is the most useful way to format the 'minutes of an exercise type' or 'minutes at a speed' variable structures
      - bc the variables of minutes & exercise type don't add information that is useful for finding energy units at a different number of minutes & a related/equal exercise type/speed, so its safe to compress/abstract them into one combined variable 'exercise type 1 unit' (rather than a variable structure of a 'variable given/applied to another variable' like 'minute of exercise type 1', or 'minute at speed 1')

  for vstandard in interface_objects['variable_structures']['variable_combinations']['variable_standards']:
    # convert the problem according to a variable standard to achieve some useful intent for connection/equalization, like simplification
    converted = convert_problem_statement(problem_statement, vstandard)
    # apply some filter to select most useful variable standard
    if interface_objects['solution_output_format'] in converted and len(converted) < len(problem_statement):
      interface_objects['standardized_problem_statement']
  '''

  interface_objects['standardized_problem_statement'] = 'find energy units used for 6 minutes at exercise type 2, assuming energy usage of 5 energy units for 5 minutes at exercise type 2 & 3 minutes at exercise type 1'

  # IV. apply 'connecting function' structure
  '''
  to connect solution output energy units and problem input energy units, 
    - a function connecting exercise type 1 & 2 needs to be built
    - then a function connecting the new value of problem input energy units & the original value of solution output units needs to be built
  '''
  interface_objects['connecting_structures'] = identify_structures_between_positions(problem_input_format, solution_output_format, interface_objects)
  interface_objects['connecting_structures'] = {
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
      'standardized_problem_statement formatted with exercise type 1 standardized to exercise type 2 (requiring fewer conversions than the opposite)', (apply 'b = 2a')
      'standardized_problem_statement formatted with energy units per unit (minute) of exercise type 2 found', (found value of a)
      'standardized_problem_statement formatted with energy units per unit (minute) of exercise type 2 applied to problem input & solution output' (apply value of a to find solution output x)
    ],
    'interim_variables': [
      'function connecting exercise type 1 unit (a) and exercise type 2 unit (b)',
      'function connecting energy units and exercise type 1 unit (a)',
      'function connecting x energy units of 6b and 5 energy units of 5b and 3a'
    ],
  }
  
  # V. apply interim formats to connect problem input & solution output
  interface_objects['current_position'] = problem_statement
  for i, subproblem in enumerate(interface_objects['connecting_structures']['sub-problems']):
    subsolution = interface_objects['connecting_structures']['sub-solutions'][i]
    interim_format = interface_objects['connecting_structures']['interim_formats'][i]
    interface_objects['current_position'] = apply_solution(subsolution, subproblem)
    # check if new current position made progress toward goal
    progress = check_progress(interim_format, interface_objects)
    if not progress:
      break
  # interface_objects['current_position'] should now be the solution output format, where the original equation has been converted into a value for x

'''
      - identify interim formats connecting problem & solution formats (interface query)
        
          - identify steps to connect input variable value & output variable value
            - identify steps to connect input exercise type units & output exercise type units
              - standardize exercise types to one exercise type
              - I. identify input/output format value (energy usage) associated with proxy variable (standardized exercise type unit, a)
              - II. convert standardized input exercise type format value (a = 5/13 energy units) to the output exercise type format value (b = 5/13 energy units)
              - III. apply output exercise type format value to unsolved solution output variable x (x = 6 * 10/13 energy units)

      - apply methods to connect problem input & solution output:

        - apply standardization & connecting (equalizing) methods to solve for interim formats connecting problem & solution formats:

          I. energy units for 1 unit of exercise type 1 (the value of a)
          II. energy units for 1 unit of exercise type 2 (the value of b)
          III. x energy units of 6 units of exercise type 2

          - standardization to equate problem input & solution output requires either:
            - A. converting minutes at speed 1 to minutes at speed 2 or vice versa
            - B. converting energy units used to a minute/speed unit or vice versa

          - identify connecting functions of:

            - 1. standardization method A
              - find connecting function of speed 2 b & speed 1 a energy unit usage
                  - connecting function:
                    - energy usage of speed 2 b = x * energy usage of speed 1 a
                    - b = xa
                - if none found, use default numerical connecting function
                  - connecting function:
                    - energy usage of speed 2 b = 2 * energy usage of speed 1 a
                    - b = 2a
              
            - 2. problem input & solution output

              - find function connecting problem input & solution output in original equation set

                - I. find value of a
                  - query: reduce original equation to variable a by applying a standardization method connecting function of b & a
                    - apply standardization connecting function of method A: energy usage of speed 2 & speed 1 (b = 2a)
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

                - II. find value of b
                  - query: convert value for that variable to value for solution output format (b)
                    - find energy units for unit of exercise type 2
                      - apply standardization connecting function of method A: energy usage of speed 2 & speed 1 (b = 2a) 
                      - how many energy units does a unit of each exercise type use?
                        - one unit of exercise type 1 (speed 1) uses 5/13 energy units
                        - two units of exercise type 1 (speed 1) uses 10/13 energy units
                        - one unit of exercise type 2 (speed 2) uses 10/13 energy units
                        - b = 10/13 energy units
                
                - III. find value of x
                  - query: apply energy units/per unit of an exercise type to find energy units for 6 minutes of type b exercise
                    - x energy units used = 6 minutes * speed 2
                    - x = 6 units of exercise type 2 (speed 2) = 6 * 10/13 = 60/13 energy units

    - deriving insight paths used by applying insight paths that are also solution automation workflows

      - apply insight path 'change the problem to a more solvable problem' (which is also a solution automation workflow) to generate the insight path:
        - standardize to variables that fulfill both categories first if possible:
          - identify proxy variables & equate those instead of original variables
          - identify variables that problem input & solution output formats have in common

      - apply insight path 'connect formats using structures of efficiency & interaction (such as standards, commonness, fit, adjacence, & similarity)' (which is also a solution automation workflow if applied to problem/solution formats) to generate the insight path:
        - identify interim formats by applying standardizing operations to input/output formats
          - standardize to common unit
          - find function to convert common unit to solution output format unit
          - apply conversion function to unsolved functions once standardized
'''