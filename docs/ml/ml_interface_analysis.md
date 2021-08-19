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

    - you generate a new ml algorithm/network when you have a theory about the structures of relevance (feature position, feature structures, feature interaction structures) for a particular data/problem type
      - these relevance structures can be used as variables to generate new ml algorithms/networks
      - interface structures that are frequently useful or specifically useful for a problem type can also be injected as variable values, instead of selecting these variable values by other methods

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

  - since neural network nodes are in between function inputs & outputs, they can be used to represent any structure of 'contribution' (like 'change potential') that could change the output
    - this means all the possible structures that could build/derive/find the output (or equivalent operations like 'filter out what the output is not') can be represented by neural network nodes, structures of them & their interactions
      - this includes:
        - interim states in converting inputs to outputs
        - type identification functions
        - prediction function subsets/alternates/bases
        - solution component/input/describer/requirement templates
        - change types & change structures like sequences, as variable structures
        - prediction components/input/describer/requirements
    - this means the number of network nodes (possible contributing features) & layers (interim conversions to create/filter contribution versions, like an aggregation layer to aggregate features into a different interaction layer) can be derived by determining the features that could possibly contribute to the answer (prediction function) and the conversions (layers) required to create them from the inputs 

  - generating a function set to fulfill an intent can encounter errors after generation time, so injecting 'self-awareness according to responsibility/ability' is a useful structure to apply at the function level
    - a function that can access usage info (the outputs of functions triggering it and the inputs of functions using its output) can identify before an error is encountered if it will produce an error for the functions using it
    - allocating awareness of context in the form of triggering function info based on a function's ability to identify & correct errors is useful at that interaction level
    - cross-interaction level interaction awareness is also useful in addition to intra-interface interaction context awareness, so an application can identify which functions that use it may encounter errors given their input/output structures
    - this is useful in ml at the function & node-level, where a function/node can identify when error structure patterns (like 'deactivation barriers to valuable feature values' or 'incorrect feature structure to identify all possible solution structures') are occurring in adjacent functions/nodes & modify its params like thresholds to account for that imminent error before it occurs
      - this adds error-correcting functionality to the network on certain interaction layers, which can create other error types if the error-corrections aggregate into an error, so network-level error-corrections can be built to handle this emerging error structure from lower layers
  
  - apply useful structures like 'alternative routes' to the ml network problem space by substituting other useful functions that accomplish the same intent
    
    - example: rather than 'feature reduction', apply 'compression' or 'summary metrics' ('average' or other common values or probability distribution) or 'cause/intent/type identification patterns' which also has a high input/output ratio, but retains the input info, which is an important input of other functions eventually applied to the output

    - example of injecting structures of relevance like certainty structures into ml neural networks
      - example of injecting structures of 'obviousness' into a network would be highlighting features manually during pre-processing

    - example of how to identify protein-folding as an important variable in illness: structures of variance (high-variation) and structures of relevance (adjacent to the processes used by various illnesses)
      - this is bc of the:
        - 'structural similarity' between input/output of the function, which is similar in the complexity of the input protein structure & the output illnesses
        - insight that 'variation doesnt just disappear in a system, it has to be routed somewhere, so if there is complexity or variation in inputs, the outputs will reflect that attribute as well, unless a complexity/variation-reducing function like a delete or cause/intent/type identification or compression function is applied between them'

  - identify interface structures that can generate a particular algorithm or interface query as a way of indexing unique problem-solving intents in the ml problem space
      
      - for the example problem 'sum a sequence', multiple interface queries to solve it include:
        
        1. identify minimum info to fulfill the following sub-intents & execute the steps to identify that minimum info for those sub-intents
          - identify various standard sequences like 'random' and 'sum of n * increasingly negative exponent n' or 'sum of factorials' or 'sum of n / (n - 1)'
          - identify distortions of these standard sequences
          - identify efficient method to filter these sequences
        
        2. generate a probability distribution or generative function from a subset & extend that as an assumption for the remainder of the sequence
        
        3. identify filters differentiating a subset of the sequence from other sequences ('opposite' structure, or 'what the sequence is definitely not') & apply to the sums of those sequences (the sum is 'definitely not the sum of the other sequences')
      
      - for each of these queries, the associated priorities/assumptions & other interface structures that allow that interface query to be seen as an optimal solution include:
        
        1. interface structures associated with 'identify minimum info to identify if a sequence is n distortions from a base sequence'
          - assumptions
            - an assumption that the 'minimum info to identify base/distortions is more computable than iterating through the sequence' and that the 'sequence is an adjacent distortion from a known base sequence'
          - errors
            - if a sequence is n distortions from a base sequence and the algorithm only checks n - 1 distortions from a base sequence, this will fail
          - error-handlers (to integrate with interface query or other solution)
            - the base sequences have to have a high coverage ratio, so that its unlikely that the distortions checked will not find the sequence if its a non-trivial number of distortions from a base sequence
        
        2. interface structures associated with 'identify generative/descriptive function of a sequence subset & apply to remainder of sequence to get summary metrics'
          - assumptions
            - that a selected subset is representative of the sequence (that it has a degree & patterns of variation reflected in the complete sequence)
          - errors
            - that the selected subset is not representative of the complete sequence
          - error-handlers (to integrate with interface query or other solution)
            - identify differences between a subset & a sequence that could make a subset non-representative, identify tests for those differences, & apply them as a filter for subsets
        
        3. interface structures associated with 'identify filters differentiating a subset of the sequence from other sequences to apply as a filter of the summary metrics'
          - assumptions
            - that the differences in a sequence are reflected in its summary metrics as well
          - errors
            - that the differences in a sequence are not reflected in its summary metrics (sums/averages can involve neutralizing terms, allowing for significant differences in sequences)
          - error-handlers (to integrate with interface query or other solution)
            - identify patterns of neutralization and tests for these patterns to identify if this solution can be effective, or if there is a subset-selection method that can offset this error (select a subset without a ratio or other structure of neutralizing structures that is not reflected in the complete sequence)

      - this is useful in determining the error types likely with a solution interface query, bc each perspective has known (or adjacently derivable) error types associated
        - this is relevant bc the idea of 'specialization' in generating algorithms for a particular intent/case, or an 'algorithm network' where problems are solved by allocating them to a network of specialized algorithms for various intents/cases, may be a standard structure, but its also extremely inefficient, involving:
          - a high degree of computation
          - dependence on assumptions about prior static solutions continuing to work
          - forced categorization of intents/cases into being handled by one of the algorithms that exists, rather than creating a new solution or adapting solution
        - whats important instead of relying on a static & computation-heavy 'algorithm or ml model network where each network is selected for a case/intent' is to identify/generate/derive the right perspective for a task, so that the associated generated interface queries or other solutions to solve a task with that perspective can be designed with error types of that perspective integrated with the solution
          - where the 'perspective' refers to the associated 'combination of interface structures', like priorities/assumptions/errors, that are associated with an interface query or other solution structure to solve a problem (associated in a 'generative' or 'descriptive' or 'emergent' connection structure)
        - this extends the interface structures used as input to a solution (beyond 'context' and 'intent') to a comprehensive set of interface structures, and connects these input interface structures with the solution in a way that allows generation of more optimal solution structures built from meaning/understanding rather than granular structure-fitting of a problem & solution algorithm that was previously found almost by accident to perform acceptably (or at least better than other known solutions at the time of testing/deployment), a structure-fitting that was constructed from the core layer of available functions without an injected sense of 'meaning' (cross-interface fit)
          - the 'granular structure-fitting of a problem & solution built from the core layer of available functions' method ignores error structures:
            - the input data allows this solution to seem acceptable for those inputs, but the input data is actually corrupted, specific to an unidentified type/other variable, reflects noise, is unlikely, reflects a disproportionate ratio of outliers, or is about to change/has changed by the time the solution is built/tested/deployed
            - the resulting solution algorithm is only effective for some subsets of the input data but cant handle (throws errors for) other subsets
            - the resulting solution algorithm works in general for most problems within a certain range of problem attributes like complexity, but cant handle problems outside of that range, like the problem the original problem is about to convert into, rendering the initial solution ineffective
            - the resulting solution algorithm identifies generally useful objects like certain difference or contradiction types, but it cant handle types of differences or other useful structures that it didnt identify in the input data
          - the first solution found with this granular structure-fitting method of 'apply available functions to form a solution that solves the problem in a slightly better way on some metric than other solutions' is also unlikely to be the optimal solution
            - however the patterns of differences between an initial solution found with this method & an optimal solution to the problem can be applied as a default conversion to any solution found with specific granular problem-solution structure-fitting
              - optimization functions that apply structures of optimization like 'structures of generalization' can be applied to make an initial solution found with available functions likelier to be optimal, to reflect differences between sub-optimal & optimal solutions like 'specificity'
              - other optimization structures include 'unique structures' (to avoid 'repetition' of functionality) and 'integration structures' (to avoid 'acontextual solutions' without a meaningful fit with other solutions that isnt just a case/intent routing function)
        - this offers a 'solution network & "solution network-routing function" generator & integrator (fitter)' as an alternative to a static & computation-heavy 'specialized algorithm/model solution network' as a general problem-solving structure
          - rather than distributing optimizations to nodes in the algorithm network (where each node optimizes a subset of optimization metrics), general optimization metrics can be applied & fulfilled dynamically by generated perspectives (with associated interface structures like interaction functions, core functions, error types, problems solvable, solutions generatable, assumptions, priorities, etc), perspective-solution connections & solution structures, so that errors of a perspective associated with a solution are built in to the solution, and when new errors are identified, the perspective/solution can be re-generated/integrated
          - a variant of this is 'generating the maximally different useful perspectives & associated solutions', rather than building a 'network of solution algorithms composed manually of available functions' from a granular level or generating perspectives & associated solutions dynamically for a problem/problem-solving intent
          - the perspectives that would be useful for solving a problem can be identified/generated as an input to identifying solutions, as a way of avoiding perspectives lacking the combinations of required structures like 'complexity' & 'functionality' required to generate solutions for a problem (such as the static granular perspective leading to a 'specialized algorithm network built for known specific cases/intents')
          - other alternatives to the 'specialized algorithm network built for known specific cases/intents' solution include:
            - generating the 'probable useful intents' (including core intents like 'differentiate', 'identify', 'connect', etc) & building a network of those rather than a set of specific intents constructed manually that would likely have errors like 'overlapping functionality'
              - this has a generative perspective that allows for the 'generalization', 'composability', 'interactivity', & 'flexibility' of intents as inherent to the definition of 'intent', making it more optimal than the 'specialized algorithm network' bc of its integration of the meaning of 'intent', which prevents by default errors of 'intent mismatches'
              - other perspectives integrating other combinations of definitions & interface structures would avoid other error types
              - some error types are higher priority to avoid in different contexts, so a routing function that connects solutions or solution-generating methods based on 'error type avoidance prioritization' in addition to other metrics like 'problem' and 'optimization/solution metrics' and other interface structures like 'assumptions' is a more effective way of connecting solutions/solution-generating methods in a solution/solution-generator network
              - a useful format to structure this is a 'perspective network, where perspectives generate interface queries & other solution-generators'
                - this is a network of perspectives (as 'cross-interface structures with varying levels of structure/abstraction'), rather than an interface network on which queries can be run
                - a network of interface queries to generate this network of perspectives is another useful relevant structure
              - occasionally a perspective in a perspective network may be associated with a granular solution rather than solution generators, like how the above perspectives can be associated with specific solutions or solution-generating interface queries
