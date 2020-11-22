'''

- a function to traverse an interface

      - this function applies an interface to a problem statement or input intent task, looking for matching objects

        - applying interface operations like combine/inject
        - finding components on the interface that match the problem structures (including related objects like insights, patterns, & functions) 
        - compressing the problem statement into its most accurate structure containing the found interface objects, identifying & reducing the solution space from this standardized problem format, by the problem & problem space definition   
        
      - outputs

        - information, interface objects, functions, or attributes compressing the problem

      - example:
        - once the problem is in system format, iterate through objects, attributes, & functions in the problem system checking for anything in the problem system that looks like a system object, such as a false similarity, an incentive, or an efficiency, with a particular focus on system objects that are associated with the problem type (if there are any insights relating that problem type with system objects such as imbalances relating to the info asymmetry problem type). 

      - interface traversal functions

        - iterate 

        - match 

        - apply

        - interface conversion function

          - convert the problem object to the interface using the interface conversion function, so that the problem is framed in terms defined on the interface. 
            - example: 
              - after converting a problem statement & problem object to the system interface, the problem should be framed as a network, so that it's easier to identify system objects within the problem such as conflicts. 
            - This function may act as a filter, isolating attributes of the problem that are specific to the interface, but may also convert the problem so that it's in a different format. 
            - This function may execute similar logic to the function to derive a definition of an object, which involves finding an alternate route (such as using the interface-specific terms) to output a set of attributes/functions (such as the problem object). 
            - Apply interface object components (functions, patterns, attributes) to problem objects.
              - If mappable objects are found between problem objects & interface objects, map the problem to the interface by labeling the problem object & a degree of certainty in the identification, as well as the attributes/functions/objects found to be similar. 
                - example:
                  - if the program finds a possible system conflict object in the problem system in step 406, apply the system conflict objects, functions, & attributes to the problem system intersection object. This means if the system conflict object has an associated function in its definition like 'diverging intents' or 'trade-off' or 'resource competition' or 'antagonistic agent', apply those to the problem system intersection and see if they fit in the problem system intersection. An intersection is an overlap at the intersection point involving different directions, so it's likely to match the 'resource competition' and 'diverging intents' components of the system conflict object definition, but may not depending on the problem definition (the intersection may just be an incidental routing object, rather than a competition for that position, and may allow multiple objects occupying the same position, and the directions may not indicate different intents if similar objects are in both directions). Then the program would follow this analysis for example with a query to the insight interface, applying any insight objects matched there to the problem system once the system objects were identified & applied. 
                  - if while iterating through the problem system, the program finds a possible similarity between a problem system intersection object & a system conflict object (a similarity in shape or other attribute value), apply the 'system conflict' label to the problem system intersection object. 
            - converting problem systems (such as the problem space, related problems, or problem) to interfaces involves mapping problem components to interface components
              - example: after converting a problem statement & problem object to the system interface, the problem should be framed as a network, so that it's easier to identify system objects within the problem such as conflicts. This function may act as a filter, isolating attributes of the problem that are specific to the interface, but may also convert the problem so that it's in a different format. This function may execute similar logic to the function to derive a definition of an object, which involves finding an alternate route (such as using the interface-specific terms) to output a set of attributes/functions (such as the problem object). If the problem cannot be mapped to an interface, log the error to be output with the final solution metrics ("error: could not translate problem 'create schedule' to the attribute interface"), and skip to the next interface in the specified sequence - if there is no next interface, return to interface selection, sequence & query design in step 403 by translating the problem to a more standard interface like the system or function or pattern interface. If it's not translatable to any interface, return an error and suggestion for additional information that could create a translatable problem that can be framed on an interface. This error may be added to a store of information generated/derived/found during traversal if the problem statement cannot be mapped to a particular interface, to be included in the output with the final solution metrics, for example "error: could not translate problem 'create schedule' to the attribute interface"). 
              - Once the program has formatted a problem as a system, it iterates through objects, attributes, & functions in the problem system, checking for anything in the problem system that looks like a system object, such as a false similarity, an incentive, or an efficiency, with a particular focus on system objects that are associated with the problem type (if there are any insights relating that problem type with system objects such as imbalances relating to the info asymmetry problem type). 
              - FIG. 1F depicts an example of determining a possible match between the problem system intersection object and the system conflict object.
              - The system on the top left depicts a subset of the Problem System containing the Intersection Object, formatted as a network.
              - The intersection & conflict object on the top right are integrated to produce an example of labeling a problem system component (like an intersection) with the possible matching component in the system interface (and a level of certainty added by each matching attribute/function) - the matching system component here is a conflict object, based on certain conflict attributes from its definition like diverging intents and resource competition.
              - As shown in FIG. 1G, and referenced in process 400 steps 404 - 407, the solution automation module 140 may include a method to convert matching mapped interface components to problem systems. 
              - FIG. 1G depicts an example visualization of applying interface object components to the problem object, where potential attributes/functions are included outside of objects and probable attributes/functions are contained in the objects.
              - It also depicts the transformation of the intersection object formatted as an object to the intersection object formatted as a system in a network structure. Now that the intersection is formatted as a network, and the system objects like conflict (and its sub-components, patterns, objects, etc) have been applied to the intersection network. In the network format, position & other types of connections have semantic value. Now it's clearer that the intersection has an ambiguity in the position sequence attribute (a variant of the position overlap where only one agent can possess the resource at a given time), creating a possible conflict (determined by which agent arrives in the position first and which agent gets the position resource first). The diverging direction attribute inherent to the intersection has not been converted to a diverging intent, but it could be if the different directions indicate different intents, and if that difference is relevant to the resolution of the conflict about which agent is allowed in the position first.The mapping function has also identified a possible trade-off in the ambiguity, indicating that only one agent can occupy the position at a given time, so only one agent can go first (a scarce resource of occupation sequence or saved time that may be causative in the system, especially if the agent changes the intersection or removes some of its value by occupying it first).
              - If while iterating through the problem system, if the program finds a possible similarity between a system conflict object and the problem system intersection object in step 406 (a similarity in shape or other attribute value), apply the system conflict objects, functions, & attributes to the problem system intersection object. This means if the system conflict object has an associated function in its definition like 'diverging intents' or 'trade-off' or 'resource competition' or 'antagonistic agent', apply those to the problem system intersection and see if they fit in the problem system intersection. An intersection is an overlap at the intersection point involving different directions, so it's likely to match the 'resource competition' and 'diverging intents' components of the system conflict object definition, but may not depending on the problem definition (the intersection may just be an incidental routing object, rather than a competition for that position, and may allow multiple objects occupying the same position, and the directions may not indicate different intents if similar objects are in both directions). Then the program would follow this analysis for example with a query to the insight interface, applying any insight objects matched there to the problem system once the system objects were identified & applied. 

        - traversing the interface network of interfaces acting as filters involves:
          - interfaces like information, insight, structure, math, concept, type, variance, potential, change, intent, perspective, system, attribute, pattern, function, cause, problem/question, solution/answer 
          - an interface is comprised of its definition routes, conversion function, core functions, objects, & attributes, and related objects like patterns & metadata specific to the interface 
          - converting the problem definition to the interface using the conversion function which applies system-mapping, position-finding, & object-fitting logic
          - looking for common attributes between problem objects & interface objects & their structures (like transformations, subsets, & paths) so that interface object relationships can be used to infer relationships about associated problem objects, where the traversal may start from various points on the interface, including core objects & functions, or directly mappable objects to the problem objects, or important or required interface objects. 

          - example traversals:
            - system interface traversal 
              - general: fit system objects like symmetries, sub-systems, sub-interfaces, false assumptions, correlations, and conflicts to problem/solution/space definition 
              - specific: find the lowest-cost path in a system (maximizing the number of efficiencies used) using incentivized paths 
            - information interface traversal 
              - general: use logic such as mapping the problem as a combination/set/path containing information problem types like an information mismatch or inequality or minimum or overflow or lack 
              - specific: frame a 'find a particular record in a data set' problem as a combination problem of a missing information problem type (composed of a filter-selection problem, an indexing problem, and a sorting problem) or a route optimization problem type (starting point in data set, search/split/sort method selection, and cost-minimization problem for worst-case destination given starting point) 
            - insight path application  
              - general: use insight paths from other fields to optimize insight generation/identification/derivation, where insight paths can contain questions, strategies, insights, & other information objects that are usable across systems to generate/ identify/derive insights in a semi-unknown system 
              - specific: use insight paths from gene editing to automate inventing by mapping gene editing functions (switch, remove, alter) to inventing problem space functions (switch components, remove assumption, alter variable) 
            - intent interface application 
              - general: convert inputs/outputs/functions, objects, & attributes to intent to check progress toward solution intent or avoid side effect intents, where adjacent reasons to call the operation & operation outputs are assumed to be included in the intent stack of an operation 
              - specific: convert inputs/outputs/functions, objects, & attributes to intent, to check progress toward target solution metric or avoid side effects 
            - structural interface application 
              - general: find a standard structure & format the problem using that structure 
              - specific: convert functions to standard structures like paths, networks, filters, or attributes to check if a function fulfills a solution metric 
            - core interface traversal 
              - general: use combinations of core functions (find, build, apply, derive), objects (layer, filter, gap, limit), and attributes (equal, similar) to create a core interaction space & system layer diagram and find target objects quickly using structural definitions of concepts like optimal or applying system filters, or predict missing objects on other layers 
              - specific: use the core functions of the 'combine' or 'organize' intent to predict the next generation of products invented 
            - a pattern interface traversal (where patterns replace missing required data, such as patterns between variables of specific types or system positions to infer their probable relationship) 
              - general: select patterns related to stated objects and traversal for patterns or pattern generators linking them to generate an origin solution space to begin compressions at 
              - specific: select patterns related to variable relationships & probability distributions to predict the likeliest ways a function will change 
            - a causal interface traversal 
              - general: match problem structures to causal structures (like tree/network/loop/ layer) to infer probable causation metadata like directness of cause, degree of cause, inevitability, ambiguity, uniqueness of cause, causal shape 
              - specific: 
                - find the set of causal objects, functions, and attributes describing a relationship to create a prediction function or reduce input features 
                - apply causal structure relationships to determine if the data is missing information 
            - concept-structure traversal (a multi-interface traversal linking the concept & structure interfaces, so a target concept combination/set/path or target structural attribute can be achieved with a combination of filters & limits or functions applied to adjust the structure until it matches the target structural attributes or concepts) 
              - general: 
                - find a structure for a certain intent that matches a conceptual priority (like relevance, organization, robustness, equivalence, or trust) 
                - modify a structure with a certain intent so it matches a conceptual priority (like power or a conceptual structure like power distribution) 
              - specific: 
                - find a structure in the finance space that minimizes trust in transactions  
                - modify a multiplication method to find a method minimizing larger calculations 
            - structure-math interface mapping 
              - general: use a multi-interface traversal to map problem structures to math objects to apply math insights to problem structures 
              - specific: if the problem is 'predict the shape of the boundary of an even distribution of change across directions from the same origin' (for problems like 'finding a container needed for an experiment growing microorganisms given the requirement of the same origin and non-overlapping paths', or 'predicting the threshold marker needed for comparing speed metrics'), apply the 'circle' definition route using the 'evenly distributed outward motion' route to infer that the boundary could be circular, with variable advantages depending on problem metadata 
            - problem interface traversal, specifically a problem vectorization framing the solution as a path in the problem space (mapping the problem definition to a one-directional tree with inputs on one side, interim inferred important problem concepts in between, and target priorities or attributes on the other, linked by available functions) 
              - general:  
                - infer important interim concepts of a problem system (like the 'duplicate line' concept for building a 'merge files' function) and use intent- mapping to connect stated problem objects & target outputs using available functions 
              - specific:  
                - infer the relevant 'duplicate line', 'similar line', 'similar', & 'equal' concepts of a 'build a function to merge files' problem system and use intent-mapping to connect stated problem objects (line, file, string) & target outputs (one file without duplicate lines) using available functions (iterate, check, is_similar, is_equal) 
                - a question-answer interface traversal (a sub-interface of the problem interface) 
                  - general: frame a question as missing information structured as a source position and a target position on a network, and the answer as the most robust path, the most relevant path for a particular intent & objects related to it, the path that moves the nearest to the target position, or the quickest path that moves in the prioritized direction on the network 
                  - specific: 
                    - frame a question like 'how to build a filter' as an optimal path-finding problem on the network between some undefined starting component set & the destination filter object 
                    - frame a question like 'why would you build a filter' as a adjacent object 
                    - finding problem to find objects that can be produced if the filter is the starting point (input) or to find intent directions moved in when you follows paths to build the filter (reasons to build it) or subsequent paths using the filter (other applications of the filter) 
                - the problem interface includes other sub-interfaces like 
                  - problem space analysis (analyzing a system composed of resources, agent intents, & problems) which is the problem interface with information & structural & system interfaces applied, to make problems & solutions visualizable within a system context 
                    - general: analyze whether the problem space changes in a way that invalidates the original or other problems once a particular solution is applied, anticipating cascading, self-sustaining & self-solving problems, and selecting between solutions 
                    - specific: organize a set of resources into a problem space system with dimensions indicating primary factors of change that are also interfaces (as a foundation where changes can develop and be described in other embedded graphs) or cross-system attributes (like relevance), for standardized comparison of solution impact on all problems in the problem space system 
     
  - logic of general program workflow, from input intent & information to supported output (like a causal relationship, interface-filtered information, or an object definition): 
    - the general interface traversal process includes general logic to automate structural information tasks as indicated in Fig. 22


- interface analysis program flow (intent to output interface information)
    1. obtaining input information from a program or user (like a data set of possibly related variables, or objects in a relational database) involving input:
      - a supported intent (such as 'find a cause of this variable in the data set' or 'find an optimal structure for this information')
      - information to fulfill that intent (like an API description, data set, or document).
    2. retrieving an interface definition
      - involves querying the database which stores information objects including definitions (as well as other interface components, like interface-specific functions).
    3. deriving the interface definition if not found 
      - involves applying logic like 'searching for examples of the interface on other interfaces', 'aggregating unhandled variance into the new interface as a potential change type formattable on that interface', 'filtering examples of an interface into core components, which can be used to generate the examples' or 'assuming common core components & patterns for the interface from other interfaces and applying distortion functions until the interface examples can be generated'.
    4. determining relevant interfaces or interface structures 
      - involves executing logic like evaluating whether an interface would frame the input information in a way that maximizes differences within the information, while fulfilling metrics like 'avoiding losing relevant information' or 'avoiding unnecessary complexity'.
    5. determining an interface query structure to organize relevant interfaces or interface structures 
      - involves assembling a structure (like a network) to connect interface structures (like an interface) into a format that will connect the input information format with the output information format given in the user-supplied intent.
    6. execute query, checking for information needed after each interface or interface structure traversal 
      - involves navigating the structure of the interface query, a structure such as a network with logical operations like conditions & exit or return statements to connect interface structures (like combined interfaces, interface traversals, or interfaces).
    7. applying the interface definition to standardize the information to the interface format, and finding relevant matching information & interface components, which involves: 
          1. convert input information to interface based on interface object definition (remove information unrelated to dependencies for the causal interface) 
          2. apply an interface to input information 
              - find core causal interface components (like structures, such as directions of dependency) in the input information necessary to do other causal interface operations
          3. apply interface components to distort information to generate additional information to match (distort input information with causal or other interface components)
              - specific interface components (like navigation functions) for that interface 
              - core/common components (like distortion functions) of that interface 
              - related components of the interface 
              - other interfaces/interface operations 
          4. find matching objects 
              - check formatted information & distorted information for objects that match the causal interface objects
          5. convert to original system format (input information format) 
              - integrate causal structures found with the input information, checking for validity of the structures & their related objects once integrated with the input information
              - integrating output into a structure relevant to the requested intent (on the meaning or interface-interface), which involves applying structure to the output information, as designated in the interface query design
        - this function implements traversal by applying interface components (like functions/attributes/objects) of a certain type (like core/common) in a structure (like a sequence) such as: 
          - applying core/common/generative/cross-system components (like functions) first 
          - applying insight/intent interface first 
            - example: applying cause-related insight paths to input information once converted to the cause interface 
          - applying interface checks first 
            - example: checking for new interface objects (like change types), if the interface changes frequently (like the change interface) 
          - applying related objects of the interface: 
            - example: applying interface info objects like related questions/insights 
        - the function to traverse an interface is referenced here: 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/math_semantic_map.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/problem_solving_matching.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/function_to_do.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/to_do.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/ideas.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/README.md 
        7.A. applying default components or prioritized structures to format or otherwise alter the information to identify its structural relevance to that interface 
            - default components or prioritized structures can include: 
                - specific interface components (like navigation functions) for that interface 
                - core/common components (like distortion functions) of that interface 
                - related components of the interface 
                - other interfaces/interface operations 
            - for example: 
                - once a data set is converted to the information interface format, like: 
                    - an information-interface structure indicating information position/distribution/identity across agents 
                    - a structural-interface structure like a language network 
                    - a system-interface structure like the interaction of two information systems (with different internal functions/attributes/objects and/or information, like two type clusters in a data set) in a host system 
                    - a math-interface graph of data points on various dimension sets 
                 - the analysis program may follow that conversion with an additional conversion to a format amenable for comparison with important components on the information interface, like: 
                      - core info objects (like a core differentiating/comparison/storage rule, core conversion/filtering/organization function for new information, or a constant fact as a core information unit) 
                      - primary info objects (like perspectives/insights/questions/etc) 
                    - for example, the structure of a question in its default format might be a structure indicating missing information (the important object of the 'question' definition) for an intent 
                - in a graph format, this core 'missing information' structure of the question info object could take the form of structures in the graph like: 
                        - mismatches (like an incomplete rule set missing a function/variable attribute/object) 
                        - assumptions (questions being the removal of an assumption, the missing information being how the graph would change if the assumption was removed) 
                        - randomness (missing relevance/dependency to the system, like a data set having outliers that are missing the information of relationship to the data set) 
                    - which could indicate several embedded questions given these question type sub-structures: 
                        - which are the independent/dependent variables? 
                        - what is the independent/dependent variable relationship? 
                        - what do the clusters mean? (group membership of a data record) 
                        - what are the patterns of the clusters? 
                        - what is the probability of various given/generated data points being in a cluster? 
                        - what causes the outliers? (randomness, group resolution/dissolution/merging/divergence/adaptation/misidentification) 
                        - what function describes each clusters' variation? (function relating variables in data set) 
                        - what functions relate the clusters? (how could you transform one cluster to the other) 
                        - what direction or other structures of causation exist between the clusters? (does one group tend to become the other, and why/how/in what contexts) 
                - as another example, once a data set is converted to the system interface format (like a network of objects & functions with attribute shapes like layers), the program would follow that by converting it to a format amenable for comparison with primary interface objects (like incentives), functions (like optimize), or attributes (like complexity). 
                    - a format that enables comparison with interface objects like incentives would attach labels & structures where known interface structures (or calculated probably interactive/relevant alternative/adjacent interface structures using core combination analysis) are found 
                        - for example, if incentives have a structure like 'a shape where resources would stabilize at rest', a related structure would be generatable with core combination analysis by applying core functions like 'condition where other system variables are simultaneously changing' instead of the 'condition where other system variables are unchanging (at rest)' to generate an adjacent structures like 'a shape where resources are constant regardless of other variables', which may be a 'constant' or 'assumption' object 
                        - if the data set has a structure matching the 'constant' or 'assumption' object definition the program just generated by applying core distortions to the system 'incentive' object definition, it may be comparable with the 'incentive' definition object, because those objects are adjacent and operate on similar interaction layers, and may even interact (the program would query for insights or functions to check). 
        7.B. identifying matching components between information & interface components (components like systems, objects, functions, attributes, & types) 
            A. then the input information objects (converted to the interface) would be compared to interface components, to find matching structures 
            B. after this initial match check, the function interface is applied, using interface-specific functions, which are either: 
                - functions of that interface (function types like core/common/interactive/relevant/change/causative/generative/other prioritized distortion function types) 
                - functions of other interfaces 
                    - patterns & functions across interfaces (apply the pattern interface) 
                    - insights & insight paths (apply the insight interface, a sub-interface of the information interface) 
                    - functions to achieve core/common/current interface intents, like core/common formats like 'minimized', attributes like a 'change-handling' priority, or other outputs like core/common/generative functions (apply the intent interface) 
                    - functions of cause/change/potential (apply change/cause/potential interfaces, to ensure youre checking versions of the structure that are probably relevant by commonness or other core priorities like causative change types, causal adjacence, or probability) 
                    - functions of concepts (apply concept interface, to identify concept structures) 
                    - functions of systems (apply the system interface & its components, like the 'optimize' function) 
            C.A. once these functions are applied, iterate through distortion sets producing different states of the input information: 
                - verify that the distortions are still relevant to the interface 
                - repeat the matching process, looking for matching structures between the newly distorted input information structures & the interface components 
                    - for example, once youve applied an insight like 'comparison is quicker if you only compare different attributes', which involves reducing the attributes of the input information to the different attributes, do you find any new matches with interface objects, like a match with a function that could produce those differences, from either point in a compared pair as the input & the other point in the compared pair as the output? 
                        - if so, this is a function that you might not have found as quickly if you were matching the object having those attributes on a different interaction layer, like how comparing two shapes would benefit from different functions than comparing two generative functions of the two shapes 
            C.B. optionally, distortion functions can be applied with intent to identify new components on the interface (apply an intent distortion function on the cause interface) 
            C.C. optionally, distortion functions can be applied to other interface objects, to identify new components on other interfaces (such as applying a causal distortion function to an insight path to check if a new insight path applies, while traversing the cause interface), using the new input information and/or the cause interface objects for comparison 
        7.C. convert matching interface components back to input information 
            - if the program identifies a matching object in step 4 like a pattern (like two variable types that are usually related in a certain way indicated by the pattern) found in the input information, apply that pattern to the input information 
            - this means: 
                - retrieving functions/attributes/objects of that matching pattern (like which variable types are applicable), as well as relationships of that pattern to related objects (like related patterns/insights/functions, such as a validation function to check variable type) 
                - iterating through those related components and/or component sets of the matching pattern from the interface 
                - applying each related component or component set to the original input information (does this variable pair have the pattern implied by their variable types, which are applicable for that pattern) 
                - testing the new state of the input information for validity 
                    - does that pattern make sense (does it match functions/outputs or other structures) or have meaning (does it interact with relevant structures), given the system context of other input information or other information generated by prior interface analysis) 
            - if the probability of an accurate match is high enough, store that matching interface component, formatted to fit the input information, as a possible version of the input information, on which other interface analysis can be applied sequentially 
        7.D. repeat steps 7.A - 7.C if the selected interface analysis intent (support intents of interface analysis including 'traversing the interface' or 'formatting input information in as many ways as possible' or 'filling out an interface definition') is not complete. 
    
    8. integrating output into a structure relevant to the interface traversal intent (on the meaning or interface-interface), interface traversal intents such as 'find a cause of this variable' or 'find an optimal structure for this information', which involves applying structure to the output information as designated in the initial interface query design 

    '''