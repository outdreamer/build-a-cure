    - logic automation problem structures

      - connecting solutions & perspectives (interfaces with a goal like a priority or metric, which makes them by definition relevant to solutions)
        - by prioritizing different components (structures/attributes/interfaces), perspectives solve problem(s) in different ways, with different variables (problem origin points, solution metrics), and may solve different problem(s)
        - applying or integrating multiple perspectives can cover more problems solved or reduce the problems to solve, or it can create more problems depending on error types, like unnecessary abstraction or complexity added (in regard to complexity handled)
        - some perspectives are more useful than others for various intents
        - some perspectives need to be applied in structures (like sequences/combinations) with other perspectives
        - some perspectives will cause error types for an intent

        - examples:
          - if you think based purely on avoiding errors, you may miss optimal solutions
          - if you think based purely about functions & their interactions, you may miss how they fit into the system or how they apply to data
          - if you think based purely in sequential time, you may miss ways to parallelize operations
        
      - problem perspectives with associated solution priorities/metrics

        - interface component perspectives

          - 'time' perspective identifying time-based interactions of components
            - the lifecycle timing of a solution/problem
            - the sequential timing of steps of a process, like validations or functions to execute in a sequence
            - timing variables like steps that should be executable external to a process or out of order in a certain context
            - state sequence that should be fulfilled by a process
            - imminent tasks to automate after this solution is complete

          - 'object' perspective identifying object changes/structures needed

          - 'data' perspective, identifying data flow, from origin state, to various alternative or sequential interim states, to target state
            - the 'data flow' perspective aligns with testing of specific examples for entire processes creating the data flows & enables identifying/preventing data flow structures like differences or interactions that shouldnt be allowed
            - as opposed to the 'function' perspective, the 'data flow' perspective focuses on inputs/outputs of logic, measured at various points in the process

          - 'system' perspective, identifying system objects like duplicates, alternatives, efficiencies, ambiguities in data/logic
            - the system perspective offers a useful contrast with the data, variable, & function perspectives
              - system: context where interactions of data, variables, functions, & processes are integrated in a way that is useful to agents
              - data: examples
              - data flow: sequential input-output examples
              - variable: input structure (combination) options, change options
              - function: input/output connection options
              - function call stack: structures (container, combination, sequence) of input-output connections
              - process: interaction objects in a system with agents

          - 'state' perspective identifying state changes/structures needed

          - 'variable' perspective identifying which variables are required for solving automation task problem before changing existing system

          - 'function' perspective identifying which functions to write before implementing solution

          - 'test' perspective identifying which tests the solution needs to fulfill (enables finding solutions by iterating changes & checking changes to see if they fulfill test)

          - 'error' perspective that enables applying an 'not error' filter to solutions to avoid known/predictable error structures (like error types)

          - 'cause' perspective identifying causal network of system components and which causes need to be changed to complete automation task
            - cause of logic selection in existing solution may be the sequence & existence of queries, whether the logic functions are available, & whether the logic variables are populated, whereas the target cause of logic selection should be which logic exists in a data store & the sequence of queries to that data store

          - 'logic' attribute-connecting perspective (attributes like type-position) 

            - sub-queries about type attributes to solve problem of 'finding correct position of components to fulfill organization intent'
              - are certain types of logic better in different positions (validation in json dict, dependency changes in database triggers, parsing/testing in another position)
              - what other types apply to logic (configuration, filters, data, examples)
            
            - examples of logic attribute (type-position) connection functions
              - if a logic type is configuration, that should be in positions associated with configuration
              - if a logic type is changed more than other logic types, that may qualify as data
              - if a logic type is an example, that suggests a testing position

        - attribute-specific perspectives

          - 'optimization' perspective: identifying the most useful functions to write that optimize a metric (like 'flexibility') to the existing system (to support other intents), while fulfilling relevant problem-solving intents of the automation task problem

          - 'organized' perspective that integrates solution with existing system of solutions & finds/handles error types
            - apply interfaces to task & integrate interface objects into solution
              1. find variables of task ('inject logic for specific cases') first
              2. identify variable interactions & important error types to avoid with those variables
              3. design solution fulfilling foreseeable error types
              - variables of 'logic injection' function (solution to automation task of 'injecting logic in specific cases'): 
                - whether specific inputs have specific associated logic
                - whether logic variables are available/populated in input
                - whether logic functions in associated logic are available in execution context
                - whether logic inputs are validated
                - whether other specific cases are supported by 'logic injection' function
                - whether specific cases of multiple injected logic compoennts coordinate or contradict each other
                - whether outputs of injected logic components suboptimally change inputs of other injected logic components
                - whether injected logic components have a correct sequence and whether it aligns with injection sequence

          - 'efficient' or 'default' perspective with low learning curve (adjust existing logic & write tests, dont change anything that isnt necessary like rearranging components)
            - apply most granular change & add changes/logic as necessary to support future intents
              - apply most adjacent solution (add specific conditions to actual logic)

          - 'consolidated' perspective with low maintainence requirements
            - move logic to position with best available testing, validation, processing functions

          - 'reusability' perspective enabling future usage
            - keep logic in position enabling future usage intents

          - integrated 'consolidated' and 'reusability' perspectives
            - keep logic in position enabling future usage intents, but add function to convert to position with best functions to support those intents (testing, validation, processing functions)
        
        - structure perspectives

          - 'limit' perspective
            - identify limit of implementations & identify whether usage will converge to limit
              - implementation limits: 
                - will adding granular specific cases directly to existing solution ever hit a point where its sub-optimal
              - limit convergence:
                - are we near that point or will we be in the lifecycle of this solution

          - 'filter' perspective
            - identify which filters exist & how to change them to implement solution
              - existing filters: conditions, dependencies, constants, validations

          - 'interaction' perspective
            - identify how system components interact & how to change interactions to implement solution

      - apply solutions to various related & sub-problems to task automation problem

        1. problem of 'dependency' between logic components
          - apply 'dependency' definition
            - separate dependent variable logic & apply after initial logic once inputs are populated as constant independent inputs
        
        2. problem of 'dependency' between problem/solution components (solution steps)
          - solving problem 3 must occur before solving problem 4
        
        3. problem of 'selecting which implementation to use for primary automation task'
          - select between strategies
            - inject variable to store logic & apply if populated (store logic in database table)
            - embed logic in other logic (store logic in query logic)
        
        4. problem of 'selecting format to use once an implementation is selected'
          - select between logic formats
            - delimited format
            - actual logic format
            - logic standardized to executing language format (python)
            - logic standardized to common format (json dict) to be used as config vs. data in a data store

        5. problem of 'finding correct interaction level to apply solution at based on interaction interface'
          - interaction level: process, query, task, script, variable, function
          - interaction interface: usage interface, logic interface, input/output interface, state interface
        
        6. problem of 'finding intents supported by implementation options'
          - storing in database supports intent of 'fast initial querying & re-querying, & subsequent querying'
          - storing in python support intents of 'maintainability, modifications to add new logic, consolidate to process/step interface'
        
        7. problem of 'finding related & aligning intents of 'enable injecting logic in query logic' automation task'
          - testing logic correctness: 
            - determining difference in inputs/outputs, as aligning with differences applied in logic (input/output difference created by logic & input/output data difference)
          - testing updated logic:
            - determining difference in original/updated outputs (original data & updated data with new function to inject logic for cases)
          - a difference-determining function would be useful for both of the above intents

        8. problem of 'finding correct structures to approach problem'
          - 'organize problem components' intent
            - position (as an input to the 'organize problem components' intent)
              - find correct position of components
                - logic, input/output/interim/duplicate/index data, validation/generative functions
          - 'reduce solution space' intent
            - filters
              - apply organization intent with regard to solution filters (as an input to 'reduce solution space' intent)
                - tasks, processes, process variables, process steps, required inputs/outputs, and cost of implementing re-arrangements

        9. problem of 'finding functions to solve these problems & selecting the functions that solve the most problems to write the least code'
          - functions that solve the most problems out of problems 1 - 8 & fulfill the most perspectives (fulfill the most perspective-associated solution metrics)
            - function to determine (data/logic) difference
            - function to find required/similar logic/data
            - function to convert logic to a format
            - function to sort (logic/data) in sequence
            - function to apply logic based on variable (execute specific logic for an input, or a specific input to execute a process step logic)
          