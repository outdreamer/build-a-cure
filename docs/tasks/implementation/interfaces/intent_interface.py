'''
  - definition: 
    - intent can be defined as possible reasons to use a function (or use an object as a function): 
      - possible outputs (optionally including the explicit intended output, resource access/usage like memory retrieval, object lock, routing information to a function while it's being looked for elsewhere, or processing usage, and side effects) 
      - explicit intents ('calculate x') 
      - implied intents (the implication of an intent like 'calculate x' is to 'use the output of that calculation to make another decision') 
      - embedded intents (implementing a function optimally has an embedded intent of 'optimize this function') 
      - injectable intents (intents that can be injected into a range of functions, like the 'use processing power' intent can be injected into any function) 
  
  - attributes (implication, directness, alignment) 
    
    - intent types:

      - abstract intent:
        - filter
      - abstract intent stack:
        - filter 
          - filter by delimiter if input is a string
          - remove delimiter if split is followed by join (non-standard use of split function)
        - organize (into subsets)
        - isolate (examine one subset at a time)
        - assign/derive position attribute (position has meaning in the input sequence)
        - optimize search (find the meaning within a positioned subset, beyond derivable position meaning)
      - side effect intents are not equivalent to the direct/intended intent of the function, though they can be required sub-steps in creating the function output
      - side effect stack:
        - remove delimiter/filter from string
        - create groups of characters
        - change memory storage/access (string to list)
        - change interface (string functions to list functions)
      - intended/supported/expected:
        - the intended use is that which should be supported by the item, at the supported level of abstraction, and including the network of supported use cases
      - direct:
        - obvious uses of a particular item like 'splitting a list of characters' is an obvious use of the split sequence function
      - indirect:
        - non-obvious uses of a particular item
          - alteration allowed by super type (sequence): 
            - if the split function implementation has support for attempting to convert inputs to a sequence of characters (if a character sequence is its only supported type) before throwing an error, then a sequence of bytes or character encodings could theoretically be input to the function
          - use of function side effect (removal of delimiter):
            - if the split function is followed by a join, it may used to remove the delimiter or replace the original delimiter with the new delimiter input to the join function
          - use of function side effect & lack of validation (organization):
            - if the split function doesnt check its requirements (string data type of input, sequence attributes/methods of input) there's more room for indirect intents
              - if a set, tuple, or list can be split by the function, then the function can be used as an organization or division method, creating sub-tuples, sub-sets, and sub-lists
              - that intent could be used for other intents not typically associated with the split function, such as optimizing search of a data structure (searching subsets rather than entire sequence)
              - the lack of enforcement of data type creates a variance gap, allowing variance to be:
                - exploited (alter data type to trigger bug)
                  - variance exploit is internal to the function & only supports malicious intents
                - injected (use function for clearly unintended functionality, like optimizing search of some object)
                  - variance injection uses function for other intents that cant be fully derived from the function itself, which are a system-level exploit
      - underivable (unless system allows one unique abstract path, which is uncommon in a changing system)
        - once you derive the limit of the possible intents of a function (like optimizing search by splitting some group into subsets), deriving intents beyond that may not be derivable
        - the reason is that this outer layer of possible derivable intents is abstract, and abstract intents fit many problem types
        - what could they be optimizing the search of? any type of content:
          - the optimal function for an encryption algorithm with a particular intent stack
          - the password for a user given their decision history
          - a keyword in a document
        - however you do know some things about their possible intents despite the abstraction layer:
          - the object must be difficult to find 
            - very similar to other objects, of which there are many
            - hard to guess given the usual amount of information known about the object when finding it becomes necessary
            - unfindable with existing filters so that search of it must be optimized
            - the space to search must be disorganized (not organized by the identifying attributes of the object to find)
              - math functions may use only two dimensions, but searching along these dimensions is costly
              - to find functions of a type (where the type is not clearly defined but its clear when a function is not a member of that type), you need efficient filters to reduce the search space
              - for example, filters for encryption functions can include:
                - narrow identifying attributes (clearly that type)
                  - repetition (repeated convergence of values at an interval, like a wave function)
                  - symmetry:
                    - symmetry in variance:
                      - ambiguity (not clear which parameter path was taken to generate a value using other parameters)
                      - lack of clarity in definition of object 
                        (not a clearly determined & therefore simple shape like a circle, with so few direct parameters (2, radius & origin) that it doesnt allow much ambiguity)
                - wide dis-identifying attributes (clearly not that type)
                  - functions with parameters having 1:1 or other simple relationship types
                    - linear functions
                - space-reduction patterns (clearly or clearly not in this section)
                  - non-linearity + ambiguity means circles, waves & circle/wave-adjacent shapes will be relevant to find these functions, 
                    so non-circular shapes can be ignored for finding this particular subset of encryption functions
                  - this is because given the symmetries, there are many ways to calculate target parameters of a circle using other information about it
                    - if you know the radius & origin, you can calculate the circle
                    - if you know the ratio of the circle compared to the unit circle, you can calculate the circle
                    - if you know the square parameters containing the circle with 4 intersection points, you can calculate the circle
                    - the circle is easily determined by its direct parameters bc of the clarity of its definition, but the derivation of other methods that could be used to calculate the circle is the set of alternative paths that are not directly calculatable
                - base or adjacent functions (and their identifying attributes/rules) to the target function type
                  - prime-finding function (adds uniqueness to the equation)
          - the object must be important
            - this implies the object is newly identified as important, like a new prediction signal
          - from there you can derive other intents given these filters
            - youre looking for a difficult to find object that escapes existing filters which is important, like:
              - a prediction signal
              - a search method
              - an encryption function

  - objects (priorities: abstract directions that intents may fulfill or move agents toward, whereas intents are more granular) 
  - concepts (applicability: what a function can be used for) 
  - functions: 
    - allow combination of intents to find malicious intent structures (like a sequence of neutral-intent functions that has an emergent malicious intent when used in that sequence) 
    - operate on intents (intent-modification intent) 
    - derive intent as a dependency of the intent interface conversion function  
    - map intent to direction & assess solution progress by movement in that direction 
    - mapping intent to structure & vice versa is shown in FIG. 18 (Intent-matching) 
        - Fig. 18 depicts examples of matching operations between intent & structure.
        - In the 'Mapping Structure to Intent' section on the top left of Fig. 18, mapping intent to direction is depicted in a system as allowing the identification of different intents, given the general intent of the direction.
        - In the 'Identifying side effects of Intents' section on the top right of Fig. 18, an example of deriving intents in a system - intents that have side effects - is depicted.
            - The system limits may force someone prioritizing a priority to move in certain directions that they ordinarily would not if left to make their own decisions in a vacuum. 
            - They start from a selfish priority, moving in the direction of being uncriticizable and building functions to enable that intent, and by the system they're operating in, they're forced to move in other directions (making a gesture of charity, copying agent with priority of improving functionality of other nodes), while still having the same intent.
            - The agent prioritizing that priorit will have pivot/angle/rotation functions/concepts, and their decisions will be buildable with those functions. The agent prioritizing improving other nodes' functionality will have cooperation, sharing, problem-solving functions and their decisions will be buildable with those functions.
            - This is an example of how different intents can not only have the same output (arriving at the same end node), but a similar/overlapping trajectory at various points, while still leaving traces of different intents in their side effects (traces such as functionality developed to serve different intents, at different stages of development).
        - In the 'Intents mapped to structure' section on the bottom half of Fig. 18, examples of structural input intents are depicted on the left, which can adjacently support example structural output intents on the right.
        - For example:
            - Intent 1A (Unenforced equal growth) and intent 1B (Enforced equal growth) may support intents like intent 1C (See which entity gets to the corner first) and intent 1D (Create the emergent entities).
            - Intent 2A (Inject variance in growth inputs) and intent 2B (Inject variance in growth inputs) may support intents like intent 2C (Create field of potential for emergent entities to grow, either within an existing or new boundary) and intent 2D (Create interaction space on emergent entity layer).
            - Intent 3A (Inject variance in state (position after a process)) and intent 3B (Incentive to move toward corners decreases, leading eventually to corner erosion) may support intents like intent 3C (Create temporary interaction layer as needed to resolve question of which entities emerge or create their functions, then dissolve it by switching their positions).
            - Intent 4A (Create evenly distributed growth incentives once corner objects & functions develop) and intent 4B (Remove square boundary & let all functions & objects develop new interaction patterns in outer circle) may support intents like intent 4C (Developing new layer functionality) and 4D (Apply a standardizing, transforming, or reducing filter (square boundary) to a system).
    
    - function to select priorities/metrics
      - something that not everyone has the potential to be (non-structural) is more valuable if it optimizes some metric
      - reductiveness: the lowest/simplest structure that complies with a metric (reductive choice like a parasite) also reduces potential, whereas the highest structure that complies with a metric (empowering choice like a mammal) increases potential
      - evaluating the potential of lower life forms is less optimal than fixing them, so the metric becomes whether you fixed/empowered them or reduced them, bc they cant fix themselves
      - the metric is whether you got the point (empowering, fixing, making other life forms complex), not whether a lower life form can become complex
      - potential is an important metric bc more complex life forms are supposed to have the potential to be complex, so its more wrong for them (like a puppy or human) to not optimize a complexity metric than it is for a simpler life form with less potential (parasite)
      - some metrics will be alignment with priorities rather than reaching a threshold value

    - function to match intent-structure

      - example: data viz can be automated using:
        - lie core function layer graph or individual lie type graphs, with an output intent layer (hide information, layer information, minimize information, obfuscate information)
        - intent-structure maps (this graph structure serves this intent stack, just like a function serves an intent stack)

      - example: data structures:
        - what kind of data structure would look like the original sequence from one angle, but look like its metadata (like the ordered sequence, or average value statistics) from another angle?
          - is the extra storage of a tree, network, or other structure with more than one dimension worth the computation gains
        - is the best storage format of a list where position would be checked later in code a map retaining order, with keys as ordered values & values as positions in original sequence (in case original position is significant and youre not just trying to find if the value is in the sequence)

      - example: map position (a state structure) to variable structures like networks/loops/trees (like how rank assigns standardized relative position to values - how would you assign a position to nodes in a network in a similarly standardized way - an attribute like connection count or node type, or a trajectory position, or another method)
        - how do rankings map to ratios, and what errors would result from direct mappings of various initial data types?
        - is there a standard set of structures like networks that should be applied to a sequence to get its probable prediction function the fastest (framing numbers as 1, a map from number type to node types, 2, a node's connection count, & 3, distance between nodes, in order to map the sequence in the most robust way)

      - program should be able to identify, predict, & finally calculate structures that will be useful for an intent, to avoid reducing/searching a solution set
        - identify with structure-matching (which of these structures can fulfill this goal)
          - example: finding a 'progression' structure for a function
        - predict with intent-matching (find structures matching these intents)
          - example: for calculating area, which structures fulfill that intent
        - calculate with intent structures (derive intent-structure relationships and find operation sequence that will produce target intents)
          - example: 
            - which structures simplify difference calculations (like area) extending the addition/core/unit operation (like how multiply is an extension of add) when increasing a parameter like number of dimensions, given that 
              - the add operation has a 'combine value' intent
              - multiply has a 'combine value with different direction' or 'describe interaction space' or 'find intersection area of limits' intent
              - length has a 'describe difference' intent for a dimension count of 1
              - and so on for other operations
            - the addition operation has an associated structure 'align with overflow in left direction' because inherent to the definition of values in their standard western depiction, higher digits are on the left, and the extra value from an operation like 8 + 3 (10) would overflow into the next digit because thats a unit of change that can be registered in the next digit's column, with no more than one digit to the left being able to register the excess change from addition two digits in a particular column (greatest value being 10, by adding 9 + 9)
              
            - tests:
              - this is a good unit test for whether your program can generate math methods by applying structure:
                - if the program can identify:
                  - 'column as a digit store' (given that existing numbers use columns as a digit store, which could also be done with rows after converting numbers to row format)
                  - 'alignment of digits'
                  - 'adding digits in the same aligned column'
                  - 'overflow extra value to the left'
                  as concepts & operations that would respect inherent digit definitions/rules while executing the addition operation, and design the addition operation itself, that would be a successful basic test

                - an example trajectory using the interim objects:
                  - insight paths:
                    - 'compare relevant objects'
                    - 'compare standardized objects'
                      - identifying the 'position' attribute as an input to the 'compare standardized objects' insight path (or identifying the 'comparison standard' object or 'standard as a required input for comparison' in the 'compare' definition route) which produces an input to the alignment process, as alignment is a process that should happen between similar objects (such as objects that have been standardized for comparison)
                    - 'apply sequence to operations based on which operations enable other operations'
                    - 'handle extreme cases'

                  to generate the addition method would be:

                  - 'compare relevant objects'
                    - 'relevance = similarity on an interaction layer'
                      - 'compare objects that interact'
                        - 'digits in the same position (distance from right) interact'
                          - 'apply a standard that aligns objects that interact (digits), to compare digit object values'
                  - 'execute the add operation after digits are aligned, for relevant comparisons' (this operation is enabled by the previous operations, which is why it comes after them)
                  - 'handle extreme cases, where value cannot be described by the digit value range'
                    - 'extra values of addition operation need to be routed to other digits'
                      - 'adjacent digits interact'
                        - 'extra values need to be routed to adjacent digits'
                          - 'adjacent left digits can hold extra values' (increasing from 9 to 10 moves value left)
                            - 'extra values need to be routed to adjacent left digit'
                              - 'add from right to left'
                  - 'apply a default operation mode, limit to unit operation, or fulfill "isolatable operation" requirement':
                    - 'add one pair of aligned digits at a time' so impact of each operation can be assessed & routed

              - other default operations, like multiplication (2 x 25) identifying 'multiply digits in one number (20, 5) by each digits in the other number (2) and add the output of each multiplication (40 + 10)' as a standard rule to execute multiplication operation, with a multiplication definition that doesnt include those rules, such as:
                - 'find the area of the space bordered by the limits generated by lower x bound = 0, upper x bound = x value, lower y bound = 0, upper y bound = y value'
                - 'add the x-value y times'
                - 'find an adjacent more calculatable or pre-computed value & subtract the difference'
                - lattice multiplication
                multiplication operation definitions which are also alternate outputs of the 'generate a multiplication method' query

              - 'find a structure where calculating the output of numbers multiplied by themselves (exponents) is a set of addition operations' (log function)

              - 'find the unit object of nonlinearity' which should have:
                - info output: x ^ 2
                - structural output: variable ^ (next value other than 1)
                - conceptual output: 'compounding change', 'multi-dimensional (multiplicative) change' (change of variable, and change of a dimension)

              - the program would integrate intent relationships like:
                - 'a unit change in this direction has x impact on change in other directions, and a change of degree n toward other change types & states'
                  - which would help predict what impact a change would have on change metrics, which are also calculatable from other change types/states, such as estimating the impact on area from a unit change in one direction (of various change types, including a unit addition/multiplication/parameter change, etc), and include the impact on difference from related change types (impact on tangents, inflection points, subsets, and related objects), and related change states (difference from adjacent functions like with one-off parameters (constants/exponents one degree away)
                  - where the intents are structural by default ('multiply by this constant' having intents like 'increase the scale of this function from the unit version, keeping this maximum as a center or this point as an origin')

    - function to select components for an intent (function, pattern, metrics/threshold values)
      - network design favors an adjacency definition that differentiates features
        - to get around this, build in a concept of default core objects like boundaries/limits/intersections to the network structure or data propagation (send data on possible boundary line positions) to look for & focus on those first rather than continuous sets of adjacent high-variance, pattern-containing features
        - why would patterns like textures make it through as a semantic filter - bc the repetition is interpreted as significant by network design, or the texture is likely to be located in more data subsets than a shape
        https://www.quantamagazine.org/where-we-see-shapes-ai-sees-textures-20190701/

    - required functions for each intent:
      - intent-derivation function (whats the probable intent stack/network of a particular event)
      - intent-metadata function (does this intent have side effects or is it granular/neutral)
      - intent-combination function
      - intent-similarity evaluation function

    - required functions for system intent analysis:
      - intent-pattern matching
      - identify gaps in rule enforcement in system
      - identify gaps in information about rule enforcement in system
      - identify gaps in computational possibility about intent 
        (some intents may not be computable, some components may not be predictably interactable until tested or more info is injected)
    

  - structures: 
    - intent matrix is the interaction space of a set of intents, where its emergent intents can be traced across the interaction space 
    - intent stack is the set of adjacent intents of a function, from granular/neutral/abstract to specific/explicit, across various interfaces like logic, abstraction, & structure 
  
    - methods to model intent:
      - network of nodes where each node represents a state & connections are functions transforming one state to another
      - network of system component nodes where direction indicates intent
      - network of variable nodes where sets of node combinations (and their transformation trajectories) achieves an intent
      - model intent as a gap in a structure (missing corner on a triangle) that needs to be supplied with a path or other structure to be considered 'complete' (or the opposite problem of an external structure that needs to be reduced in order to be considered 'closed')

  - related objects

    - related questions: 
      - find specific implementations of a general intent like 'optimization', such as a specific intent of 'optimizing the metric in question'
      - which intents should follow or be combined with which intents 
      - which intents are likelier, given the context implications of the function 
      - which intents are missing, given an overall function intent 
      - which intents do the optimized/simplest/reusable function versions fulfill 
      - intent-logic interface question: which intents align with logical objects (assumptions, conclusions) 
      - intent-system interface question: which intents are common to all functions in the system 
      - intent-function interface questions: 
        - which functions are most exploitable for malicious/neutral intents 
        - which functions' explicit intents don't match their implicit intents (or emergent intents when combined with other functions), which is like analyzing the structural difference between developer expectation vs. user intention 
      - do variable, type, logical, & output intents match overall given function intent 
      - what is the logical sequence that best fulfills this intent (useful for automating code generation) 
        - what is the function linking these variables, given the variable intents a, b, c and the combination intent matrix ab, bc, ca, and the possible output intents of that matrix, and similarity to output intent of y 
      - what intents/directions/priorities does this path align with or could be built from? 

      - intent-matching applications:
        - function chaining for target intent
        - testing
        - finding exploit opportunities
        - predicting output intents of object combinations
           - example: predicting industry tech combinations:
            - risk analysis (finance, insurance)
            - science
            - statistics
            - machine learning
            - information tech
            - quantum
            - computing
          - when these combinations have been exhausted with normal methods of value creation (automation, standardization, combination, platform, search, metadata), 
            there will be a phase shift in the direction of the variance/vulnerabilities of the last combination 
          - can you derive the order each component combination will happen in?
          - the main concern is whether there will be safeguards to control the last combination's potential exploits, or whether any safeguards will be invalidated by prior tools

  - examples:

    - example of queries to find opportunities to position an intent like 'phishing attempt'

      - finding legitimate relationship structures on an interface, such as other relevant intent types:

        - prior intents like 'receving legitimate email triggering risk-aversion process involving a step containing a link click' to target intent of 'clicking link'
        - related intents like 'permuting assumption or variable like authentication status that would trigger a related process, in the form of sending email about related process with a step containing a link click that wasnt triggered like disabling account authentication'
        - required/important intents like 'maintaining account security' or 'avoiding risk' or 'minimizing risk' 
          ('if my account was hacked and someone disabled auth, I need to fix it right away')
        
      - finding rule enforcement gaps, like required priority-switching triggers, such as:

        - where priorities such as 'rule enforcement' are ranked lower than other priorities, like 'speed', such as when handling a high volume of emails
        - where intents are over-prioritized, intents like 'contradicting lies', which could trigger a priority switch
          ('no, I did not disable account authentication')

      - whats the query that could generate both examples of exploit opportunities to inject this malicious intent?
        - find causes (triggers, sequences) of change types (switching, change sequence) of core interface structures (relating/connecting functions, requirements, rule gaps, rule enforcement gaps)
      
      - whats the query that could generate the generative query?
        - find structures (causes) on a generative interface (cause) of generalized (apply pattern, core, or abstract interface) core structures (types) a high-variation interface (change) of core interface structures

    - example intent implementation for a priority like 'security'
      - accessing a particular site by stating intent, where intents are mapped to a static network/route/server set, so that content cant be replaced with malicious content
        - a browser accepting a request for a site can only deliver values specified in the intent map for that site key
        - keys in the map represent partitioned content
          - requested intents like 'whatsapp.myuserid' can only deliver content from the values associated with the key path map['whatsapp']['myuserid'] (server/database/network/content values)
        - the integrity of the universal intent map as a source of truth/legitimacy/trust is the main point where requests/responses can be compromised, and if its enforced by lack of editing ability & verified with local copies, it cant be compromised
        - edits to the intent map are supported by continuous & coordinated 'voting' as legitimate mappings, so new request intents can be supported, with increasing degree of readonly capacity as the new intent entry is more confirmed by votes
        - paths (IP addresses, usernames/handles/email addresses, paths in the mapping, id numbers) in this system wouldnt change (changes such as inheritance/editing/randomizing/sharing)
        - users & the requests they make would be intrinsically linked, and would be trusted with content relevant to them, including inputs like voting requests (they can vote on legitimacy of content relevant to them)
          - intents would be evaluated by context, to sync/fit them into the absolute system of meaning
            - intents like 'deactivate/hack encryption tools on the server associated with this site they just visited' would be fulfilled if the context was justified, such as contexts like 'in a location where encryption has been abused, like a porn or ransomware distribution site', where new intent requests support a particular change/difference/variation ratio & other metrics associated with calculating justifiability like 'intent (ability in the form of a justified actionable plan) to prevent harm'
            - the browser would be the primary enforcing agent in this system, confirming the integrity of the intent map & edits made, as well as determining justified contexts of intent requests not specified in the map (allocating them to voting agencies in cases of uncalculatable justifiability)
          - this implements a centralized source of truth, applied in a decentralized way (everyone can view the keys of the map & has a local copy of the keys & the value hashes), synced with definitions of meaning & understanding (like how requests from a particular user follow patterns specific to their decision history, and how intents can seem but not be similar to other intents, and common manipulation patterns like using ambiguous intents to hide malicious intents)

    - example of applying structures like 'approximation' and 'adjacence' to achieve intents like 'create proxy identification functions' fulfilling core alternate high-level intent functions like 'derive' rather than 'find'
      - monitor accessible signals (user showing signs of detecting anomalies like staring at a phone number or frowning in concentration) surrounding the inaccessible target signal (attack)
      - the relationship between core structures (like core functions such as apply/derive, core objects like implications/assumptions/conclusions/definitions) can provide a first-level data source on rules to design interface queries (try find information first, otherwise try alternatives to find like derive/build/test information or proxy information, with the assumption that proxy signals amount to the target signal)

    - example of organizing system in a structure optimizing for 'security' priority:
      - with rules like:
        - a function that can edit signals of an attack (request logs) should not be the same function as (or an accessible function to) a function that can cause damage
        - the delete function can only be applied to file content, not file metadata or request logs
        - any rules about a function also apply to any functions that amount to that function when combined
      - these are abstract rules about structures like functions & concepts like organization/integration that offer a new layer of testing for system optimization
      - workflow testing is another type of testing that is not fully supported/automated (by tracking expected side effects of a task set, having conditions to select tests to execute, and having accepted range of variability in outputs like timestamps)

    - example of intent mapped to structure: 
      - the outlier or data point in the middle of two categories isnt supposed to be categorized, its supposed to be identified as belonging to a different group (a group in a state of change), which can be used to derive group boundaries, but shouldnt necessarily be integrated into a categorization function

    - function intent-indexing example
      - rule gaps are created by trust (lack of enforcement in rules)
      - layers of rule gaps can form a possible exploit trajectory to achieve a malicious intent that seems legitimate at various points of validation
      - if a function has multiple intents, that set should be propagated to the next line
      - you can index intent using various layers of functions, which are assumed to have indexable intents
        - sample intent map (semantic: core: code):
          assume: input: parameters
          define: assign: variable = value
          check: condition/filter: if/else/then/switch
          vary: change: iterate (for)
          apply: transform: processing functions (format)
      - so in a code sample from the sample logical flow in "Select & apply method of reducing possible relationships" of Problem Source Identification example 2,
        you can assign intents to each line:
        1. assume: variable1 is variable and in hypothesis_objects and data_is_available(variable1):
          "since location differs between samples:"
        2. check: condition2 variable2 is variable and in hypothesis_objects and data_is_available(variable2):
          "if window.position can differ:"
        3. vary: for each value in variable2 in each variable1
          "if so, alternate window.position across locations:"
            "if window.position is iterable"
              "if len(window.position.possible_values) > 0:"
                "iterate window.position.possible_values"
                - repeat for location
        4. check: does value match any target directions (focus condition intents)?
          "check if alternate window.position achieves student.intents aligning with location object metadata: does opening the window achieve anything in south vs. north room?"
      - the output intent of the combination of these four intent sets in order should be symmetric with the overall function intent
        - the output combination intent, by layer:
          - semantic: "assume, check, vary, check"
            combination intent: "filter subset by iterable subset matching set"
            - the subset is the set of possible value combinations that pass each filter (in this case, that means only variable values of defined variables & the data type we expect, etc)
            - you can derive from this simplified intent form that you should have added a check of the set variable (focus condition intents), without which the whole function is invalid, so that condition should be one of the first checks
          - semantic + objects:
            1. assume variable1 varies (location is a variable)
            2. check variable2 varies (window is a variable)
            3. vary variable2 and variable1 to get combinations (location + window values)
            4. check each variable2 & variable1 combination for match with any target intents (focus condition intents)
            combination intent: "given that variable 1 and variable2 are both variables, vary variable2 and variable1 to get combinations matching target intents"
            - this leaves out the logic to assess the key emergent variables of variable1 & variable2 combinations (temperature, sunlight), 
              which are the actual attributes that should be used for comparison with target intents, 
              since they have a computable/measurable relationship (temperature maps directly to "temperature regulation")
          - semantic + objects + variable values:
            - you can add data analysis based on generated test data to conduct possible intent sets with various data permutations, which should alert you to exploit opportunities
        - given the abstract function intent "find variables explaining target variable", the other intents:
          semantic: "filter subset by iterable subset matching set"
          semantic + objects: "given that variable 1 and variable2 are both variables, vary variable2 and variable1 to get combinations matching target intents"
          line up with what the function is supposed to do, though they are incomplete and have variance injection opportunities (given the lack of direct mapping between combinations & target intents)
        - you can see how lack of direct intent mapping & alignment can alert you to exploit opportunities, or tell you when a function is not done or sub-optimal as youre building a function

    - intent matching examples:

      - "exploit requires that the user has recently visited a site with a TLS cert chained to an ECC-signed root certificate, since the root certificate must already be cached by the targeted system. If a targeted system doesn't have the root certificate cached, an attacker could still pull off an exploit by adding JavaScript that accesses a site chained to the root certificate."
        - intent of sending a request to another site:
          - retrieve info
            - execute function on info
            - display info
          - if there is no subsequently retrieved or already loaded code using the contents of that info, thats a signal that this info is being used for other intents that dont match the intents for visiting a web site (view info, interact with info)
          - the intent of sending a request to a site has sub-intents related to all the site's objects/attributes/types & their side effects
            - if a request has a side effect "caching info", that must be assumed to be a possible intent of the request, rather than more common explicit intents like displaying info

      - an intent of an item (object/function/system) is a 'reason to use it'
        - with human actions, there are good & evil reasons to do anything, although some reasons are more adjacent than others - what matters for deriving intent is the context around the action
          - example: 
            - action: good/evil reason
            - you can see that some reasons are more adjacent (likelier, involving less work) than others - however sometimes functions that required more work in the form of transforms are the correct explanation, when nodes become truly independent so they have to do more work themselves
        - intent stack is full set of reasons to use it, based on known/derivable intents
          - overlapping variance gaps of layered systems in exploit.svg create opportunity chains between system variance gaps
        - function metadata should all be assumed to be possible intents:
          - side effects of a function
          - non-standard uses of a function
          - underivability of a particular intent for the function
          - variance gaps of a function 
        - unknown intent examples:
          - 'to crash the asteroid into the other asteroid' 
            - isnt a known intent, but it will be in the problem space where space mining is an actual problem relevant to solve & the tech is there to support it, or if alien species are doing this
            - this is also not a need of any known system (unless theyre already crashing asteroids into other asteroids using explosions, radiation, & gravity manipulation & Im just a fool)
        - known intent examples: 
          - 'to find the word in the document'
          - 'to classify the species'
        - derivable intent examples:
          - 'to distribute fault for a problem' is a derivable intent using core functions:
            - 'avoid punishment'
            - 'minimize effort'
            - 'ignore error potential'

'''