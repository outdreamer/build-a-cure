# to do

  - organize new_examples.md
    - identify any examples missing from patents in docs/tasks by diffing patent spec texts
    - organize function implementations, to do list, examples, logic
 
   - create configuration for 2-3 list items every day

      - create compilation script to compile code/config into a network graph on every change
        - add support for equivalent synonyms
        - add conversion to standard vocab

      - finish lists:
        - useful perspectives
          - useful to think of prediction functions as generative functions to select the variable interactions that are most likely
        - interface component definition routes
        - ai structures with supported intents & solution success causes
        - solution filters to apply in functions
        - useful interface components
          - aligning/balancing structures, to solve problems like 'a balance position of structures producing errors when unbalanced'
          - questions formatted as a disconnection between components like causal positions, paths, directions
        - subset indexes of an interface useful for solving most problems (structure indexed by metadata like problems solvable, fitting systems, interactive structures, supported intents)

  - identify useful perspectives

  - add to science
    - cancer cells' mutations might just be some of the more adjacent/common/interactive mutations out of all the mutations that are possible or actually occur with any frequency
      - if this is true & the primary cause, that means these mutations will continue occurring unless actively prevented
        - substances should be examined for mutation-prevention functionality
        - root causes can be addressed as a prevention method, like:
          - the reason mutations occur more frequently for a gene structure (like a gene type, pattern, or set), such as gene position in relation to another structure
          - the host system's inability to prevent malicious interactivity/cascading of mutations that protect mutability & promote additional mutations
          - lack of a substance structure that would prevent or reverse these mutations, or particularly damaging subsets of mutations that enable the others
          - whether signals that enable/activate cancer cells can be routed where mutations are needed
      - examine what mutations almost never occur & determine the cause of mutation frequency (at a certain position on chromosomes, protein folds, relative position to gene types, or other structures on different interaction levels)
      - simulate whether changing position of genes reduces the frequency of mutations of those genes, if position is a variable to the mutation frequency
        - ultimately it should be possible by analyzing components like structures/functionality as combinable attack vectors, to calculate what diseases are possible/probable & will happen given a genome, their metadata like frequency & degree of impact on the host, and the substances/processes/stressors that can prevent or neutralize them
        - genomic data can be enhanced with data from output system & interaction structures

    - the idea of a 'cure' may be invalid, the concept of a 'functional state' may be a more valid goal
      - an example would be rather than returning someone to a prior or absolute state of optimal health, adjust their system to a state where its more functional, even if that functionality is distorted

    - the theory of 'the universe as a simulation' is only now getting popular bc our brain structures & functions are such that we are only now recognizing the influence of physics on human decisions, noticing that we can influence these decisions, and therefore fake them, which reminds us of computer simulations

  - interim functions to build:
    - derive definition routes on various interfaces from a definition
    - apply a standard format (function/attribute/object) to an input
    - derive function intent stack
    - identify error types
    - identify structures of cause
    - identify variable types & structures
    - consolidate repo, remove repeated content, merge similar functions

    - finish processes:
      - finish interface analysis of physics to determine other useful components like efficiencies, incentives, trade-offs, closed systems
      - finish applying interface components (like abstract) to useful interface components
        - core interaction functions of core interaction functions
      - create interface queries of finding useful interface component filters

  - why do structures overlap across interfaces:
    - different interaction types:
      - one interface may define the structure, and another may apply it
    - interfaces may have different definitions of the structure while still referencing the same underlying structure
    - interfaces have other interfaces injected in them by default
      - example: every interface has the core interface injected, bc it has core components
    - there's usually one interface that is the base interface for any given structure

  - add to useful structures
    - intent sequences
      - a 'requirement to survive' is the reason why an animal might develop bright colors, with varying intents:
        - with intent to 'attract prey', bc 'prey are difficult to find'
        - with intent to 'mimic a scarier animal' bc 'theyre not scary enough to disincentivize predators'
        - with intent to 'store excess mutations' bc 'mutations occurred for no reason other than structural damage'
      - the two intent sequences above overlap at the 'bright colors' node and diverge bc of different requirements, given their different positions relative to useful objects for survival (prey, predators, energy storage, change as energy)
      - this is a way to determine alternate causes of the same variable, given useful system objects like requirements & incentives

  - add to solution automation workflows

    - apply pattern-identification methods of differences between solution automation workflows, isolate into difference types, & add to variables determining difference between workflows to generate them
      
      - example of applying differences to generate alternate solution automation workflows (different routes to connect problem & solution)
        - standard basic workflow: 
          - trial & error
        - alternate workflow: 
          - apply 'trial & error' to filtered solution space of 'adjacent' solutions
        
        - the differences between these workflows include:
          - container structure (one workflow contains the other)
          - different position of components (position of 'trial & error' in one is different from position of 'trial & error' in another)
          - one workflow has an attribute applied to filter solution space ('adjacent')
        
        - these can be reduced to known interface component variables, even if the variables interact in a new way thats different from other workflows:
          - 'structure' variable including structures like containers & positions
          - 'workflow component' variable including other workflows, solution spaces, solution metric filters
          - 'core component' variable including attributes/functions/objects (like 'adjacent' attribute, which is relevant to intents like 'finding solutions quickly' or 'finding feasible solutions with existing resources')
          - 'interaction function' variable including interaction functions like 'apply' & 'filter'
        
        - so an example of generating a workflow from another workflow using differences between these two example workflows would involve applying three logic rules that can be used to connect the two example workflows, which can presumably connect/generate other workflows:
          1. 'apply workflow components as inputs of core interaction functions'
            - example application of this rule:'inject one workflow into the other'
          2. 'apply relevant core components like attributes to workflow components like the solution space to generate a different workflow'
          - apply any remaining general logic rules once the workflows are generated:
            3. 'filter generated workflows by whether they connect components in a way that can connect problem input & solution output'

        - other differences between alternate workflows may identify other variables that can be used to generate one workflow from another

        - solution success cause: why does this method work to generate different workflows?
          - analyzing 'differences' between workflows is by definition relevant to identifying variables between workflows, which can by definition be used to generate them
          - one workflow is a more abstract version of the other, and varying abstraction level is by definition applicable to many contexts like inputs, within a range

        - given these solution success causes (inputs of success of the solution), we can derive other methods to generate workflows:
          - 'abstract a workflow within a certain range of abstraction' (so it doesnt lose its meaning)
          - "apply definitions of relevant components to workflows like 'differences' with an interaction function like 'generate' that is relevant given their definition like 'variables'"

    - derive & apply workflow template/structure to fill with workflow variable values once interface analysis is fully applied to workflows
      - this means once components like standard/base workflows, common workflows & workflow patterns, & workflow variables are identified
      - this is an alternative to writing static function logic to design interface queries

    - derived alternate merged interfaces (like the meaning interface) to avoid sub-optimal metrics inherent to each interface perspective, where the problem can be adjacently solved
      - the 'survival' and 'evolution' perspectives have their own disadvantages, so merge them into an interface to avoid these disadvantages
        - 'survival' disadvantages include errors like 'over-identifying threats', from survival functions like 'constantly checking for threats'
        - 'evolution' disadvantages include errors like 'excess change, incompatible with other changes', from evolutionary functions like 'gene modification/activation/addition/movement'
      - applying the survival function 'check for threats' to identify a threat of the change type that is 'incompatible changes with other changes' is one way to merge those components on these interfaces (using the error of one interface to fix an error in the other interface, assuming no other errors are adjacent in these merged positions)

    - apply definition of any other components of the workflow that havent been applied in other solution automation workflows or workflow-generating workflows
      - an 'insight path' is a 'shortcut to find new useful info' so apply the definition of 'shortcut'
        - by definition, its a method that requires less work
        - so generate methods requiring less work as an initial solution space
        - solution success cause: this works bc of the overlap between the definitions of adjacence and efficiency
          - paths are 'efficient' bc they require less work, meaning they may use 'adjacent' resources (nodes or methods)

    - identify the shortest, lowest-cost, most adjacent or otherwise most efficient/optimized route/function to known solutions from problem definitions and identify patterns in these routes or the variables/components/structures/formats enabling them to be optimized (sub-interfaces, definitions, interaction levels), and generate function to iterate through those patterns based on usefulness for a problem definition, and apply those patterns

    - apply trial & error except with the injection of the concept of 'solution progress' as a filter of multiple methods attempted in parallel, derived from maximizing difference types based on filter capacity (solution progress assessed similar to learning from error/cost)
      - identify the most different structures you can apply (like directions of motion) and apply them iteratively, checking for progress toward the solution metric based on solution patterns of progress (accept costs of these types up to a particular threshold or other structure), and stopping the pursuit of any differences that dont match solution progress patterns

    - identify & apply alternative inputs (variables) of solution automation workflows to create other workflow-generating workflows, given the definition of 'generative' meaning 'an input to', and given that this workflow for the default inputs (variables) of workflows is already stored elsewhere, so this applies 'alternative' as a transform
      - example of alternative inputs:
        - to identify that a method is especially useful out of all the possible methods, you can use alternate variable sets:
            - start with solution metrics as limits creating the structure/template of a solution, and fill it in or work backwards
            - common components of useful solutions, or components of commonly useful solutions
            - adjacent combinations of available resources at the origin state (problem position)
            - core interactive components
          - these are alternates bc they have equivalent/similar input/output when applied to this problem of 'identifying a useful method in a large set of possible methods'
        - a function (structure of connections between specific inputs & outputs) can have alternate formats like:
            - a set of filters
            - a set of differences
            - a set of intents
            - a set of requirements
          - these are alternate versions of the function that dont lose info expressed by the function, and they can serve as alternate inputs to the function outputs, since the function itself is also an input

    - iterate through optimization priorities & apply other optimizations to workflows, like 'find alternatives to optimize for robustness', which when applied to workflows would generate the previous 'apply alternative inputs to workflows' workflow-generating workflow

    - apply useful interface components (like 'interactivity', 'ambiguity', 'incentive', 'contradiction', 'requirement') to fulfill core interaction functions (like connect, complete, reduce, merge) with interface structures for optimized querying
      - fulfill optimization intent 'avoid full interface standardization'
        - map interactive structures across interfaces for queries that support avoiding full interface standardization
        - map corresponding structures across interfaces to avoid standardization to an interface in case an isolated operation like 'identify one object' is needed
          - this allows for an efficient interface query that executes only the conversions necessary & keeps the processing on one base interface, pulling in isolated structures from other interfaces with sub-queries as needed

    - standardize interface queries & solution automation workflows to other interfaces (to avoid converting problem system to a particular interface just to implement a workflow)
      - apply other interfaces like 'structure' interface to specify a query/workflow and interfaces like 'concept' to abstract a query/workflow

  - finish list of useful interface components, including structures of useful interface components (like structures of specific useful concepts)
    - example: 'apply concepts to system interface to identify conceptual structures in system'
      - system
        - system structures of uniqueness: exclusivities
        - system structures of power: trigger, input

  - finish interface query design rules
    - 'if solution requirements arent given, derive/predict them or apply default requirements from related/similar problems'

  - example of different structures of an interface component on different interfaces
      - alternative
        - 'structural alternative': where one or more structures are options where one or the other or both if not mutually exclusive can be chosen (applied at a given time), with varying relevance/optimization, for a particular intent (like 'navigate in a direction', having structural alternatives in the form of a set of paths)
        - 'conceptual alternative': where one or more concepts can be applied at a given time with varying relevance/optimization for a particular intent (concepts with an intent in common)
        - 'structural conceptual alternative': alternative conceptual structures, like varying structures of power or balance
      - alignment
        - 'structural alignment': based in the structural interface, where a 'structural alignment' takes the form of an equivalence/similarity in components (attributes/functions/objects/structures), such as:
          - interchangeable attributes/functions/objects
          - a fitting/matching structure
          - a parallel structure
          - a structure having similar shape or other attribute like size
        - 'conceptual alignment': translated to the conceptual interface, an 'alignment' takes the form of concept such as 'equal' and/or related concepts like 'similar'
        - example of injecting the structural interface to components on other interfaces:
          - a 'structural conceptual alignment' is the 'alignment' in structures of concepts, like 'similar conceptual connections' or 'equivalent concepts'

  - document useful component/sub-structures of interface queries (interface components, interaction rules, cross-interface interactions, generative functions)

  - interaction rules of useful cross-interface or useful interface components (efficiencies/alignments)
    - to answer questions like:
      - with what 'frequency' can a 'random combination' of 'alignments' create an 'efficiency' in a given 'system'?
    - having variables:
      - solution formats
        - certainty (probability, frequency, average) 
          - format solution as 'certainty of a particular structure given inputs' rather than other formats like 'method to generate a particular structure given inputs'
      - solution filters
        - requirements
        - intents
      - problem space
        - system context
      - interactions
        - applicable connecting logic rules
        - attributes (random, adjacent, difference-maximizing, similar, opposite)
        - structures (combination, subset)
      - interacting components
        - useful components (alignments, efficiency)

  - identifying useful cross-interface interactions

    - examples:
      - 'merge difference types' function
      - 'common relevant efficiencies' structures
      - 'find simplifying/generative/change-generating function' function

    - how to identify useful cross-interface interactions:

      - structures of useful components from one interface applied to another interface
        - example: useful structure interface components (combinations) of useful system components (incentives, ambiguities) applied to other interfaces

      - useful interaction structures of relevant problem-solving structures (like core interface structures or problem interface structures like errors)
        - 'merge' is a useful interaction structure of error structures like 'difference types'
        - 'common relevant efficiencies' combines multiple useful interface structures/attributes to create a useful structure for 'fulfilling an intent', which is relevant to 'problem-solving'

  - document useful structures & generative functions of cross-interface interactions (like structure-concept interactions)
    
    - example:
      
      - structures that generate function to 'merge difference types'
      
      - structures with conceptual attribute 'relevance':

        - a 'database index' structure gathers & searches just the information useful for 'find' intents based on structures of standards like 'what is commonly searched for' and 'what varies across data' and 'what combination of fields uniquely identifies/differentiates data', so it can be used to fulfill intents like:
          - intent: 'identify unique records'
            - fulfills 'unique combination' standard
          - intent: 'find records quickly by only searching relevant data'
            - fulfills 'what is commonly searched for' standard
          - intent: 'differentiate records'
            - fulfills 'what varies across data' standard
        
        - applying the above structures of standards as solution filters can find the 'database index' structure in the 'search database' problem space

        - the solution creates an efficiency for the 3 'search database' intents, while creating inefficiencies for the 'minimize storage' & 'generalize solution' intent
          - these intents could be fulfilled with modifications to the 'database index' solution:
            - 'minimize storage': store static values in a nested index
            - 'generalize solution': apply 'database index' solution dynamically or for other queries or query types

        - interface query to generate implementation of this cross-interface interaction
          
          - identify variables
            - core variables
              - data set format
              - data set stores
              - data set store format
              - data set store fields
              - data set store records
              - search method
              - sort method
              - storage method
              - query
            - variable combinations
              - data set/store-query relation
              - search-sort relation

          - apply requirement filters to solution space:
            - iterating data of some format is required
          
          - apply variable expansions to solution space:
            - apply probability interface to 'input/output formats' structure: 
              - data doesnt have to be in original input format or output format of 'common' queries
            - apply change interface to 'input/output formats' structure: 
              - data doesnt have to be in a static format
            - apply structural interface: 
              - data can be in 'multiple' formats
              - data 'subsets' can be stored in addition to the 'complete' data set

          - apply structure filters: 
            - what structure in the 'search database' problem space can identify unique field combinations, enable quick searching for common searches, and differentiate data (even if it differentiates them incompletely, or to a contextual definition of 'differentiate')

            - apply differences to variable values to generate core adjacent combinations of variable values
              - store subset of rows for a query type (search only these rows for queries involving these fields/operations/conditions/values)
              - store subset of fields (search only these fields)
              - store subset of example rows with allowed variation (search for these examples for these queries & anything adjacent to the example)
              - store data patterns to search for a query (search for these patterns for these queries)
            
            - filter combinations by usefulness for 'search database' problem intents
              - apply filter with 'system optimization' ('only add required functionality')
                - which of the combinations fulfills the above 3 intents without fulfilling extra unnecessary intents (aligned demand/supply of intents)

  - ml explanation of finding coefficients of prediction function by applying distortions to coefficients & ruling out distortions that dont contribute to prediction accuracy
    - can be optimized with reductions like:
      - 'calculating the most different distortions that will reduce possible values the quickest & applying those distortions'
  
  - proof/determination structures
      - what makes something possible to determine/calculate
        - a solution structure where the solution metric is clearly defined (structural or having other structures of certainty like consistency or inevitability or requirement)
          - checking a path to see if it includes a node twice is clearly defined (it uses the structure of 'node visit counts' in the 'path' solution structure)
      - what makes something difficult to prove
        - where there are ambiguities (lack of certainty/structure/definition) between the input parameters & the output function value
          - ambiguities such as where multiple inputs produce the same output, like how different x-values can produce the same y value on a wave function
      - useful proof structures
        - apply possible components to create an absolute or scalable definition include components framed in terms of interactions with other components that can be used with a consistent measurement (like a stable structure across interfaces or dimension sets) & can also scale (boundaries), rather than framing them in terms that can have different meanings at different parameters (closed, hollow)

    - add to causation variables
      - ability to change (if a variable cant be changed, it is less causative for problem-solving intents)

    - give examples of identifying vertex variables
      - general vertex variables: topic, origin/destination, reason/cause/point/intent, errors, variables, types
      - comedy vertex variables: sincerity, stupidity, stakes, tension-resolution/expectation-subverting pattern variation
      - music vertex variables: tone, tension-resolution/expectation-subverting pattern variation, lyrics
      - optimization metric vertex variables: solution metric patterns (what other solutions optimize for, to determine optimization metrics to apply)

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
  - determine core graph variables (definition of adjacence/difference, connectivity, dimensions, info storage methods, interactivity of structures like sequences)
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
