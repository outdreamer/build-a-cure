# to do

  - de-duplicate logic
    - integrate problem_solving_matching.md & analysis_examples.md
    - integrate changes from interface_analysis.py and solution_automation_analysis.py to repo
    - integrate example.py & workflow logic
    - integrate rules from diagrams to relevant documents

  - organize interface analysis definitions
  - add functions from workflows & analysis (to do list, questions answered, problems solved, interface definition & functions) as files in functions/ folder
    - resolve duplicate functions
    - organize into primary core functions & list sample parameters (like objects to identify for the identify function)
  - function to translate interface query logic into interface language (combination of core functions (find/build) & other core components)


## examples to make

  - add diagram for intent-matching

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
    
    - update links
