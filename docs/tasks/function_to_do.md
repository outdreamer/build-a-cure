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

  - insight analysis includes:
      - identifying how an insight is generated
      - identifying alternate ways to generate the insight
      - identifying how an insight fits into its problem space
        - identifying the relationship between the problem space structure & the insight
  
  - example of a system analysis function: identify a system object (error) in the problem space system

    - general method: pull error cause types, error types caused, identify known possible information problem types, match error types with info problem types by applying structure, find matching solutions for error types once linked to info problem types

    - function to generate/identify errors in a solution (function set, host system) within a problem space formatted as a system

      - identify error root cause types using combinatorial core analysis

        - find components
          - structural mis/matches
            - intent mismatch between function combinations across layers 
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

      - find error types caused by those cause types
        - structural mismatches cause:
          - lack of system/context-function fit (function-scope mismatch)
          - lack of rule enforcement (function/responsibility mismatch, expectation/usage mismatch)
          - lack of intent restriction for using a function (intent mismatch)

      - filter caused error types by which generated errors would cause information problem types (process failure, access vulnerability, corrupt data)

      - identify specific errors of filtered caused error types, organized by interface
        - lack of intent restriction for using a function
          - malicious function sequences matching validation requirements
          - breaking input/output sequence for later functions
        - lack of system/context-function fit: 
          - incorrect permissions for context
        - lack of rule enforcement
          - unhandled function inputs
          - granting cache access to unauthorized scripts

      - match specific interface (intent, structural) error types with information problem types (apply information interface to error types)
        - lack of intent restriction
          - breaking input/output sequence for later functions
            - injecting function with less validation in function chain

      - match specific interface (intent, structural) error types with solution types
        - intent mismatch: align intent
        - lack of intent restriction: reduce intents supported by function (re-organize logic, add validation)
        - incorrect permissions for context: scope permissions, generate permissions for a context/intent & check for a match before executing
        - breaking input/output sequence: check that all valid/supported function sequences are maintained
        - lack of rule enforcement: check that all rules & rule structures (like sets or sequences) determining resource access are enforced, or rule gaps where error/attack types could develop are closed
      
      - reduce by solution types that cover the most error types without contradicting other solution types or creating additional unsolved problem types
        - intent-matching covers multiple structural error types
        - system-fitting or structure-matching as a superset of intent-matching
      
    - invariant vs. symmetry

    - applying 'combination' structure to type patterns:
      https://www.technologyreview.com/2020/10/30/1011435/ai-fourier-neural-network-cracks-navier-stokes-and-partial-differential-equations/

    - generating false data to 'balance racially biased datasets' removes the embedded info that some races are oppressed
      https://www.zdnet.com/article/this-startup-wants-to-fix-your-biased-ai-one-dataset-at-at-time/
      
      - how would you derive that info (derive the concept of 'racial oppression') from a data set with 'racially biased data' that reflects real problems, without erasing the information of those problems, information which might be relevant to what youre predicting?
        - if you only have race/location columns in your data set:
          - if races are differentiable by location:
            - why are they isolated? is one race being targeted by the other? is there another conflict, like previous oppression, creating economic disparity (an alternate cause of separation by location)?
          - if races arent differentiable by location:
            - check for crime data by location:
              - is crime higher in locations with integration? why might that be the case?
            - check for other types of location separation (granular separation, like by neighborhood rather than zipcode)
      
      - the concept of 'oppression' can be inferred in many ways, depending on the data set
        - resource access
        - health metrics (image & consumption habit data will show signs of stress)
        - state changes:
          - if the data is new, it will reflect different problems based on the different state of power distribution
            - previously powerful oppressive groups experiencing a backlash, reflected in stressors
          - if the data is old, it will reflect problems like:
            - clear differences in health/culture from severe segregation of groups
        - 'group' changes
          - group dynamics between oppressors/oppressed through phases over time
        - 'tech' changes
          - other variables, with info tech & science applied (science to improve health metrics, info tech to magnify & integrate group dynamics)
        - the concept of a 'health standard' ascribed to racially-associated traits that doesnt correlate with actual health, but allows variation in social choices, given other metrics like social skills
      
      - real 'balancing' of a data set is meaningfully balanced, not just variable value-balanced:
        - a data set with exclusively minority criminals could be balanced by adding real data of majority criminals (not generated data)
        - this doesnt remove the information implying oppression, but it does include a standard to compare different causes of crime
          - the oppressors who are poor are likely to be poor for different reasons (intellectual poverty, drug addiction) than oppressed minorities (systemic/compounding inequality)
            - how would you identify this difference in cause in the data set?
              - the poverty of an oppressor is likelier to be a choice, so the key factors would be:
                - signs of intellectual poverty (facial tattoos, signs of aggression, copying pop culture, lack of social skills)
                - signs of addiction (lack of habit variation, lack of other consumption habits)
                - signs of agency (lack of optional health habits, access to expensive health options)
                - signs of power (lack of self-modification, lack of stress)
              - the poverty of an oppressed minority is less likely to be a choice, so the key factors would be:
                - signs of group membership/strong relationships (gang signs, embedded cultural symbols, similarity of habits/consumption within groups, signs of social skills)
                - signs of lack of power (self-modification, signs of poor health/high stress, lack of planning for future)
                - signs of lack of agency (lack of health habits, modifications are likely to be cheaper, a/antisocial behavior)
                - visible differentiating factors (enabling others to identify them as similar/different)
        - a data set that correlates gingers with crime would be balanced with data where that trait is not targeted for oppression (is it associated with more crime in Mexico too where theyre given more power than average - what about where its not noticed/targeted at all, like a community of gingers)
        
      - a good AI would identify relevant causal concepts (depending on the data set) like:
        - positive concepts of health, social skills, intelligence, strong relationships as factors in success that can offset the negative concepts associated with oppression
        - negative concepts like stress, poverty, & gangs
        - neutral relevant concepts like tech & science, which can be used to oppress or liberate

      - a good AI would infer that this was a complicated problem requiring conceptual analysis by the complexity of language & variation in social interactions or language progression, which would give it information about how new terms develop (to categorize & identify oppressive behaviors, often using comedy, so those behaviors can be stopped) and how they propagate (used by oppressive groups for profit, leading to self-awareness), giving the AI information sufficient to infer the concept of oppression

      - a really good AI would identify causal structures like causal loops in the data:

        - example: 
          - oppressing a group by an irrelevant factor like hair may upset members of that group, which may either cause members of that group to develop social skills like emotional regulation, or do crimes
          - this creates a self-fulfilling prophecy in the form of a causal loop: the hair used to be irrelevant, until they were oppressed for it and reacted to that oppression in a negative way, which made the oppressors think they were right, and may make oppression continue
        - it would also isolate strong causative anti-crime factors like emotional regulation, which will have some different signs & problems (lack of emotional expression, signs of intelligence, signs of stress to correct other people's problems)

        - it would also generate its own standardized language to generate/infer/associate concepts:
          - 'emotional regulation' would be translated to 'irrelevant status change signal response regulation' by a very good AI that can process concepts & apply standards
          - once that concept is formatted that way, it can infer structures to look for like facial expressions & chosen status signals, without knowing about them
          - the concept of 'emotional regulation' can be inferred:
            - 'status change signal responses' that are identifiable by other agents

          - 'status change signal responses' (emotions) can be inferred from core concepts like 'status', applying 'change', and 'information processing' or 'communication', as well as 'stress' and the associated concept 'stress handler', identifying a 'status change signal' as a stressor

          - once concepts are generated & standardized in this way, other concepts (like 'intelligence' or 'oppression') can be fit into this standard & the meaning of each concept identified quicker

    - energy stored in information/structures has stability physics, where information in a certain structure can support other information of different structures, including structures allowing variation in change/potential

    - config manager that allows specifying conditions/processes (check for approval from Artemis), data source (url or queries) & UI components/graphs (template or queries) to build apps/pipelines  automatically
    
    - migration/integration automation using app architecture/code/config search: searching other stack resources (application code, API, data store, resources, security & pipelines) in a repository of stack resources of existing or optimal applications, to test the original app test cases to see if a particular codebase/database/config/pipeline will work for the users' needs, without having to manually code a migration or integration to another stack (either migrating code, cloud, pipeline, data store, security tools, or all of the above), and using incremental tuning of the application code (mixing in code components, injecting dependencies, executing adjacent transforms, etc)
      - the primary work involved on the dev side would be ensuring the test cases covered all user needs
      - the migration/integration logic would involve search filters in the form of exit conditions that would skip to the next resource stack if a particularly important test doesnt pass, rather than trying to fix the resource stack that is clearly too different from user needs to be adjacently useful
      - it could also start from a standard set of application resource stacks in various stack combinations and add logic/config/schema until it fulfills the test cases
      - identifying probably successful transforms of code/config can be done with code queries if indexed by intent, or by translating code to the currently iterated resource stack given pre-defined mappings

    - ml explanations: embedded interface structures (causal structures, type paths, problem types, change types/bases), function subsets/alternate functions composing the prediction function

    - core operators in math space
      - structure
        - format (as a series, function, function set, coordinate set, vectors, matrix, aligned values, base, on dimensions, as an embedded parameter)
      - differentiate
      - set
        - include (add, increase, multiply, combine)
        - exclude (subtract, decrease, divide, filter)

      - focused information with values
        - when you inject information (value set) into a structure (dimension), what happens?
          - the limits & functions of the dimension, combined with other dimensions & rules of the space, are activated as causes of those value outputs
          - the intent of a value set combined with a format can be to highlight connections between these causes


    - structures of difference: chaining difference types (like randomness, core operations & definitions) across different component types like objects/variables are a quick way to identify new objects/systems to explain or fill rule gaps

    - identifying randomness vs. false illusion of randomness (temporary equivalence)

    - pattern matching/anomaly detection/noise reduction in finding relevant information eliminates information based on:
      - commonness/similarity to patterns (focus on common patterns)
      - similarity to other data (isolate anomalies)
      - reducing equivalence from randomness (isolate non-random processes that follow rules)

    - efficiency in calculation
      
      - why is finding a proxy value (that is a multiple of 10) of a multiplication value quicker at some multiplication problems?

        - because of the efficiency present in applying the definition of a digit (base 10), which may make multiplying 65 * 10 and subtracting 65 quicker than multiplying 65 * 9,
          - the operation 65 * 10 just involves moving 65 one digit to the left and adding a zero
          - subtraction is held to be less computationally expensive than multiplication
        
        - the definition of a digit positions multiplication output of base 10 in a sequence that allows indexing of values in comparison to 10 & degrees of 10
        
        - how to find the "definition of a digit' as a relevant object in all the objects of that space
          
          - filter: by noticing that:
            - multiplication changes positions of numbers in some cases
              - relevant concepts to number position
                - 'digit'
                - 'base'
            - multiplication preserves the original numbers in some cases
            - the original problem can easily be transformed into one of these cases (multiplying numbers rounded to an output of multiplying by 10), and easily converted back into the original problem (adding/subtracting remaining value)
              - these two operations may be less computationally expensive than the multiplication operation
          
          - query: in order to notice the above relevant objects, you can do the queries:
            
            - change interface: 
              - find variables of value changes and change types (value position change)
              - static/anti-change (apply 'not' operator or 'lack' problem type to 'change' concept):
                - find cases where change types dont apply (value position preservation and value preservation)
                  - find method of translating problem to case where work is minimized, if work-maximization conditions dont apply
                    - find secondary method to connect translated problem back into original format (with original parameters, meaning adding/subtracting remaining value)
            
            - intent interface:
              - intent of preserving values is to minimize work of calculation
                - find cases where work is maximized by preserving values
                  - filter by whether work-maximization conditions apply
                    - apply method of translating problem to case where work is minimized, if work-maximization conditions dont apply

        - in other words, the original question is 'why do value position & digit base produce calculation efficiencies in multiplication?'
          - because position (and emergent objects of position, like sequence) matters, as adjacent values have inherent relevance/meaning
            - 1000 has more meaning in some contexts than 1, and the second one in 1101 has more meaning than the 1 next to the decimal in some contexts, or in a default definition of 'meaning' as 'value' or 'distance from origin', except with definitions where the definition of meaning is a concept like 'clarity' or 'unit' or 'standard'
          - difference from base values is another way to measure relevance in values having position
          - the more different a multiplier is from 1, the more relevant these digit-based adjacent values become in optimizing the multiplication process
          - important metrics of relevance:
            - value position difference
            - non-zero value position difference (distribution of non-zero values in multipliers)
            - value difference from zero
            - value difference from adjacent digit base multipliers
            - difference in calculation operations between digit base multipliers (move position operation) & original multipliers (multiplication operation)

          - intent-matching:
            - intent-change
              - the intent is to change position of a value, there is an efficient operation to accomplish that intent (move value position) if the inputs qualify given the base standard
                - difference in multiplier value position = value position difference source, if difference between inputs & digit base requirements are negligible
              - this is how you can frame a math problem on the change interface, framing the differences needed (intents) with the input differences (variables) and other relevant differences (differences from standards)
              - an efficient solution is one that minimizes use of costly functions like transformation operations (maximizes use of adjacent resources or other efficient methods)
                - so the inputs to an efficient solution will minimize the difference type that is 'input differences'
                - efficiencies minimize differences/difference types needed to achieve an intent in general (an efficient alternate route may use fewer steps or lower-cost steps than the default route)

          - these differences align in a structure that clarifies the increase in value from using digit base multipliers followed by conversion to original multipliers
            - if a multiplier fulfills the threshold values of these operations on the difference types:
              - maximize (value difference from zero) + minimize (value difference from adjacent digit base multipliers) + minimize (non-zero value position difference)
                = minimal difference from efficient calculation (multiplying digit base multipliers)
            - the solution structure points to the alignment of these differences:
              - use methods (convert to digit base multipliers) that allow the use of position operations (move position) rather than more expensive operations (multiplication)

            - how could you derive efficiencies if you didnt already know that using a digit base multiplier was lower-cost than using the original multipliers?

              - you can apply definitions of objects to other definitions, and check for conversion adjacency to those objects
                
                - examples:

                  - find difference/change types (like differences in variables like bases, adjacent transforms)
                  - apply aligning structures of difference types
                    - difference from digit base multiplier (multiple of 10) aligning with value position difference operation (move)
                    - (difference from common base) combined with (difference from common base) = exponent addition/subtraction 
                  - apply a pattern to a parameter set
                  - apply an average operation to a function
                  - the points formed by factors of a number that align with the digit base form a pattern of efficiencies in multiplication intents for certain original multiplier sets
                  - apply transformation sequeence:
                    - standardize to common interface (in the form of a common base value)
                    - find derivative/slope
                    - this transformation sequence identifies the difference type of a constant difference between exponential values of a multiplier (4 ^ 0, 4 ^ 1, 4 ^ 2) once transformed to derivatives, constants being easier/more efficient to work with than other value/function types

                - youre looking for object intersections or object patterns that share resources in some way and reduce costs for each other by interacting
                  - this means you want to focus on combinations that increase the likelihood of interactions with other objects, just like the base number 10 has interactions with value position (digit definition) & the move operation, and multipliers having a common base having interactivity in their exponents
                  - youre also looking for shared spaces that can act as interfaces (common bases, formats, standards) where calculations are more trivial (addition rather than multiplication) because the values are already standardized
                  - operations may develop on these shared spaces, leading to efficient object interactions

              - you can also start with a set of unit or efficient operations and build functions out of them that iteratively fulfill higher & higher intents
              
            - how to derive efficient operations in the first place:

              - identify when there are alternate paths to an answer (65 * 10 = 650 * 1) while changing a minimum of other variables (having the same number types, like integers), and check if alternate paths are lower-cost, and in what cases (ratio of cases, common cases, etc)
                - a variant of this is identifying that multipliers share a common base, which has another calculation efficiency in the application of addition/subtraction to exponents instead of multipliers
                  - example: 64 * 16 = 4 ^ 3 * 4 ^ 2 = 4 ^ (3 + 2)
                  - if you dont need the result of the operation or can standardize other relevant values to that base, you can keep it in this format instead of executing the operation 4 ^ (3 + 2)

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
