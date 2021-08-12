# to do

  - yes, there's more torture, every day Im on my diet Im going to torment you with my achievements

  - merge examples in implementation_examples from various patents
    - identify any examples missing from patents in docs/tasks by diffing patent spec texts
    - organize function implementations, to do list, examples, logic
 
  - main variables of ml:
    - data
    - data pre-processing & standardizations applied
    - data format
    - data processing functions in network
    - network constants
      - node count, node layer types, node layer type count
      - activation function & thresholds
      - loss function (how a prediction error is determined)
    - network learning algorithm (how weights are updated, like backpropagation)
    - network learning algorithm parameters
    - interface structures embedded in ml, either explicitly like 'feature subsets' or implicitly as emergent structures like 'merged feature structures'
    - general combination types of these network structures
      - supervised, unsupervised, reinforcement

    - out of all the interface structures, a given network structure set can identify a subset of them better than other algorithms
      - difference types, interaction types, function types

    - given the variance & interactions in the data set, only so much info can be derived from it
      - additional restrictions are added by other network structures, like the algorithm
        - meaning a subset of the 'possible info derivable from a data set' is derivable with a particular algorithm
        - in addition to this subset:
          - a set of errors can be created and added to the 'derived info' as legitimate info by the network structures
          - a set of errors can be identified by the network structures
        - the network constants, learning algorithm, & other network structures allow other errors/info to be derived/identified/created
      - these structures combined may interact in a way that allows progress toward the optimization metric, or neutralizes/contradicts progress
    
    - applying interface analysis to network structures
      - the interface structures of a set of network structures may not align
        - for example, a set of network structures standardized to the logic interface may not allow logical connections between the structures once converted
          - including logical structures like assumptions, connections, conclusions, contradictions
        - applying the concept of 'adjacence' as a source of 'relevance' with intent to 'identify causation' may not make logical sense if the output of that operation is later 'randomized' in some way, so these operations would have to be reversed
          - example: if randomness in the form of 'noise' is added to the data set to augment it for robust training, and then 'adjacence' is added as a source of inputs to the 'identify causation' intent, that wouldnt create a 'logical contradiction' structure
          - the original sequence cant use logical structures to reach the target structure, indicating that a particular set of network structures isnt a useful combination
      - a useful solution space-filtering structure is 'if it doesnt make sense with the laws of physics (connectible on the physics interface), its not a good idea'
        - example: 
          - aligning 'attention' in the form of extra computation power with 'complexity' makes sense with the laws of physics, even if its not an optimal complexity-reduction method (such as reducing a complex structure on other interaction layers that compress features efficiently)
          - if its more costly to create, its less likely to be true/real
            - high-variance functions connecting exact data set points are less likely than a general function with fewer changes/terms
            - functions of one variable with many terms of that variable are less likely than functions of one variable with few terms of that variable, just bc of the improbability of a variable having a causal relationship to another variable without any other variable interactions in isolation
          - if x's causal variables arent correlated with y, a causal relationship between x and y is not established, bc of how the 'sequence' structure works

    - the problem with incremental weight adjustments typically found in network learning states is that they might miss non-adjacent weight adjustments that would be useful

      - an algorithm that looks for minima with incremental steps and encounters only costs in one particular direction, resulting in a deactivated node or deactivated node set barrier, would fail to identify a minima in some functions with more complexity
        - this is why its important to generate maximally different bases of the possible solution space, and start with those as initial inputs
        - in a network structure, this could be fixed by adding nodes where a deactivation occurs, optionally according to known 'deactivation followed by epiphany' patterns or up to a general threshold of added nodes, to avoid failing to explore a useful high-cost direction, that may not occur in the data set but may be possible given the problem space & variables
        - its also useful to calculate possible stabilized solution & error structures in the problem space to:
          - identify error types of failing to identify these stabilized solution structures
          - design an algorithm that can find these stabilized structures efficiently in the data set, if they exist
          - example: 
            - generating all the possible sub-species (stabilized solution structures) given a set of required & probable features of the general species (as well as other important variables like costs the species sustains & their interactions with environment & other species), so that if a deactivation in one direction occurs but there is a sub-species possibility in that direction, the algorithm adds nodes/iterations as needed to pursue that possibility in the data set, and retains a nonzero weight or activation path in that direction just in case, even if no examples of it are found in the data set, once the direction of a particular sub-species is identified in the network structure

      - the whole point of 'weights' is to 'highlight features that are useful' (after identifying & removing irrelevant variables like 'orientation' in the 'image-categorization' problem)
        - the corresponding error type for a learning method is:
          - 'if a learning method of weight update cant update weights in the structure that matches the actual prediction function'
        - other error types:
          - 'if a useful feature structure like a combination cant be identified by the network structures like the network feature/weight processing functions, the weights cant reflect the right feature structure to use in the prediction function'
            - its important to identify what feature structures a network structure set can identify & use
            - you can also derive what feature structures would be useful to solve a particular problem & start with those as an initial structure when generating/identifying an algorithm to create those useful feature structures
              - example: 
                - for the 'image-categorization' problem, derive that 'features of varying size/position' (leading to 'subset' feature structures) might be a useful feature structure to generate in the network & assign weights based on this feature structure
                - for the general 'find a prediction function' problem, derive that 'function-subset functions, variable subset functions, base functions, or data point subset-functions' might be useful feature structures to allocate training computation to

      - identifying irrelevant variables for a problem type
        - variable structures & interactions likely to indicate an irrelevant variable
          - variables whose changes dont correlate with changes in the other variables, so they might as well be converted to a constant
          - variables whose changes/interactions can be compressed in a type variable, where the type variable is sufficiently predictive & variations within that type are irrelevant

  - generating a function set to fulfill an intent can encounter errors after generation time, so injecting 'self-awareness according to responsibility/ability' is a useful structure to apply at the function level
    - a function that can access usage info (the outputs of functions triggering it and the inputs of functions using its output) can identify before an error is encountered if it will produce an error for the functions using it
    - allocating awareness of context in the form of triggering function info based on a function's ability to identify & correct errors is useful at that interaction level
    - cross-interaction level interaction awareness is also useful in addition to intra-interface interaction context awareness, so an application can identify which functions that use it may encounter errors given their input/output structures
    - this is useful in ml at the function & node-level, where a function/node can identify when error structure patterns (like 'deactivation barriers to valuable feature values' or 'incorrect feature structure to identify all possible solution structures') are occurring in adjacent functions/nodes & modify its params like thresholds to account for that imminent error before it occurs
      - this adds error-correcting functionality to the network on certain interaction layers, which can create other error types if the error-corrections aggregate into an error, so network-level error-corrections can be built to handle this emerging error structure from lower layers
  
  - add to science
    - a quantum superposition is a 'lack of information' or 'semi-information' as in a 'lack of efficient stability' (or a mismatch between a structure and the space its observed in vs. the space its clearly defined in, like how imaginary numbers are partially structural in euclidean space in their reference to 1 & square roots and negatives) so that the interaction with the 'observation' function gives the not-information or semi-information of the superposition the efficiency/energy it needs to stabilize, like a template being filled with variable values according to a query, where the template represents 'partial/semi-information' and the values injected into it crystallize it into a more certain form
    - energy transfer from observer to observed in the form of certainty/structure allowing resolution of observed 'lack of structure' (as a variable) into a 'structure' (value)

  - add to math mapping: 
    - information is a form of certainty that has energy from various sources, like interactivity/similarity/efficiency/requirement/composability
      - this energy will follow other energy patterns, like energy dissipation/distribution & energy storage
        - if a number has more energy than its structure can contain, it may distribute it into a system of related numbers, like components or variants
    - similarity of structures like data type in connections (like how 'absolute references' are a possible connecting structure between absolute structures like 'infinities' and referential structures like 'ratios' or 'constants')
    - imaginary unit as a unit of non-definition, or non-structural definition (requires a different axis to portray bc its not defined in the original axes), or a unit of isolation/independence from a dimension set
    - numbers as symmetries given the adjacent change types available to them, and math as the interaction space of these symmetries, where values that dont have structure can exist between the interactions of these symmetries but only while they can maintain a lack of structure & interaction
      - math helps with calculatable problems
      - there are limits to what math can calculate, bc there are limits to the interaction space of number types
        - like how 'integers' and 'infinities' can interact bc you can have 'multiple infinities' and 'infinite integers' and so on, but not every number or number type/attribute can interact like this, in such a clearly defined (structural) way
        - for example, the 'root of negative infinity' is less structural than the 'root of infinity', and the 'root of infinity' is less structural than the 'unit of infinity', bc the less structural interactions require special definitions/limits creating spaces in which they can exist, rather than having structure in a high ratio of spaces
      - relevant questions
        - can you extend the direction of reductions in structure in the interaction space to determine the limits of structure
          - does it reach zero structure at its limit
          - does it extend indefinitely by definition, bc of the lack of structure and a corresponding lack of limits enforcing structure to exist/develop
          - at what point do the requirements of the 'special definition' prevent any structure from being defined?
          - is the interaction space continuous (does it form a topology)
      - some questions (lack of structure) cannot be adjacently resolved by any combination of known structures (such as ambiguities that are more efficient/stable than any structure that can deconstruct them or any input/output structure)
        - is this an absolute limit or does it result from logical flaws, lack of info, or other errors
        - example: calculate interactions of infinite sequences (like in quantum field theories) with perfect accuracy in less than x time type
          - in order to calculate these interactions, the following would be necessary:
            - rules about sequence interactions (why one sequence is adjacent to another, if there is such a rule, and how they can be combined)
            - info about the probability distribution or function that could generate the sequences
            - rules about combining infinities, where each infinite sequence could be defined as an object in the space of infinities
            - rules about interactions in a space that compresses to other relevant info about the sequences
              - meaning alternative compressions than the value/sequence attributes of generative functions, progressions or probability distributions
              - rules about other interface structures than the values or the values' attributes themselves, such as structures like:
                - requirements/opposites & other standard structures
                - alternative equivalents
                - approximations/probabilities
                - difference topologies (rather than infinite sequence value topologies)
                - rules about the system where these sequences could exist rather than the values that exist in the system
                - the structures (of differences & patterns & other useful structures) in the sequences/values that would be impossible, possible, adjacent to calculate, and adjacent functions to determine structures of calculation impossibilities/possibilities/adjacencies in the original topology
                  - finding the structures of sequence sums that would be adjacently calculatable creates a test that can filter out structures that are not adjacently calculatable, like finding local minima using gradient descent
                    - this is an example of why other system structures than input/output sequences/networks are useful, such as the 'structural similarity' of 'gradient descent' and 'filters of structures of adjacent calculation potentials'
          - if there is an ambiguity that defies calculation (without checking every value), it means there is a certainty in its structure of uncertainty (like an ambiguity between a 'random generative function' and an 'input structure that generates output that seems random') that can be relied on to calculate its attributes (like requirements/limits, such as 'equal distribution of outcomes as trials n increases'), if not its actual output values at a given input
        - in terms of graphing these structures, a space where every variable can be reduced to a spectrum with opposites indicating a difference type would be able to visualize these structures
          - a variable indicating additional operations added to a function, where each operation has an opposite, and each operation adds a change type, still doesnt have an inherent ordinal value indicating how far from the origin it should be, unless there's a clear association in increases in complexity/potential between change types added by each operation
          - the definitions of 'ambiguity', 'inevitability', 'intent', 'output', and other structures may allow visualization in a mathematical space without using vectors or networks, if their definitions can be mapped with opposites & incremental increases in an attribute with an inherent ordinal ranking and a zero value having no structure
            - ambiguity: 'lack of differences in alternatives (different options)'
            - inevitability: 'lack of alternatives (different options)'
            - requirement: 'exclusive trigger'
            - output: 'subsequent causal node'
          - if 'lack' can be mapped to the negative direction, the other structures can be mapped to structures of certainty (largely in the form of logical sequences & variables as useful axes)
            - 'output' creates a certainty in the form of a sequence (as in a 'guaranteed product of the cause')
            - 'requirement' is a 'certain input' if another structure occurs (a function is triggered), which is also a sequential structure
            - 'ambiguity' is a lack of 'structure indicating difference between different objects', meaning the differences cant be mapped in the current space, indicating the structure of a sequence of a 'conversion' (like 'adding a variable') before the difference can be mapped, which makes sense bc it offset the 'lack of structure indicating difference' (a variable), and if change types (variables) are mapped in this space, this can be structured as a function converting the current or previous change type value to the required change type value

  - example of applying interface components to solve problem of 'generating arguments to make a point'
    - change variable 'location of power':
    - this company is welcome to build their own app store with their own phones or team up with their coalition to do so
    - add variable 'time sequence' to 'location of power' change:
      - if this company operates an app store someday, they will set rules to benefit themselves too, just like theyve done in the past
    - offer an alternative to charging app store rate
      - is there a one-click button to migrate from this company to the monopoly that could replace any difference in taxes on this company
    - apply conceptual definition filter 'does concept of persecution (and related components of the definition like focus) apply to the behavior (does behavior have a specific target that is the focus of persecution)'
    - are the monopoly's rules applied exclusively to this company? if not, it's not anti-competitive behavior
    - apply intent filter
    - is this company's mission nobler than the monopoly's
    - apply system cost-benefit analysis
    - what features were improved bc this company exists? are those features worth anything or required needs? did they develop those features better than competitors?
    - if this company is just charging rent on a catalog, are they adding value to the market, so they should be allowed to dictate the market at all?
    - what products/features would the monopoly develop if they didnt have to pay a fine, and what are those features worth, and are those features required?
    - apply logical fallacy filters
    - apply 'hypocrisy' filter
      - apply 'anti-competitive' conceptual definition structures & test if these structures fit the opponent
      - does this company plan on raising prices at some point or will they keep prices low even if the app store rate holds? are they only keeping prices low to dominate the market & plan on raising prices later? isnt that anti-competitive behavior?
      - if they are so concerned about anti-competitive behavior, why arent they trying to compete by building their own app store? isnt there a risk that the apple app store is sub-optimal and needs to be improved with competition from this company

  - organize examples of logic for functions (interface query design logic)
    - document default static config objects that are inputs to core objects (like functions & concepts)
      - core functions like 'change', with locked objects which should be generated as inputs to other functions and should not be removed bc they enable other rules & core objects
        - a 'check for errors' function
        - a concept of 'self-correction/optimization'
      - these locked objects can be used to generate rule-generating/deriving/finding structures, by forming an initial structure of locked objects and filling that structure with conditional & changeable structures
        - these rule-generating/deriving/finding structures can be used as solution automation workflows
    - design an optimal sorting structure for general interface queries to apply to problems manually
    - example of how to predict most interactive/causal concepts in a system
    - list interface selection (based on inputs like available APIs/data sets/definitions)
    - problem interface structures: solution constraints/metrics, problem space variables, available functions, useful formats/structures
    - function to translate interface query logic into interface language (combination of core functions (find/build) & other core components)
    - function-usage-intent::output or demand::supply combination/merging/building/matching functions (alternatively formatted as a solution-finding query for a problem or lack-resource matching function) as an alternative solution to ads
    - decision points (required/optional resolution of variables to constants, as in selecting a variable value)
      - identify when a method & data set can be identifyd to be capable of deriving the answer to a prediction function problem
    - alternative intent coordination & compatability of metrics
      - calculating interactivity by coordinating/adjacent/convertible structures

  - add structural queries to insight paths
    - alignments present in security innovations (like alignment in inputs like keys)
    - source of rule development as structures of conflict between forced interactions like change causes & constant structures like limits
      - incomplete inevitability of interaction as a decision structure
    - other examples  
      - group device history authentication: authenticate credit card by proximity to cell phone & continuity applied to user usage history pattern
    - functionalize insight paths & integrate functions in optimized program with parameters to select function subset & structure for input problem

  - create configuration for 2-3 list items every day
      - create compilation script to compile code/config into a network graph on every change
        - add support for equivalent synonyms
        - add conversion to standard vocab
      - write some default interface queries to use until logic is written
      - finish lists:
        - most valuable interface queries & workflows
          - find the sets of differences/dependencies/formats/errors & other useful structures that are the most valuable in a particular structure like a sequence to solve a problem
        - useful perspectives
          - useful to think of prediction functions as generative functions to select the variable interactions that are most likely
        - interface component definition routes
        - ai structures with supported intents & solution success causes
        - solution filters to apply in functions
        - useful interface components
          - aligning/balancing structures, to solve problems like 'a balance position of structures producing errors when unbalanced'
          - questions formatted as a disconnection between components like causal positions, paths, directions
        - subset indexes of an interface useful for solving most problems (structure indexed by metadata like problems solvable, fitting systems, interactive structures, supported intents)

  - add to conceptual math examples
    - example of a conceptual math operation that builds a boundary structure leaving an inevitability of a matching concept (numbers) filling the structure
      - the concepts of 'missing', 'multiple/more', 'unit', 'type', 'identifiable as similar/equal/different' and 'difference in amount' allow for/require/build the concept of 'numbers'
      - also functions like 'compare' or 'reduce' or 'expand' require the concept of 'numbers' when comparing objects of that data type or objects having a quantifiable attribute

  - interim functions to build:
    - derive definition routes on various interfaces from a definition
    - apply a standard format (function/attribute/object) to an input
    - derive function intent stack
    - identify error types
    - identify structures of cause
    - identify variable types & structures
    - consolidate repo, remove repeated content, merge similar functions

   - finish processes:
      - finish interface analysis of physics to identify other useful components like efficiencies, incentives, trade-offs, closed systems
      - finish applying interface components (like abstract) to useful interface components
        - core interaction functions of core interaction functions
      - create interface queries of finding useful interface component filters

  - example of structural version of solution difference from original solution: 
        - this is like using a pair of connected lines at different angles to connect two points (multiplying alternate multiplier pairs to create a product), where summing the line lengths produces an equivalence, so different solutions would look like differently angled triangles connecting the two points
        - https://www.popularmechanics.com/science/math/a30152083/solve-quadratic-equations

  - add to useful structures
    - identify what is the system structure format where the maximum number of interface queries can be executed structurally, with minimal conversions required? is it a merged format of variable/function/concept/cause network graphs, or system state networks, or a set of variable subset graphs, or differences visualized as vectors, or input-output sequence visualizations, or a network with all identifiable interface components visualized
    - identify useful perspectives

  - document useful component/sub-structures of interface queries (interface components, interaction rules, cross-interface interactions, generative functions)

  - ml explanation of finding coefficients of prediction function by applying distortions to coefficients & ruling out distortions that dont contribute to prediction accuracy
    - can be optimized with reductions like:
      - 'calculating the most different distortions that will reduce possible values the quickest & applying those distortions'
  
  - proof/determination structures
      - what makes something possible to identify/calculate
        - a solution structure where the solution metric is clearly defined (structural or having other structures of certainty like consistency or inevitability or requirement)
          - checking a path to see if it includes a node twice is clearly defined (it uses the structure of 'node visit counts' in the 'path' solution structure)
      - what makes something difficult to prove
        - where there are ambiguities (lack of certainty/structure/definition) between the input parameters & the output function value
          - ambiguities such as where multiple inputs produce the same output, like how different x-values can produce the same y value on a wave function
      - useful proof structures
        - apply possible components to create an absolute or scalable definition include components framed in terms of interactions with other components that can be used with a consistent measurement (like a stable structure across interfaces or dimension sets) & can also scale (boundaries), rather than framing them in terms that can have different meanings at different parameters (closed, hollow)

    - add to causation variables
      - ability to change (if a variable cant be changed, it is less causative for problem-solving intents)

  - examples of identifying vertex variables
      - general vertex variables: topic, origin/destination, reason/cause/point/intent, errors, variables, types
      - comedy vertex variables: sincerity, stupidity, stakes, tension-resolution/expectation-subverting pattern variation
      - music vertex variables: tone, tension-resolution/expectation-subverting pattern variation, lyrics
      - optimization metric vertex variables: solution metric patterns (what other solutions optimize for, to identify optimization metrics to apply)

  - when is it optimal to store a mixed structure of varying specificity (like a type, intent, cause & a specific example)
      - when there are potential uncertainties to resolve, like whether the example represents a new error, type, or variable, bc the example doesnt fit known structures

  - all primary interfaces can act like the problem-solving interface (start solving problem from the concept or structure interface and integrate all info back into that interface & frame the solution in terms of that interface) but the meaning interface (the interface interface) is the most powerful

  - visualizing higher dimensions with changes in a network of visualizable variable subsets like:

    - dimension subsets: displaying dimension subsets in groups of sizes that are already visualizable (from 1 - 4 dimensions), where orthogonality is preserved across the network of subsets

    - dimension groups: grouping similar dimensional changes into a change type across a dimension subset, to visualize the change types
    
    - relevant (robust) dimensions
      - dimension invalidations: grouping invalidating/neutralizing change types
      - causative dimensions: just visualizing higher-impact/causal dimensions
      - vertex dimensions: graphing variables as differences from vertex variables
    
    - mapping dimensions: group value sets as other structures like points or networks in a space where change types like 'continuous change' are supported
      - embedded dimensions: dimensions graphed visually using extra dimensions as parameters
      - base dimensions: dimensions standardized to a base and graphed in alignment, like multiple functions on a graph with a common base
      - mapping other dimension metadata: interactions between dimensions units/change types/limits/definitions are graphed
      - abstract dimensions: abstract value structures are graphed ('a point on a line') instead of specific values in a dimension
      - constant dimensions: adjacent limiting constant dimensions are graphed instead of dimensions of change

    - dimension interactions: 
      - interactive dimensions: dimensions that interact are condensed into an input/output of the interaction structure, and input/output dimensions are graphed instead
      - dimension interaction structures: structures of interactions between variables (like direction/circuits/networks) are preserved, where values may be lost
        - dimensional difference: difference between dimensions is graphed instead of different dimensions & values, where dimension values are structures associated with graphed dimension interactions
        - conversion requirements: conversion requirements to a visualizable shape are graphed instead of actual dimensions/values
        - interaction structures between value structures like positions on dimensions when graphed as a standardized shape
          - example: with dimensions formatted as a standardized form like 'lines of equal length, & values as points on these lines', the interaction structure would be the lines connecting the points on the dimension lines, when arranged in any order

    - example of resolving a conflict between structure/limits using a structural similarity between a structure (gradient of function) & its container/limits (gradient of constraints)
      - https://en.wikipedia.org/wiki/Lagrange_multiplier
      - also an example of a solution space (the whole function is the solution space of possible minima/maxima) and a filter applied to it (constraint)

    - make a function network of math domains (inputs/outputs of geometry, algebra, calculus that align)

    - resolve definitions of components so you can finish organizing useful structures like combinations of concepts such as "format sequence", "solution automation workflow", "insight path", "reverse-engineer solution from problem requirements or opposite structures", "connect problem & solution"

    - value isnt created/lost by companies in the timespan of hype/short cycles, so stock market price swings aren't reflective of reality from a macro perspective
      - it takes years to build value, it doesn't happen overnight, excluding almost magical insights that create cascading efficiencies like my system
      - losing value also happens slowly, excluding extreme natural disasters, like the value of a community still being relatively high despite shared losses, bc of social network effects & organization/coordination effects
      - value can be calculated differently, using metadata like the lifetime & total possible value of a product
        - what is the total supply of the product inputs (fossil fuels)
        - what is the usability lifetime
        - what are the costs
        - what are the product intent alternatives (can intents fulfilled by the product be fulfilled by other products)
        - what is purchased with revenue from a product (research, insights, other more valuable resellable products, etc)
        - if this pricing method is applied to fossil fuels, oil companies would be paying people to use them

    - identify filters for definition routes

    - database polling/prompting user for update & predicting updates or searching for & receiving user-approved updates from other services, rather than being a passive receiver of input from user
      - based on local usage/change patterns or integrated usage patterns to identify expected transactions with other services
        - once a credit card is marked as lost in a banking service, a change of credit card numbers is expected by other services which can poll for updates to this flag
          - user option like 'yes, allow other approved databases containing my address poll to collect this update'
        - once a renters insurance policy is changed in an insurance service, a change of address might be expected by other services

    - make list of variable structure variables measured by algorithms & why they are measured by a network algorithm

  - make diagram of absolute reference connections with metadata structures like networks/paths
  - identify core graph variables (definition of adjacence/difference, connectivity, dimensions, info storage methods, interactivity of structures like sequences)
  - crypto as community consensus, where a decision can have value if backed by a community

    - examine connection between fractals, sequences, averages, origins, multipliers (self, as in power), & circles
      - fractals as a relevant structure for adding sequences of fractions (adding numbers similar to itself on a smaller scale, infinitely) as a way of producing inputs to circles created by transforming a fractal spiral, where the origin is the original number as a base for applying increasingly smaller scales
      - the set of points forming roots of an infinite negative number sequence (roots of unity, rather than roots of any negative integer number) as a way of producing a circle because of their common distance to their average (center) forming the radius
      - lines of equal length having a common average point (center/origin)
      - fractals & infinite sequences as a way of calculating area under a continuous line (increasing small subsets of structures with area calculatable with multiplication of x & y)
      - what continuous line segments would have an area equal to a circle of relevant proportions?

    - how to identify the killer counterpoint
      - point: 'election fraud claims'
        - counterpoint: you dont think the other party has members?
          - followup points:
            - how are they organizing? why do you even hear about them?
            - who's benefitting from investing massive funding in creating a false illusion, if its all fake?
            - why wouldnt they choose cheaper methods of doing so than an elaborate illusion?
      - identify most extreme false assumption of point by identify causes of the output metric (vote count)
        - the primary/basic false assumption of the point is that the other side doesnt have votes that are comparable in quantity
          - possible causes (inputs) of 'not having similar vote count' include:
            - not going to vote
            - not being able to vote
            - not having members to vote
          - the most extreme false assumption is the most extreme cause of 'not having similar vote count' (that the other side doesnt even have members (input of votes) that are comparable in quantity, let alone votes (output))
      - identify 'incentives', 'side effects of party/member/vote existence & size' as other relevant concepts to generate followup questions

    - the work of 'stealing my work' and 'pretending not to' doesnt produce efficient brains with a good grasp of concepts like 'meaning', so it emerges as an inefficiency bc the type of brains developed wont be good at finding solutions to output problems generated by granularly copying/pasting to a specific problem/solution & hoping it works better
            - 'understanding my work' is a better goal if you cant look away bc youre not done experiencing awe
              - once you understand it, you wont need to watch me work, youll be able to generate my work
  
  - apply nn to derive error types & bias incorporated into other nn data/parameters/algorithms/structures/models    


## general

  - integrate objects/.md text with interface implementations

  - apply to structures

    - concept of attention in structures
      - mixed interim high-variation & high-similarity structures tend to maximize attention
    
    - examine error type of conflating intent & requirement
    
    - consciousness as choice to move between neural nodes (rather than being directed) required:
      - the development of alternative node paths performing equal/similar functions, requiring:
        - the development of excess resources, delaying required decision time (making immediate decision unnecessary, avoiding a forced decision), requiring:
          - the existence & application of previous efficiencies & functions for alternative evaluation, energy storage, storage-checking, & energy requirement-identifying
      - the cause could be framed as structures such as an 'efficiency stack' or 'energy maintenance functions' or 'alternative options' or 'navigation/motion control' or 'lack of requirement/need'
    
    - examine similarity (alignment/overlap) structures between: 
      - extremely different components (when an error type is an incentive or a function used for other intents) 
        - when the solution format of some problem has similarities to the error type, like when you need randomness so errors generating randomness are a possible function to use for that intent
        - contradictory/opposite components (have some metric in common, with opposite values)

  - finish organizing lists of examples, functions, info objects (insight paths, definitions, questions), components for configuration

    - organize examples

      - label examples so they can be queried more structurally
      - query for logic in examples when implementing functions
      - organize examples of useful structures & questions in index.md
        - identify useful questions in notes
        - check reduced language components for any other useful functions (what terms cant be adjacently, clearly & accurately framed in terms youve defined) for completeness


## examples


  - examine the distortion vector paths that adjacently decompose a data set into a prediction function from a base point/function set

  - give example of mapping to structures & identifying contradictions its safe to ignore for applying a structure

  - example of permuting assumption: "reports of power consumption have to be exact measurements" 
    - a temperature monitor sensitive to a hundredth of a degree might provide similar but non-specific power reporting for important/extreme usage patterns without revealing such specific information as that which could infer exact operations being done, bc the interval of temperature measurements allows for greater variation in calculations that could explain it
  
  - query examples for use cases like:
    - lack of information stored (match problem of type 'information lack' with interface query 'check pattern interface for similar patterns')
    - query problem breakdown & integration diagram
    - calculating various different problem breakdown strategies first before executing normal query-building logic for each
  
  - add examples of system/object/rule/type change patterns
  
  - include example workflows with example problems
    - include example of how to generate other workflows (different starting/ending points & trajectories)

  - example of using set theory in query operations:
    - edges as core organizing/formatting operations (find/apply) & interfaces (connecting/explanatory concepts/functions)
    https://en.wikipedia.org/wiki/Hypergraph

## diagram
  
  - diagram with error types
  - diagram of the network of formats
  - make efficiency map
  - diagram of alternate interfaces (information = combination of structure, potential, change or structure, cause or structure, system)
  
  - give structural query example diagram for GANs + image compression problem

  - chart type: overlaying multiple 2-dimension variable comparisons to identify common shapes of variable connections (density of points added with a visible attribute like more opacity)

  - finish core function structure example diagrams

  - diagram with joke types
    - 'annoying when they bring up human rights in a conversation'
      - conversation system context
        - functions
          - change topic 
            - change topic structure (sequence)
              - introduce a topic (first time topic is included in conversation)
          - expected interaction functions
            - criticism of a behavior
              - 'conversation with dictator' system context
                - criticism of power abuse (law violation, specifically human rights violation, which are a related object to dictators)
                  - interpreted as right in the 'conversation with dictator' system context
                    - expected interaction in this context
                      - 'should bring up human rights to a criminal'
            - norms:
              - for low-stakes interactions & interaction errors (manners, annoyance, disrespect)
            - laws: 
              - for high-stake interactions & interaction errors (rights violations)
        - placing a norm (or related objects) in the place where a law (or related objects) would normally go:
          - 'its annoying when someone doesnt let you end the conversation'
            - 'its annoying when someone keeps going on & on about your previous conversations where you ordered deaths of a dissident'
              - 'its annoying when someone keeps going on & on about your previous conversations where you ordered deaths of a dissident for being annoying & then abruptly stops without explanation'
            - 'its rude when someone doesnt let you end a conversation with a laywer interrogating you for war crimes' 

  - diagram for structures of emergence
    - example: 1-1 input/output relationship up an interaction layer, where extra resources that dont dissolve immediately on the higher interaction layer aggregate & form core structures like combinations, where interactions between combinations & sequences have different dynamics than the individual output interacting with other individual outputs
    - emergent functionality/attributes come from interaction structures (sequences & layers)

    - add diagram for intent-matching
    - add structures to diagram: interface overflow (to sub-interfaces), interface foundation
    - diagram for workflow 1: 
      - function to identify relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'
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

    - diagrams for specific concepts, core functions, concept operations (combine, collide, connect, merge, apply), ethical shapes
        - variable accretion patterns (how an object becomes influenced by a new variable, complex system interaction patterns, etc)
        - make diagram of potential matrix to display the concept
          - map parameter sets to potential matrix shapes 
        - finish diagrams for cause (shapes & ambiguity), concept (evolution of concepts, networks, distortion functions)
        - diagram for argument
      - make a system layer diagram for each interface to allow specification of core interfaces & other interface layers (interface interface)
        - make a system layer diagram for structures to include layers of structures 
          (beyond core structures like curves, to include n-degree structures like a wave, as well as semantic output structures like a key, crossing the layer that generates info structures like an insight, a probability, etc)

    - map variable structures to prediction potential for problem types, given ratio of equivalent alternate signals

    - vertex variable structures
      - quantum physics, prediction/derivation tools, build automation tools, testing tools, learning/adaptation tools, system rules, computation power are all vertex variables of information, since they can generate/derive/find information
        - which structure (sequence, network, set, or cycle) of vertex variables is most efficient

    - core component attributes: identify any missing attributes/functions that cant be reduced further

# content/config

    - import insight history data to identify insight paths (info insight paths like 'lie => joke => distortion => insight', system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub')
    - define default & core objects necessary for system to function (out of the box, rather than minimal config necessary to derive other system components & assemble)
      - add default functions to solve common problem types
      - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially identifyd in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.
    - document time structures (concave time explaining compounding similarities up to a point of maximum concavity, a structure that can separate from the other space-times)
    
    - systematize definitions of info objects, to include analysis that produces relationships of core objects like opposites to their relevant forms (anti-symmetry) in addition to permuted object states (asymmetry), such as an anti-strategy, anti-information, anti-pattern
      - organize certainty (info) vs. uncertainty objects (potential, risk, probability)
      - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers
      - add technicality, synchronization, bias, counterintuition, & certainty objects leading to inevitable collisions
        - error of the collision of compounding forces producing a phase shift
        - lack of attention in one driver and false panic in a second driver leading to a car crash given the bases where their processes originate
      - define alignment on interfaces (compounding, coordinating, parallel, similar, etc)
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
    - examine implementing your solution type (constructing structures (made of boundary/filter/resource sets) to produce substances like antibodies, using bio system stressors)
    - resolve & merge definitions into docs/tasks/implementation/constants/definitions.json
    - update links
    - integrate archive_notes/finder_info/functions
    - de-duplicate logic
      - organize interface analysis logic definitions
        - organize functions in problem/interface definitions, before organizing functions in implementations/*
      - integrate problem_solving_matching.md
      - integrate find/apply/build/derive logic from system_analysis/ & maps/defs*.json
      - separate interface analysis logic into implementation/functions (functions dont need unique info)
      - add functions from workflows & analysis (to do list, questions answered, problems solved, interface definition & functions) as files in functions/ folder
        - organize into primary core functions & list sample parameters (like objects to identify for the identify function)
      - integrate rules from diagrams in patent applications to relevant documents
            

- examples
      - joke mapping insight paths
        - unlikely hypothetical
          - several degrees of assumption chains to generate an unlikely hypothetical (sequence of assumptions from a starting assumption/premise, generating a background story/context)
            - serious + petty + important: 'none of us can figure out why he tucks in his tie'
              - implies that the problem was so serious that a discussion happened to investigate & research it to fix it
              - implies that no one is allowed to ask him or has the courage to ask him directly, implying he's powerful in some way & cannot be questioned, which implies these are his subordinates who are not doing work in order to discuss this, which implies this could cause their work arrangement to be invalid 
            - 'none of us ever figured out why he tucked in his tie'
              - repeated + important: implies that the discussion was repeated bc it was such an important matter
            - 'none of our lawyers or R&D staff ever figured out why he tucked in his tie'
              - important: adds another level of importance in that they hired an expensive legal team to investigate the matter for liability/indemnity/litigation potential as if it made the company look so bad they had to hire a legal team
            - "the tie-tucking survived ex-girlfriends' interventions"
              - important: it has ruined multiple relationships with people who cared about him who tried to stop him from doing this to himself
              - briefer than previous version & uses more evocative verb
              - different: 
                - add assumption: assumption that the audience is rooting for the tie-tucking to continue
                - add concept of 'agency': attributing personhood to the tie-tucking, which is fighting for its life against cruel monsters
            - 'even after being accused of being a double-tucker who tucks his tie but not his shirt, he persisted'
              - important + petty + similar: fashion is a petty thing to care about this much, and a special jargon term 'double-tucker' implies a whole community or sub-culture based on or caring about this issue or related issues, which he has caused controversy in, with added importance by association from term 'double-agent', typically reserved for high-stakes situations like foreign wars, as if he's betraying someone or his heritage or group or people who rooted for him, and rhymes with a curse word
            - 'the mysterious tie-tucker left the board of directors' 
              - important + reduced: condensing the entire story into a brief structure like a nickname and casually referencing it despite the importance implied in a problem that generates a nickname
        - topics
          - conspiracy theory (a muffling device to prevent the Chinese from listening to his balls chafe for blackmail material)
          - cults/ex's (definitely worshiping the wrong things)
        - total opposite: 'your fatal flaw wasn't so much all the excessive drunk online shopping purchases at the police store & the corporate sabotage so much as the curtains from korea that spied on us & posted our arguments to porn sites' (it was absolutely the excessive spending at the police store)
        - changing definitions to very different alternate definition
          - 'tucked in his tie' or 'used unnecessary protection' or 'packed heat'
        - resolving awkwardness
          - 'i dont hate your dick pics (introduces the problem, 'uh oh does she hate my dick pics'), I just think theyre (foreshadowing something that seems like a difference but is actually similar) more optimal when directed at enthusiasts (or professionals), such as doctors/researchers, who might appreciate it more than I ever could (optional: from a curiousity perspective)'
        - mixed contexts/styles
          - talking about an unimportant matter in the same terms used for important matters
            - 'his parents couldnt deal with the idea of confrontation so they gently let him lose touch rather than disowning him outright' 
        - adding relevant structures of meaning like:
          - aligning layers like double entendres
            - calling him a 'magician' bc they have a function of 'hiding scarves' which is similar to 'tucking a tie' bc 'tucking' has a related output of 'hiding'
        - defeating the purpose/self-defeating
          - listing all the manipulations youre using, while using them, to the target 
        - false dignity/over-generousity
          - calling him a 'international man of mystery' bc its a very dignified way to portray having mysterious fashion habits that defy analysis from subject matter experts
          - 'he must be doing it to scare away women bc theyre always chasing him'
        - injecting stupidity/extremes
          - he thought it would act like a talisman to protect him from rape or unwanted pregnancy
          - he was told by a foreign holy man (has association with 'wise foreigner' stereotype) that it would protect him from fertility like a 'cosmic condom' (repetition, catchy) 
        - removing a point/agency (its not an intent, he just had the clingiest underwear/reproductive organs known to mankind)
        - fitting with existing systems without obvious contradictions
          - 'using existing phrases in a new way with minimal distortions' is surprising bc its unlikely to find a new distortion of an existing component that someone hasnt tried, so the simpler the better for this type
