# to do

  - de-duplicate logic
    - integrate problem_solving_matching.md & analysis_examples.md
    - integrate changes from interface_analysis.py and solution_automation_analysis.py to repo
    - integrate system_analysis code & defs, including example.py & workflow logic
    - integrate rules from diagrams to relevant documents
        [0010] Example embodiments will be described and explained with additional specificity and detail through the use of the accompanying drawings. 
        [0011] FIG. 1. 'User Interface Module' illustrates a diagram of a user interface that can accept user input about a problem & program configuration. 
        [0012] Fig. 2. Interface Analysis Module 140 is a diagram of example components (such as functions & constants) of a program to automatically apply information formats to achieve an input intent. 
        [0013] Fig. 3. Machine learning system 120 is a diagram of an example wrapper component that would call a machine learning system to predict a variable. 
        [0014] Fig. 4. API finding/calling system 130 is a diagram of an example wrapper component that would call an API finding/calling system to retrieve data. 
        [0015] FIG. 5. 'Structure Application Function - Apply Function' illustrates applying a structure to another structure. 
        [0016] FIG. 6. 'Problem space visualization' illustrates an example visualization of a problem space. 
        [0017] FIG. 7. 'Network of related problems' illustrates an example of a network of related problems. 
        [0018] FIG. 8. 'Problem Types' illustrates a set of common problem types formatted as information or structural problems. 
        [0019] FIG. 9. 'Problem formats, with matching solution formats of problem formats' illustrates an example of various problem formats & solution formats that match them. 
        [0020] FIG. 10. 'Problem-solution structure-matching: apply a solution function to a structure containing the problem to find specific solution structures for that problem' illustrates an example of matching a problem with a solution. 
        [0021] FIG. 11. 'Finding alternate solution formats that fulfill different metrics' illustrates an example of selecting a solution format that fulfills a solution metric. 
        [0022] FIG. 12. 'Network of problem sub-problems, breaking a problem into components problems' illustrates an example of breaking a problem into a set of sub-problems, which once solved, can be aggregated with a solution-aggregation method as shown. 
        [0023] FIG. 13. 'Causal structure-matching' illustrates a method of matching causal structures to a variable set. 
        [0024] FIG. 14. 'Design Interface Query' illustrates a method of assembling input information into structural meaning relevant to the input intent, using a structure containing information formats. 
        [0025] FIG. 15. 'Concept definition network' illustrates a network of related concepts. 
        [0026] FIG. 16. 'Alternate definition routes' illustrates a set of definition routes for a concept. 
        [0027] FIG. 17. 'Match structure for a definition of a concept' illustrates matching a structure to a concept. 
        [0028] FIG. 18. 'Intent-matching' illustrates matching intent to structure & vice versa. 
        [0029] FIG. 19. 'Insight path application' illustrates insight path examples and an example of applying an insight path. 
        [0030] FIG. 20. 'Interface conversion & matching' illustrates an example of selecting an interface to traverse. 
        [0031] FIG. 21. 'Interface & traversal diagram' illustrates an example of a diagram indicating an example interface, & a diagram indicating which interfaces to traverse in what sequence (forming an interface query). 
        [0032] Fig. 22 is a diagram of a process that describes the general workflow for implementing interface analysis. 
        [0033] Fig. 23 is a diagram of an example usage of the system. 
        [0034] Fig. 24 is a diagram of an example environment in which systems and/or methods, described herein, may be implemented, including interface analysis module 220 in FIG. 22. 
        [0035] Fig. 25 is a diagram of example components of one or more devices of FIG. 22. 
        [0006] Figs. 1A - 1J contain diagrams of an overview of an example implementation 100 described herein. 
        [0007] Fig. 1A User Interaction Module 110 is a diagram of an example user interface implementation to gather input about a problem & program configuration for Solution Automation Module 140.
        [0008] Fig. 1B Solution Automation Module 140 is a diagram of example components (such as functions & constants) of a program to automatically find/derive/generate a solution for a problem, to implement the general execution workflow of Fig. 4. 
        [0009] Fig. 1C Machine learning system 120 is a diagram of an example wrapper component that would call a machine learning system to predict a variable. 
        [0010] Fig. 1D API finding/calling system 130 is a diagram of an example wrapper component that would call an API finding/calling system to retrieve data. 
        [0011] Fig. 1E Solution Output 150 is a diagram of an example output of the process in Fig. 4 that could be displayed & edited in the User Interaction Module 110. 
        [0012] Figs. 1F - 1I contain diagrams of an example problem-solving automation workflow (such as problem space structurization (formatted as filters/limits/functions/networks/vectors)) detailing a particular interface traversal format sequence that can be used to solve most problems. 
        [0013] Fig. 1F Finding matches between problem & interface components is a diagram of an example implementation of step 404 - 406 of the process of Fig. 4 (converting a problem to an interface, mapping between components of the problem & interface). 
        [0014] Fig. 1G Applying matching interface components to relevant problem system components is a diagram of an example implementation of step 407 of the process of Fig. 4 (applying matching mapped objects from the interface to the problem system). 
        [0015] Fig. 1H Applying solution metric structures to solution structures is a diagram of an example implementation of step 408 of the process of Fig. 4 (applying solution metric structures to solution structures). 
        [0016] Fig. 1I Example Object Definition Structures is a diagram of example structures forming the definition routes of an example system object on the structural interface. An example of a definition route is documented here: https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/find_existing_solutions/system_analysis/maps/definition_routes.json 
        [0017] Fig. 1J is a diagram of an example usage of the system. 
        [0018] Fig. 2 is a diagram of an example environment in which systems and/or methods, described herein, may be implemented, including solution automation module 220 in FIG. 2 which refers to solution automation module 140 in FIG. 1. 
        [0019] Fig. 3 is a diagram of example components of one or more devices of FIG. 2. 
        [0020] Fig. 4 General Execution Workflow is an overview of an example process 400 for implementing problem-solving automation workflows in steps 402 - 410, from initial problem formatting to solution matching to solution application & analysis. 
          
  - organize interface analysis logic definitions
  - add functions from workflows & analysis (to do list, questions answered, problems solved, interface definition & functions) as files in functions/ folder
    - resolve duplicate functions
    - organize into primary core functions & list sample parameters (like objects to identify for the identify function)
  - function to translate interface query logic into interface language (combination of core functions (find/build) & other core components)
  
  - function to generate/identify errors in a solution (function set) within a problem space/system context
    - identify error cause types using combinatorial core analysis
      - find components
        - structural mis/matches
          - malicious function sequences matching validation requirements
        - unnecessary structures
        - missing structures
      - apply components
        - apply combinations
          - combine components in various structures
            - inject componeents into other components
        - apply changes
          - remove/add limits/rules/assumptions
          - use alternate paths
          - switch expected with unexpected components
      - build components
        - function sequences granting access
    - filter error cause type by which generated errors would cause information problem types
      - process failure
      - access vulnerability
      - corrupt data
    - identify specific error types of filtered error cause types, organized by interface
      - intent mismatch between function combinations across layers
      - incorrect permissions for context
      - breaking input/output sequence for later functions
      - lack of rule enforcement
    - match specific interface (intent, structural) error types with associated solution types
      - align intent
      - scope permissions, generate permissions for a context/intent & check for a match before executing
      - check that all valid/supported function sequences are maintained
      - check that all rules & rule structures (like sets or sequences) determining resource access are enforced, or rule gaps where error/attack types could develop are closed
    - reduce by solution types that cover the most error types without contradicting other solution types or creating additional unsolved problem types
      - intent-matching covers multiple structural error types
      - system-fitting or structure-matching as a superset of intent-matching
    
    - invariant vs. symmetry
    - energy stored in information/structures has stability physics, where information in a certain structure can support other information of different structures, including structures allowing variation in change/potential

## examples

  - example of permuting assumption: "reports of power consumption have to be exact measurements" (platypus)
    - a temperature monitor sensitive to a hundredth of a degree might provide similar but non-specific power reporting for important/extreme usage patterns without revealing such specific information as that which could infer exact operations being done, bc the interval of temperature measurements allows for greater variation in calculations that could explain it

  - example of applying problem-structure interface: https://en.wikipedia.org/wiki/Anti-pattern
    - these are examples of contradiction/error types of the system-optimizing insight 'align relevant intents', which have the structural problem type 'misalignment' of the concept 'relevance':
      - local & global intents (local efficiency/fulfillment of local incentives/priorities, at the expense of global inefficiency/lack of fulfillment of global priorities/requirements/incentives, by allocating local solution side effects to global entities)
      - misaligning prioritization & intent (over-prioritize job duties like monitoring, to benefit the manager) that doesnt align with other intents (subordinate productivity) which benefit the company
      - imbalance/missing/disconnection from related objects (criticism & solution, solution & responsibility)
      - mis-aligning functionality (learning/potential) with requirement (repeating task)
      - mis-aligning intent of a product (making customer independent) with dependency structures (requires customer to use it beyond its value to them)

  - finish dilemma example formats
  - query examples for use cases like:
    - lack of information stored (match problem of type 'information lack' with interface query 'check pattern interface for similar patterns')
    - query problem breakdown & integration diagram
    - calculating various different problem breakdown strategies first before executing normal query-building logic for each
  - give interface math examples, like standardization of all distinct components into their own interfaces, rather than within a system context
      - rather than framing the behavior of objects in a system, you can:
        - remove the assumption of the system limits forcing interactions
        - frame each object on its own interface (containing all its possible forms, variables, attributes, generators, cooperative contexts, etc)
        - compute the interactions of those interfaces
  - give example of generating problem types by applying structure
    - for instance, a common problem type is a mismatch/imbalance
      - by applying the 'mismatch' to the cost/benefit relationship, you get an 'inefficiency' problem type, which can be defined as a mismatch/imbalance between the cost & benefit, favoring the cost side (the negative object out of (cost, benefit), associated with problems)
  - add examples of system/object/rule/type change patterns
  - include example workflows with example problems
    - include example of how to generate other workflows (different starting/ending points & trajectories)
  
  - interface analysis example with government components: 
    - democracy with an individual leader or group of elites/advisers/influencers which are treated as representatives of different population subsets is inherently contradictory - an alternative is in moving the leader to the same level as their adjacent advisers & other influencers, and giving them executive or majority/weighted/veto power over some decisions like whether to go to war, and the structure of the top advisers & the president would change according to needs
      - do they need a consensus? then make sure the network of advisers has an odd number
      - do they need an accurate resolution rather than an efficient one? then allow an even number & have regular re-calculations of votes until the issue is resolved
    - the application of different analysis methods in calculating the different probable & relevant perspectives on an issue & the optimal structure of the issue should be integrated as AI voters into human decision systems, as an independent third party that is biased in its incentives embedded in its learning algorithm (which can be selected for relevant issues, like a bias toward priorities like accuracy or efficiency depending on what type of decision is required) but not biased by financial incentives
    - a network or other structure of biases that is updated constantly is one way to counteract over-prioritization leading to a particular bias


## diagram
  
    - add diagram for intent-matching
    - add structures to diagram: interface overflow (to sub-interfaces), interface foundation

    - diagram for workflow 1: 
      - function to determine relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'
    - add conceptual math interface query diagram
      - use lattice multiplication as standard example, other than core operations (add/multiply mapped to language, concepts like irreversibility/asymmetry mapped to math)
    - interface conversion, matching, starting point selection (applying structure, checking if relevant information is found)
    - diagram to document sub-functions of core functions with distortions
    - make diagram for dimension links higher than 3d that are depictable in the same network space
      - should show variables that impact other variables, the change rates of these relationships
      - overall impact should be calculatable from these relationships
      - should show similar movements for correlated variables
      - should show skippable/derivable variables (variables that can be resolved later than they normally are)
      - should show meta forces for overall trends in change rules (direction of combined variable forces)
      - should show limits of measurability & threshold metrics
    - structurize (apply structure to) definitions of objects specific to interfaces
      - example: info asymmetry is associated with an info loss in a particular direction between info types/formats, rather than just an info imbalance or mismatch
      - diagrams for specific concepts, core functions, concept operations (combine, collide, connect, merge, apply), ethical shapes
        - variable accretion patterns (how an object becomes influenced by a new variable, complex system interaction patterns, etc)
        - make diagram of potential matrix to display the concept
          - map parameter sets to potential matrix shapes 
        - finish diagrams for cause (shapes & ambiguity), concept (evolution of concepts, networks, distortion functions)
        - diagram for argument
      - make a system layer diagram for each interface to allow specification of core interfaces & other interface layers (interface interface)
        - make a system layer diagram for structures to include layers of structures 
          (beyond core structures like curves, to include n-degree structures like a wave, as well as semantic output structures like a key, crossing the layer that generates info structures like an insight, a probability, etc)

# content/config

    - import insight history data to identify insight paths (info insight paths like 'lie => joke => distortion => insight', system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub')
    - define default & core objects necessary for system to function (out of the box, rather than minimal config necessary to derive other system components & assemble)
      - add default functions to solve common problem types
      - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially determined in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.
    - document time structures (concave time explaining compounding similarities up to a point of maximum concavity, a structure that can separate from the other space-times)
    - systematize your definitions of info objects, to include analysis that produces relationships of core objects like opposites to their relevant forms (anti-symmetry) in addition to permuted object states (asymmetry), such as an anti-strategy, anti-information, anti-pattern
      - organize certainty (info) vs. uncertainty objects (potential, risk, probability)
      - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers
      - add technicality, synchronization, bias, counterintuition, & certainty objects leading to inevitable collisions
        - the collision of compounding forces producing a phase shift
        - lack of attention in one driver and false panic in a second driver leading to a car crash given the bases where their processes originate
      - define alignment on interfaces (compounding, coordinating, parallel, similar, etc)
      - start with these info object transforms that filter the most info: opposite, invalidating, symmetric, core, aligning, boundary-breaking, phase shift activating, structure stabilizing, constant changing, converging
      - add core info objects (core strategies, core assumptions) so you can make a network of graphs for a system
    - concept analysis:
      - how new concepts (gaps in network rules) evolve once structure is applied to prior concepts 
    - interface analysis:
      - limitations of interfaces & how to derive them
      - how rules develop on stability & how foundations are connected & destroyed
      - explainability as a space limited by derivable attributes from data set & cross-system similarity
      - vertex definition & give examples (as an intersection/combination of interface variables, such as determining/description(compressing)/generative/causative/derivation variables), around which change develops
    - change analysis:
      - generated object change types
        - constant to variable
        - variable to removal of assumption in variable type/data type
    
    - research implementing your solution type (constructing structures (made of boundary/filter/resource sets) to produce substances like antibodies, using bio system stressors)
    
    - merge definitions into docs/tasks/implementation/constants/definitions.json

    - clarify/resolve terms that can be conflated: 
      - shape/structure
      - rule/test/metric/limit/threshold/boundary/state change/phase shift
      - intent/priority/motivation/incentive
      - method/function/rule/pattern (pattern is a sequence of specific objects)
      - path/route/trajectory/traversal/order/list/sequence
      - object/entity/item/component
      - type/class/category/group/subset
      - closed/isolated/independence/unique/orthogonal
      - model/perspective/filter
      - standard/interface/index/symmetry
      - dimension/variable/axis
      - space/system/context
      - perspective/filter/standard/index & relationship to variables/operations on the interface
      - filter vs. rule is a similar question to attribute vs. rule - sometimes one format is better based on the info you have, sometimes its worth it to transform the format
    
       - info conceptual relationships:
          priority = direction
          observation = insight = function = result = relationship
          conclusion = ordered_list(observations) + guess = coefficients + bias
          strategy = ordered_list(insights)
          strategy = insight + context
          problem = (combination of intents having different priorities) or (an resource distribution imbalance)
          intent = strategy + priority
          solution = (combination of strategies operating on variables with insight functions that reduce dimensions of problem (function-combination) or (resource-imbalance))
          type = combination(attributes)
          intents = function outputs, including unintended/emergent/unforeseen side effects (target/avoid)
          roles = functions
          relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
          components = compounds, symptoms, treatments, metrics, conditions, stressors, types, variables

    - update links
