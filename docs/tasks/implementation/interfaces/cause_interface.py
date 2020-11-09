'''
    - conversion function 
      - standardize to the cause object definition 
        - default conversion operations: 
          - mapping objects that can be converted 
          - adding/deriving missing objects required for the interface 
          - removing irrelevant objects 
        - conversion operations that apply other interfaces on top of the causal interface 
          - structure-function interface: 
            - linking inputs & outputs for causal functions that have structure (sequential functions, hub functions, etc) 
          - concept interface:
            - identify core causal concepts like:
              - state: important for identifying sequential causation 
              - structure: important for identifying inevitable causation 
              - agency: injection of intent into structure (like with organization) 
              - adaptation: important for identifying causal potential (an organism that can learn/change is likelier to be causal) 
              - dependence (structure: causal links) 
                - mutual dependence (structure: causal loop) 
              - ambiguity vs. determination/uniqueness (reducing possible alternatives) 
              - determining concepts 
              - adjacent concepts 
            - structure-type interface combination: 
              - identifying causal types, such as ambiguous cause, structured as multiple alternate similar routes or multiple unenforced rules/variance injection points 
      - the conversion function can be formatted with many different formats (like filters/limits/routes/combinations) to achieve conversion intents (like add/derive/change/remove attributes, or apply metrics)  
      - the intent of the conversion function is to represent each component in the problem space (or data set) as a component of cause (attribute, structure, concept, related object, etc) 
      - the conversion function will attempt to standardize to related interfaces, if the minimum information for the current interface is not met 
        - adjacent causal interfaces (interfaces acting as inputs/outputs or with similarities to this interface, like how information, math, and structure are related interfaces) 
        - alternate/proxy causal interfaces (interface combinations/embeddings that can act in place of this interface) 
      - a structure with a causation attribute (standardizable to the causal interfacee) can have: 
        - causal attributes (causal inputs/outputs, function variables, causal metrics, and descriptive attributes like direction, ambiguity, relevance, uniqueness, directness, inevitability) 
        - causal types (root, direct, hub) 
        - causal functions (converge/diverge, catalyze, depend, isolate) 
        - causal structures (vector, tree, loop, network) 
        - related objects (related concepts like dependence, ambiguity, relevance, agency) 
      - you can look for cause in structures by prioritizing: 
        - known causal structures & causal patterns 
        - causal vertex variables (like dependence) 
        - variables that are often found with cause 
          - combinations of identifying objects/attributes/functions, like ambiguous-direction or inevitable-unique structures 
          - causal function inputs/outputs 
          - related objects to cause 
          - preceding/determining/generative structures of these components (generative structures of related objects, causal function outputs, inevitable-unique structures) 
   
    - cause object definition 

      - definition: 
        - cause can be defined as dependency 

      - concepts:
        - interface: interfaces are causative in that they enable change to develop
        - causative structures: some structures like limits are particularly causative

      - objects: 
        - dependencies 

      - structures: 
        - most causal shapes are cyclical, layer, or network-shaped rather than one-directional vector-shaped (like a tree), which is why some existing methods are inherently incapable of producing system-fitted insights that wont break the system when applied (a particular drug that is not evaluated for bio-system impact, just impact on a particular pathogen or process) 
        - stack: set of adjacent (or other definition of relevant) causes 
        - causal loop: a function that generates information may end up using that information or its side effects like decisions as an input, creating a causal loop 
        - the causal network that can generate a set of values for a variable given a traversal structure like a random walk with probability x
        - causal units (like direction, dependence, input/output parameters, causal vectors)

      - attributes 
        - identification/description variables 
          - degree (x is n degrees of cause away from y) 
          - direction: describes direction of control between nodes (x is always an output so it couldn't have caused y) 
          - interchangeability: can function as another cause (x is a proxy for z, so x & z are not both required to explain y) 
          - ambiguity: occurs with multiple alternates that are not clearly different in their input/output (alternative causes that cannot be resolved or invalidated) 
          - directness: adjacency of cause (x indirectly causes y, x immediately precedes y on a causal chain) 
          - uniqueness: describing whether multiple causes can be ruled out (x is guaranteed to cause y and nothing else does) 
          - inevitability: pre-determination of cause, which occurs from structure 
          - explicit/implicit (x is defined to cause y or x implies y) 
          - abstraction (x contextually or absolutely causes y) 
          - relevance 
          - set of possible alternate causes 
          - requirement/probability of cause (x must cause y regardless of most possible system contexts; if x this hadn't caused y, something else in the system probably would have caused y anyway, given all the similar structures in the system that interact with y, so x is not a required cause of y) 
          - generatability/controllability (how many inputs does the causal have, how fragile is the causation) 
          - dominance (x is almost always causative if allowed to interact with any object - example 'a source of power') 
          - function (x is descriptive rather than generative so it cannot be a cause unless descriptions are an input) 
            - difference from randomness 
          - difference between actual/possible functions (if an agent doesn't solve a problem, but they could have efficiently solved it, is the problem caused by them or its origin) 
        - types (apply attributes with varying values to generate core types) 
          - root cause: an origin cause of a causal branch 
          - catalyst: triggers cascade of causes 
          - hub: a causal node where causes aggregate, are generated, or connect (like a structural or information cause) 
          - indirect/inevitable/ambiguous/unique cause 
          - relevant cause: cause on similar interaction layer or in similar position as: 
            - agents ('describe the problem' has relevant causes like direct cause) 
            - agent intents ('intent to invalidate the problem' has different relevant causes, like the root cause) 
          - alternate cause 
          - interface causes 
            - structural cause 
              - cause from position 
              - cause from interaction layer 
            - concept cause 
              - balance/power as a cause (balance/power attributes/functions caused the output) 
          - causation bases 
            - decision-based cause (from an agent) 
            - time-based cause (the cause is the default/natural progression from a prior state) 
            - random cause (from lack of agents or organization) 
        - inputs (interaction, adjacence, similarity, cooperativeness, potential, structure, change) 
        - outputs (inevitability, influence) 
        - description attributes (structure, type, causation potential, randomness) 
        - generative attributes (structure, system context, change rules, object identities, interaction iterations) 
        - metric attributes 
          - number of steps between causal nodes (measures directness of cause) 
          - number of possible causes (measures uniqueness/ambiguity of cause) 
        - function parameters 

      - function interface 
        - patterns 
        - functions 
          - core functions 
            - inherits structural core functions (combine, merge, rotate, convert, format, limit, enforce) 
            - resolve: identify cause in a set of possible alternate causes 
            - isolate: identify contribution of a particular cause to an output 
            - inject/extract dependency 

            - function to identify alternate routes

              - example of identifying alternate explanations: for a pattern like why people have different responses to a pathogen, is it bc of coincidences like that:
                - the pathogen fits into the bio system in a way that requires the same functions used to protect it from another second condition, taking protection against that condition away
                - the pathogen coincidentally applies mutations that the bio system hasnt yet evolved to handle
                - the pathogen applies mutations that coincidentally spiral out of control bc theyre mutations to important/core change/regulation rules, or that it causes another error that triggers the second condition
                - the pathogen evolved in an animal that didnt have those vulnerabilities so it was able to live in the host indefinitely rather than killing the host
                - the pathogen needs a function that requires evolving other functions that are coincidentally harmful to the bio system
                - the pathogen misidentifies the genes to target or cant identify the right genes in different systems
                - how to generate the set of possible alternate explanations:
                  - apply structures (evolution process of change sequences), concepts (identification function error, coincidence), functions (functions producing changes, such as mutations), and position them using other structures (causal network)

            - function to identify proxy variables

              - compare equivalencies of given & target information
                - check for interim information between given & target information
                  - if interim information exists, its a proxy variable candidate
                - example:
                  - if you dont know the exact functions linking two objects, do you know the functions' metadata, such as:
                    - generative variables: the questions that are normally asked to find the functions linking two objects
                    - metadata (input/output) patterns: the relationship patterns of input/output of connective functions?
                  - this is a comparison between equivalent structures (functions, input-output maps), being equivalent on some metric (contextual impact), connecting the given information (input/output relationship patterns or questions generating connective functions) and the target information (functions)
                - comparisons
                  - equivalencies
                    - given information
                      - sample outputs
                      - target probabilities of sample outputs to qualify for a metric (like fairness)
                    - interim information
                      - interaction space of sample outputs (total outcome combinations)
                        - probability of interactions & interaction types
                          - equivalencies between compared sample outputs
                          - net ratio of equivalencies between compared sample outputs
                            - sum from 1 ... n
                              - how often do they have (1 ... n) outcomes equal
                            - divide sum by total outcome combinations
                          - equivalence of net ratio & fairness ratio
                    - target information
                      - equivalence of sample output of compared objects

              - function to identify proxy variables of a missing variable
                - includes inference of alternate variables that could generate the same information
                - also includes inference of side effects of the missing variable
                - example: if you dont have a variable like 'level of education' or 'level of intelligence' which is a predictor of income, how could you derive it from other variables, as an interim dependent variable to predict, before other dependent variables like income can be predicted?
                  - apply a variable type pattern: 
                    - 'variables with metadata similar to income have a predictive variable with metadata similar to education (which could point to intelligence, info access, tech access, group membership, and other variables with similar functionality to education)'
                  
                  - identify functionality produced by other variables you do have in the data set
                    - 'what functionality does a system with these types of variation in genes, experiences, medicine, & information access produce?' 
                      - output: the concept of 'agency' (and its related functions), which is a causal input/output of intelligence

                  - identify insights in interactions of other variables explaining the missing variable
                    - "these data points are distributed in physical position (data comes from several countries), which implies difference in 'information access', which is correlated with target dependent variable 'income', if you add a related interim variable (given insights like 'accessible information is not always used') like 'information usage' (a proxy for intelligence variable) that varies by cross-indexing with pollution-location data (creating mutations), indicating the 'information usage' is impacted by gene mutations (a gene determining information usage, such as intelligence genes) or other side effects of pollution (impacting 'information usage' functionality)"

                    - bc we had:
                      - location data in the original data set
                      - another data set relating location & pollution
                      - an insight data set about information usage not being equivalent to information access (indicating a need for different terms)

                      we could:
                        - identify the concept of 'gene' from any genetic attributes like gender/race in the data set 
                          - the definition of the concept can be as simple as 'a set of constants for a record' or 'a set of constant inputs for a record' or 'a set of constant inputs of original position for a record', depending on necessity of specification
                          - later we alter the gene concept to generate the 'genetic mutation' concept by applying the core function 'change' to the 'gene' concept, so we probably dont need 'constant' in the gene definition
                          - we also infer a core component like 'functionality' being determined by the 'gene' concept, which can be added to the definition in this initial step rather than inferred later from other components
                          - we also infer that the 'pollution' concept can be an input to the 'gene mutation' concept, which may be included in the original definition as a variable rather than inferring 'pollution' from other components like 'location'
                        - identify a relationship between the 'location' variable correlating with the 'information access' variable
                        - identify location-specific variables, like the 'pollution' concept
                        - pull 'pollution-location' data
                        - generate a possible interim 'information usage' variable by altering the 'info access' variable or pulling an 'info access' insight about the difference between those two terms
                        - identify a relationship between 'info usage' and 'pollution-location' data
                        - infer concept of 'gene' from original data set if it had any genetic attribute data
                        - infer concept of 'gene mutation' from pollution definition
                        - generate the concept of a possible function linking 'gene' concept and 'functionality', with 'gene' as an input
                        - identify 'info usage' as an example of 'functionality'
                        - infer that 'gene mutations' are also possible inputs to 'functionality', in addition to 'genes'
                        - infer that 'gene mutations' are a possible input to functionality example 'info usage'
                        - infer that inputs to gene mutations ('pollution') is a possible input to functionality example 'info usage'
                        - infer that related variables to pollution ('location') is a possible input to functionality example 'info usage'
                        - infer that 'info usage' variation generated by 'gene' concept or 'pollution' concept is a possible input to 'income'

                    - you could infer the link from functionality (such as info usage) to 'intelligence' by further inferring that functionality varies in effectiveness by usage ('info usage' usage, or learning), which implies the concept of 'agency' or 'intelligence' (defined in similar terms as 'having the option of using a resource')
                    - you could also infer 'education' as 'info storage' (remembering it) or 'info exposure' (reading it rather than just having access to it) from the 'info access' variable in the original data set, where education is an alternative or proxy variable for intelligence in some cases

            - function to identify causal structure, as shown in FIG. 13 (Causal structure-matching) 
                - FIG. 13 shows causal structure-matching on information standardized to the cause interface. 
                - In FIG. 13, the program logic may fit variables to a causal structure, like one of the structures depicted in the top half of FIG. 13. 
                - A unit example of a causal loop structure is where the output of one function is re-routed to its input.
                - An example of an alternate cause structure is where multiple conditionally interchangeable but independent causes can activate a function.
                - An example of a causal chain/sequence is a simple sequential set of causes linking the objects/functions, with no alternatives & having one direction.
                - This analyis answers questions like 'how would you identify which causal structure applies to a set of variables?'
                    - As an example, to determine the causal structure for a dog's tail shape, bark sound, spine, and DNA, logic may:
                        - identify that DNA causes the other features, and identify other causes involved
                        - identify the actual causal structure, which is the causal variable network on the bottom of FIG. 13.
                        - to generate that causal variable network, the logic may identify interfaces like environment & change rules, 
                        - it may also identify the concepts in the bio system relevant to those interfaces (mutations, regulatory mechanisms, DNA copies, etc)
                        - then the logic may apply the causal structure between the environment & DNA to generate interim causes like needs or stressors, which create demand for change in DNA.
                    - You can also identify those causes using other interfaces:
                        - system objects (identifying incentives in the bio system rewarding adaptive responses to stressors or maintaining DNA, matches between environment stressors and changes to DNA, sub-interfaces that provide a platform for change to develop like the spine provides a platform for variation within change limit)
                        - structure objects (identifying the rules that act as hub nodes, like change rules do, identify sequences like needing an audio communication system on the vocal chord sub-interface, once that interface is enabled with a spine, so the spine acts as an input requirement for the bark).
              - answers the question:  
                  - why did something work (because of its causal position/structure/layer/pattern/interactions/attributes/similarities) 
                  - what layer of the causal stack is the relevant cause   

          - change interface (change functions of cause)
            - change structure 
            - change intent 
            - change cause metrics 
            - change cause attributes or attribute values 
            - change causal direction 
            - dis/ambiguate (clarify) cause 
            - distance/connect cause 
            - apply/inject cause 
            - intend cause (use a cause to fulfill an intent) 
            - require/invalidate cause 
            - assume cause 
            - depend/isolate 
            - converge/diverge 
          - boundary functions 
            - cause is not: 
              - lack of a resource that couldnt be expected (divine intervention, meaning/reasons/incentives, connection across distant systems) 
          - condition/context functions 
            - cause of the same event can have different structure across contexts, such as: 
              - being poisoned by a plant while lost on a hike (evolution, randomness, lack of information, low agency injection) has a different cause than taking the substance for a research experiment (high level of agency injection), and this will impact the causal structures activated by that substance (being eaten by bears, receiving antidote) 
            - conditional cause functions assess the conditions/context of a cause, to determine contextual (system-fitted) cause 
              - accidentally taking luggage on a plane that someone planted drugs in often has a different cause than agreeing to do it 
                - unless the only reason they accidentally didnt check their luggage was fear of gangs, and if the agreement would also occur bc of fear of gangs 
            - functions include: 
              - determine causal position relative to other causes (like context or system structure) 
              - determine range of possible structures of a cause, with other conditions/contexts applied 
              - apply context/condition to a cause 
          - connecting functions 
            - combination functions 
              - these functions determine how causes of different attributes/types/change states interact, answering questions like: how does an agent cause combine with a structural cause? 
    
    - related objects of causal interface 
      
      - information interface 

        - definitions 
          - cause: input, power, excess unhandled energy, lack of organization 
        
        - strategies 
          - 'when creating ambiguity, use abstract rules' 
        
        - insights 
          - 'causation is a relative term' 
        
        - questions 
          - 'which causal relationships should be checked first when finding variable relationships?' 
          - given the position between these causal factors, which causal patterns are likeliest?
          - given that a species occupies an interim position between evolution, efficiency, time, and environment, what is the likeliest causal shape linking a species with its environment?
            - for more evolved organisms, this is a network causal shape, though species with less developed cognitive ability may have simple or uni-directional shapes with environment
          - what is the function linking these variables, given these functions linking other adjacent generating variables/functions further up/down the causal shape
          - how to define causal structures, in terms of a particular interface
            - example: define cause in terms of the structure & math interfaces:
              - the corresponding assumptions of independent random variables that are emergent outputs (having no agency to interfere with cause) and are resolvable into orthogonal dimensions and reason to believe theyre causative in the pattern (direction of influence established, direct causation, similar object interaction layer, lower-layer symmetry established like DNA being established as a cause of species variation)
          - how to identify causal objects in other interface formats, such as info objects like games/trade-offs/forced decisions/equivalent alternates
            - once you identify causal info objects of independent variables of a data set, that can be used to select an algorithm or abstract the prediction function
              example: 'tradeoff between efficiency & accuracy creates types with vertices x, y, z which match algorithm or prediction function a'
          - how often is cause determinable given the attribute sets necessary to determine it? 
            - how often is a variable set determinable as uniquely causing a relationship, definitely different from random interactions, adjacent in causal distance, having no agency, and clear? 
            - which systems/vertices generate determinable cause (difference ratios, change rates, alignments, interaction layers, pivot points, causal structures, problem types, trade-offs, symmetries)?
          - finding causal structures
            - part of the problem with using a one-directional vector to model a relationship is that the underlying parameter (usually time) may not be relevant for predicting the relationship evolution
            - rather than modeling it by a standard of changes over time, it can be modeled by a standard of changes over variance potentials
              - will a particular variance source change compoundingly or converge to a constant in all possible parameterizations of that variance source
              - does a particular variance source have the potential to generate variance or will it eventually become static in all possible implementations, 
                meaning it either:
                  - doesn't exist (at any time), like a final output that doesnt ever return to interact with other systems as an input
                  - is one of the few things that does exist (across all times), like a concept that never stops influencing variance
          - how to erase causation contributed by a prior/root cause to subsequent variables if root cause & subsequent variables are both included in the data set
          - change phases for causal analysis (interim, changing, diverging, standard, efficient state, constant, interacting, converging, on the verge of obsolescence, outlier, etc)
            - superficial cause, alternate cause in the case of a function, addressing input/output causes

        - context 
          - system context 
          - problem space context 
          - dimension set context 
            - spaces where cause is measurable (dimensions maximizing or displaying differences) 
      
        - examples

          - causal shapes integrated with networks (patterns of aggregation matching causal shapes like trees & circuits)

            - integrating system analysis with networks
              https://twitter.com/remixerator/status/1150578597339340805
              https://twitter.com/remixerator/status/1205724743741014018
            - system of causal types (integrated with type path example as a version of weight paths)
              https://twitter.com/remixerator/status/1156860484294852609
            - causal types
              twitter.com/remixerator/status/1126040476023279616
            - applying causal shapes to a network
              https://twitter.com/remixerator/status/1004579263507566592
            - position on causal type network
              https://twitter.com/remixerator/status/1018540899859607552

      - intent interface 

        - causal intents 
          - outputs (direct/combined/emerging) 
          - side effects (indirect side effects of outputs, processing side effects like locking inputs, opportunity cost of processing) 
        
        - intent vs. incentives: an intent without an agency cause is an incentive 
          - incentives are usually considered less causal than intents, from the agent perspective:  
          - agents cant be expected to go against incentives every time, as theyre generated by system structure 
          - but agents can usually inject agency into the system, to change its structure & the intents resulting from it 
          - intents exist outside of the system, which can motivate agents to change a system 
          - so structure of a system is not the cause of all causes, but it is an important interface to apply on top of the causal interface 
          - if there is an absolute root cause, it may be change rules (how systems change) 
      
      - type interface 
        - attribute sets differentiating objects 
        - attribute sets without types 
        - type hierarchy 
      
      - system interface 
        - causal system 
          - system objects 
            - symmetries/efficiencies/similarities 
            - definitions (difference, power, direction) 
          - system functions 
            - core system function (apply, inject, combine) definitions on the causal interface 
      
      - structural interface 
        - structures 
          - structure network (links between causal & other structures) 
          - causal structures 
            - causal structure network (links between causal structures like sequence, hierarchy, tree, network, etc) 
              - structures (filters, limits, maps, networks, trades, sequences, links, circuits) 
          - determining structures 
            - input/determining structures 
              - filters 
              - functions 
          - structures identifying cause 
            - tree origin (root cause) 
            - adjacence (causal degree) 
            - layer (alternative cause on layer) 
   
    - interface operation (combined/applied/injected) output 

      - intent-structure interface 
        - intents identifying cause 
          - aligned intents (compounding cause) 
      
      - pattern-structure interface 
        - 'a causal tree often has multiple layers & may converge to fewer nodes'  
      
      - structure-function interface 
        - functions as structures (filters, limits, maps, networks, trades, sequences, links, circuits) 
        - structure functions (traverse, combine, find, build) 
      
      - cause-concept-system interface 
        - causal concept system 
          - system objects 
            - symmetries/efficiencies/similarities 
            - definitions 
            - structures (networks, trades, sequences, links, circuits) 
          - system functions 
            - core system function (apply, inject, combine) definitions on the causal-concept interface 

      - cause-change:
        - example:
          - the classic parabola of a ball's motion when thrown from the ground has two primary cause-values:
            - origin force until the peak x-value change rate, and gravity force after the peak x-value change rate
            - if the y-value starts changing more from gravity than from origin force, the gravity force becomes determining
          - additional cause values travel farther up the causal stack:
            - forces causing the emergence of gravity & origin forces are other causes
'''