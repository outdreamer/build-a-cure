# to do

  - add to structures
    - multiple causes of the same variable

  - structures like origin/destination points, loops, layers, boundaries, & paths for solving problems (like logistical resource allocation, adding variable to an automated process, or finding search path (sorting))
    
    - 'logistical resource allocation' problem
      
      - 'select a delivery method' problem

        - deliver to local warehouses rather than centralized warehouses & customers pick up (warehouses, stores, or locker boxes)
          - becomes a 'pick-up schedule allocation & reminder timing' problem
          - search version: decentralized data stores, CDN's, cached data, indexes based on common request metadata shared locally
        - deliver to local drop-off points rather than local warehouses (dropboxes in neighborhoods, like a designated safe house)
          - becomes a 'trust neighbor' problem
          - search version: decentralized servers hosting services
        - crowdsource using existing routes used for other errands
          - indirectly paid favors from social network
            - becomes a 'favor repayment finding & distribution' problem
            - search version: using patterns & other crowd-sourced knowledge to direct search or as a data source
          - directly paid favors from app network
            - this then becomes a 'ride-allocation & route-finding' problem
            - search version: paying for expert search routing
        - deliver with drivers & cars (standard method, other than using government delivery service)
          - becomes a 'fund car investment, monitor & insure drivers' problem
          - search version: fund investment in discovery/testing infrastructure, to test for & find info directly with experimentation
        - deliver with drones
          - becomes a 'test tech to avoid causing damage or being damaged and navigate regulations' problem
          - search version: build discovery/testing tools that can be purchased by users or run by groups/organizations
        - deliver to vault inside or near home
          - becomes a 'vault access & integration' problem
          - search version: distribute data based on permissioned access and intent
        - sell resource-generation tools (3d printing, gardening, other machines to produce products)
          - becomes a 'import product to resource-generation tool format' or 'create resource-generating tool for this product' problem
          - search version: tool to automate connecting question/answers with available methods like testing tools, applying patterns, or AI
        - sell info on how to build products (either original products or resource-generation tools)
          - becomes a 'index info & write clear documentation' problem
          - search version: info response to query is instructions on how to find info from data sources with other queries or processes
        - change delivery strategies based on how local conditions interact with global conditions
          - becomes a 'integrate local & global context like state/rules/processes' problem
          - search version: integrate search methods based on available resources, imminent/adjacent resources, reasons not to use resources, meaning of resource metadata like position, etc
      
      - 'select a route-finding method' problem
        - allocate delivery method components (origin, destination, method, required method resources), resources to be delivered, & assign costs

    - 'finding search path' problem

      - identify metadata of info being searched for (type, content, perspective, structure, purpose/intent)
      - identify info variables to generate info structures (completeness, language/phrasing, containing structure formats like lists, adjacent info structures found with the info)
      - identify info structures (partial info, info pattern, info beginning, info keywords) to search for
      - generate search strategies
        - search for info structures (content)
          - search for adjacent info like links to constitution when searching for text of declaration of independence
          - search for info structures like law reference format 1.2.3 or law keywords or law-specific terms
        - search for opposite of not-info structures (filters)
          - exclude logical fallacy structures when searching for facts
        - use patterns of previous searches with similar inputs
          - use patterns of previous searches for similar topic or similar keywords or similar intents
        - search for relevant info containing structures (template containing content, html structures, logical trajectory like a 'intro-explanation-summary' sequence structure)
        - search indexes of info, organized by most efficient 'input keyword' to 'output content link' relationship
        - identify need for new efficient keyword-content link relationship, predict most efficient relationship, create new index for it, & search the index while creating it to optimize for future queries
        - predict likely sources of info & select interim points in likely sources to start search in (search at intervals of size n within likely sources of info)
      - select between search strategies
        - randomly select search strategy
        - diversify across search strategies until gains clarify optimal strategies to invest further searching in
        - dont search, just index info to optimize for this query
          - index info in a way that identifies possible uses/intents that apply to the query, and identify intent of search & conduct the search by the intent index going forward
          - example: 
            - if 'cost of product x' is a common query, index products by cost attribute by default
            - 'why does x happen' indicates a need for a 'cause' index ('cause' is the object being sought)

    - structural similarity of logistical resource allocation & search path-finding problem
      - allocating efficiencies & investments in various processes (like building, indexing info, moving resources, allocating resources to operate on resources)

    - 'adding variable to automated process' problem

        - identify timeline of solution lifecycle (when it will & wont be needed)
        - identify impact on related processes, based on interactions or common variables/inputs/outputs/dependencies
        - identify if a solution can be re-used for another process
        - identify existing functionality that can handle the task (configuration options that can do it like a database field type or built-in validation)
        - identify abstraction layer to inject variable at (whether to parameterize function, split function, copy function & modify logic to handle new variable)
        - identify if components (variable, function using variable, etc) are necessary or if connecting other components would resolve the problem
        - identify position of logic to inject variable at
        - identify format structure benefit/cost (keep in database for query advantages, store in csv's for data version tracking, store in dataframe for filtering query-like capacity)
        - identify problems to solve for each solution (add a variable, change function conditions to use parameter, etc)
        - identify optimizations like storing info & logic in as few positions as possible, ideally in one place
        - identify tests
          - structures of components:
            - variables
              - function parameters
              - assumptions
              - dependencies
              - context
            - variable values (ranges, types, sequence, uniqueness)
            - variable structures (components that use variables, like indexes made from a column, code modifying/using a column, or functions calling a function or using the same input elsewhere)
            - variable structure variables (how many conditions allowed in a condition statement, or levels of nesting allowed in a dictionary)

  - add to definitions
    - reason as source cause node ('this happened because of this causal factor')
    - intent as target cause node ('this happened because this intent was the goal used as a cause of the agent's decisions')

  - add to causation variables
    - ability to change (if a variable cant be changed, it is less causative for problem-solving intents)

  - add to false similarity examples
    - set of interactions that are unrelated but appear correlated

      - examples
        - system B has an output that is structural similar to outputs of system A
          - interactions of system B that happen at a later time but their interim outputs may have a structural similarity to the outputs of system A
        - system B may cause a similar or equal output to that of system A, for a different intent/reason
          - if the output is used as a metric, they will seem similar or related

      - efficiencies are a reason (source cause node) that structural similarities occur
        - efficient structures follow patterns that may produce similar structural outputs

  - add to connect function examples
    - how to map connections between two systems
      - standardize structures (like sequential structures such as time), standardizing to either system's structures, interim structures, common structures, interface (like system or core) structures, contextual system-containing system's structures, etc
      - abstract to patterns (like type, cause, system structures)
      - conversion functions (like remove, apply, connect, define)

  - map gravity to similarity (in position) as a calculation efficiency, where calculation efficiencies (like how to minimize surface area or how to apply a key to decrypt info) are an input to information
    - gravity between bulk/boundary creating the mapping of equivalent attributes
      - gravity as:
        - the average or highest-weighted path of interacting paths
        - structure of efficiency through organization 
    - definition: 'structure of minimized surface area as a component of 'entanglement' connecting function of two boundary points'
      - reduced mapping (minimized surface area) is a calculation efficiency to determine boundary position
        - this reduced mapping could be used to connect boundary positions (or their components like an attribute)
    - entanglement as an efficiency to handle risk of information destruction or to handle over efficiency (distribute efficiency (in the form of information) across multiple points)
      - use a mapping efficiency to connect distributed info with structural similarities
    - particles lose their adjacence/similarity bias/efficiency inside the black hole
    - "highest-weighted path from point a to b is the most efficient space-time path, which is not always equal to the 'classical physics' space-time path" (find examples of intents that classical physics is not efficient for)
      - is quantum physics using a different definition of efficiency/similarity or is it using another priority (like energy storage vs. energy usage)
      - how do weighted quantum paths interact with the weighted paths of other particles
    - nonlocality/entanglement as a calculation efficiency in the form of the replica trick
    - wormholes as:
      - calculation efficiencies
      - radiation given off of calculation efficiencies, removing information or filters preventing possibilities
      - sequence of a lack of filters preventing possible paths
      - interfaces (connecting standardizing functions)
      - hidden variables/differences (masquerading as similarities)
    - 'replica trick' as:
      - a way of transferring energy stored in sequential repetition (one coin outcome repeated a number of times in a sequence structure) to energy stored in distributed equivalence (two coins having equal outcome)
    - time as:
      - energy store
        - if time exists, it means change is possible, because energy has been organized in a structure that allows change to occur, meaning structures have developed, meaning efficient structures have been found (organization of energy formats)
        - can you attract other spacetimes so theyre adjacent by storing energy in a way that is adjacent to their storage methods

  - give example of deriving formula with definitions of components 

    - problem metadata

      - problem statement (formula to derive):
        - expected value of the random variable f(x) = actual average of distribution

      - definitions of components:

        - average definition: 
          - sum of all values divided by number of values

        - expected value definition: 
          - average of all possible values, weighted by probability of each possible value
          - expectation is linear

        - p(x) probability density 'distribution sample' definition
          - independent & identically distributed values

      - solution statement:
        - independently & identically distributed samples (data points) from a distribution inside the boundary of the area to estimate, divided by the total number of data points in the distribution is a way to fulfill intent 'approximate area inside boundary'

    - definition connections

      - identify 'probability' as a useful concept to map to problem space:
        - because of structural similarity in probability structures & problem definition (proportion)
        - or as a useful method to find a representative subset to avoid trial & error (or combinationatorial) calculation of area

      - connect concepts of core components ('probability', 'average value', 'sample size', 'data points', 'area') using definitions
        - this should produce the concept of 'convergence' as sample size variable is changed & average value approaches actual area

      - definitions of concept interations
        - 'area' is a related concept to 'probability' when:
          - data points are mapped to possible outcomes
          - problem-solving intent is either:
            - general structure: estimate the proportion of a subset relative to a whole
              - specific structure: estimate the probability of a subset of possible outcomes relative to all possible outcomes

    - alternate routes to derive formula

        - apply conceptual structures

          - apply 'opposite' structure
            - probability of being in the area to estimate
            - probability of not being in the area to estimate

          - apply 'random' structure
            - reduce 'trial & error' solution structure in this problem space of 'testing all possible points' to a subset of all possible points
              - how to select a subset of points
                - extreme points
                - evenly distributed points
                - random selection of points would produce a representative sample of points in a bounded area with increasing accuracy given increasing number of points
                  - randomly distributed points are a way around trial & error of all possible points

        - generate counter-arguments (questions) as filters to reduce error types

          - question every decision, with decision defined as 'variable selections that impact future decisions (future variable selections)'

            - variables

              - method of selecting points
                
                - beginner question: 
                  - why not just generate integer or .1 points starting at origin until all possible outcomes have been covered by an even lattice of points
                - beginner answer:
                  - this introduces bias in the form of an anchored starting point & applies unnecessary meaning to the sequence of points added, which means estimates with low number of points would be biased towards the area around the origin graphable with that number of points
                  - this bias represents a structure of certainty, rather than a way of estimating probability, which by definition is uncertain
                - generate beginner question
                  - apply error type "lack of concept of 'probability'" (indicating an uncertainty like a random distribution, rather than a certainty like a constant in the form of an origin)
                - generate beginner answer
                  - generate differences in between structure posited by beginner and actual requirements
                    - meaning assigned to the origin/sequence is unnecessary and even the opposite of what is required (independent samples that are not connected to subsequence samples in the sequence)
                
                - advanced question:
                  - wouldnt this take a lot of data points to converge to the actual mean

        - apply concept of 'probability' to 2d graph problem space to solve the problem of 'estimating 2d scalar multiplication or summing of 2d scalar multiplication' 

          - probability definition route: 
            - observed x outcomes in proportion to all possible outcomes = probability of x outcome

          - applied concept of 'probability' to 2d graph problem space: 
            - subset of 2d structures (points) in proportion to total set of 2d structures (points) = bounded area


  - resolve definitions of components so you can finishing organizing useful structures like combinations of concepts such as "format sequence", "solution automation workflow", "insight path", "reverse-engineer solution from problem requirements or opposite structures", "connect problem & solution"
    - example useful structures with type stacks
      - format sequence
        - type of structure
        - type of structure that is useful for connecting origin/destination formats 
        - type of structure that is useful for connecting problem/solution formats 
      - solution automation workflow
        - type of insight path
        - type of insight path that is useful for connecting problem/solution
      - insight path
        - useful rule to derive/find/generate insights in a system
      - reverse-engineer solution from problem requirements or opposite structures
        - specific example of a general insight path (like a structural strategy)

    - example connections between useful structures
      - a format sequence can be used to connect any structures
      - an insight path can be used to connect some structures relevantly/efficiently/usefully (like problem/solution structures, input/output structures, origin/destination structures)
      - a solution automation workflow can be formatted as a format sequence

    - example meaning of connections between useful structures
      - because a format sequence can be a connecting structure, it can be used to implement functions with 'connecting' intents

    - change variables to check & complete definitions of interactions between components
      - variables
        - components used:
          - structures: filters, sequences, formats
            - variables: variable selection sequence
            - structures: format sequence
            - functions: conversion/connecting function sequence
        - origin/destination points
          - connect context to problem/solution:
            - start from system in which problem & solution occur (given solution potential) and fit/connect systems gap structures to problem/solution structures, rather than starting from problem & navigating to solution or connecting them in the middle or working in reverse
              - 
          - connect solution components to solution
            - start from existing solution structures & apply filters or other structures to reach solution
          - general form of 'filter connecting sequence': 
            - apply structures of standards such as filters to both/either problem & solution until theyre equal (meaning connected, or similar in structure like position/variables)
    - change variables to complete definitions of interactions between components
      - origin/destination points
        - connect context to problem/solution:
          - start from system in which problem & solution occur (given solution potential) and fit/connect problem/solution structures to system, rather than starting from problem & navigating to solution or connecting them in the middle or working in reverse
        - connect solution components to solution
          - start from existing solution structures & apply filters or other structures to reach solution
        - general form of 'filter connecting sequence': 
          - apply structures of standards such as filters to both/either problem & solution until theyre equal (meaning connected, or similar in structure like position/variables)

  - example of how to generate monopoly case arguments
    - change variable 'location of power':
      - spotify is welcome to build their own app store with their own phones or team up with their coalition to do so
      - add variable 'time sequence' to 'location of power' change:
        - if spotify operates an app store someday, they will set rules to benefit themselves too, just like theyve done in the past
      - offer an alternative to charging app store rate
        - is there a one-click button to migrate from spotify to apple that could replace any difference in taxes on spotify
    - apply conceptual definition filter 'does concept of persecution (and related components of the definition like focus) apply to the behavior (does behavior have a specific target that is the focus of persecution)'
      - are apple's rules applied exclusively to spotify? if not, it's not anti-competitive behavior
    - apply intent filter
      - is spotify's mission nobler than apple's
    - apply system cost-benefit analysis
      - what features were improved bc spotify exists? are those features worth anything or required needs? did they develop those features better than competitors?
      - if spotify is just charging rent on a catalog, are they adding value to the market, so they should be allowed to dictate the market at all?
      - what products/features would apple develop if they didnt have to pay a fine, and what are those features worth, and are those features required?
    - apply logical fallacy filters
      - apply 'hypocrisy' filter
        - apply 'anti-competitive' conceptual definition structures & test if these structures fit the opponent
          - does spotify plan on raising prices at some point or will they keep prices low even if the app store rate holds? are they only keeping prices low to dominate the market & plan on raising prices later? isnt that anti-competitive behavior?
          - if they are so concerned about anti-competitive behavior, why arent they trying to compete by building their own app store? isnt there a risk that the apple app store is sub-optimal and needs to be improved with competition from spotify

  - example of calculating possible functions with core functions applied to function structures like combinations (convolution of function structures)
    - ai functions
      - categorize
      - generate text
      - falsify realistic data
      - identify anomaly
    - core functions applied to ai function structures
      - ai function structures
        - ai function combination
          - categorize & generate text
          - structures generated by core function applied (a convolution of a function structure using core function operations)
            - categorize text generated by an algorithm
            - generate text of a category function input
            - generate missing interim category text
        - ai function sequence
          - falsify realistic data, categorize, generate text
            - falsify realistic image to fool a categorizer used to generate standardized text

  - example of calculating possible questions/problems that are solvable using metric filters
    - convolution of metric structures to determine what can be measured
      - example metrics
        - specificity of solution
        - reusability of solution
        - accuracy of solution
      - example metric structures
        - apply metric filter combination as equal priorities
          - specificity of solution & reusability of solution
        - apply metric filter sequence
          - reusable solution, specific solution
      - example problem structures that can be solved with metric structures
        - a problem of 'find approximation' can be solved with metric structures like accuracy & specificity':
          - apply filters of specificity (to make sure the problem solved is the right problem to solve, like 'find an approximation for a prediction function' rather than finding an approximation for another object)
            - apply filters of accuracy (to make sure input/output values are within a range that can be fit to the definition of accuracy in the problem space)
          - in other words, because we can measure specificity & accuracy, we can solve problems like 'find an approximation function'

  - example of calculating possible error types 
    - error type:
      - alignment of structures can from an unpredicted error
        - core example: stacking layers in a filter opening can eventually fill the opening, preventing the filter from working (arteries lined with fat)
    - apply structure of error type to AI problem space
      - multiple stacked or sequential pre-processing alignments of data that standardize data too much and make the data so homogeneous (self-similar) & similar to the filter node's threshold value that everything passes or fails, or pass/fail is equally likely

  - exploit filter structure examples:
    - anomaly
      - non-standard data flows
        - does data normally follow this pattern
    - requirements
      - is there a required basis for communicating info
    - intersection:
      - data * time/sequence
        - state/content of a data flow intersecting with a possible access chain
    - code x time/sequence
      - state of a build to check intent multiple times during build phase of code

  - bio system general strategies
    - calculate & inject vulnerability in pathogen dna language
      - trial & error implementation example: 
        - use dna code switcher to apply change to all positions in pathogen dna
      - common pattern implementation example:
        - inject known dna error types to see if any work on new pathogen
    - standard pathogen dna to host dna language

  - a nn that fails when its original training set 'clues' are gone can identify:
    - alternate variable sets to generate predictions to use in cases without information
    - differentiating functions to separate those variable values to make them clearer & the predictions more accurate
    - variables, variable operations & variable structures that can be applied to generate more accurate predictions, given a lack of information

  - calculating a flow field numerically can be optimized by calculating:
    - possible/probable/fitting components of functions 
      - connections between prior calculations, to find connection structures that re-occur, as the output of a function
        - find core connection structures like waves, peaks, inflection points
      - connections between connection structures, to find: 
        - patterns in connections between:
            - identified patterns of difference, like degree of difference observed between adjacent points
            - structures of approximation & accuracy (what kind of structure could add prediction accuracy, in what contexts)
            - base functions & base function components & useful/stable functions
            - similarities in structures of difference, between function structures like variables & error structures like distortions
          - variables of & distortions to those variables common to connection structures & connections of those structures
        - connection components that coordinate for some intent
          - intents like calculation in an input/output sequence, or fitting into a structure that is efficiently compressed or retrieved
            - incentivized connections that are optimal for some calculation intent
      - generate & test predictions of future calculations, to find local/adjacent prediction functions
        - generate set of prediction functions to test predictions
          - apply operations & structures known to produce common connection structures to calculations in reverse to derive possible function components
        - generate set of prediction function filters (extreme prior connection structures) to select prediction functions
        - generate set of opposite structures (like non-adjacent points) to test predictions
    - filters of functions (reduce solution space of possible function & function components)
      - filtering functions by these connection structures & patterns, filtering out functions that wouldn't adjacently produce these connection structures
    - interaction structures of functions & function components
      - function components that can interact by coordinating, vs function components that invalidate each other & can't coexist absolutely or be adjacent locally/directly
    - function & function component causal structures
      - apply patterns of causation between functions (function of structure A causes function of structure B) to identify the level of cause a function is based at

  - relevance attribute filters to determine cause of x
    - exclusivity/specificity
      - could this component be the cause
      - what else also has this attribute/function/component without the cause (what else doesnt have the component but still causes x)
    - intent
      - does this component indicate agency or other direct/clear intent
      - could this component be accidental (not useful or not used) vs. intended (is it useful to some degree for some goal)
    - requirement
      - is this component required or optional
      - could the requirement be the cause
    - expectation
      - what is the expected/standard component
      - could the standard or the distortion from the expected/standard component be the cause
    - commonness/uniqueness
      - is this component common or unique
      - are unique components the cause, if common components don't cause x
    - input/output
      - is this an input or output
      - can the output be the cause, if the goal causes it
      - can the input be the cause, if another input wouldn't cause it
      - can the function be the cause, if any input would cause it
    - system context
      - can the system be configured to not need the component (is the system or system configuration the cause of x)
      - would the component be re-generated if you removed the component or the direct cause of the component
        - would the component be created anyway, even with a minor barrier
        - is the component incentivized in the system
        - how much work would you have to do to prevent the component from being generated in the system (it would be created unconditionally, or in what percent of conditions)
        - does that work change the system to an extreme degree (changing its identity/type/intent)
    - change.structure:
      - opposite: can the component be changed to not cause x
      - symmetry: do changes to the component still cause x
    - potential.structure
      - alternatives: are other structures like combined errors capable of causing x
      - are those structures possible in the system (do they exist in the system)

  - identify probably useful (relevant) structures of organization that integrate interface objects for a problem type
    - standard structure for solving a 'find variable connection' problem
      - variable structure in a common format or standard format with connection structures (network) 
      - using 
          - equal as a base function to generate the origin network structure differences (position)
          - causal direction
          - type
          - core functions as sub-components

    - how to generate a standard useful cross-interface structure of organization
      - find connection change structures (variables):
        - type is relevant bc variable types have direct connections (like 'variable of one data type like boolean likely to be connected to another variable of a data type like condition')
      - find connection core structures (components):
        - core functions are relevant to build new connections where info is missing about a connection
      - find connection interface or structure structures (standards, filters):
        - equal positions of variables are likelier to find differences (distortions from equal) faster than starting from an extreme positioning function
      - find connection structures associated with interfaces (direction structure associated with intent):
        - causal direction is directly defined to be relevant in the 'connection' definition, which implies an input/output connection, inputs being liked to 'dependency', which is linked to 'cause'

  - integrate objects/.md text with interface implementations

  - apply to structures

    - concept of attention in structures
      - mixed interim high-variation & high-similarity structures tend to maximize attention
    - examine conflating intent & requirement
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
      - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially determined in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.
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
            
