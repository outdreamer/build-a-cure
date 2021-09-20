# to do

  - how to derive 'apply differences to inputs to see if they can change the output to see if the solution is true'

  - add impact of methods on various network types given the differences in method/network structures & include assumptions

  - how to derive the rule 'choose algorithm with low bias/high variance for large data sets'
    - use 'random forest' bagging method to reduce high variance
    - high variance is a problem when a sample data set is not representative of the population, producing accuracy for the training data subsets & errors for all other data subsets
      - if a data set is relatively large in relation to the population, the 'sample data set is not representative of the population' is less likely to be a relevant problem
      - 'variance can only be reduced by averaging over multiple observations, which inherently means using information from a larger region'
    - high bias is a problem when sample data sets differ from the population mean by a lot, producing errors for most samples unless they happen to be represented by the general model
      - if a data set is relatively large in relation to the population, the 'sample data sets differ from the population mean' is less likely to be a relevant problem, so the large data set can be used as a basis for the general model
      - 'bias is reduced using local information'

      - If training set is small, high bias / low variance models (e.g. Naive Bayes) tend to perform better because they are less likely to be overfit.
      - If training set is large, low bias / high variance models (e.g. Logistic Regression) tend to perform better because they can reflect more complex relationships.

  - derive the best explanation for a complex connection structure (like a neural network)
    - identify an example in the form of the simplest specific solution format sequence between input/output, with structures indicating:
      - structures representing the most unique information possible, to reduce structures required to visualize (if its a large network, this means indicating the inputs/outputs of as few node layers as is necessary to explain the functionality, cause, intent, etc)
      - relevant differences (structures indicating different activated nodes, different functions/weights/node types)
    - generate 'opposite/difference' structures that would not be the solution format sequence (why 2 interim nodes wouldnt work for a multi-layer perceptron)
    - translate the structure into language terms relevant to the input/output or at least the adjacent surrounding structures (a 'node that enables output equivalence or output neutralization' as opposed to a 'node with output -2')
    - include info about 'why' so the intent/cause is always connected to the structure
      - example: include info about 'why it cant be some other structure' so structures of 'requirement' are included, as structures of 'cause' (requirements being causal)

  - go over possible alternate implementation strategies & the path connecting different versions of the implementation
    - examples:
      - creating fundamental structure (like 'difference') space structures of varying structure ('difference') types, so interface queries can be implemented for example by selecting a 'difference network' to compare structures on (like interface structure differences, like input/output, value, definition, structure (sequence/position/path), interaction structure (like 'connection/change type') differences')
      - creating the set of useful functions of the referenced function types (general, core interaction, problem-solving intent, interim functions, interface structure functions, problem-function functions, commonly useful interface functions, function-connecting functions, etc), and adding any new functions required, to use as possible interface query steps or workflow components
      - storing useful interface queries & other problem-solving structures that typically produce solutions in configuration & iterating through those according to similarity of problem to the problems associated with those solutions
        - for example, using the interface query to 'apply useful structures by default as a problem-solving or solution component/input' by default, & iterating through other interface queries like those implementing "formatting problems in more solvable problem structures like 'find a prediction function' & applying known solutions" based on success probability, either for problems in general or for similar problems
      - implementing interface queries & other problem-solving structures by applying similarities to configured interface queries & structures where they are similar, and applying variables & associated differences where they differ, rather than designing specific interface queries for each new problem with interface query design logic
      - a sorting function to sort structures in a problem space as either problem/solution structures & apply useful function types based on their classification
      - apply 'useful structure map applied to a problem space' to find likely useful structures in a problem space

  - validity/relevance as attributes associated with interfaces

  - finish processes:
      
      - finish applying systematization of solution automation
      
      - finish interface analysis of physics & other interfaces to identify other useful components like efficiencies, incentives, trade-offs, closed systems
      
      - finish config
        - add useful structures & questions from index.md to systematize_solution_automation.md
        - useful structures
            - identify filters for useful structures like definition routes
            - the system structure format where the maximum number of interface queries can be executed structurally, with minimal conversions required? is it a merged format of variable/function/concept/cause network graphs, or system state networks, or a set of variable subset graphs, or differences visualized as vectors, or input-output sequence visualizations, or a network with all identifiable interface components visualized
            - interface queries optimizing finding useful interface component filters
            - useful perspectives/specific interfaces
              - useful to think of prediction functions as generative functions to select the variable interactions that are most likely
            - useful solution filters to apply in functions
            - aligning/balancing structures, to solve problems like 'a balance position of structures producing errors when unbalanced'
            - questions formatted as a disconnection between components like causal positions, paths, directions
            - subset indexes of an interface useful for solving most problems (structure indexed by metadata like problems solvable, fitting systems, interactive structures, supported intents)
            - ml structures with supported intents & solution success causes
            - most valuable interface queries & workflows
              - find the sets of differences/dependencies/formats/errors & other useful structures that are the most valuable in a particular structure like a sequence to solve a problem
                    - interface component definition routes
            - useful component/sub-structures of interface queries (interface components, interaction rules, cross-interface interactions, generative functions)
            - useful interface components (like abstract) of useful interface components
              - core interaction functions of core interaction functions
          - creating useful structures
            - organize automating useful structures like combinations of concepts such as "format sequence", "solution automation workflow", "insight path", "reverse-engineer solution from problem requirements or opposite structures", "connect problem & solution"
            - convert structural queries to insight paths
              - alignments present in security innovations (like alignment in inputs like keys)
              - source of rule development as structures of conflict between forced interactions like change causes & constant structures like limits
                - incomplete inevitability of interaction as a decision structure
              - group device history authentication: authenticate credit card by proximity to cell phone & continuity applied to user usage history pattern
            - functionalize insight paths & integrate functions in optimized program with parameters to select function subset & structure for input problem
        - default config
          - write some default interface queries to use until logic is written
      
      - finish scripts
        - create compilation script to compile code/config into a network graph on every change
          - add support for standardizing equivalent synonyms
            - add conversion to standard vocab

  - integrate logic
      - integrate objects/.md text with interface implementations
      - integrate archive_notes/finder_info/functions
      - organize interface analysis logic definitions
        - organize functions in problem/interface definitions, before organizing functions in implementations/*
      - integrate problem_solving_matching.md
      - integrate find/apply/build/derive logic from system_analysis/ & maps/defs.json
      - separate interface analysis logic into implementation/functions (functions dont need unique info)
      - add functions from workflows & analysis (to do list, questions answered, problems solved, interface definition & functions) as files in functions/ folder
        - organize into primary core functions & list sample parameters (like objects to identify for the identify function)
      - integrate rules from diagrams in patent applications to relevant documents
      - organize function logic (interface query design logic)
        - document default static config objects that are inputs to core objects (like functions & concepts)
          - core functions like 'change', with locked objects which should be generated as inputs to other functions and should not be removed bc they enable other rules & core objects
            - a 'check for errors' function
            - a concept of 'self-correction/optimization'
          - these locked objects can be used to generate rule-generating/deriving/finding structures, by forming an initial structure of locked objects and filling that structure with conditional & changeable structures
            - these rule-generating/deriving/finding structures can be used as solution automation workflows
        - design an optimal sorting structure for general interface queries to apply to problems manually
        - list interface selection (based on inputs like available APIs/data sets/definitions)
        - problem interface structures: solution constraints/metrics, problem space variables, available functions, useful formats/structures
        - function to translate interface query logic into interface language (combination of core functions (find/build) & other core components)
        - function-usage-intent::output or demand::supply combination/merging/building/matching functions (alternatively formatted as a solution-finding query for a problem or lack-resource matching function) as an alternative solution to ads
        - decision points (required/optional resolution of variables to constants, as in selecting a variable value)
          - identify when a method & data set can be identifyd to be capable of deriving the answer to a prediction function problem
        - alternative intent coordination & compatability of metrics
          - calculating interactivity by coordinating/adjacent/convertible structures
        - check reduced language components for any other useful functions (what terms cant be adjacently, clearly & accurately framed in terms youve defined) for completeness

  - integrate examples

      - index examples so they can be queried more structurally when implementing functions

      - move examples from:
        
        - drinkme/examples_from_faq.md
          - check other examples of high-value use cases (other than identifying important concepts) from faq:
            - identifying the important base to frame changes on (identifying new interfaces)
            - identifying the right interaction level to focus on (identifying the change-maximizing layer of a system to examine a particular relationship)
            - identifying the right perspective to filter with (like 'identifying whether the legal/scientific/progressive perspective is most useful for an intent')
            - identifying the right context/position for an object (derive context when it's missing or fit an object to a system)
            - identifying the most causative function set (like identifying core functions, or the most misused functionss, or the most change-causing functions)
            - identifying important differentiating types (like function types indexed by intent & structure types, like boundary/change functions)        
        
        - patent implementation_examples
          - identify any examples missing from patents in docs/tasks once examples are organized

        - specific examples from specific_problem_analysis
          - example of permuting assumption: "reports of power consumption have to be exact measurements" 
            - a temperature monitor sensitive to a hundredth of a degree might provide similar but non-specific power reporting for important/extreme usage patterns without revealing such specific information as that which could infer exact operations being done, bc the interval of temperature measurements allows for greater variation in calculations that could explain it
          - example of using set theory in query operations:
            - edges as core organizing/formatting operations (find/apply) & interfaces (connecting/explanatory concepts/functions)
              - https://en.wikipedia.org/wiki/Hypergraph
          - example of structural version of solution difference from original solution: 
              - this is like using a pair of connected lines at different angles to connect two points (multiplying alternate multiplier pairs to create a product), where summing the line lengths produces an equivalence, so different solutions would look like differently angled triangles connecting the two points
                - https://www.popularmechanics.com/science/math/a30152083/solve-quadratic-equations
          - examples of identifying vertex variables
              - general vertex variables: topic, origin/destination, reason/cause/point/intent, errors, variables, types
              - comedy vertex variables: sincerity, stupidity, stakes, tension-resolution/expectation-subverting pattern variation
              - music vertex variables: tone, tension-resolution/expectation-subverting pattern variation, lyrics
              - optimization metric vertex variables: solution metric patterns (what other solutions optimize for, to identify optimization metrics to apply)
          - example of resolving a conflict between structure/limits using a structural similarity between a structure (gradient of function) & its container/limits (gradient of constraints)
              - https://en.wikipedia.org/wiki/Lagrange_multiplier
              - also an example of a solution space (the whole function is the solution space of possible minima/maxima) and a filter applied to it (constraint)


## examples

  - add to govt
    - rather than payments from consumers, payments from central ledger based on production of supplies & proof of usage
      - this would invalidate the need for individual ledger accounts to acquire standard supplies like food/medicine, and suppliers of standard supplies can be paid from a general central ledger to continue their enterprise based on their supplies, their usage ratio, their relative contribution compared to other suppliers, and their relative value added by solving problems of supply like pollution & optimizing minimal cost of production & environmental impact
      - some transactions can require private accounts like for optional goods

  - add to predictions
    - where you say that 'activity interacting with a neuron is relevant in its functionality': https://www.quantamagazine.org/how-computationally-complex-is-a-single-neuron-20210902/
    - relevance of intelligence (successful learning/thinking) & disease (unsuccessful learning/thinking/stressor-handling): https://www.quantamagazine.org/brain-cells-break-their-dna-to-learn-more-quickly-20210830/
    - example of priorities leading to errors:
      - the 'selfish' perspective prioritizes simple, structural objects, which is why 'selfish' programs can only see & act on those things rather than producing solutions that can be used for many problems, even ones they dont have

  - add to science
    - curvature implies momentum of change of a particular type rather than constant change, applying a structure of incentives toward various positions & connections
      - is there a set of 'time crystal' space-times where change could be stuck in a 'local minima' where momentum doesnt reward movement in any direction (are space-time spaces continuous and is a method like momentum applied to determine motion in this space of space-times)
      - time as a 'continuous overlap' of dimensions where change is still possible
        - the change of 'possible change' implies a change in the restrictions on change (its boundaries), like the intersection & overlap of restrictions on change
        - the interaction space of restrictions is a useful structure to determine possible change types (how various definition routes of dimension can interact without invalidating another definition or each other)
        - https://www.quantamagazine.org/a-mathematicians-guided-tour-through-high-dimensions-20210913/
    - examine differences in functionality in cancer cells, like why some cell types dont have the same problems from aging/inflammation/exhaustion that other cells do - is it enabling genetic configuration or other factors?
    - examine 'inner product space' in relation to correlated universes (a 'similarity function' in the form of quantum entanglements producing an extra higher dimension)
      - https://www.quantamagazine.org/one-labs-quest-to-build-space-time-out-of-quantum-particles-20210907/

  - add to ml
    - how to identify that bias vs. variance can be resolved with 'conditional' or 'alternate' or 'subset' functions, assigned to data subsets based on data point attributes (like change type cause/patterns & type of a data point)
      - minimizing bias 
        - intends to predict as many points as possible in a data subset
        - outputs a specific function for a data subset
        - has errors when applied to different data subsets
      - minimizing variance
        - intends to predict as many data subsets as possible with minimal error, rather than specific points
        - outputs a general function for many different data subsets
        - has errors for each data subset, but fewer errors across many different data subsets
      - functions can be assigned to predict data points with attributes (like a range of standard deviation) based on the cause & patterns of their differences
        - if the cause of a data point is likely to be randomness, it can be excluded from functions that dont include randomness as an input
        - if the type of a data point differs from other data points predicted by a function, it should be predicted by another function that predicts that type
      - this solution involves re-arranging data subsets so they can be better predicted by functions


  - add to math mapping
    - add to dimension definition routes:
      - 'adding an independent sequence/state change type to other change types, containing but not changing or limiting other change types of lower dimensions'
      - limiting a change type to two possible values requires a structure in the form of a value (line, or hyperplane) separating them

    - a set of related change types (like a sequence of fourier/taylor expansion terms providing different polynomials) provides different change types that can be combined to produce the required changes to produce a function
    - example 'alternate connection' structure: wheels (rotations of circles) provide an alternate connection between waves & circles, in addition to trig functions
    - fourier transform is an example of energy from change stabilizing into a pattern of a new change type - https://mathlets.org/mathlets/discrete-fourier-transform/
    
    - examples of applying interface analysis to find/derive/generate useful math formats

      - traveling salesman: 
        - apply the useful structures of 'components', 'interactivity', & 'adjacence' structures to find interactions between points that form components that form a set (having unique components) with other components, where the component interactions also optimize for 'nearest neighbor' distance solution metric in the points connecting the components
        - components being "sets of points that locally form components optimizing for 'nearest neighbor'" (minimizing the 'distance' solution metric)
        - this applies the 'break a problem into sub-problems and merge sub-solutions into solution' solution automation workflow

      - https://math.stackexchange.com/questions/733754/visually-stunning-math-concepts-which-are-easy-to-explain

      - for the power of 2 sequence with the square visual

        - why 'adjacent rotation of a half of the current area' would produce an equivalence between the 'length' of the 'emerging sides of the shape' (producing a square instead of a rectangle, as square sides as equivalent) and why it would be produced by a power of 2 (each subsequent term is half the area of the previous term)
          - bc each adjacent rotation of half the current area produces an overlap leading to a set of three equivalent squares (1/2 and 1/4 overlap to produce three squares equal to 1/4, meaning 3 squares of 1/4 area, totaling to 3/4)
          - so the adjacent rotation doesnt produce a difference, but rather a symmetry based on the middle square where they overlap (leading to an equivalence on both sides of the middle square, meaning there are two protrusions rather than one which is how it starts with the first term, as a rectangle of 1/2 equal to two stacked squares of 1/4 area), and if change continues in the direction linking each 'middle square' symmetry, another symmetry is produced pointing in the diagonal direction toward the corner of the square, and the limit of the sequence's potential to add more area aligns with the intersection of the emerging sides that create the corner

        - in summary, the 'overlap' creating the 'symmetries', and the 'alignment' creating a 'corner' ('alignment' between 'emerging sides', their 'intersection' & the 'limit' of the 'sequence'), and the 'adjacent rotation' creating the 'overlap' and its 'symmetries' are the structures necessary to resolve/predict the interactions between these structures
       
        - same for the example with (odd sum of n integers) = n^2

      - for the area of a circle problem, the signal of the relevant basic formula for circumference being 2 * pi * r should indicate that there is a reason why the pi * r is repeated (hence the 2 as a constant), which occurs in many shapes, including sides of a rectangle
        
        - formatting pi * r as the sides of a rectangle leaves one unknown, the length of the other side, and trying out 'r' is an adjacent move
        
        - this fulfills known formulas & is verifiable, and provides another format for the area of a circle that is more calculatable and also adjacently connectible to the original shape & its relevant known variable interactions
          
          - 'connecting the formats' of a circle with a rectangle can be done with the 
            - 'rearrangment of circle partitions created by arcs' as shown in the diagram at the link, in which the arcs get progressively more linear as the arc lengths get shorter 
            - the 'adjacent positioning of unrolled progressively larger circles', forming a 'structural similarity' between the 'increasing third side of a triangle from 0 to the remaining endpoint', and the 'increasing lengths of the unrolled lines of progressively larger circles', the area of the triangle being easier to calculate & visualize & prove
              - identifying 'progressively larger circles' as useful for connecting a circle with a triangle requires:
                - applying 'adjacent transforms' to the given 'circle' shape to an 'extreme' value of zero, keeping the 'origin position' parameter the same
                - identifying the 'adjacent transform' of circle boundaries into lines (with unrolling operation)
                - identifying the 'structural similarity' between increasing lines and the third side of a right triangle increasing from zero to the remaining endpoint
                - this converts:
                  - a circle => vary shape to extreme value with same origin position => multiple circles of varying size => unroll => multiple lines of varying length => sort => multiple components of triangle area => triangle area

          - additional methods can produce this connection between circle/rectangle formats:

              - apply 'default' interface to the 'change' interface
                - another way to arrive at this format to display area of a circle in a simpler (& therefore more calculatable/verifiable) is arranging the known formula for the area in a way that doesnt have pi as a side length
                - the 'few only options' for formatting the known area formula as a 'simpler shape' like a rectangle are pi * (r^2) or (pi * r) * r, so this visualization is one of the 'default' options (if you assume or are given that the rectangle is the simplest possible 'format' for the area)

              - apply 'definition' interface
                - the 'rectangle' is also an 'overlap' with the 'unit' 'definition' of area (x * y, or 'x columns of rows with length y') so it doesnt need to be guessed at as a relevant shape
                - the interaction rule 'if you align lines by their endpoints, they create a shape with area' is also the 'definition' of multiplication, applied at an 'extreme' value for one of the multiplier parameters (a line having zero area)
                - so by applying the 'definitions' of 'area' (and its relevant objects like 'multiplication' & 'rectangles'), you can derive a way to connect the circle & rectangle formats
              
              - 'function input-output sequence': 
                - this can also be reached with an 'input-output sequence' query, which queries for functions with the 'attribute' of linearity as an 'output', and functions that take pieces or adjacent transforms of a circle as 'input'
                - this connects the attributes of the circle (as a set of shapes produced by arcs) with a 'linear emergent border' structure that happens to be a set of horizontal/vertical lines
                  - curvature & center => completeness & alignment at origin/corner & curvature => separation/partiality & alignment at vertically straightened tops & linearity => emergence of vertical & horizontal borders (of aligned shapes forming a rectangle)

              - 'structural similarity between inputs/outputs': 
                - this can also be reached with a query for combining triangles into rectangles (two triangles make a rectangle), since the pieces of the circle created with arcs resemble triangles with an extreme arc length parameter value
                - given the 'structural similarity' of 'triangles' and the 'shapes of a circle produced with arcs with extremely short lengths', and the 'structural similarity' between 'triangles' and 'area', apply interaction rules of 'triangles' and 'area' (such as 'two triangles having side lengths in common, positioned adjacently with a common side, create a rectangle')
                - this connects the structures:
                  - 'circle' => 'shape produced by arcs' => 'triangle' => 'rectangle' (simpler output format for visualizing area of a circle, starting from the circle, to prove area formula visually)
                - this can also be reached using structural similarities between curvature-area interaction rules, like those determining area under a curve, specifically those determining area under a sin/cos wave function, the change patterns of areas of triangles created between a circle's origin and its boundary, the change patterns of areas when a circle is distorted according to wave patterns, etc

              - 'generative functions': 
                - apply 'difference' structure of the 'change' interface
                  - the 'difference' between how a circle is generated from a line and how a rectangle is generated from a line is just a 'fixed endpoint' of the line as its shifted, so these formats can be connected by reducing/converting/removing that difference
                - this can also be reached with the generative formula for a circle using a rotation of a line:
                  - the line is a unit of a rectangle, so aligning the pieces of the circle created at each state of the line during its rotation using a different alignment than the common central point uniting the lines' endpoints (a vertical alignment of line endpoints) can also be used to generate the rectangle from the circle
                  - given the interaction rule of the line as a generative input to the circle, we can determine (rather than guessing as with the triangle) that the line is closely related to the circle, and 'interaction rules of lines & area' can be applied to represent the shapes that lines adjacently generate, which includes circles)
                  - interaction rules of lines & area include 'if you align lines by their endpoints, they create a shape with area'

  - give examples of why other tech solutions are insufficient
    - regression is insufficient even if its a good temporary solution if you dont have other resources than the data set, bc its conclusion/outputs (in the form of the regression function) can have the opposite meaning 'random noise' as the intended meaning 'causal relationships'
    - statistics in general is built on the insight that 'probability is associated with certainty/truth', but it ignores other certainty structures like structures that are more useful than patterns/probability, such as definitions, concepts, meaning/understanding/integration/organization, cause, inevitability/requirement, determination/generation/description structures, functions of varying interaction levels, etc
    - machine-learning can have the opposite functionality given extreme data values or update functionality manipulation (to train it to give the wrong answer in its online learning functionality), as well as other exploits from interactions of the algorithm, network, parameters, emergent structures, & data, and it is not built on understanding
      - 'one-degree connection structures' which are present in 'foundation models' are incapable of capturing multi-degree connection structures like sequences/chains or structures of connections like trees/networks/groups, even though other structures can be formatted as core structures like 'connections', it doesnt mean a one-degree connection network will capture them, or that a network of connections is the most optimal structure for that info given its usage
      - machine-learning based on neuroscience leaves out other brain interfaces like psychology, chemistry, & language
        - a psychologist might interpret a thought as 'an emotional reaction to a chemical stimulus that retrieved a memory'
        - a neuroscientist might interpret a thought as 'a response to electrical stimulus given weighted connections between neurons that previously handled that stimulus'
        - a linguist might interpret a thought as 'a deviation from a previous phrase that captured an experience to handle a change to that experience'
        - a chemist might interpret a thought as 'a result of scaled electron dynamics in response to a chemical'
        - a biologist might interpret a thought as 'a useful way to produce serotonin to offset a signal from the gut'
      - https://thegradient.pub/has-ai-found-a-new-foundation/

  - give example of how structures could have been derived (symmetry, isomorphism as common important objects to derive an interface, alternative interfaces to solve a problem) from another direction

  - derive logic types that would be necessary to complete the logic interface & give examples of logical object interactions

  - add to problem/solution structures

    - a 'find a solution' function should be able to be converted into a 'generate a solution' function & other functions like 'test a solution' & 'apply a solution', bc as the brain learns, it can generate solutions on demand once understanding develops

    - give example of identifying meaning of emergent structures:
      - nn structures should include 'iterative combinations of combinations of inputs' in a tree structure, in addition to weight paths & other emergent structures of the algorithm when applied to the network, and when data extremes & other important points are applied

    - organize workflows using useful structures as being on the meaning interface, where useful structures from other interfaces overlap & connect with the meaning interface

    - write interface queries to generate each workflow

    - finish math mapping so you can find other useful/solution structures (interaction space as convolution, core functions as basis vectors, etc)

    - abstract interface queries to generate workflows
      - example:
        - workflow: apply the function generated by the interface query 'apply format sequence to connect the "categorize" problem input with a solution format' as a general solution function for 'categorize' intents
          - identify known relevant info
            - identify known types
          - identify functionality of known info
            - known types are a 'final filter' to apply before the solution format is reached
          - identify relevant interface structures
            - identify variables (isolatable change types)
          - identify functionality of relevant interface structures
            - variables can be applied to find similarity to other variable values & to average type values or value ranges
            - variables can be applied to change variable values
          - identify possible interaction between functionality of known info structures & relevant interface structures
            - applying changes to an input (data point) can identify 'degree of difference' between the input and a type value range or average type value, which can be used as the 'final filter'
          - identify if possible interactions are useful for a given intent
            - applying changes to identify 'degree of difference' is useful for the 'final filter' intent ('categorize' intent)

        - the interface query is generally to 'identify missing info & functions to find/derive/generate that info', but specifically implements it as:
          - abstracted workflow: 
            - 'identify info & interfaces structures and their functionality, and the interaction of that functionality, and the useful interactions among those functionality interactions for solving the specific problem'
          - this can be generalized into another solution automation workflow
            - 'identify structures & their structures & the interactions of these structures, filtering for usefulness for problem-solving intents'
        - the 'solution function' output by this query is 'apply changes & identify if the differences required to convert a data point into a clear member of a type are greater for one category than another'
        - the workflow to generate a solution function for 'categorize' intents involves generalizing that interface-query generated solution function for varying 'categorize' problems & applying that as a solution-generating/finding function for 'cateogorize' intents
        - the general workflow is to generalize the design of interface queries (to identify missing info & functions to find/derive/generate that info) to fulfill specific problem-solving intents, rather than solving a specific problem
          - 'functionality' is a specifically useful & important structure, so the specific interface query can be retained, or it can be fully generalized & the 'useful structures' can be a variable rather than specifying 'functionality' as a useful structure

    - generate workflows based on other core interaction functions than 'connect' & 'interact' & 'filter' since many are based on those functions
      - connect: 'connect problem/solution structures', 'solve adjacently related/connected problem'
      - reduce: rather than workflows to 'connect a problem/solution', workflows to 'reduce a problem into a solution' or 'reduce a problem into a non-problem or neutral structure'
      - abstract: 'abstract/specify a solution & solve for the abstract/specific/example solution instead'
      - filter: 'filter the problem attributes to just the relevant attributes' and 'filter the problem attributes that cannot be converted into solution attributes'
      - interact: 'determine which interface queries interact in a way that allows the problem/solution to interact in a way that fulfills a core interaction function', 'determine which function interaction levels, workflows, queries are interactive'
      - multiple: 'determine which interface objects interact in a way that fulfills multiple core interaction functions' (given the insight that functions which generalize tend to be more useful & accurate)
      - missing: 'determing which functions are missing & could be generated that would solve the problem more quickly than existing functions'
      - position: 'position the problem so its a neutralizing structure (a problem for a problem), or a non-problem, or not interacted with'

    - identify interim & cross-interaction level functions & other interface structures that fulfill various workflow variations (like fulfilling a specific core interaction function)
      - connect: 'find structures fulfilling an interaction or connection structure, like a sequence/tree/network'
      - reduce: 'find the important variables' is a function that is particularly useful for the 'reduce a problem' problem-solving intent
      - abstract: 'find abstraction levels that tend to be useful for resolving a particular uncertainty type', 'find'
      - filter: 'find the most reductive filters that dont lose an info type'
      - interact: 'find interaction structures of interaction structure (gaps, overlaps, intersections)'
      - multiple: 'find solutions fulfilling multiple metrics'
      - missing: 'find gaps in functionality that would be useful to fill'
      - position: 'find position of a structure where functionality would develop'

    - give examples of when an input/output sequence or other useful structure is not applicable
      - in most cases, you can use an input/output sequence, like when you have the inputs/outputs of functions indexed, so outputs can be routed to functions with matching inputs to create a sequence connecting problem/solution, but this doesnt work without other interface structures when:
        
        - when you dont have inputs/outputs indexed

        - when you have inputs/outputs indexed, but there are no functions to connect inputs/outputs in part or all of the sequence between problem/solution, so other methods like pattern/logic interface functions are necessary to fill in the gaps in the sequence left by missing or non-indexed functions
          - the 'derive' function can be fulfilled in various ways
            - the logic interface can infer connections that are implied, or find another route to connect problem/solution than a route requiring a missing function
            - the pattern interface can infer connections according to common patterns & probabilities
          - the 'build' function can construct missing functions out of available functions/structures
          - these alternate interfaces fulfill the 'input-output sequence' with a variable definition of 'connection' applied to 'inputs/outputs', where there is flexibility added to the degree of certainty in matching & connecting components of the sequence, resulting in a partial implementation of the input-output sequence that may be resolved into a more certain structure with more information, similar to a function with some certain/constant one-line sections and some conditional/variable multi-line sections

        - when there is a more effective workflow/query that solves the problem than the 'find input-output sequence' interface query fulfilling the 'connect problem/solution' solution automation workflow
          - finding other useful structures, like 'finding required functions', 'finding general interaction structures' (rather than specific interaction structures like input/output sequences), or 'finding useful reductive filters', may be a more effective or efficient query than 'find an input-output sequence', depending on available & adjacent info
            
            - other interaction structures include:
              - 'completion' or 'combination' structures, where structures fit together to form a component
              - 'integration' structures where structures are merged to create another more useful structure
              - 'variable' or 'type' structures, where one structure is a variant of another with different parameters
            
            - so useful alternatives to input/output sequences include:
              - 'combination sequences/sorts/trees/networks' to create combinations of structures that produce useful components (like creating a 'shape' out of components such as 'defining attributes like boundary lines')
                - rather than using input-output sequences to solve a:
                  - 'find an optimal route' problem, combinations of interaction structures like 'route sequences' or 'difference structures of sub-optimal routes' can be used
                  - 'find a prediction function' problem, combinations of structures like 'subset functions' or 'conditional functions' or 'base functions & conversion functions' can be used

              - 'integration sequences/sorts/trees/networks' to create merged structures that are useful (like creating a 'type' definition out of 'two examples')
                - rather than using input-output sequences to solve a:
                  - 'find an optimal route' problem, integration structures like 'integrations of route filters like differences from sub-optimal routes and definitions of benefit/cost of movement' can be used
                  - 'find a prediction function' problem, integration structures like 'weighted averages of alternative functions found with varying regression metrics' can be used

              - 'variable sequences/sorts/trees/networks' to create changes to a standard/base/origin structure that are useful (like creating an 'example' out of a 'type' definition)
                - rather than using input-output sequences to solve a:
                  - 'find an optimal route' problem, 'change structures' can be applied to a standard sub-optimal route
                  - 'find a prediction function' problem, 'change structures' can be applied to a standard sub-optimal prediction function

            - the reason there are other useful structures is bc there are other solution automation workflows than 'connect a problem/solution', with associated useful structures for the workflow, bc there are other core structures than inputs/outputs and sequences
              - 'combination' structures go with the workflow 'build a structure out of components to solve a problem'
              - 'integration' structures go with the workflow 'break a problem into sub-problems and merge sub-solutions'
              - 'variable' structures go with the workflow 'adjust an existing standard solution until it fits the problem, according to its differences from the standard problem, like different solution metrics'
            - this means solution automation workflows can be derived from these core structures & interface structures applied to these core structures

        - interim interface queries can be used to connect a workflow with a solution-producing interface query
          - 'find an input/output sequence of useful structures fulfilling this workflow' can be an interface query used to determine if a particular workflow has a useful structure input/output sequence available, and if not other interface queries can be applied

        - a variation of 'interim interface queries' is 'interface queries for interface queries to fulfill/implement a workflow'
          - 'interface queries' are 'queries for structures/functions to fulfill an intent' so they can be plugged in wherever there's a lack of info (problem to solve)
          - problems to solve can include:
            - 'find an interface query to solve the problem of finding an interface query'
          - where solution automation workflows are applied to solve the problem, such as:
            - 'connect a problem (solution automation workflow requiring an interface query to implement it) with a solution (an interface query to implement it)'

    - give examples of how each workflow can be applied to various standard problems (find a prediction function, sorting problem, ml configuration/algorithm-design problem), which can be used as a data source to derive implementation logic/interface queries to generate solutions

    - simplified definitions

      - workflow:
        - a way to connect a problem with a solution automatically

      - interface query: a way to automatically implement something
        - when applied to implement a function intent, the interface query is a function-finding method
        - when applied to implement a problem-solving intent, the interface query is a solution-finding method

      - interface: standardizing filter where any problem can be solved
        - why an interface isnt a language - its definition overlaps with the definition of a set, which is a sub-structure found on interfaces and doesnt encapsulate the whole definition of an interface, which is a specific structure in which all problems can be solved, whereas language encompasses all concepts/structures without refinement by a filter that adds value in reducing computations
        - ambiguities/overlaps as sources of info to identify interfaces (overlap of 'difference' & 'change' definitions indicates that they are related variations in a potential field of a unifying concept acting as a symmetry)

      - perspective: 
        
        - a filter with priorities (which may be structures, causes, abstract prioritized attributes, or other interface structures) which highlight something as particularly important
        
        - example:
          
          - a perspective like 'find the function that minimizes distance from as many points as possible' produces a solution that can qualify as 'regression' to the 'find a prediction function' problem
            - this perspective can be a function structure, but its still a perspective because its highlighting some objects (distance from points, average) as particularly important
            - a function like 'find the function that minimizes distance from the average line' is a lot closer to the definition of 'regression'
          
          - differences in perspectives:
            - the first perspective highlights a specific problem-solving intent to generate a solution-finding method or solution for, which has many possible implementations
            - the second perspective highlights an adjacent inevitable solution-finding method, which has very few possible solutions/implementations, given some variance in the definition of the average
        
        - perspective variables
          - degree of implementation variation
          - info captured/created
            - perspectives may be useful structures & may contain useful structures (like averages), which capture a lot of uncertainty, complexity or variation/change, providing useful info like a direction to move toward when searching for a solution, or a specific problem-solving intent to fulfill
          - adjacence to solutions/solution-finding methods
          - definitions
          - priorities
          - filters
          - useful structures referenced
          - problems the perspective is useful for
          - relation to other perspectives
            - differences in perspectives can be used to generate other useful perspectives, and identify which perspectives would be most useful to guide a problem-solving workflow or interface query, given perspective attributes like implementation variation
          - perspective structure (interface, function, priority set, etc)
            - a perspective may be formatted like a particular interface structure, like a function or interface, while still qualifying as a perspective bc it prioritizes some objects over others
          - abstraction (abstract perspective or a specific perspective)

        - how is a perspective different from other structures?
          - its definition overlaps with an interface, but the interface includes an abstract concept like 'cause' that is prioritized & focused on, and all the structures relevant to it, & standardizes everything to that concept's structures, whereas a perspective may just focus on a particular set of structures rather than changing structures (for instance to be formatted in terms of causal structures like dependencies on the cause interface, rather than their original format, whereas a perspective may just focus on causal relationships or filter out anything that is not causative)
          - how is a perspective like 'find a function minimizing distance from average line' different from a function?
            - a perspective can be formatted as another structure than its standard structure (a filter with priorities), because other structures can have default priorities & act like a filter
          - how is a perspective like 'find a function minimizing distance from average line' different from an interface query?
            - an interface query may also produce a step with an intent like 'find a function fulfilling x' but in the context of the interface query, the intent of this step is to fulfill another intent, like a problem-solving intent such as 'create a function to fulfill y automatically', which may involve solving the sub-problem of 'finding a function to fulfill x'
            - this doesnt contradict the definition of the interface query or perspective, something can be both without violating either definition
          - the reason to call something a perspective is if it highlights a priority or prioritized structure in a way that adds value by filtering out other structures, and filtering is a very useful function that is frequently used in other problem-solving processes, like the problem-solving intent 'filter the solution space' or any call to the 'find' or 'identify' functions
      
    - list of useful structures & intents
        - mixed abstract/specific structures, for 'apply' and 'connect' intents
        - specific standard problem formats ('find a prediction function', 'sorting algorithm') that any problem can be converted into
        - position relative to other objects of the same type
        - function interaction levels & function types
        - interchangeable structures that can be used to generate each other
        - problem/solution structures (problem-solving intents, solution components, solution metrics, solution workflows)
        - solution-determining/adjacent structures (making the solution trivial)
        - causes of interface structures (intents, changes, differences), for 'predict' intents
        - perspectives that make solving a problem quicker with alternate priorities
        - core structures, for 'build' intents

    - basic solution automation workflows
      - trial & error
      - reverse engineering
      - break problem into sub-problems & merge sub-solutions
      - apply rules from other systems to see if they work in another system
      - apply machine-learning
      - use a rules/solution database & look up the answer

    - example of format/intent matching
      - formatting a 'tree' as a 'set of overlapping sequences' so functions can be formatted for different intents like in 'parallel processing'

    - add to input structures
      - input variable/trigger/requirement/component

    - add to output structures
      - limits on what a structure can be used to create
      - similarities/differences to inputs (inputs change can be preserved in outputs)

    - identify new interactions/structures
      - trying structures of structures that havent been tried yet (like how new words evolve as a 'combination' of other words to describe new experiences that are similar to both combined words)

    - 'testing/simulation' involves querying for related rules (like how 'gravity' rules are related to 'motion' rules so any change involving motion should have a 'gravity rule check' applied as a filter) & checking if they apply to relevant components (like how specific components are involved in 'motion', like 'energy', 'motion restrictions', 'motion functions', 'motion triggers/inputs/components')
    - this is an important process for checking if a structure is valid/consistent in a system, which is a useful function
    - this is different from basic testing, which is where a function is applied and the output is checked against an expected value, bc it involves testing for validity/consistency in a system context where the change is being applied

    - examine interaction space of tech stack layers (ml models, algorithms, data, apps, bugs, os, chips) as a source of new errors
      - example: 
        - ai applied to design chips
        - chips with data erasure bugs that exacerbate os data erasure bugs
        - chip designs that produce error types for various ai models/algorithms/parameters
        - how 'gpus are known to be better at building ai models'

    - add to ml: optimizations/derivations applied to standard ml process

      - give examples of formatting ml in different formats (variable network, tree, sequences, etc)

      - give examples of errors produced by compressing algorithmic input/output connection logic

      - give an example of why to choose position of a function in data pre-processing vs. in an algorithm (lack of certainty)

      - backpropagation corrects weights based on 'differences' between expected/actual values (a standard error definition structure)
      - other error definition structures
        - prediction accuracy should reflect ability of info to predict output (only so much accuracy can be produced from info, without using other methods) - if its more predictive than what the info can predict, theres an error in the data/network/params/functions
      - optimizations can be applied to various functions of the network & its processing functions, using workflows that use an answer/solution once a standard solution is known
        - more efficient networks/weight updates can be found to reverse-engineer a weight-update algorithm or a network structure/parameter that would have sped up learning or used less info or produced higher accuracy
          - from this, a reason why its more efficient can be derived, like it includes info that was missed in the original network bc of activation threshold config, or integrates the concepts driving feature importance like adjacence depending on the data type
      - the domain of the data type can be derived by which changes produce higher accuracy
        - if adjacence determines interactivity/relevance & combinations of adjacent features improve accuracy, the data is likely to be a graph or image of a system
          - inferring domain allows other rules/structures to be integrated
          - once you know its a visualization of a system, you can look for nodes/components of the system & other system objects & apply system interaction rules

      - for a data point, change in weight for various node types (normal, hidden) can be calculated based on using gradient descent for determining the weight change that would minimize the 'output node error degree'

        - finding useful structures like symmetries in correct/high-impact weight paths & average/central correct/high-impact weight values around which other correct values vacillate is a first step to connecting raw numerical data with the meaning interface
          - other useful structures
            - ambiguities between correct & high-impact weight values
            - more efficient weight paths & weight values to reverse-engineer a network that would have found the answer sooner

        - output node error degree     = difference between target & predicted value
        - all output node error        = mean least squares applied to (output node error degree)
        - (normal) weight change       = - learning rate                                                       *        derivative of all output node error with respect to weighted input sum for output node         * previous node output
                                       = - learning rate                                                       *        change in all output node error with respect to change in weighted input sum for output node   * previous node output
                                       =   learning rate * output node error degree * derivative of activation                                                                                                         * previous node output
        - (hidden) weight change       =   learning rate                            * derivative of activation * sum of derivative of all output node error with respect to weighted input sum * weight(output node k) * previous node output

  - add to science

    - examine deriving 'protein' & 'gene' & 'activation state' as the location, components, input & structure of functionality

    - examine association of energy production, mitochondria & ribosomes, with stressors/metabolism & immune exhaustion

    - what is the connection between entropy (which Ive been using 'variance', 'potential', 'uncertainty' in place of at various points) and temporary information (information that is temporarily true, like electron position, rather than conditionally true, like laws of physics, or absolutely true, like rules governing quantum & standard physics interactions)
      - are black holes related to the output of accurate natural 'clocks' that formed
      - higher distribution of energy leads to higher entropy (possible states), but also a higher number of possible info interactions (which produce at least temporary certainties)
      - what is the relationship between entropy as 'possible' information, & 'probable' information
      - which of these possible states can be filtered out, either by probability, energy efficiency/stability, state connections, or other rules (how to add info of varying parameters to high entropy systems)
      - how to build a clock with consensus aggregated from various info sources that feed off each other in an input/output cycle
      - isolated systems are more useful for timekeeping
      - if the 'flow of time' is 'lack of organization', can 'organization' condense or connect or reverse time
      - if time is potential (ability to change), it is created by organizing info as a side effect in the form of entropy
      - whereas if time is lack of potential (certainty acquired as info, and entropy generated from it), there is a finite amount of it
      - if time is a system involving both info (lack of potential) & the entropy/potential generated from it, such as a ratio required to maintain for both to continue to exist
      - whether the ratio points to a convergence of one superceding the other is an open question
      - what is the connection between related concepts: 'randomness' as 'lack of info', 'potential' as 'ability to change', 'variance' as 'change injection points', 'uncertainty' as 'lack of certainty structures (like identifying/differentiating/determining/describing variables)', 'info' as 'specific stable connections, with varying time/scale/condition/position/state of applicability', 'entropy' as 'number of possibilities', 'possibility' as 'structure that isnt ruled out by other structures', 'energy' as 'change trigger/input, which can be stored/organized/formatted as info/potential', 'accuracy' as 'correct info measurement or info prediction/generation/finding function', structures like 'similarity/efficiency' as 'info inputs (which make it likelier that something will be proven true)'

    - what junk dna could be added that would enable production of the most useful types of RNA/proteins & other components for immune system functions, repair processes, & other anti-illness processes

    - https://www.quantamagazine.org/mental-phenomena-dont-map-into-the-brain-as-expected-20210824/

      - why memory sections might not always be necessary
        - bc complex memory structures might only be necessary to represent complex sensory structures like overlaps/ambiguities, or necessary to represent chromological/sequential structures

      - why might functions not be mappable to isolatable brain regions
        - bc they should be broken down or combined into other functions (general, interim, common, interchangeable, core, etc) than those on the interaction level theyre examining

      - why might movement info be stored instead of sensory info:
        - bc movement is a proxy variable of sensory info reactions

      - why might metabolic regulation & memory formation be connected:
        - relation to available energy used for forming memories (excess energy is prioritized for tasks like memory)
        - relation to rewards for using energy a particular way such as in forming memories
        - relation to regulatory schedule linked to sleep cycle & memory formation during sleep
        - distortions in metabolic function are prioritized in memory formation

    - "In the developing immune system, double-stranded breaks enable pieces of DNA to recombine and generate a diverse repertoire of antibodies"
      - examine how states that trigger useful functions like stem cell production or antibody production can be triggered

    - explore how much functionality can be developed by using incentives
      - if you create rewards like dopamine when a dysfunctional cell process is triggered or replicated artificially, does the system re-build or correct or re-learn that functionality
        - like when cholesterol prevents immune system from reacting to cell death, can you force the immune system to re-learn its original reactions, forcing it to react to cell death by associating that reaction with rewards or some other trigger like inflammation/pain that would correct its dysfunctional state?
        - if not, can you apply a change in the opposite direction (triggers of an 'over-reaction' error type to cell death, but only enough to move it back toward its original state)

    - check how much of the 'bio interactions' with a 'rules database' is available, to predict missing interactions from the rules database
      - this could be used to predict which combinations of structures (states like genetic mutations, bio system & cancer states, attributes like acidity, components like microbes/enzymes, functions like inhibitors, inputs like energy sources) will switch off cell proliferation processes & which will have the opposite effect
        - this should be able to identify when the immune system will hinder treatment, when oxygen deprivation will be an enabler of a disease, when pathogens will be synergistic/antagonistic, etc
        - it should also be able to identify which states are adjacent/accessible that the system can be converted to, which would have beneficial effects like 'neutralizing negative effects as defined in a particular state' 
          - conversions such as 'find a awy to standardize neoantigens so theyre similar to neoantigens targeted by an existing treatment' or 'find a way to standardize tumors/immune cells by giving them inputs that will trigger a state sequence that produces a more standard or more treatable tumor' or 'find a way to make tumors seem more like pathogens already defended in memory cells' or 'engineer microbes that feed off cancer cells and then travel to the gut or eat each other or are eaten by other microbes/enzymes' or 'find neurons that map to nerves around the tumor and stimulate those neurons' bc standardization takes the risk & the work out of applying immunotherapies & other customized medicine
          - standardizing immune cells could help reduce variation in immune responses to treatments: https://medicalxpress.com/news/2021-09-vaccine.html

    - autoantibodies as possible reaction to 'not having any actual pathogens to attack so they start attacking the immune system components which are just nearby or easier to attack than pathogens or have structural damage that disrupts their immune functionality' 
    - what alternate inputs have the outputs of useful structures that have antitumor or antimicrobial activity
      - what can produce components (enzymes/antibodies/t-cells), functions, or attribute states that eat cancer cells ('adapting to mct oil')
      - what combinations of structures are particular useful in general or specifically against a particular pathogen/condition
    - what other pathogens/conditions are synergistic with other conditions (do specific fungal/bacterial infections help cancer, and which ones if its a specific set)
    - what is required to make the body 'allergic' to a substance like a cell membrane attribute of specific cancer cell types 
      - is this the same as a normal immune response
      - is it similar at all to a 'pain' response alerting the immune system to a problem, and what can produce a 'pain' response if that response is useful
      - what other attributes could cancer cells have that make certain compounds likelier to bind to them or surround them to cut them off from energy sources or separate the tumor into attackable pieces (surface structures, attributes in various solutions like fat/water/mucus/blood, response to enzymes/pathogens)
      - what ratios (stress, acidity/alkalinity, enzyme ratios, energy ratios, cell distribution ratios, blood waste ratios, kidney/liver/pancreas/digestion function ratios, immune cell ratios) and other structures are associated with cancer progression/triggering
        - what ratios do some anti-cancer foods like almonds have that other foods do not

  - add to error-finding methods
    - identifying & generating known useful structures like 'symmetries', 'variables', 'subsets', 'interchangeable alternatives', 'maximally different inputs' & 'bases' & 'type/phase shift thresholds'
      - identifying & generating combination structures of useful structures like 'maximally different values around bases'
    - identifying gaps in known useful structures explaining data points (where data points arent explained by those known structures) & generating inputs in those gaps other than those data points

  - add to conceptual math
    - example of a conceptual math operation that builds a boundary structure leaving an inevitability of a matching concept (numbers) filling the structure
      - the concepts of 'missing', 'multiple/more', 'unit', 'type', 'identifiable as similar/equal/different' and 'difference in amount' allow for/require/build the concept of 'numbers'
      - also functions like 'compare' or 'reduce' or 'expand' require the concept of 'numbers' when comparing objects of that data type or objects having a quantifiable attribute

  - add to causation variables
    - ability to change (if a variable cant be changed, it is less causative for problem-solving intents)

  - add to info problems
    - this manipulates:
      - audience objects:
        - ego
        - assumptions (about patterns, what you would notice/figure out)
        - attention
        - feelings 'opposite' to logic (safety, confusion)
      - using objects like distractions, activations, distortions, core structures like combinations/sequences, complexity, patterns, input/output similarities/alternatives (complex/simple implementations), logic, patterns of logic, logic avoidance, jokes
      - to produce:
        - errors in expectations (in order for the audience to expect y, they have to have assumption x, as x is an input to y)
      - these important variables can be identified by identifying the inputs to these objects
        - what 'input' is 'required' for this expectation error to happen? (an assumption)
      - https://www.smithsonianmag.com/arts-culture/teller-reveals-his-secrets-100744801/?all&no-ist

  - add to nn

    - concept of 'comparative features': features that were enough to differentiate a category in the training set but not in test, bc they have too many overlaps with other category feature sets
      - adding sub-parameters allows variation within these overlaps to be identified/differentiated, using any remaining differentiating features that are still available in inputs but dont change overall input/output connections (change direction, average change rate, etc)
        - https://www.theregister.com/2021/09/02/imaginary_numbers_help_ais_solve/

    - weighting & position make emergent structures like functionality probable & possible in a neural network
      - identify all the emergent functionality/attributes/structures in a neural network with different input variations & parameters
      - identify how these structures could interact (coordinate, align, or neutralize each other) to create other interaction level of emergent structures
      - identify how these various interaction levels & the interaction structures defined on them as possible/probable would create possible/probable solution/error structures
        - avoiding error structures like 'too many differences in outputs of nodes with similar input info (feature) or similar potential info (info required to identify a feature)'
      - identify how these structures can be optimized to avoid error structures or prioritize solution structures
        - like 'prioritize applying weights to connect nodes to create a particular similarity/difference type'

    - neural nets should have a target structure (like a target 'variable interaction structure') based on understanding of variable interaction probabilities & other useful structures that their emergent structures comply with and that their structures can optimize for extracting from versions of input data, deriving the neural network structure from this target structure & filtering it based on the emergent structures that would optimize info extraction from input data versions

  - add to math

    - https://www.quantamagazine.org/how-a-mathematical-paradox-allows-infinite-cloning-20210826/

      - how to generate the target solution of 'a source of duplications'
        
        - start at the enabling structure of duplications (multiple sets having different final direction value):
          - find 'overlap' or 'combination' states (with sets including multiple different final operations) and find a way to connect them with standard objects (countably infinite sets with a final value determined by the final operation's direction) using allowed operations (rotation)
        
        - start at the standard structure (one set having same final direction value):
          - apply adjacent transforms like rotation to the standard structure (countably infinite sets that are complete, having their final value determined)
        
        - identify the highest-variation changes (like changes in final values between adjacent states - since one state has north/south/east nodes, the next state has only east nodes) as a possible source of changes for other values (a change in one value can produce a change in another value if theyre relevant)
      
      - generate the standard structure of countable infinite
        
        - use 'irrationality' to generate the standard structure of countable infinite sets in the first place (enough difference in rotation angles to not generate an uncountable infinity, but restrictions on the angles in that they remain static & restriction in movement avoiding the opposite of the previous direction)

        - during the creation of a set of points having the same previous final direction, there will be states where the previous directions of points in the state are maximally different (not every state will have the same previous direction) bc a countable infinite set is not a series of repeating the same rotation, and differences in corresponding rotations across sets are allowed

      - how to identify the standard structure (countable infinity) as a useful structure
      
        - its required to use the standard structure to base transforms off of (like a countable infinity) bc its a subset of the original, and you have to use the original structure as an input to generate the target solution structure
          - identify structures (components/attributes) of the sphere which can be used as components/inputs of the solution
            - subsets of the sphere
            - operations like 'rotation', 'repeat infinitely'
            - uncountably infinite points
          - apply 'structure' interface to find possible standard structures like 'differences' in these structures of the sphere
            - identify differences in relevant attributes ('number of points', 'location of points', 'generative method of points') that different structures ('subsets') of the sphere can have
              - attribute: cardinality of infinities
          - identify whether differences in those attributes would be useful (in producing a useful difference/similarity)
            - what is the relationship between countable & uncountable infinite sets
              - can one infinity type be generated from another
                - can an uncountable infinity be generated from a countable one
                  - this seems like it could be possible, identifying 'countable infinities' as a possible useful structure
              - what ways can countable infinities be generated that makes them exclusive (no repeated points)
              - what is adjacent to a countable infinity if generated a particular way that is not adjacent to an uncountable infinity
              - what functions does a countable infinity have that an uncountable infinity does not

      - question
        - is 'infinity' the same as 'all possible values of that type'

  - add to govt

    - if the taliban dont believe theyre stupid, they should try their own tricks on each other and theyll see that they work, so they can verify how similar they are to their victims
      - they can try the simplest tricks like 'violent threats to get compliance' to see if theyll comply once theyre threatened, or 'repeating things' to see that they are likelier to believe things that have been repeated a lot bc theyre stupid, which is how they got indoctrinated in the first place, and its how their prophet started to believe the ridiculous things he did, by repeating his fantasies to himself so often that they seemed true bc his brain was extremely stupid
      - help the taliban see other business opportunities than violent govts, which may be the lowest-cost business opportunity in their neighborhood, but has high future costs in that they run out of people to oppress and they lose the potential higher profits from other opportunities, like growing different varieties of plants with drug compounds (non-addictive drugs, drugs that can treat conditions, drugs that can produce a particular brain function, etc)
      - they can also look at who theyre helping to find out how stupid they are 
        - their actions help Russia, virtue-signalers on social media, anyone who wants to hate their people (bc theyre attacking their own people & always have, and they dont have solutions except violence, which animals could think of too), and anyone who wants to profit off of war/poverty/disease/oppression (China, the US, Russia, other hostile foreign govts & entities)
      - if you want the taliban to switch to farming/engineering drugs, you have to make it easy - give them education on how to do it & other resources, so its even easier than violent govt
      - same with other revenue changes, eventually leading to legal revenue sources
      - if their prophet wasnt a loser he would be able to promise them a better fantasy like 'infinities' of virgins (one in every neighborhood, with maximum genetic variation, and they have to fight over him first, and first every other man doesnt exist), but he was an idiot who couldnt think of anything better, or he thinks his followers dont deserve more than 72, and he would be able to explain using physics how to get to heaven, such as how to travel to other universes where this situation would be the stable/efficient situation that would actually happen in other universes
      
    - suppliers shouldnt be supplying input resources like funds (the possibility of a solution), but solution metric/goal-based output resources like solutions (a guarantee of a solution), which can form a basis for a currency, in addition to adjacent solution inputs like insights

    - feudalism/castes built around access to & investment in computational methods/tools (communication, regulation/legislation/enforcement, quantum computing, optimal storage, compression algorithms, optimal data structures, powerful chips, pre-computations, storage of prioritized info, info prediction/derivation/finding/generating/learning/understanding/organizing/integrating, task automation, cryptographic blockchain-based asset-tracking/verification, security creation, error creation, hacking/theft, experimentation tools, people manipulation, infinity computations to reduce overall computational complexity by identifying an infinite set by differences from other infinite sets, info falsification) which can replace & compete with each other
      - each entity that survives will have to have a competitive implementation of all of these if they dont want to be susceptible to an attack from any of them
      - predators arent good at solving problems bc they always use the same tactics, which work enough times on other predators to keep using in all circumstances, even when they dont work - lying, stealing, forcing, killing 
        - bc they keep re-using the same sub-optimal solutions, their brains arent evolved and they cant compete with smart people, theyre dependent on smart people who have the only power that matters anymore, and if smart people collude to prevent them from accessing solutions, they dont get solutions bc they cant generate them on their own, even when you explain everything to them & they have all the info they need (which they already did before being educated, they just couldnt use the info they had to derive solutions bc they cant think at all), & theyll fail without smart people
        - predators would still be struggling & failing to invent fire if it wasnt for smart people to figure it out & copy
        - solutions to this problem
          - if smart people collude to hide their work permanently, they would be able to destroy all the predators by depriving them of solutions
          - smart people can take pity on predators and try to make them smart so they can grasp meaning, become independent of smart people & independent of crime, & solve problems on their own

  - when is it optimal to store a mixed structure of varying specificity (like a type, intent, cause & a specific example)
      - when there are potential uncertainties to resolve, like whether the example represents a new error, type, or variable, bc the example doesnt fit known structures

  - all primary interfaces can act like the problem-solving interface (start solving problem from the concept or structure interface and integrate all info back into that interface & frame the solution in terms of that interface) but the meaning interface (the interface interface) is the most powerful

  - apply concepts to structures

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
    - examine the distortion vector paths that adjacently decompose a data set into a prediction function from a base point/function set

  - add examples of:
    - mapping to structures & identifying contradictions its safe to ignore for applying a structure
    - system/object/rule/type change patterns
    - query examples for use cases like:
      - lack of information stored (match problem of type 'information lack' with interface query 'check pattern interface for similar patterns')
      - query problem breakdown & integration diagram
      - calculating various different problem breakdown strategies first before executing normal query-building logic for each
    - example of how to predict most interactive/causal concepts in a system

## diagram
  
  - diagrams:
    - error types
    - network of formats
    - efficiencies
    - alternate interfaces (information = combination of structure, potential, change or structure, cause or structure, system)
    - chart type: overlaying multiple 2-dimension variable comparisons to identify common shapes of variable connections (density of points added with a visible attribute like more opacity)
    - structures of emergence
      - example: 1-1 input/output relationship up an interaction layer, where extra resources that dont dissolve immediately on the higher interaction layer aggregate & form core structures like combinations, where interactions between combinations & sequences have different dynamics than the individual output interacting with other individual outputs
    - how emergent functionality/attributes come from interaction structures (sequences & layers)
    - intent-matching
    - interface overflow (to sub-interfaces), interface foundation
    - workflow
      - function to identify relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'
    - conceptual math interface query
      - use lattice multiplication as standard example, other than core operations (add/multiply mapped to language, concepts like irreversibility/asymmetry mapped to math)
    - interface conversion, matching, starting point selection (applying structure, checking if relevant information is found)
    - sub-functions of core functions with distortions (identify/filter of find)
    - dimension links higher than 3d that are depictable in the same network space
      - should show variables that impact other variables, the change rates of these relationships
      - overall impact should be calculatable from these relationships
      - should show similar movements for correlated variables
      - should show skippable/derivable variables (variables that can be resolved later than they normally are)
      - should show meta forces for overall trends in change rules (direction of combined variable forces)
      - should show limits of measurability & threshold metrics
    - specific concepts, core functions, concept operations (combine, collide, connect, merge, apply), ethical shapes
        - variable accretion patterns (how an object becomes influenced by a new variable, complex system interaction patterns, etc)
        - potential matrix to display the concept
          - map parameter sets to potential matrix shapes 
        - cause (shapes & ambiguity), concept (evolution of concepts, networks, distortion functions)
        - argument
      - system layer diagram for each interface to allow specification of core interfaces & other interface layers (interface interface)
        - system layer diagram for structures to include layers of structures 
          (beyond core structures like curves, to include n-degree structures like a wave, as well as semantic output structures like a key, crossing the layer that generates info structures like an insight, a probability, etc)
    - map variable structures to prediction potential for problem types, given ratio of equivalent alternate signals
    - vertex variable structures
      - quantum physics, prediction/derivation tools, build automation tools, testing tools, learning/adaptation tools, system rules, computation power are all vertex variables of information, since they can generate/derive/find information
        - which structure (sequence, network, set, or cycle) of vertex variables is most efficient
    - core component attributes: identify any missing attributes/functions that cant be reduced further
    - absolute reference connections with metadata structures like networks/paths


# content/config

    - import insight history data to identify insight paths (info insight paths like 'lie => joke => distortion => insight', system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub')
    - define default & core objects necessary for system to function (out of the box, rather than minimal config necessary to derive other system components & assemble)
      - add default functions to solve common problem types
      - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially identifyd in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.
    - systematize definitions of info objects
      - include analysis that produces relationships of core objects like opposites to their relevant forms (anti-symmetry) in addition to permuted object states (asymmetry), such as an anti-strategy, anti-information, anti-pattern
      - organize certainty (info) vs. uncertainty objects (potential, risk, probability)
      - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers
      - add technicality, synchronization, bias, counterintuition, & certainty objects leading to inevitable collisions
        - error of the collision of compounding forces producing a phase shift
        - lack of attention in one driver and false panic in a second driver leading to a car crash given the bases where their processes originate
      - define alignment on interfaces (compounding, coordinating, parallel, similar, etc)
      - add core info objects (core strategies, core assumptions) so you can make a network of graphs for a system
    - add function logic for:
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
