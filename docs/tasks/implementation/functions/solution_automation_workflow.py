'''
- solution analysis program workflow

    - workflow implementing problem-solving automation workflows (from problem validation/metadata extraction, to interface query design, to applying interface to problem, to generating/evaluating solutions)
    - translates a problem definition into a structure that allows for resolution of the structure into the corresponding solution format with a set of queries 
    - identifies solution spaces, solution sets achieving different solution metrics within the solution space, & may also identify optimal solutions for a particular problem, problem type, or problem network in a particular problem space. This enables the automation of finding solutions that optimize specific solution metrics defined in a problem statement in a discoverable system (where relevant system objects can be described, core system functions can be derived, solutions can be tested, & success can be measured with some metric & threshold or target value). This enables arriving at insights sooner, building products optimally sooner, inventing products sooner, and predicting patterns sooner, with less data & computational capacity. 
    - components:

        - inputs: 
            - required: 
                - the problem statement 
                - the interface definitions 
                - logic functions to traverse interfaces, visualize the impact of a solution on the problem/problem space, & test for adherence to a solution metric, check input for validity 
                - solution automation module repository, containing: 
                    - an index of info objects (a data store containing info objcts like definitions, formats, concepts, insights, problems, solutions, functions, strategies, patterns, etc)
                    - program configuration (data sources, query & usage statistics, optimization configuration, prior queries & related objects) 
                    - tables to store 
                        - found associations & objects in queries
                        - data sources & solution sources
                        - standard objects & their metadata (such as definition routes & conceptual queries) following the schema specified in my repository: https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/objects/schema.md  
            - optional: 
                - the problem space context, without which the program will make API calls to fetch data & definitions (including data like alternate definition sources, object behavior rules, latest version of an open-source solution 
        
        - process: 
            - database storing example objects (example insights, problems, solutions, questions, patterns, functions, causes, concepts, types, systems, etc), as well as previous queries if configured to do so 
            - solution automation program flow, conditionally making calls to the machine learning system and the API finding/calling system if predictions, data, or definitions are needed 
                - solution automation program flow (converting input problem statement to output solution space)
                  1. obtaining a problem statement
                  2. identifying the problem & problem space metadata
                  3. identifying the optimal origin interface to start traversing from & interface traversal sequence
                  4. traversing the interface network, with interfaces acting as filters, starting at the origin interface 
                  6. iterate traversal process to reducing the problem space to a solution space
                  7. matching a problem and a solution with various interface traversals, potentially determined by the selected origin of the traversal, problem & solution definitions & associated space definitions
                  8. determining the success of a particular solution
                  9. returning the identified optimal solution as a set of steps to compress the problem as well as solution metrics, attributes, & actions, and/or insights/patterns/system/ standardized description related to the problem if no solutions are found 

        - outputs:
            - a particular solution implementation of a strategy 
            - a solution set of solutions that were not reducible given input filters 
            - a solution space identifying that a solution is possible in the problem space 
            - a set of information objects about the problem, problem network, or problem space that clarify the problem to some degree, such as causes deemed not likely or additional problem metadata derived or a problem- invalidating event identified 
            - query, program, problem, and solution metadata
'''