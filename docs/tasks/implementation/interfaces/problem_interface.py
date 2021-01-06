'''
    - definition:
      - on this index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface
      - problems can always be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries)
        - finding a prediction function can be framed as an optimal path in a network of variable nodes
      - once you frame a problem as an info problem, you can map info to structure:
        - conflicts can be vectors with different direction or which overlap
      - this involves 
        - identifying the given problem & solution target structures in the problem space & the related problem network, so the problem & solution can be visualized
        - identifying & anticipating problems in a system, which includes identifying problem structures (inefficiencies, conflicts, etc) that exist or could emerge
          - for example, in the bio system, DNA regulation functions don't prevent pathogens from injecting DNA or mutations from occurring, so if you derive the concept of a pathogen or mutation without already having that definition available (using core system analysis), you could predict that the current DNA regulation functions wouldn't be able to offset the changes exacted by those concepts & you could predict problems of DNA disregulation in the bio system before they occur
        - identifying solvable problems, as well as what problems a solution matches or doesnt match, such as how a solution automation workflow involving a structure like a 'subset' (like 'break a problem into sub-problems & aggregate solutions') wouldnt match on a structural level with a fractal structure with certain problem types possible on that structure
      - all problem-solving automation methods have a variance assignment, allowing for variation to be explored in a certain location 
        - you can either map problems to fit that structure or design new automation methods based on the variance gap necessary to solve a problem


    - objects (problem, solution, problem/solution space/network) 

    - structures:
      - problem-solution formats (shown in FIG 9 (Problem formats, with matching solution formats) & FIG 10 (Problem-solution structure matching))
        - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system
          - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape
          - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc)
            - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent)
        - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function
          - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information)
        - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems)

      - problem shapes 

        - problems can have multiple dimensions creating the output problem shape, 
          which can occupy a network of related problems (both specific problems and problem types)
        - the problem space is the system in which the problem is relevant (can be a network of problem spaces)
        - different problem types have different default problem shapes
        - example problem type shapes:
          - a misalignment problem has at least two vectors differing in direction, where the optimal alignment is calculatable or at least the alignment is clearly improvable
          - a variance injection problem has a opening in a closed system
          - an asymmetry has an uneven resource distribution
        - if a problem has a misalignment problem and a variance injection problem, the problem shape can have both shapes in isolation, 
          or they can be merged, applied, added, mixed, intersecting, or combined in another way
        - example solution shape for problem shape:
          - for a misalignment problem, the solution shape would be:
            - a vector aligning them
            - another adjustment to the system that makes the existing misalignment a correct alignment
            - a combination of the two
          - for a variance injection problem, the solution shape would be:
            - an object (resource, function, constant) to close the opening in the system
            - an object to prevent further variance injections
          - for an asymmetry, the solution shape would be:
            - an optimal transport operation set to distribute the resource optimally according to the metric of symmetry

    - concepts (anomaly, outlier, conflict, inefficiency, mismatch, inequality) 

    - attributes: 
      - number of problem-causing variables/solution metrics fulfilled 
      - complexity: (number of core function steps required, variables, differences/inefficiencies, counterintuitive steps (requiring non-standard solutions), contrary processes (requiring scoped/nuanced solutions)) 
      - abstraction (does it solve the same problem when framed on an abstraction layer above) 
      - number of steps required to create problem from stable system base state, once work is standardized, & adjacence of steps required 
      - how much work is required to convert to a particular problem format (route, combination, composition) 
      - structure of problem types causing or forming the problem (number/position of information asymmetries, resource limits) 
      - structure of information objects in the problem (decision points, variance sources, unanswerable questions of the problem, the structure of causes generating the problem if known) 
      - type/intent ranges/direction (of individual objects or composite stack) 
      - similarity (how similar to a standard problem type, or how near to limits within a type dimension) 
      - ratio of positive to negative outputs (problems solved vs. caused) 
      - inevitability vs. agency of problem cause 
      - agency involved in the problem 
      - problem types (examples shown in FIG 17. Problem Types)
        - dependency/fragility 
        - mismatches 
        - conflicts 
          - intersection/collision 
          - comparison 
          - coordination 
          - competition 
          - conflicting direction/misalignment 
          - incentives/intents 
          - expectations/potential 
          - requirements/enforcement 
          - intent mismatch, like an unintended use (involves integrated third party tech not under review), like unintended side effects: whether it's a closed system or leaks variance (example: pre-computation, memory access, or process re-start event) 
          - misidentification  
            - incorrect structure (metric, information position, or organization/format) 
        - imbalances/inequalities (misdistribution of resources) 
        - inefficiencies (unmaximized benefit/cost ratio, such as unnecessary complexity/work) 
        - gaps 
          - missing information 
          - ambiguity (example: ambiguous alternatives) 
          - gap in rule enforcement 
          - gap in boundary (example: leaks (variance, resource/info), and injection points (assumptions/variance/control/randomness)) 
        - limits, such as enforced rules, or limited resources/functions 
        - specific problem types:
            - malicious alternative route to get same output
            - legitimate/alternative route to get malicious output

    - related objects: 

      - solution types:
        - problem-metadata solution: evaluating problem metadata to evaluate metrics like problem-solving postponement
        - generative solution: solution that generates solutions
        - solution framework: provides starting point & structures for solutions to be built in/with
        - problem decomposer: solution that reduces a problem's root causative (as opposed to just varying) parameters
        - interim solution: clearly suboptimal solution while optimal alternative is built
        - solution query constructor: solution that builds new solutions out of known solution types (existing structural solutions or core functions)
        - structure-finding/fitting solution: solution that assigns a structure to information or matches the gaps/limits in a problem structure to neutralize them

      - questions 
          - what are the problems (inefficiencies, conflicts, mismatches) in this system 
          - what solutions are associated with this problem type 
          - what problems are related to this problem 
          - what problems will develop in this problem space system 
          - what is the probable cost of solving this problem 
          - what is the adjacent format of this problem 


    - examples:

      - example of applying problem-structure interface: https://en.wikipedia.org/wiki/Anti-pattern
        - these are examples of contradiction/error types of the system-optimizing insight 'align relevant intents', which have the structural problem type 'misalignment' of the concept 'relevance':
          - local & global intents (local efficiency/fulfillment of local incentives/priorities, at the expense of global inefficiency/lack of fulfillment of global priorities/requirements/incentives, by allocating local solution side effects to global entities)
          - misaligning prioritization & intent (over-prioritize job duties like monitoring, to benefit the manager) that doesnt align with other intents (subordinate productivity) which benefit the company
          - imbalance/missing/disconnection from related objects (criticism & solution, solution & responsibility)
          - mis-aligning functionality (learning/potential) with requirement (repeating task)
          - mis-aligning intent of a product (making customer independent) with dependency structures (requires customer to use it beyond its value to them)

      - examples of problem types on different interfaces:
        - system problems: inefficiency, conflict, mismatch
        - information problems: excessive information, conflicting information, information asymmetry
        - structural problems: unnecessary components, contradictory function requirements, mismatch in shapes
        - intent problems: adding specificity where unnecessary, intents that neutralize each other given position, sub-intents that dont match function intent
        - concept problems: excessive definition routes, overlap in definition routes across concepts, definition route that more adjacently matches another concept
        - logic problems: excessive assumptions, contradictory conclusion & assumption, using specific logic to make absolute inferences

      - problem prediction example with market organization 
        - anticipating problems across many agents with n steps, and calculating which problems will develop and which solutions can be constructed in advance
        - unit example: predict when a dev will need a tool based on usage/purchase/request data (alternatives with different priorities/perspective built-in)
          - which problems will develop from which tool sets used at scale (migration tools between comparable alternatives)
          - which problemss will be prioritized & have solutions constructed
          - how to optimize by constructing other calculated solutions to prevent high-risk problems

    - dependencies
      - this interface relies on the find_format_for_metric.py function 

    - functions

          - function to filter/reduce solution space
            - use intent & system filters & concepts as a way to reduce solution space from defaults (find space & shape limits where intents are supported) when looking for alternate efficient methods of calculation
              - example: a method of calculating area under the curve can be built with relevant concepts (subset, linearity, similarity (to curve) as a input to the conceptual trajectory to the concept of approximation) once those concepts are identified in the problem space, and combined with different structures, each having their own intents (prioritized metrics like efficiency)
              
          - this interface implements a function that calls find_format_for_metric.py with intent to find structures that neutralize other structures (rather than a basic match)
          - convert a problem statement (and problem space context if provided) into the problem object metadata 
          - mapping function, to map problems to structures, problem functions, & other problem types (as graphing a problem is depicted in FIG 7 (Problem space visualization))
                      
          - validate user-provided GUI input information (for example, if the problem statement doesn't match problem type specified), entered in a form as shown in FIG 1 (User Interface Module)
          
          - optimizing functions to analyze prior queries, optimize & maintain the program, such as: 
            - removing duplicates 
            - calculating & compare query & solution statistics 
            - optimizing a performance metric like interface traversal once found 
            - pre-computing & storing frequently requested traversals 
            - optimizing data storage & logic given how other users are using the program
                 
          - function to graph the problem space, problem, related problem network (as shown in FIG 7), solution space, solution, embedded graphs, interfaces, and other relevant objects
          
            - function to apply limiting rules to problem visualization/formatting
              - if you reduce a shape of a subset of problem dimensions, those variables cant be used later in the solution, so even though some reductions may seem obviously right, more than one solution should be tried
                (side length if defined as a cube, or variable set like identities of sides, number of corners/sides, angle of corner, shape identity), 

              - mapping problem types to functions has side effects without limits & standardization applied to the format:
                - removing a problem variable can only be mapped to lowering the number of variables (whether limits, multipliers, or other objects) creating a shape once the problem variables are formatted with the same term set

            - function to derive the problem space metadata (which is returned & displayed to the user is shown in FIG 3 Problem Space Metadata), optionally including the solution metadata in FIG 4 (Solution Metadata) & additional solution metadata in alternate formats as shown in FIG 5 (Additional Solution Metadata), if a solution is found or if solution space information is found.
            
            - function to derive, analyze & compare solution metadata, for solution selection purposes
                - input filters 
                - risk contributed by input filters 
                - risk contributed by traversals (using a pattern instead of an insight contributes risk) 
                - solution(s) and/or solution space 
                - solution implementation steps  & components 
                - visualization of solution impact on problem space 
                - set of queries used to generate/find/derive solutions 
                - methods to generate optimizations of those queries which the system will store for any future users with a similar problem 
                - other solution information, like solution statistics, success probability, ratio of patterns to insights used in the solution, etc. 
                - any non-fatal errors encountered, such as missing optional information or components, or patterns/predictions made in the absence of clarity 
                - any problem space information derived during the traversal, such as identified possible/probable insights, questions, strategies, patterns, causes, etc.
            
            - function to derive problem metadata not provided, including:
                - optional filters such as the following metadata, which may also be derived if not provided:
                    - problem variables (such as agency involved in the problem, etc)
                    - optimal problem format
                    - solution metrics to filter successful solutions
                    - definition of solution success
                    - the origin interface
                    - inputs for known metadata like the problem type
                    - required solution metrics (such as a certain object structure, priorities, functionality, or attributes) 
            
                    - identifying the problem type & sub-problem types, given the most adjacent type (such as an information asymmetry, incentive conflict, unenforced rule, finding a prediction function, route optimization) 
                    - identifying the minimum information required to solve the problem (inputs like alternate attribute sets; solution requirements; constant assumptions & other dependencies), then mapping the inferred or stated assumptions describing the problem space to a multi-dimensional structure, usually bounded by assumption limit or filter conditions, & indicating possible interactions between the problem objects & the other system objects, & containing the problem object in that space (as a network or other shape indicating the problem variable interactions within the problem space structure). 
  
            - function to standardize/validate problem input 
              - receiving a problem statement & translating the problem statement into its most standardized form, using standardization methods like replacing esoteric words with more common synonyms, converting passive to active language, and removing words that don't change the meaning of the statement. 
              - checking input for validity, like if user-specified problem type matches the problem statement

            - function to graph the problem space, which includes:
              - the solution space for the origin problem (and for all related problems on the network that the solution space applies to)
              - the solution space: a reduced version of the problem shape or structure, or all changes possible in a problem space, or the set of all possible solutions, whichever is the most specific definition that can be identified
              - a problem space depicted as a set of boundaries indicating limits creating the problem space (like limited tech creates a problem space) 
                - the problem space dimensions maximizing variance between related problems - a network of related problems in the problem space & their state 
                - the origin problem occupying a position on the problem network, which can be represented differently according to the type & the solution generation method, for example: 
                - problem types have structure once they're framed as an information problem, and once concepts are converted to more structural interfaces, they also have default structural forms reflecting their definitions 

            - function to graph the problem on a network of related problems (on the same interaction layer, in the same problem space, etc) such as how the problem of building a technology is related to the problem of managing usage of & access to it
              
              - map related/approximate problems/problems (by a metric like cause or similarity) into a related problem network (like a generative vs. identification problem)
              - defining the problem space as a contextual system where the problem is active
                - this includes other problem spaces where it is or could be active
                  - for example, how the 'tech distribution' problem (where most tech is inherently neutral & can be used for good or malicious intents so what matters most is how it's distributed) acts differently in different problem spaces where distribution tools & government ethics & policies differ
            
            - function to graph a problem as a set of structures indicating boundaries (filters, conditions), limits (assumptions, resource limits), or vectors (priorities, forces), creating the problem space (like limited tech creates a problem space) , where the space inside the shape indicates potential for change
              
              - the problem object can be represented differently according to the type & the solution generation method by applying interface filters to the problem space visualization, for example: 
                  - if your problem object is represented as a 3-d shape like a cube (indicating it has three main variables expanding each other from an origin corner & forced to create a closed system to maintain state, or limits intersecting with each other), the solution would need to be in a vector format to remove dimensions of the shape or reduce the size of the problem shape 
                  - if the user is representing their problem on the information interface, they may want to represent it as an information problem type within a system context, like how: 
                    - a conflict between system incentives & agent intents could be represented as two vectors with the same origin or two vectors going in different directions 
                    - an information imbalance would look like extra information in different positions 
                    - an information asymmetry would look like information in a position where it's not needed & can be exploited to charge rent 
                    - an information market would have some trust structures embedded so information can be bought instead of derived for conveniences, similar to how concepts like delegation would look like a node sending calls to other nodes that run tasks & return response data  
            
            - function to compare & select between comparable solutions, optionally including selecting solutions based on input preferences selected (preferences like 'avoid using ML in solution', 'use a particular interface', 'use pre-computed solutions from database', etc) 
            
            - functions to select/add/remove problem dimensions  
            
            - functions to identify/reduce solution space 
            
            - function to derive trajectory between problem graphs where each graph represents a decision/state, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
            
            - function to graph solutions to the origin problem, which can be represented with formats like:
              - a subset of the problem shape (like a path answering a question, where the solution space is all possible routes between origin & destination nodes) 
              - a structure within a system containing the problem (an optimal route with a required attribute like efficiency or a route answering a question, or a combination of objects reducing variance in a rule gap, or a filter sequence that creates a function optimally while storing minimal code)
              - a structure (other than reductions) to aim for when transforming the problem and the available resources implied in its definition (a solution defined as an optimal version of the problem structure, like the optimal structure to represent a concept or build a function) 
              - a reducing transform of the problem shape (solution vectors removing problem dimensions until it's a point) 
              - a problem-solving effect may be measured based on whether a solution contains or comprises a vector that: 
                - neutralizes a problem vector , applying force in opposing direction to a problem vector (reduce an incentive)
                - reduces the problem shape size  or dimension (resolve an ambiguity)
                - fills the problem shape with relevant structures (build a function, find a route)
                - or does any combination of the above for the origin problem & related problems, potentially neutralizing the problem space itself or converting it to another problem space. 
        
            - graphing functions to visualize:    

              - the impact of solutions on the problem network or the origin problem (depending on the problem & solution format as stated above) 
              - the expansion & compression of embedded objects (such as problems, solutions, systems, concepts, and interfaces which change on other dimensions than the problem space dimensions) to the embedded graphs in the problem space using vectors 
              - alternate versions of the problem space with other attribute sets as dimensions, to isolate impact of a solution on other attributes 
              - concepts having structure in a problem space depending on the context determining that space 
                  - example of structure applied to a concept: dependence is a form of the power concept with nodes running tasks for a powerful node 
              - interfaces represented as a filter converting objects to a foundation where vector sets representing different unit core functions of change possible on that interface (where core interface functions are depicted in embedded graphs or adjacent converted graphs of a problem space, and including a function to convert other objects to combinations of the vectors in that interface's vector set 
                  - example: converting objects to the type interface involves identifying attribute sets that are unique, and then identifying types that can describe multiple unique objects as variations of an attribute in the attribute set 

            - function to apply the solution to the problem space , as shown in FIG 5 (Additional Solution Metadata)
              - applying a problem-reducing solution vector to a problem space should reduce the origin problem, and possibly other problems or the problem space itself
              - applying a 'route optimization' solution may take the form of adjusting the system structure to invalidate the route, may attach a function to nodes, or inject an efficiency structure to the system, which may also reduce the problem dimensions in the problem space visualization in addition to changing the system structure in the associated visualized system-structure interface format of the problem.
          
            - a function to apply solution metric structures to solution structures
                - return to interface selection, sequence & query design at step 403, to apply standard interface origin/sequence/queries stored, after retrieving them from the database, translating the problem to a more standard interface (like the system or function or pattern interface), if there is no next interface in the sequence/query. 
                - check if the standard interface origin/sequence/query have been applied already, and if there is also no next interface in the sequence, it may skip further traversals & return any information generated/derived/found, including the processes tried & results, to the user interaction module 110. 
                - also involve calculating some solution statistics given stored information in the database such as information about previous queries or feedback on solutions entered by user on returning to the solution output in the user interaction module (stored as its own problem output report & accessible with the user interaction module). 
                - also allow the user to download solution steps, optimize the system or the traversal (skipping unnecessary nodes & so on), examine the queries that generated the solution, review the risk contributed by each filter or pattern or other risky object depended on by the solution or solution generation process, & execute other actions on the output information. 
                - if the re-calculation function is called & determines that a re-calculation is necessary, the program may determine which step contains the functionality for that re-calculation, and returns to that step, to create a new version of the solution output sent to the user interaction module 110. For example, - the program may determine if the edit requires returning to step 402 to re-define the problem definition, step 403 to execute interface selection, sequence & query design, or step 404 to convert to the same interface or a standard interface and execute the traversal generating the solution output. 
                - if the re-calculation function is called & determines that no re-calculation is necessary, the program may adjust the solution output according to the edit, using visualization logic & output information. 
                - solutions that optimize metrics not specified by the user may be included in the output, such as solutions optimizing the user-specified solution metric and metrics that impact other problem-solvers, like the environment. For example, even if a user didn't request clean energy solutions for their traversal to find the optimal implementation of a Air Conditioning unit, the program may still return energy-conserving solutions like automatically shutting itself off when target temperature is reached, given that this energy- conserving solution optimizes more metrics than the requested solution, or that other users preferred the energy-conserving solution metric, or that the program identified energy- conserving solution metrics as conserving available resources, which would not only improve cross-system design for many agents using the program but also increase the likelihood that the program would have energy to run parallel processing or large queries or self-maintenance & self-optimization logic. 
                - after being presented with the solution 150, the user may be dissatisfied with the solution 150. In these and other embodiments, the user may modify or adjust one or more of the input filters provided to the solution automation module 140 regarding the problem/problem space/solution metadata derived and the origin interface & the formats selected for the problem-solution matching process. 
                - By iteratively repeating the process of adjusting the input filters by the user, the solution automation module 140 may repeatedly generate different solutions 150 until the user is satisfied with the solution 150. - the user may be dissatisfied with the solution based on preference the user has about their preferred optimal solution for the problem statement. In that case, they can add a filter to reduce the solution output, and if the program can find or derive the definition for that metric, it will apply it in the next query. If some metrics or formats contribute to uncertainty in the problem/solution filtering, formatting, compression, interface traversal, or other processes run by the program, the program will return output about the contribution of risky metrics to the uncertainty in the solution output. For example, if the user adds a custom filter like 'importance' and the program were to retrieve or derive an over-specific definition such as 'number of hub connections', it would cause distortions in the output, which would be included in the report as a risky filter that can be removed. Otherwise the solution may speed up the user's problem-solving process, to identify improvements to a product design, prediction function, or route with just a problem statement. 
                - FIG. 1H depicts Solution Metric 1 on the top left, which is where the agent position occupation sequence is determined. 
                - It also depicts Solution Metric 2, where the agent position occupation sequence is determined as needed with an intersection change (such as by adding a decision function to the intersection). An example solution fulfilling solution metric 2 (the Sequence decision function attached to the intersection object) is on the top right of FIG. 1H.
                - This step identifies whether the output creates information that is easily transformed into the solution metric, given the relevant objects/attributes/functions of the solution metric. Is it clear which agent goes first, or whether the intersection can be changed in a way that determines which agent goes first?
                - If the solution metric 1 is fulfilled, the agents have no antagonistic agent attribute & there is no trade-off because no variance from a decision is allowed at the intersection.
                - If the solution metric 2 is fulfilled, the intersection loses its position overlap attribute & the diverging direction attribute doesn't matter anymore, but it does have a decision function at the intersection.
                - If the intersection object with the system interface is applied can be easily transformed into having one of the solution metrics fulfilled, that transformation can be considered a possible solution.

          - function to check if solution metrics are fulfilled with applied interface object components
              - example: once the program formats the problem as a system, identifies system objects in the problem, & applies their objects/functions/attributes, it checks for a clear way to solve the problem or determines if other functionality needs to be applied. 
              - the program may run processes like identifying all the conflicts & incentives in the problem system & applying insights moving derived/generated/found information toward the minimum information to solve and/or fulfilling the solution metrics, then checking if there is a clear route or transformation that removes the problem as it was defined. 
              - example: once the intersection object has had the system interface applied, checking if 
                - it's clear from the system interface application which agent should go first, 
                - whether there is an optimization possible in the intersection that will invalidate the conflict of who goes first, 
                - whether other functionality need to be applied, such as other conflict sub-systems such as finding substitutes of a resource (like an alternate route) to invalidate a conflict of the resource competition sub-type. 
              - once the solution metadata is identified, the interface network traversal process is repeated for reducing the problem space to a solution space & then deriving, finding, matching, applying, or building a specific solution or general solution method that compresses the problem into a form that is more adjacent to its final solved form (occupying a point rather than a multi-dimensional structure in the problem space definition), where the solution method may be executed on other interfaces and is then converted to a vector or other object impacting the formatted problem on an interim interface used for calculations, and is then converted to an object impacting the original problem in the problem space structure. 
                - iterating the origin interface selection & interface traversal process for the solution space, repeating the traversal method on other interfaces, given the achieved distance from the minimum information required to solve the problem, fulfilled solution requirements, & progress in compressing the problem, where information output by each traversal may include information, interface objects, functions, or attributes compressing the problem. 
                  - if solution metrics are not fulfilled, the program may move on to next interface in sequence if there is one, and iterates as needed to execute functions like adjusting interface sequence or query, converting objects to the interface, finding similar objects between the problem & interface, applying interface objects, & checking if the solution metrics are fulfilled by that application. In some embodiments, this step may return to interface selection, sequence & query design at step 403, to apply standard interface origin/sequence/queries stored, after retrieving them from the database, translating the problem to a more standard interface (like the system or function or pattern interface), if there is no next interface in the sequence/query. In some embodiments, this step may check if the standard interface origin/sequence/query have been applied already, and if there is also no next interface in the sequence, it may skip further traversals & return any information generated/derived/found, including the processes tried & results, to the user interaction module 110. 

            - function to select the right format for the problem & solution
              - each format is better for different information, problem types/formats (with varying structure in the problem definition) & solution intents, but if you have a particular required solution format, you may need to translate a sub-optimal problem format into one associated with that solution format
              - each format involves a standard form like a set of vectors (which may represent a set of database/interface queries or insight paths, info objects like questions/insights/related problems, decisions/actions, causes/explanations, steps like removal/addition of variables, directed structures like distortions/intents, etc) which may be applicable in the interface network to retrieve/connect information, or in the problem space to reduce a problem shape, move around problem components to change the problem, or traverse a route in the problem network system (not necessarily the network of related problems, but the problem framed as requiring a solution route within a network
              - example logic of function to find alternate solution formats in FIG 11 (Finding alternate solution formats that fulfill different metrics)
                - how to identify alternative solutions that would be interchangeable with this solution in various contexts (like for different solution metrics):
                  - in other words, how to translate 'find optimal route fulfilling a metric' to an alternative interchangeable solution that makes the initial problem trivial to solve 'find system-wide cost-reduction function that makes system routes equally costly', at which point the original problem's solution is 'any route'.
                  - we are looking for ways to invalidate the problem (generate an adjacent object to act as a proxy or replacement for the solution, generate the solution automatically, change the system structure so solving the problem isnt necessary, etc) rather than generate a specific solution (like how 'trial & error navigation of all possible routes' is a specific solution)

            - a set of definitions, set of core objects, and a set of functions (converting, filtering, applying core interface functions, traversing interface network) for each interface 
            
            - a set of functions to select filters to display in the GUI, and validate input (for example, if the problem statement doesn't match problem type specified) 
            
            - a set of functions for core operations like: 
                - find (function to apply filters to a structure) 
                - build (function to assemble components given a particular definition of combine) 
                - derive (function to identify possible paths, compare them, and select one given a solution metric) 
                - change (function to apply an object, function, or attribute to another) 
                - define (function to identify & define attributes, functions, & objects (given minimal information like their position in a system or their set of attributes compared to other system objects)) 
            
            - a set of utility functions, including: 
                - a function to convert an object between formats (function => attribute sequence, function => filter sequence, etc) by mapping attributes & functions & other metadata of the objects & removing attributes that don't fit in the target format definition (for example, if the user is converting to a type, the output should be in an attribute set format) 
                - a function to identify structure matching a pattern (like identify a structure embodying a mismatch, which is a problem type, given a system network definition, where the system could represent an object, function, or attribute) 
                - a function to identify sub-components or system context of a component (a component which could be either a function, object, or attribute) 
            
            - a set of problem & solution functions 
                - a set of functions to evaluate & select between comparable solutions, including selecting solutions based on input preferences selected (avoid using ML in solution, use a particular interface, use pre-computed solutions, etc) 
                - isolate the solution space in the problem space 
                - break the problem space into sub-problems that can execute their own interface traversal & solution-matching process to find sub-solutions 
                - reduce the solution space 
                - apply the solution to the problem space 
                - a function to check if a solution reduces a problem or fulfills a solution metric 
                - a function to check if a solution fits a structure such as input assumptions & limits 
            
            - a set of specific functions for each interface, for example: 
                - intent: a function to derive intent as a dependency of the intent interface conversion function 
                - core: a set of functions to generate the set of possible combinations in an interaction space to conduct core combination analysis & identify probable important objects like an incentive would be identified as an important system object given the system filters it passes after being generated by core combination analysis) 
                - type: a function to identify the type an object belongs to, given its metadata 
                - system: a function to identify system objects given their definition, such as a variance gap (a gap in rule enforcement) 
                - concept: a function to identify concepts given their definition & a system network (either structures applies to abstract concepts - or useful combinations of objects, functions, & attributes that are causative or interfaces in a system) 

'''

'''
      - on this index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface 
      - problems can be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries) 
      - different problem types have different default problem shapes 
          - example problem type shapes: 
              - finding a prediction function can be framed as an optimal path in a network of variable nodes 
              - conflicts can be vectors with different direction or which overlap 
              - a misalignment problem has at least two vectors differing in direction, where the optimal alignment is calculatable or at least the alignment is clearly improvable 
              - a variance injection problem has a opening in a closed system 
              - an asymmetry has an uneven resource distribution 
            - if a problem has a misalignment problem and a variance injection problem, the problem shape can have both shapes in isolated analysis, or they can be merged, applied, added, mixed, intersecting, or combined in another way 
          - example solution shape for problem shape: 
            - for a misalignment problem, the solution shape would be: 
              - a vector aligning them 
              - another adjustment to the system that makes the existing misalignment a correct alignment 
              - a combination of the two 
            - for a variance injection problem, the solution shape would be: 
              - an object (resource, function, constant) to close the opening in the system 
              - an object to prevent further variance injections 
            - for an asymmetry, the solution shape would be: 
              - an optimal transport operation set to distribute the resource optimally according to the metric of symmetry 
      - this analysis involves: 
        - identifying the given problem & solution target structures in the problem space & the related problem network, so the problem & solution can be visualized 
        - identifying & anticipating problems in a system, which optionally includes identifying problem structures (inefficiencies, conflicts, etc) that exist or could emerge 
          - example: in the bio system, DNA regulation functions don't prevent pathogens from injecting DNA or mutations from occurring, so if the program derives the concept of a pathogen or mutation without already having that definition available (using core system analysis), the program could predict that the current DNA regulation functions wouldn't be able to offset the changes exacted by those concepts & the program could predict problems of DNA disregulation in the bio system before they occur 
    - functions: 
      
      - mapping function, to map objects to structures, functions, & other object types 
          - graph an object, like the example problem space visualization depicts a problem space object & problem objects of the problem space in FIG. 6
            - FIG. 6 depicts a problem space of building information technology with differentiating attributes like Resource Limits, Standard, & Priority, including problem objects indicating problems (like Finding or Derivation problems) that exist in that space & differ in those attributes.
          - graph a related object network (as shown in FIGS. 6 - 7) & other relevant objects 
            - FIGS. 6 - 7 contain a network system relating relevant problem objects. 
            Problems like info problems, pattern problems, & derivation problems are adjacent (similar) and have similar dependence structures, because they are alternatives, and act as interfaces in hte problem network.
            The resource limits, priority, and standard generating the problem space of info problems & related problems might be limited derivation technology resources, a priority to find rather than derive information, and a standard information format.
            Other variables that can determine the shape of a problem space include other interface objects (a problem generating the problem space, unanswered questions, perspectives, default structures, attributes like relevance, etc). 
            Resourcs can refer to any object potentially having value (information, technology, information-derivation protocols like science, social resources, physical resources, time, etc).
            Priorities can narrow the focus of the problems or incentivize motion in a particular direction - like a priority to acquire resources, a priority to distribute information or rights, a priority to respect existing laws, etc)
            A standard applied to the problem space can mean a format, a particular definition of a concept like similarity, or a reducing function that isolates particular attributes, like how cause narrows the focus to dependency relationships, inputs & outputs.
                
          - function to apply an object to another object, as shown in FIG. 5 (Structure Application Function - Apply Function) 
            - example: applying a 'route optimization' solution may take the form of adjusting the system structure to invalidate the route, may attach a function to nodes, or inject an efficiency structure to the system, which may also reduce the problem dimensions in the problem space visualization in addition to changing the system structure in the associated visualized system-structure interface format of the problem. 
            
            - FIG. 5 depicts the application of a solution to a problem space (standardized to the problem interface) in the top left, specifically the solution of adding an efficiency to the system, which reduces the problem dimensions (like resource limits), leading to smaller problem objects & decreased distance between problem objects.
            - It also depicts the application of a solution to the problem-containing system format (standardized to the system interface) in the top right, specifically the solution of adding an efficiency (like an alternate charging station in between nodes, or a position-switching function to each node) to the system, which removes the need for an optimized route between A & C.
            - Below these two examples, on the bottom half of FIG. 5, the figure depicts an example of applying the structural definition of an information function to information. This solution applies the structural definition of the Allocation function (in which information is distributed to other system positions), to the Input Info Distribution structure, to produce the Allocated Info Distribution structures. 
            - The Allocated Info Distribution structures are structures of examples of two solutions: Solution 1 applies the 'allocate' function to both information resources, and Solution 2 applies the 'allocate' function to unique information resource.
            
          - each format is better for different information, problem types/formats (with varying structure in the problem definition) & solution intents, but if the user has a particular required solution format, they may need to translate a sub-optimal problem format into one associated with that solution format 
          - each format involves a standard form like a set of vectors (which may represent a set of database/interface queries or insight paths, info objects like questions/insights/related problems, decisions/actions, causes/explanations, steps like removal/addition of variables, directed structures like distortions/intents, etc) which may be applicable in the interface network to retrieve/connect information, or in the problem space to reduce a problem shape, move around problem components to change the problem, or traverse a route in the problem network system (not necessarily the network of related problems, but the problem framed as requiring a solution route within a network) 
          
          - functions to match & select a problem-solution connecting format trajectory 
          - break the problem space into sub-problems, that can execute their own interface traversal & solution-matching process to find sub-solutions  
          - find a structure to combine solutions & combine sub-solutions to create the origin problem's solution, once the sub-solutions to sub-problems are found 
          - example logic of function to break a problem into sub-problems, shown in FIG. 12 (Network of problem sub-problems, breaking a problem into component problems) 
            
            - this logic includes functions to decompose/aggregate problems/solutions (as shown in FIG. 12, Network of problem sub-problems, breaking a problem into component problems) 
                1. decompose a problem into sub-problems
                2. solve sub-problems after the decomposition
                3. identify structures to combine sub-solutions
                4. apply structures to combine solutions & test combined solution output
            - The initial split of sub-problems is indicated in the boxes under the original problem statement, which is 'find a prediction function for a data set'. 
            - The subsequent splits of sub-problems are indicated with the connecting operations creating the splits in between the shapes inside the sub-problem boxes.
            - The bottom half of FIG. 12 indicates a logical solution aggregation structure, which depicts the logical method of aggregating sub-problem solutions into an origin problem solution, formatted as a directed network.
            - The sub-problem aggregating network on the left of the bottom half of FIG. 12 begins to resemble a sub-problem solution aggregating network on the right, with solution details such as requirements, queries, & operations applied.
            - This solution-aggregation structure can be applied to sub-solutions (like by positioning causative sub-solutions before filtering sub-solutions), given the logic establishing precedence (logic derivable with iother interface objects, like using logic interface analysis indicating that requirements establish sequence of conditions, or causal interface analysis indicating that inputs establish direction of causation, since filters can be applied on info, so info is required to use the filter). Because causal structure & generator functions (core functions, variable/component combination functions, base-distortion functions, etc) are alternate solution formats of the origin problem, they can be merged & the output solution can be filtered for success solving the origin problem, 'find prediction function for data set'. 
            - These sub-solutions can be organized by dependence (causal interface) or requirement (logic interface). The causal structures & generator functions can link the data set to an output function format. The function format produced by the causal structures (such as linking variables in a causal network to generate the prediction function) & function generators (such as an average base with distortion functions generating the prediction function) is an input format to the compare function that compares alternative solutions (prediction functions). Applying structure to combine sub-solutions can also be done with analysis from other interfaces (insights like 'connect formats by adjacent structures' or patterns like 'reduce complexity with standardization' or intents like 'find a sequence of solution formats matching this intent sequence').
            
            1. decompose a problem into sub-problems, using core functions like alternate/meta/find applied to problem objects (like how measurement is a core object of a solution, and the prediction function is the default solution object, and a variable is a sub-component object of the prediction function, and so on) 
              - an example is breaking a problem into a problem of finding core components & arranging them in a way that passes filters formed by its solution requirements 
                - a requirement of a function that follows another is a possible match of input/output, if the functions are dependent, rather than relatively independent functions (occupying different function sequences), thereby translating a requirement to a filter that can be used to reduce the solution space to only function sequences that have matching inputs/outputs. 
            2. solve sub-problems after the decomposition 
            3. identify structures (like a sequence containing combination operations, or other combination structures like an unordered set, or filters) to combine solutions 
              After sub-problems have individual solutions, the user needs a way to integrate the sub-solutions so they can solve the original problem 
              - for example, once the problem is broken into a set of filter structures to reduce the solution space, the user needs a way to arrange those filters so their output generates the solution (so that the input/output of the filters match, & the sequence of filters makes progress toward reducing the solution space). 
              - the positions of each sub-problem set can be derived using logical positioning. A generative set should be followed by a measurement set because the output of the generative set (prediction function generated) matches the input of the measurement set (prediction function to measure); this involves a basic input-output chaining operation as mentioned before. A causal set may identify missing information in a variable set to establish cause between variables - that type of structure (missing information) should be followed either by generating the missing information, and if not generatable, should be integrated into the accuracy/confidence/error metrics, as not being able to find the information required to solve the problem (creating an accurate, robust prediction function). 
            4. apply structures to combine solutions & test combined solution output 
              - function to convert/represent objects (like a system/decisions/problem/solution) as a particular format (like a set of vector trajectories across interfaces, or a function) 
              - function to check if a structure (like a solution) fits/matches another structure (like input assumptions & limits or a solution metric) 
              - checking if a solution matches a metric structure is shown in FIG. 11 (Finding alternate solution formats that fulfill different metrics) 
              
              - FIG. 10 depicts an example of object structure application, by applying a function to a structure containing an object to find specific object structures for that object).
                - Specifically, FIG. 10 depicts an example of applying a solution function (like 'apply definitions of objects') to a structure (like a system or network) containing the problem ('optimize a route'), to find specific solution structures for that problem (like specific functions or routes).
                - As an example, FIG. 10 depicts a route optimization problem structure, to optimize a route from nodes S to E in a system network.
                - The first step in applying one structure to find another is finding & standardizing definitions.
                - The FIG. 10 includes a route optimization problem definition, an efficiency definition, and a cost definition, which can be retrieved from a data store or otherwise found/derived/generated.
                - The default problem structure (for the route optimization problem) can have many solution formats, which apply the definition of efficiency (like resource re-use) and the solution metric (cost-reduction and benefit-maximization to reach the end point from the starting point) to network structures (like paths & nodes), given that the default problem format is in a network structure.
                - Standardize definitions: focusing on the cost-minimizing definition, and the structural definitions of cost, we can standardize definitions to arrive at a structural definition of efficiency by applying the structural cost definitions:
                    - minimizing cost:
                        - minimizing number of steps
                        - minimizing complexity of step
                        - minimizing distance of step
                        - maximizing certainty of step (uncertainty is high-cost)
                        - selecting for necessity of step (only select required steps)
                        - maximizing reuse of step
                        - maximizing abstraction of step (unless abstraction adds steps like queries)
                - Apply definitions to find matching structures: as an example of applying the object definitions to translate the problem into a solution, now that we have a structural definition of efficiency, we can translate the problem from 'find a route between start & end points fulfilling a metric the most' to a problem of 'add efficiencies until cost is reduced'.
                    - Translating the new problem to add more structure (making it more specific & executable) means changing variables like:
                        - scope of cost (whether it reduces all costs or just a certain type of cost or just a cost on a particular route)
                        - type of cost
                        - type of metric calculation (how to calculate cost, cost definition, etc)
                        - type of efficiency (applying structural definitions of efficiency to the network structure, like route invalidation (position start & end in adjacent positions), cost distribution (routes are equally costly), cost reduction (path-shortening, system organization), cost invalidation (routes are equally costly), etc)
                        - logical & causal position of solution (create a cost-reduction generator or reduce costs for just this system)
                        - whether to re-calculate optimized route at each application of additional efficiencies
              
              - function to compare & select between comparable solutions, optionally including selecting solutions based on input preferences selected (preferences like 'avoid using ML in solution', 'use a particular interface', 'use pre-computed solutions from database', etc) 
              - functions to select/add/remove problem dimensions  
              - functions to identify/reduce solution space 

        - An example problem-solving automation workflow for a problem like 'find an optimal implementation of an intersection' (shown in application 16887411 Figs. 1F - 1I),  
          using the system/structure/concept interfaces. 
          1. Problem definition: determine possible match between the problem system intersection object and the system conflict object. 
          2. Standardize the problem to the system interface 
            - Apply the context of the default interaction defined for the intersection (agents crossing the intersection) 
            - Apply structures of possible matching objects in the system interface to the problem object, by applying the structure interface: 
            - components capable of interacting (they have a nonzero interaction space) can be formatted as a network 
            - the position overlap is an example of a tradeoff, so the 'subset' structure is applied) - this can be applied iteratively to check for structures that can be organized/optimized 
            - the antagonistic agent & diverging direction components are merged with the agent component, where the diverging direction structure is applied directly and the antagonistic agent component is implied by their mutual approach of the intersection 
            - the ambiguity system object is inferred by the match of the ambiguity 'unenforced rule' definition route, which matches the 'agent traversal sequence' intersection interaction attribute. 
            - Now the intersection's default interaction (agents looking to cross) is formatted as a network, and system objects like conflict (and its sub-components, patterns, objects, etc) have been matched & applied to the intersection interaction network. 
            - This is a structure of a problem type - 'find traversal sequence conflict resolution rule' - and given that it matches a known problem type 'resolve resource competition', it's likelier to be possible. 
            - The traversal sequence rule can be found by applying other agent & intersection attributes, looking for system & other interface objects like: 
            - irreversible changes (in case one agent will change the intersection in a way that prevents other people from traversing it, like burning a bridge) 
            - intents that are higher priority 
            - intent alignments (both agents have an incentive to apply social norms to maintain rule of law or trust, so their intents can be aligned to follow social rules to determine who traverses first, rather than building new rules to determine this). 
          3. This step identifies whether the output of the previous step creates information that is easily transformed into the solution metric, given the relevant objects/attributes/functions of the solution metric. Is it clear which agent goes first, or whether the intersection can be changed in a way that determines which agent goes first? 
            - If the solution metric 1 is fulfilled, the agents have no antagonistic agent attribute & there is no trade-off because no variance from a decision is allowed at the intersection. 
            - If the solution metric 2 is fulfilled, the intersection loses its position overlap attribute & the diverging direction attribute doesn't matter anymore, but it does have a decision function at the intersection. 
            - If the intersection object with the system interface is applied can be easily transformed into having one of the solution metrics fulfilled, that transformation can be considered a possible solution. 
    - objects (problem, solution, problem/solution space/network) 
    - structures: 
      - problem-solution formats (shown in FIG. 9 (Problem formats, with matching solution formats) & FIG. 10 (Problem-solution structure matching)) 
        - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system 
        - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape 
        - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc) 
          - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent) 
        - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function 
        - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information) 
        - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems) 
    - concepts (anomaly, outlier, conflict, inefficiency, mismatch, inequality) 
    - attributes: 
      - number of problem-causing variables/solution metrics fulfilled 
      - complexity: (number of core function steps required, variables, differences/inefficiencies, counterintuitive steps (requiring non-standard solutions), contrary processes (requiring scoped/nuanced solutions)) 
      - abstraction (does it solve the same problem when framed on an abstraction layer above) 
      - number of steps required to create problem from stable system base state, once work is standardized, & adjacence of steps required 
      - how much work is required to convert to a particular problem format (route, combination, composition) 
      - structure of problem types causing or forming the problem (number/position of information asymmetries, resource limits) 
      - structure of information objects in the problem (decision points, variance sources, unanswerable questions of the problem, the structure of causes generating the problem if known) 
      - type/intent ranges/direction (of individual objects or composite stack) 
      - similarity (how similar to a standard problem type, or how near to limits within a type dimension) 
      - ratio of positive to negative outputs (problems solved vs. caused) 
      - inevitability vs. agency of problem cause 
      - agency involved in the problem 
      - problem types
        
        - FIG. 8 contains examples of problem types & associated example structures.
        - On the left of FIG. 8, structures for core problem types standardized to various formats are depicted.
        - An example Info Asymmetry problem structure is depicted in FIG. 8, which is an imbalance in information (when depicted in an information format) or position (when depicted in a system format).
        - An example Intersection problem structure is depicted in FIG. 8, which indicates a problematic intersection, like vectors that shouldn't interact.
        - An example Conflict problem structure is depicted in FIG. 8, which indicates a conflict structure, such as the problem of selecting between alternatives, or the problem of conflicting vector like intents
        - An example Independence problem structure is depicted in FIG. 8, which indicates an independence structure, such as orthogonal directions of change.
        - An example Dependence problem structure is depicted in FIG. 8, which indicates an example dependence structure, such as where one attribute is determined by another which is used as a standard.
        - An example Inequality problem structure is depicted in FIG. 8, which indicates an example inequality/mismatch structure between a solution (like a square shape) and a solution format (like a circle format).
        - An example Information Inequality problem structure is depicted in FIG. 8, which indicates an example structure of an inequality of information, when formatted on the structural-information interface, rather than being formatted on a structural interface one layer of abstraction above it.
        - An example Extra Dimension problem structure is depicted in FIG. 8, which indicates the structure of extra dimension added by integrating a circle across a vertical dimension.
        - An example False Limit problem structure is depicted in FIG. 8, which indicates an example structure of a limit, such as a corner organizing change in a direction.
        - On the right of FIG. 8, structures of problem types that may be generated with (operations like 'combine') are depicted.
        - An example Organization problem structure is depicted in FIG. 8, which indicates an example organization structure, such as finding the right interaction layer to frame an interaction on, or resolving a mismatch/misalignment/imbalance is an organization problem space, where there are clear optimal structures for a certain interaction.
        - An example Inefficiency problem structure is depicted in FIG. 8, which indicates an example inefficiency structure, such as navigating up an abstraction layer when there's no reason to do so.
        - An example False Assumption problem structure is depicted in FIG. 8, which indicates an example false assumption structure, such as starting from the wrong starting point, or assuming there is a required starting point, or using over/under-restrictive limits.
        - An example False Similarity problem structure is depicted in FIG. 8, which indicates an example false similarity structure, such as similar shapes that can develop with independent causes & contextual impact (for example, the appearance & behavior of a square between circles vs. an actual square).
        
        - dependency/fragility 
        - mismatches 
        - conflicts 
          - intersection/collision 
          - comparison 
          - coordination 
          - competition 
          - conflicting direction/misalignment 
          - incentives/intents 
          - expectations/potential 
          - requirements/enforcement 
          - intent mismatch, like an unintended use (involves integrated third party tech not under review), like unintended side effects: whether it's a closed system or leaks variance (example: pre-computation, memory access, or process re-start event) 
          - misidentification  
          - incorrect structure (metric, information position, or organization/format) 
        - imbalances/inequalities (misdistribution of resources) 
        - inefficiencies (unmaximized benefit/cost ratio, such as unnecessary complexity/work) 
        - gaps 
          - missing information 
          - ambiguity (example: ambiguous alternatives) 
          - gap in rule enforcement 
          - gap in boundary (example: leaks (variance, resource/info), and injection points (assumptions/variance/control/randomness)) 
        - limits, such as enforced rules, or limited resources/functions 
    - related objects: 
      - questions 
        - questions answered: this analysis definition answers questions like: 
          - what are the problems (inefficiencies, conflicts, mismatches) in this system 
          - what solutions are associated with this problem type 
          - what problems are related to this problem 
          - what problems will develop in this problem space system 
          - what is the probable cost of solving this problem 
          - what is the adjacent format of this problem 
'''