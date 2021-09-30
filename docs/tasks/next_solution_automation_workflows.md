# add to solution automation workflows

      - format problem structures in various default formats determined by various useful structures (like core interaction functions such as 'filter' or interfaces like 'change'), where the useful structures have associated useful structures to design structures of these useful structures that can be used to fulfill problem-solving intents
        
        - like how by default:
          - 'strictness' is relevant to 'filter' intents
          - 'change types' and 'change units' and default operations like 'combine' are relevant to 'change'

        - change
          - identify relevant unit structures ('change' unit structures)
          - generate structures of 'completeness' of relevant unit structures ('all possible combinations' of change unit structures that can be used to create other changes)
          - find contribution of each change structure, prioritizing solution metric of 'fewest possible change structures'
          - solve for changes (v,w,x,y) applied to all possible types of relevant unit structures (change unit structures, like variable, variable transformation, & variable interaction units) to generate output z
            - v * core change unit + w * synced change unit + x * compounding change unit + y * constant change unit = z

        - filter
          - strictness: apply filters of varying strictness as needed
            - required
              - probable
                - possible

        - these structures have associated useful structures by default bc of their definitions, and they can be used to represent/solve all problems/solutions

      - apply useful structures to fulfill problem-solving intents applied to problem/solution structures, to find new solution automation workflows
        - example: apply 'input-output sequence' to fulfill problem-solving intent of 'filter solution space' or core interaction function 'connect' applied to problem/solution structures to identify new ways problem/solution structures can interact in a useful way (as in fulfilling a 'problem-solving intent' like 'find new solutions given known solutions' or 'filter solution space')

      - derive error metrics (indicating an incorrect solution) that could have solved the problem faster if known in advance & apply to fulfill problem-solving intents like 'filter solution space'
        - example: for the 'find a prediction function' problem, find neutralizing differences as a way of finding a 'balanced/representative/average' or 'approximate/general' solution that minimizes some error
          - derive input/output-connecting metrics of successful prediction functions
            - input/output-connecting metrics could include:
              - the ratio of numbers of data points above/below or difference between local/absolute extremes or near/far or points on exponential/constant/subset connecting lines from a successful prediction function representing those points
            - nn algorithms are not really 'laerning' in the sense of learning 'absolutely new info' (only locally new info about which way to move weights) so much as 'approaching an equilibrium representing a data set'
            - the equivalence represented by the function is the balance between differences like errors & sample statistics, incentivizing the decrease/increase of a particular output value for the function, which is represented in a standard implementation using an average to represent/approximate that equivalence
            - other structures that represent a 'balance between differences' can also act like a symmetry/equilibrium, and other representation structures can be applied to find alternate/subset/integrated prediction functions
          - once the prediction function is known, derive a custom 'error metric' (similar to least squares) that could have been applied to arrive at the output prediction function faster, and derive an algorithm that could have connected inputs/outputs to the error metric, so the logical flow is 'predict useful error metric for these inputs/outputs' then 'apply error metric to find prediction function'
        - alternate 'representation' structures would include:
          - high-priority points, where x-values that map to an less important y-value are instead assigned the adjacent high-priority y-value
          - another algorithm to select a more representative adjacent point or to select between equally adjacent & high-priority points
          - find & apply 'adjacent averages' if the data set is adjusted in some way like with regularization or imputing missing values or applying an adjacent transform or identifying alternate population means with random subset sampling
        - generalization: this is different from other solution automation workflows in that it connects problem inputs (data points) and solution outputs (prediction/summary/representation function) using relevant statistical metrics like averages about the input/output connection function that can be used to find the solution output faster bc the statistics are relevant & descriptive of the solution requirements & the problem/solution connection (the 'average' is relevant to intents like prediction/generalization/representation), and it applies similar inputs (like error metrics) to related solutions like regression to optimize finding the prediction function, so the problem becomes a problem of solving a related problem (regression) with a known solution or solution-finding method

      - apply useful structures to fulfill useful core interaction functions (like 'replace') applied to other useful structures with known solutions to fulfill problem-solving intents like 'find new solutions'
        - example: with the 'find a prediction function' problem that applies insights about optimal interaction rules (like 'regularize' to 'generalize') and structures (like 'alternate routes to support non-linearity'), other structures that can replace an 'alternate route set' or 'input-output sequence set' include: 
          - other structures that a neural network can support to capture useful structures like 'change types', in addition to or replacing 'alternate routes' (which can be implemented specifically as 'input-output sequences')
            - 'alternate definitions (definition of difference, relevance/significance, representation/average, cost) & functions (routing, activation) & constants (initial weights, learning rates)'
            - 'alternate structures (trees, networks, routes)'
            - 'alternate data sets within a change range'
            - 'alternate start/end points' (start with different variables, aim for different output variable that has relevance to the original problem)

      - filter structures of truth by those structures which dont require a structure of falsehood to fulfill core interaction functions like 'connect'
        - example: for the 'find a prediction function' problem, filter out variable interactions that can only be connected using structures of falsehood (lie of omission, false equivalence, etc)

      - identify the meaning (context, or 'system fit') of existing solutions, & apply methods to abstract the meaning to generalize it to other contexts, switch contexts & execute other meaning operations that are useful for fulfilling problem-solving intents
        - example: for the 'find a prediction function' problem, the meaning of a particular regression function would include various definition routes, such as:
          - 'the regression function, given the data set, pre-processing (data conversions, data filters, data standardizations/normalizations, etc), error function, & method to find the regression function'
          - 'the application of the concept of average to find a line minimizing error determined by a particular distance definition from that average, given data preprocessing, error function & regression function-finding method'

      - derive meaning of a problem & its associated solution meaning to detect if a context switch or meaning generalization can be a useful structure for a problem-solving intent
        - example meanings of a 'problem' include:
          - 'a difference that shouldnt exist, given rules about what differences should exist & the definition of a difference'
          - 'a structure that shouldnt exist, given rules about what structures should exist & the definition of a structure'
          - 'a change that shouldnt occur, given rules about what should change & the definition of a change'
        - example meanings of the associated solutions include:
          - 'a function to reduce differences that shouldnt exist, given rules about what differences should exist & the definition of a difference'
          - 'a function to remove structures that shouldnt exist, given rules about what structures should exist & the definition of a structure'
          - 'a function to prevent changes that shouldnt occur, given rules about what should change & the definition of a change'
          - 'a generative function of solutions to this specific problem type'
          - 'a solution-finding function of solutions to this specific problem'
          - 'parameters of generative functions of solutions that would solve this specific problem'
          - 'a function to change parameters of generative functions of solutions to solve problems in general'

      - identify more accessible info structures that can act like structures of truth even if theyre not & apply as structures of truth conditionally where possible
        - example: 
          - for the 'find a prediction function' problem, a 'sample data set + regression function' or a 'sample data set + regularization + neural network to find prediction function' are not explicitly structures of truth (the data may be inaccurate or contain noise, the neural network may not produce an accurate answer, the regularization may remove conditionally important info) but it has enough structures of truth (such as insights like 'remove inputs that dont change the output' and 'dont create a function that fits data samples perfectly to allow for generalization') applied that it may act as a good approximator/predictor of truth in some contexts (such as if the data has a sufficient ratio of correct points, if the neural network has enough nodes/layers to capture the complexity of the variable interactions, etc)
          - similarly, structures like 'consensus from democratic or weighted voting', 'patterns', 'useful structures', 'implications', 'difference from average', 'probability', 'previous success', 'prior information', and 'correlation' may act like structures of truth even when they're not, so these structures (& other useful structures) may act like a temporary substitute for truth when it isnt available (when 'no structure like a combination of known truth structures aligns/fits')

      - apply useful structures like 'alternative routes' to important/useful structures in a problem space (like 'probability of solution success' of an approximated or neural network-derived prediction function or composition/ensemble of multiple alternate functions or function subsets) in the form of solution metrics (like 'accuracy')
        - for example, for the 'find a prediction function' problem, apply 'alternate routes' to 'probability' to find other solutions to find useful structures like 'probability of solution success' among relatively similar possible solutions, using aggregation/integration structures like 'averages' or selection structures like 'filters' to 'filter the solution space', by applying 'alternate routes' and 'averages' to useful relevant structures like 'probability distributions'
          - calculate different probability distributions for each point in a set of 'important points' (like points on an input interval in the data set) with a big enough interval to connect the points in a generalized function, such as:
            - probabilities determined by adjacent points & adjacent point sequence/set patterns (patterns scoped generally, or for this data set, or for similar input variable change types, etc)
            - probabilities determined by stat measures like averages/modes & variance
            - probabilities determined by function/variable interaction patterns
          - use a weighting/prioritizing scheme to weight these distributions to predict a point given surrounding points, input variables, variable interaction patterns or other function structures
          - remaining points can be filled in if the interval is small enough to avoid missing important unique difference types or repeated difference types between other intervals
        - probability is an inherently important concept to 'prediction functions', and the probability of an output is an inherent statistic to functions in general, so its important that way, but is also important in that it can be used to differentiate solutions & measure their success & anything else that probability can be applied to help predict, given the complexity of differentiating between alternate prediction functions in some cases, like between those produced by slightly different neural network configurations or data sets
        - where probability distributions are those of related functions & subsets of the data set, such as where probabilities are determined as the conditional probability, given the implication of the slope change patterns of a subset of one possible likely prediction function, so this involves forming prediction functions for a point based on other points
          - apply prediction functions of structures (like points) given other structures (like subsets or adjacent points) to find a prediction function of the whole data set

      - avoid over-simplifying a solution so it appears to have no errors (or not identifying errors in a system where errors would be expected) by applying error structures (where they are likely to be erroneously missing) to build a more robust solution that handles errors
        - example: 
          - for the 'find a prediction function' problem, some variables cant be used to predict some other variables, so in a prediction function of those variables, errors would be expected ('no errors' would be the error in that function)
          - structures like 'similarities' or 'differences' are useful for a few different intents like 'compare' or 'identify' or 'filter', so if the problem requires more functionality than these functions can adjacently compose, there is a missing structure to avoid an over-reduction error
            - over-reduction error can occur by reducing a system to just similarities/differences, without the connecting functions on other interaction layers building meaning out of those similarities/differences (such as why are they different, in what contexts are they different, what types of difference are included in that difference, and how is that difference useful to other structures)
            - even if a problem can be solved in some case (like a best case) by over-reduced structures, its unlikely to be a robust solution that can change as needed according to input changes
        - generalization: this can be generalized to finding 'errors in errors' (a 'lack of errors' in an open system where variance would be expected is an error (a 'lack') of an error)

      - apply relevant functions (like a 'reversal') that preserve functionality in a useful way to structures with relevance matching structures (structures that have a 'sequence' like a function) to identifying alternate routes
        - example: the function 'understanding a system is a way of generating it' can be reversed to 'generating a system is an input to understanding it' if 'understanding' is the target output

      - identify optimal states (destinations) and work backwards to identify error states (origins) that an agent with a valid intent in the system might occupy that could be considered problem states, which are separate from the optimal states, optionally with error structures like barriers/gaps separating them, and identify routes & route patterns to connect those problem/optimal states of a problem space, as well as standardizing transforms of the problem space & corresponding state points that would reduce the problem into a more obvious solution set of connecting routes, to apply these routes & route patterns to other standardized problem spaces

      - apply 'approximate' structures of 'useful structures' like 'input-output sequences' (such as 'sequences with approximate input-output matching') as a way of finding useful structures to fulfill problem-solving intents
        - generalization: apply other problem-solving intent (like 'filter solution space') & related function type functions (like standardize, organize, approximate) to problem/solution structures such as useful structures as a way of finding adjacent & other important structures of problem/solution structures

      - standardize problem to a standard format & apply standard solutions for that format
        - example:
          - if problem input data has a sequence or a correlation or a variable (change type) structure, it can be identified by variable solutions like specialized machine-learning algorithms/networks
            - standardizing to 'change types' could invalidate the gains from specialized networks/algorithms
            - changes in a 'sequence' can be formatted as 'adjacent change sets' to represent changes usually found together
            - 'correlated' changes can be formatted as 'aligned change sets' to represent changes that co-occur
            
      - identify perspective that minimizes errors according to the solution requirements & apply that perspective as a solution filter
        - example: for the 'find a prediction function' problem, the perspective of 'find the average function' (a perspective which prioritizes common general expected values & patterns rather than specific examples & therefore has the implied errors associated with that priority) has errors of 'possible high differences between actual & average value', with an opposing error of the opposite solution 'find the best-fitting function that accurately predicts every point' being 'possible high differences between one sample value and another sample value', and if the solution metric is 'accuracy', error types of a solution that maximizes 'accuracy' would be preferred over error types of other solutions

      - incentivize or otherwise maximize errors to create the most differences between error & solution possible, then apply opposite structures to errors which should create solutions once theyre maximally different
        - workflow fit: this is a corrollary to the 'apply differences to errors to create solutions' workflow, but errors may be closer to their maximized state than to solutions, in which case this workflow would be more optimal

      - create a space where points represent states of variables that differentiate solutions & other states, where known solutions are indicated by minima or maxima, then identify useful structures like 'patterns of point sampling to find maxima quickly' and 'differences between solutions & other states' and 'differences in useful structures for solution-finding across different state spaces' and 'maximum change types between adjacent or any points (like exponential, signed change, intersection/zero/tangent-crossing change, etc)'
        - a variant of this would be an 'error state space' where known conceptual errors like 'inaccuracy' and 'over-simplicity' and 'trade-offs' occupy maxima and minima are found as possible solution states
        - a space can have overlaps in the structures determining errors, so isolating interface structures would be ideal, so that an error of 'ambiguous cause' would occupy a different point than an error of 'false similarities', but these would overlap semantically, as a 'false similarity' can indicate an 'ambiguity', so the state variables would have to be isolated as much as possible rather than including semantic overlaps, or overlaps could be indicated by other structures and the number of error structure overlaps closest to zero would indicate a possible solution structure, where structures would be arranged so that their semantic positions would be as adjacent as possible to form the corrollary of 'areas' (rather than a 'false similarity' appearing in multiple very different points)

      - standardize solutions from other systems & convert them to the problem system, calculating any missing solution structures & determining variables & generative functions of solutions & useful structures like efficient routes to solutions from input problem starting points
        - example: for the problem of 'finding a sorting algorithm' (like binary trees), standardize solutions so they can be applied to 'find a prediction function problems' (like bi-directional function non-linearity additions or other changes)

      - solve a more complex problem first & apply as a solution space or solution-finding method filter to find simpler problem's solutions in that problem space quickly
        - example: for the 'find a prediction function' problem, solve more complex prediction problems like 'whether a solution is biased', 'the correlation between AI research & weather' (should be somewhat correlated bc extreme weather requires tech to survive) or 'the correlation of interaction patterns of an environmental system with a social interaction pattern in cities' (should be correlated bc of system similarities in complexity, structure, & other attributes) and apply as a filter to simpler problems like 'find the correlation between these adjacent variables in the same system' (which are likely to have causal relationships so their interaction should be determinable with simple statistical methods rather than requiring complex analysis), which should have simpler relationships than the corresponding complex problem, and any simple prediction problem within the same system should necessarily have less variation structures than the complex prediction function of a system it inhabits, so the complex solution should be composable with the simple solution, and other logical relationships between these solutions should also hold

      - apply solution improvement/optimization patterns to generate solutions & derive more efficient methods of applying these improvements
        - example: for the 'find a prediction function' problem, this could take the form of applying adjacent operations like shifts & adding exponents to specify the function for the data set, & stopping specification at a certain point to avoid over-specificity, and a more efficient method of generating these improvements could be 'deriving average difference or difference patterns from function & data points & generating functions having that average difference or difference patterns'
        - the 'more efficient method' finds a 'vertex variable' in the form of the 'difference structure' applied as a 'requirement' of the solution function, which can generally 'find & apply useful structures to fulfill problem-solving intents' or specifically 'find a reduced route between input variable values & the prediction function'

      - find interface structures like 'interaction levels' where changes can align, as a component of solutions where change input/output is known on one level but not another & the interaction on another level is the target solution, or where the problem can be solved on the other interaction level
        - example: 
          - levels of interaction where changes align in the machine learning (specifically the multi-layer perceptron example) structure include:
            - weights/thresholds/biases & sum/routing/activation functions
            - value changes from inputs to outputs
          - so the unknown changes can be in one set of parameters that enable another set of known parameters
            - unknown parameters (weights/thresholds) and known parameters (sum/routing/activation functions)
            - unknown parameters (weights/thresholds & sum/routing functions) and known parameters (activation functions & required value changes (labeled data))
        - another example would be where the high-level or general intent requirement is known, but the sub-intents to fulfill that high-level or general intent are not known, on another more specific interaction level

      - if existing problem/solution structures (like useful functions) dont solve a problem, derive errors in those structures (like missing functions) & solve the problem of correcting those errors
        - example: 
          - for the 'find a prediction function' problem, if a causal relationship cant be established using time-based structures like chronological sequences, check if other structures can be explanatory, like adjacence determined by similarity (of inputs or position or interaction level), which is a good approximator of cause when sequential causal structures like causal chains cant be verified
          - if no structures are sufficient to explain a variable relationship function, then there is an error in the structure set, such as a 'missing structure', which may be found by applying interaction functions to structures (like function types) that havent been connected yet

      - find the interface structures like interaction level of related/sub-problems & sequence of sub-problems (related/sub-problems of the original problem, which are solved in the interface query) where connections can most efficiently & otherwise optimally be made (using adjacent or available operations) and solve the problem there first, then design the rest of the interface query to fulfill that solution on other interface structures (like on other interaction levels)
        - example: find out if solving the 'input-output connection problem' as a sub-problem of the 'find a prediction function' problem using a function & weight network can be solved more efficiently by connecting value sequences first, or by connecting function input-output sequences first, or by deriving weights first & then other parameters like threshold values, or the reverse, etc
  
      - connect adjacent structures to find standard/base solutions (like 'where adjacent point-connecting functions create averages that intersect to create a regression function bc an average is by definition related to the prediction & is also relevant as a symmetry structure'), and connect aligning structures on multiple interfaces to find meaningful solutions (like 'where subset functions are reflected in an aligning neural network structure, thereby also creating an alignment between inputs/outputs to model more nuanced change types, bc the network can support customized function units representing local average functions, allowing the solution to be re-used across many function types', which aligns on the structural interface bc of the 'structural similarity' between subset function & the local averages formed in neural networks, and the system interface bc of the 'alignment' structures and the meaning interface bc its 'useful' for other queries) bc some structures like adjacence/alignment can more optimally find solutions of a particular solution metric like accuracy 

      - find useful interactive structures (like 'matching structures', such as 'requirements' & 'functionality to fulfill requirements') as an input to problem-solving intent functions, workflows, or interface queries

      - find symmetries & variables/functions of them between alternative workflows having the same problem/solution structures & result, and apply these variables to generate other workflows
        - example: 'aim for adjacent state to the solution instead of the solution, then transform it to the original problem solution' and 'solve a different but similar problem' and 'solve the opposite problem, then transform it to the original problem solution using opposite structures' can both have the same resulting interface query & result
          - their common structures involve variations of the 'aim for a different problem-solving intent or destination' and 'change a base solution into the original problem solution' functions, to which changes can be applied to generate other workflows
          - examples of 'adjacent states' or 'similar function formats' for the 'find a prediction function' problem include 'parameterizing a function based on a general function specified by the parameters' (where the function would be in the format of the 'parameter values')

      - apply useful functions/structures to describe a problem space's interactions so that if structures of those useful structures dont solve the problem, any other interactions must necessarily contain the problem structures
        - example: identify all the structures in a problem space that would be the output of the 'find' function (identify all the 'definitions' that would be found by applying the 'find definitions' function to the problem space)
          - then do the same for the other useful functions ('organize', 'explain', 'reduce', 'connect') 
          - once you have the problem space described by these functions/structures, if the problem isnt solvable using those structures, then the other interactions not mapped by those useful functions/structures must contain the problem
          - this applies the 'opposite' structure to create a 'solution space filter', where possible solutions are initially the set of structures of useful structures and if not found among those structures, the solution space is the set of structures not mapped by the useful structures
        - this mapping can be re-used for future interface queries in that problem space
        
      - apply interface structures to the cross-interface interface structure (apply 'differences' to 'variables' which are both on a cross-interface structure connecting associated structures on the structure/change interfaces), given that the cross-interface structure forms a symmetry of related structures and applying changes to this symmetry would identify alternate combinations of structures that preserve the original meaningful connection, as a way of generating useful structures

      - identify 'problem-function connecting' functions on the interaction level of specific problem structures and other function types, such as 'overlap equivalent problem structures' or 'limit possible connections between problem structures' as specific useful structures in the problem space to start from, to fulfill the 'filter the solution space' problem-solving intent
        - this connects other function types with problem structures, other than general known problem-solving intents like 'filter the solution space' or 'reduce/remove the problem or its cause' and generally useful function types like useful interface functions like 'find structures in a structure', and core interaction functions like 'reduce' and general functions like 'find' or interim functions like 'organize'
        - useful structures produce some output that fulfills a useful intent, and functions that connect problem/solution structures with other useful structures like useful functions, either generally or specifically, would also be useful by default
        - generalization: a generalization of this workflow would be to find a function interaction structure (like an interaction level or interaction level cross-section) that would be particular useful for solving a problem, and find/derive/generate functions on that interaction structure

        - example of creating a logical 'requirement' structure by applying interface structures (like 'equivalence', 'definitions', 'connections', 'interim structures', 'overlaps', 'skips', 'new structures', and 'difference/opposites/reversals')

          - 'requirement' rule structure created by two initial rules: 
            - 'if all cats are mammals, and a particular animal is a cat, then that particular animal is required to be a mammal by definition'
          
          - why is this true? bc:
            
            - one of the objects has a definition:
              - a 'cat' is 'defined' to be a 'mammal'
            
            - and another object has a definition:
              - a 'particular animal' is 'defined' to be a 'cat'
            
            - using the connection function 'is', indicating some form of 'equivalence' or 'containment'
              - the connection function 'is' indicates equivalence (a cat = a mammal) in this context
                - theyre equal in the context of 'containment/possession', not in the context of 'identity'
                  - 'is' here means 'is a member of the type': 'a cat is a member of the type of mammal' and 'a particular animal is a member of the type of cat'
              
            - and a 'connection' in the form of an 'equivalence' exists between these two defined 'equivalence' rules
              - a 'cat' is in both of the rules, indicating an equivalent structure they have in common, thus forming a basis for connecting the rules around their common component
              
            - and an 'equivalence' in the form of the equal connection functions
              - the connection functions used in both rules are also equivalent ('is' is used in both rules)

            - alternatively, there is an 'overlap' structure between a 'particular animal' & a 'cat', and between a 'cat' and a 'mammal', which create another overlap structure between a 'particular animal' and a 'mammal'

            - which means that:

              - a 'requirement' in the form of a 'combination' rule or 'overlapping rule sequence' can be created
                - the rule "a 'particular animal' is a 'cat' is a 'mammal'"
              
              - a 'requirement' in the form of a 'new connection' or a 'interim node-skipping rule' rule can be created from the equivalences in the connection function 'is'
                - the rule "a 'particular animal' is a 'mammal'"

                - the 'interim' structure of a 'cat' can be removed, since the 'is' equivalences connect the objects, and applying the corresponding version of the attribute of 'associativity' available to equivalent operations
                
              - a 'requirement' in the form of a 'connection rule limit', in that the following rules cannot be applied to 'connect the defined structures', only to 'limit possible connections'
                
                - attributes that reverse the order of the connections cannot be applied in an equivalent way
                  - the reversed-order rules of 'a mammal is a cat' and 'a cat is a particular animal' cannot be applied to infer the rule that 'a mammal is a particular animal' (false because it implies that 'all other mammals that are not the particular animal are not mammals')
                  - the reversed-order context-specific rules of 'a mammal is a type of cat' and 'a cat is a type of particular animal' are similarly false

          - in summary, these structures can be applied to generate a 'requirement' structure, given how 'equivalence' structures can be 'connected' and the attributes associated with 'equivalence' that can be applied to them

            - the primary requirement structure (the associated connection rule) can be inferred in multiple ways, from the multiple equivalences that exist in the initial two rules given
              - it can also be inferred by the common component of the two rules, assuming that if two rules have a component in common ('cat'), they might be related and might interact
                - if they further have other equivalences ('is') they are likelier to be related
                - if their connections indicate equivalence itself ('is' is a form of 'equivalence') or are a definition route of equivalence or some version of equivalence, they can inherit attributes of the 'equivalence' concept definition (like associativity), and their interactions can be inferred from uncontradicted implications or requirements from those related definitions

            - the second requirement structure (the limit) can be inferred using opposite structures, to check if the attributes/connections are true once negated/reversed
              - this is applied to the attribute 'order' of the 'connection rule', rather than negating the 'connection rule' itself

            - so by deriving the concepts like 'equivalence' related to a structure (like the initial set of two rules), and pulling the attributes/functions of those concepts given their definitions & applying those to the structures, other structures related to 'definitions' like 'requirements', 'limits', & 'rules' can be identified

          - identifying core/interface structure (like 'combination') functions like 'limit possible connections between rules/components' and 'connect definitions by equivalences' is useful, but identifying how these can add value in this particular problem or how they can interact given their requirements/definitions & other structures is even more useful 

            - apply the core/interface structure function 'identify required structures from defined equivalences & differences' to 'find a requirement/rule connecting "particular animal" and "mammal"'
              - this applies a useful core/interface structure function to this specific problem

              - why is this useful? bc:
                - the problem is:
                  - specifically to 'find out if particular animal and mammal are related'
                  - generally to 'find out any other rules or other requirement structures that can be inferred'

              - so identifying useful core/interface structure functions relevant to these intents is useful, and fitting them to the problem/solution structures is even more useful

              - these functions fulfill functions like problem-solving intents & other functions specific to this problem, so they are inherently useful, even if not to this specific problem
                - 'connect definitions by equivalence' fulfills a 'connect' core interaction function
                - 'find limit structures of connection rules' fulfills a 'filter the solution space' problem-solving intent function

              - once you know these specific functions would be useful, you can direct your interface query to find/derive/generate those functions, so this is another way of building an interface query, making it a solution automation workflow
              
      - find/derive/generate problem structure that would produce a solution to a problem in another system
        - if a solution structure with a particular attribute/function is required, find/derive/generate a problem structure like a problem system that would produce that solution structure in another system & test it in the original problem system
        - find/derive/generate a system with reasons/causes to generate a structure with the attribute/function, and which uses the structure for a similar cause/intent
        - example: for the 'find a prediction function' problem, this would involve finding a similar data set & using a successful solution function for that data set, similarity based on interface structures like cause or variable interactions or change types

      - apply intent interface specifically to derive specific problem-solving intents for a specific problem type that all problems can be converted to, intents that would be useful in solving the problem
        - example: deriving the intent of 'reducing variables' as a useful problem-solving intent for the 'find a prediction function' problem involves applying the definition of concepts like noise/outliers as an indication of irrelevant variables
          - 'reducing variables' could then be an intent in a default interface query connecting the problem/solution for the specific problem type of 'find a prediction function', after converting a problem to a problem of 'finding a prediction function' 
        - generalization: 'reducing variables' would be relevant specifically in 'reducing variables to unique change types', which is a useful structure, so applying useful functions like 'reduce' to important problem structures like 'variables' and connecting those functions with useful structures like 'unique change types' is a generalization of this workflow

      - apply core interaction functions (like 'reduce', 'connect') and other function types (like 'abstract') and other useful structures to all relevant structures of the problem space to find useful changes to relevant problem structures that would reduce the problem of fulfilling problem-solving intents for those structures
        - example: applying 'reduce' to a 'variable' structure in the 'find a prediction function' problem into its components/inputs/attributes/generator may make useful structures like 'structural similarities' between relevant structures like 'variables' more obvious so they can be 'reduced' into one variable like a 'type' for relevant specific problem-solving intents like 'reduce dimensions' or 'feature engineering'

      - identify the maximally different functions fulfilling a 'core interaction-interface' function (like 'reduce change types') from existing functions to begin a search for new solutions if existing solution functions produce errors
        - combinations of core interaction functions & interface structures would be likely useful in solving problems
          - examples: 'filter cause structures', 'connect interaction layers', 'sort useful structures'
        - this function type connects core interaction functions with interface structures, similar to interface functions like 'find a structure in a structure', or interim functions like 'organize' or 'predict'
        - the difference in this function type is that these functions are likelier to be useful than other function types like general functions, core interaction functions which must be combined in a structure in order to be useful, or interface functions which are likely to require their own interface query
        - this function type is similar to problem-solving intent functions, interim functions, & interface queries, and may be able to be used as a substitute of some interface queries
        - generalization: 
          - after generating the set of possible useful interface queries to solve a problem, identify the emergent functions that are the most often required in the interface queries, to identify new or temporarily/conditionally useful function interaction levels & their metadata (why theyre useful, what is required for them to be useful, useful variants, etc)

      - find cross-interface structures (like the 'intersection' of 'structures' and 'causes' and 'patterns' of 'variable interactions') that interact with important problem structures that are determining for the success of a solution in various error type conditions
        - example: for the 'find a prediction function' problem:
          - if a function has an error type of 'false similarity' (with different cause), the actual cause is different than the assumed cause allowing selection of that solution, so structures of variable interactions & causes would be useful in filtering out these solutions
          - 'variable interactions' are an important structure for the 'find a prediction function' problem, so applying interface structures to this important structure can identify useful structures for building a robust solution to error types
          - other important structures include the following, but 'variable interactions' are particularly important, as theyre the highest variation structure that is adjacent to the solution format ('a prediction function') & require fewer non-standard assumptions than function formats (subsets/alternate/component/conditional)
            - input structures: data points, variable ranges, data types
            - interim structures: data subsets, function filters/requirements
            - output structures: subset/alternate/component/conditional functions
          - functions like the following would identify useful structures of variable interactions & other interface structures that would determine success under various error type conditions
            - find multiple alternate functions that follow variable interaction patterns more adjacently than the original line or better align with variable interaction causes
            - apply changes to data set to find adjacent data sets with clear regression lines

      - change inputs/outputs to solve a different problem or change the sequence/structure of problems to be solved
        - example: rather than solving the initial problem to connect the original problem with a solution, solve a problem that is one-step closer to the solution & solve for a solution that is one-step away from the original solution, then apply changes to the inputs/outputs of that solution until it fits with the original problem/solution
          - rather than solving the problem of 'find a prediction function' for original independent variables, solve the problem of 'find a prediction function' for aggregate variables (like types that summarize the original variables), because an alternate intent of 'predict the data' is 'summarize the data', so starting from a summary as an input is a step closer to the original solution format, which is a prediction (or summarization) function
            - independent variables of data set => summarizing variables like types or aggregates or compressions => prediction/summarization function for dependent variables
          - once you have this 'inner' solution, fit it to the original problem/solution by applying changes to the 'inner' solution
            - apply changes to the summarization function of the summarized independent variables until it acts as a summarization function of the original independent variables that can predict the dependent variable
          - another example would be to change the dependent variable predicted (find a prediction function that predicts z instead of y) then apply changes to that solution until it predicts y
          - another example would be to abstract the inputs/outputs and solve for that prediction function instead, then applying specifying structures to the general solution, until it solves for the original problem that is an example of that generalization
        - workflow fit: this is a generalization of workflows that change inputs/outputs to solve a different problem, or solve a different sequence/structure of problems

      - identify alternate interchangeable structures that form an interchangeable solution to a problem in some condition, to cover as many conditions as possible
        - example: an 'explanation', 'description', 'generator/cause', 'compression', and 'summary' are alternate structures that can replace/approximate a 'prediction function' for the 'find a prediction function' problem, so if those can be solved for more quickly than a 'prediction function', they may be approximate/temporary/conditional substitutes for the 'prediction function' solution format
        - workflow fit: this is similar to the 'find an approximate solution' workflows, but involves applying the analysis to interchangeable structures in general & to as many conditions as possible to approximate/replace the original solution format

      - find/derive/generate 'counterintuition' & other 'complexity' structures that a solution-finding method should be able to handle & their associated difference structures from error & error-causing structures, using cause as a useful structure to find other relevant info that can be used to filter the solution space or differentiate between solutions/errors
        - example: distorting input so its maximally distorted but should still be identifiable as a category label in a categorization problem, and connecting it to differences from error structures (structures that would result in output of the incorrect or unknown label), or producing/expanding those differences in the input
        - 'alternate generative functions' of a species (like an agent building an artistic representation of a species) could produce 'structural similarities' resulting in an 'unknown' label error, so identifying features indicating alternate generative functions would be important to include in the solution-finding method (differences between a 'dog' and a 'drawing of a dog')
        - differences from structures of complexity like ambiguities would also be required to identify, as well as alternate feature sets that could differentiate between labels when some features are missing or unidentifiable
        - the highly distorted image isnt an error (it would be a complexity structure) but structures differentiating it from errors & errors that happen to also be complexity structures would produce a more robust solution-finding method, so the solution-finding method would have to included those differentiating structures
        - a 'photo of a cat with a cartoon in it' would be differentiable from a 'photo of a cartoon of a cat' by features like natural vs. agent-generated randomness & natural vs. agent-generated detail, so the solution-finding method would need to be able to identify those structures
          - this means the interface query would include 'find randomness structures' and 'find detail structures' and 'find agency structures' as calls to find/derive/generate functionality fulfilling those intents
        - by generating the distortions, we start by knowing the cause of the distortions ('an agent drew a cartoon'), and the related objects of those causes ('human error', 'limited time or attention span leading to lack of detail')
          - this means we know what features would differentiate these distorted inputs from error inputs of various types (incorrect output label, unknown output label), so error structures & error causes should be more identifiable given the extra info we have about solution structures that happen to be complex

      - the interface query is basically 'what questions need to be answered to solve this problem' - another variant would be 'what information could allow this problem to be solved with this solution-finding function'
        - example: in the 'find a prediction function' problem, this would take the form of 'finding what structures of information would have enough complexity to require a machine-learning algorithm to find a prediction function'
          - the 'find a prediction function for image categorization' problem would require complexity in the form of structures like ambiguities, similar alternative opposites, distortions, & randomness, so images with those structures should be expected & could be derived from the problem statement
          - a solution function that can determine the outputs from those inputs would have structures like 'variable isolation' (using 'feature engineering' functions) & 'complexity reduction' (using 'generalizing' functions) to connect those inputs/outputs
          - if a solution-finding function cant solve the problem given the expected inputs, changes can be applied until it can connect the expected inputs with the outputs
          - this means 'the solution-finding method requires the referenced 'variable isolation' and 'complexity reduction' structures, to resolve the ambiguities & other complexity structures requiring the solution-finding method in common image categorization data sets'
          - from the typical complexity & other problem-causing attributes of the problem, which would require using this solution-finding method (given the method intents like 'find a prediction function'), we can derive the structures the solution-finding method would need
          - all that is required to use this workflow is the problem statement 'find a prediction function to categorize images' and the solution format 'categorization labels', from which the structures required for the method can be derived given the implied complexity of the problem
          - this applies the logic interface to derive implications & requirements as well as the concept interface to derive complexity structures

      - apply various alternate formats like sequences, preceding/succeeding sequences, & adjacent subsets, & defining values like extremes as inputs to prediction functions, to predict the adjacent/next item in a structure having relevance by adjacence/order (like a sequence of y-values for an x-value sequence)
        - example: rather than 'trying to predict a line', the problem can be a problem of 'trying to predict the likelihood of a value, given the preceding values' and 'trying to predict whether the y-value sequence is likely given the prediction functions that succeed at predicting the next value'
          - predicting an initial value from the following values, predicting an adjacent value from neighboring values, and predicting local from global values are examples of predictions that can be made by applying prediction functions to find a likely prediction function
        - generalization: this can be generalized to applying prediction functions to predict various interaction structures, predict which functions will be useful, predict important variables, and other structures required by a particular workflow
        - another variant would be to 'apply probability & structure interfaces so that from structures that can be verified, identify probability of other structures until theres a structural interaction that cant be verified with some degree of certainty'
          - example: for the 'find a prediction function' problem, given that there's a structure of 'many change types' in a parabola as opposed to a line (one change type, as in constant/charged change), whats the probability of a cycle structure or intersection with zero in the same function (how often do 'many change types' occurring in a parabola defined locally occur with a cycle structure defined elsewhere in the function)
        - this is only applicable in cases where the structure being predicted has relevance to the input structure (values in a continuous function can be connected in a sequence structure or adjacence structure like a subset)

      - solution automation workflows can be derived from core structures like combinations, sequences, and variables & interface structures applied to these core structures like inputs/outputs, interactions, & types
        - example: 
          - 'combination' structures go with the workflow 'build a solution out of components', where components are interface structures that can be combined to create a solution
        - generalization: 
          - this can be generalized to 'find the core structures of a system, and apply interface structures to those core structures, then fit these applications to fulfill an interaction function of problem/solution structures'

      - identify causes like inputs/requirements of useful structures (like a 'question that triggers a useful structure like an optimization'), & connections with useful structures (like systems where useful structures are default), & system context structures that allow/incentivize useful structures to develop or dont prevent useful structures from developing (like a 'lack of limits'), and apply those structures as the adjacents/inputs to finding useful structures or the generative structures of useful structures
        - alternatively, apply the definitions of useful structures & their metadata, like that a useful structure is defined as:
          - having a structural alignment with an intent, making it useful for that intent
          - existing in a space with variation, allowing for the existence of non-useful structures that make it useful by comparison, like the existence of alternative sub-optimal routes
          - developing in a system where the system's existence is only achievable by developing a better way to fulfill an intent, incentivizing development of useful structures

      - apply solution structures that fulfill one problem-solving intent (like 'preventing a problem' or 'solving a related problem') to another problem-solving intent (like 'fixing a problem')
        - example:
          - preventative solutions like vaccines have a solution success cause (using the immune system to prevent infection) that allows for re-use across other problem-solving intents such as fixes (like immunotherapy treatments)
          - the 'golden rule' draws attention useful 'preventative' objects like empathy, but can also be used for other problem-solving intents like 'restitution' (fixing a crime), by connecting criminals/victims in other ways than empathy thought experiments (like trading criminal/victim positions, progressively applying more punishments rather than applying the same crime, connecting criminals with other victims of the same crime rather than their victim, etc)
          - the reason the 'preventative' solution works is its interaction with 'empathy' or the 'immune system', and this cause can be re-applied in other problem-solving intent solution structures than 'prevention'
        - generalization: this can be generalized to re-applying any problem/solution structures across different problem/solution variables (like different problem-solving intents) that have an important structure in common (like 'success cause'), indicating there is reason to re-use one structure in another context

      - apply useful structures (like opposite structures) once applied to interfaces to fulfill functions of relevant types (like problem-solving intents, core interaction functions, interim functions, general functions) & organize these 'useful structures for function types' to find other useful structures connecting the useful structures (like useful structure sequences, hubs, overlaps, symmetries) in the 'useful structure network'
        - example: with the 'find a prediction function' problem, the function might be verifiable as not a shape, a set of subset or conditional functions, a linear function, & other solution formats
          - this is applying the 'opposite' structure to various difference types in solution format structures to fulfill the 'filter solution space' problem-solving intent, applied to various interfaces ('opposite' applied to 'potential' interface to produce 'conditional alternative functions')
          - another example is how the 'reduce' function applied to 'distance' or 'difference' structures is a useful structure for the 'connect' function
        - 'format a problem in terms of an interface query that can be fulfilled with functions on this function type network or useful structures on the useful structure network to reduce computations required' is a solution automation workflow that can use either of these networks once defined

      - calculate how much certainty can be determined with input info & apply that as a filter of the solution space & the solution format
        - example: with the 'find a prediction function' problem, the function may only be determinable within a certain range of alternative functions or within a certain parameter range, which may form a solution format of an area rather than a line/curve
        - knowing that only so much certainty in a solution can be derived with given inputs, the solution space can be filtered with an interface query connecting to that certainty structure instead of the original solution structure

      - find/derive/generate specific structures that are useful for specific problem-solving intents, general/core/interim function intents, or interface query intents, to implement those intents automatically
        - this involves identifying the cause of useful structures' usefulness & applying as a generative function
        - example:
          - specific structures like 'maximizing differences' and 'input-output sequences' that are useful for problem-solving intents like 'filter solution space' & 'connect problem/solution', and other function intents bc of the useful structures they generate like 'adjacence to inputs of function intent'
            - maximized differences are more adjacent to the input of 'identify/filter' functions & may reduce the work required by those functions to reach the output
            - input-output sequences provide default possible solution or solution component structures to reduce the work of filtering the solution space, making the input to the 'filter solution space' function more similar to its required output (a reduced set of solutions)
            - useful structures can be found/derived/generated by which structures create differences (like a difference in the form of a 'reduction' in possible solutions) that happen to be useful for various required intents (like 'avoid errors' or 'identify difference')

      - derive functions connecting function interaction levels (general, core, interim functions) and all the routes on the function network that are particularly useful for a specific function that solves a problem, then identify the average implementation & its parameters to define a standard function to solve that problem (fulfill the specific function) which can be adjusted as needed for varying intents
        - example: 'remove similarities for comparison' and 'standardize to emphasize differences' are useful connecting paths on the function network for the 'find a prediction function' problem (or the 'predict' interim function) which can also be formatted as a path on the function network

      - apply ml with useful structures for a problem-solving intent (like 'generate code for a general function automatically') that combines specific features into general features to combine specific structural functions ('combine', 'sort', 'reduce') to generate general functions ('filter', 'identify', 'standardize')
        - the reason 'find a prediction function' is a standard problem format that any problem can be formatted as, is bc its adjacent to an interim function 'predict' ('find input-output sequence', 'identify causal variable', 'identify vertex variable')
        - other standard problem formats are adjacent to other core/interim/general functions
        - generalization: this can be generalized to 'find a solution with useful structures like 'similarities' in 'inputs/outputs' for a standard problem format like finding prediction functions that can be applied to the original problem once formatted according to the standard problem format'

      - apply interchangeable problem/solution & interface objects to each other, bc when there are interchangeable objects, that indicates they can be applied to each other in a useful way
        - example:
          - variables/functions are interchangeable formats, which can be applied to each other to generate useful objects ('variables of functions' like 'inputs/outputs/intents', and 'functions of variables' like 'determining/generating/causing')
          - find/build/apply can be applied to generate interim functions & common intents ('find a build method', 'apply a find method to derive a build method')
          - applying problem-solving intents to each other can direct the design of interface queries fulfilling each intent 'filter solution space' of problem of 'finding other problems to solve'
          - applying specific problem formats which any problem can be formatted as ('find a prediction function', 'apply sorting algorithm') can be applied to each other
          - core interaction functions can be applied to each other ('reduce connections', 'sort reductions', 'combine sorts')
        - these interchangeable objects tend to be on the same interaction level which can mean they are different useful variants of a core underlying base object, with overlapping definitions, and applying them to other objects on the same interaction level can produce more gains for an intent

      - identify useful structures for sub-intents of an interface query to use as default structures
        - example: for a sub-intent of 'find an example', structures of 'specificity' are more useful bc theyre 'more adjacent to attributes of inputs' of the sub-intent, 'more adjacent to input attributes' being a useful filter for useful structures
        - generalization: this can be generalized to 'find all the interface & problem/solution structures of useful structures', which would include 'useful filters' of useful structures for the 'filter solution space problem-solving intent'

      - identify the structures with highest impact on solution success
        - example: in the 'find a prediction function' problem, this would include standard 'contributing variables' & 'variable interactions', but also 'function structures' like 'averages', 'continuity', 'change rate patterns', 'waves/peaks/inflection points'
          - these have high impact on solution success bc theyre 'high variation', 'represent a standard', 'reflect the output of relevant variables like exponents or patterns', are 'relevant inputs like function component structures', or are defined to be useful 'patterns are defined to represent an abstraction of a change type'

      - identify the complete structures in a problem space & format the problem in terms of the complete structures for solution metrics like accuracy/robustness
        - example: variables arent a complete structure until some understanding rules are injected about their interaction structures such as cause & relationship to other variables, the context in which they are variable/constant, and their associated change types

      - derive which interface structures (like combinations/subsets) are relevant to useful structures (like variable interactions) using insight rules (like that 'adjacent features are likely to be dependent') & comparing possible usefulness structures
        - example: how to derive 'combinations' of 'variable interactions' as useful structures, given the insight rule 'adjacent variables are likely to be dependent'
          - 'adjacence' is 'similarity in position', and structures that are 'similar in position' are easier to fulfill intents like 'group', so 'combinations' are an 'adjacent' structure of this structure
            - the 'combination' structure also fulfills intents like 'isolate' for structures like 'dependent variables', and 'isolating related objects' or 'isolating objects of a type' are a useful function for various general/problem-solving/interim/core function intents
            - given that it can be adjacently used for various known useful intents, it can be considered a useful structure (after comparing it to the adjacently useful intent ratio of other possible useful structures)
        - workflow fit: this is similar to other workflows involving deriving useful/interface structures useful for other useful/interface structures or problem-solving intents, but with a filter for evaluating probability of usefulness compared to other structures

      - identify structures of determination (where once a structure is determined, the other structures dependent on it are also determined) & apply as 'reduction' structures of computation requirements in an interface query

      - generate maximally different perspectives to avoid over-incentivizing one perspective & its resulting error types, to apply as solution filters
        - example: in the 'find a prediction function' problem, maximally different perspectives would include:
          - 'find the right unique isolated variable interaction to equal the output variable'
          - 'check if the definition of objects is applicable'
            - if a 'variable' concept is not applicable to a particular structure, it will generate errors
              - example: 
                - if the 'sound' variable is only measurable by 'vibrations', it might be handled incorrectly, miss all the variation within the 'sound' variable, miss the fact that the 'sound' variable can act as an interface, and be a poor predictor of 'sound' variation & metadata like inputs/outputs
                  - the 'variable' concept refers to a 'unique change type', but it leaves out the 'related variable network' structure that all variables are nodes in & other structures relevant to that 'variable' definition, and would misidentify 'vibrations' as a change-determining variable rather than an attribute of the 'sound' variable, bc it would miss their interaction in the 'related variable network' inherent to a complete 'variable' definition, where usually a limited structural definition of 'variable' as 'unique change type' is applied
                - in the 'chihuahua/muffin' class identification problem, adjacent features arent isolatable bc they determine what adjacent features are possible (the structure of a skull determines what configurations of structures surrounding it are possible), but they are treated as isolatable (the correlation between bone/organs is treated as independent), whereas other variables are isolatable but are treated as one variable (damage to one eye/ear doesnt necessarily correlate with damage to the other)
                  - this is bc there is no 'requirement' structure requiring that any damage to one side be reflected in the other (the inherent symmetry can be distorted), but there are structures that 'can' require that (causes of organ damage)
                    - 'requirement' structures can be checked for using attributes of adjacent structures (does the skull seem to have a firm structure or would it necessarily change if another feature was removed)
              - not all variables treated as isolatable are actually isolatable, but with missing data they might seem isolatable
        - these perspective can be filtered by which would have the most impact on the solution success (solution success impact, as a variable that can limit or enable solution success)

      - find difference causes of interface structures (like concepts) and apply structures of them to create various solutions to filter as an initial solution space
        - example: find the reasons why data set points might differ (randomness, indicative of change in the underlying interaction, variation within expected/valid variable ranges) and create combinations of these reasons to explain the data set, by adjusting which points are included in the 'find a prediction function' problem input, which are excluded bc of reasons like 'random noise'
        - this is useful bc difference causes are a powerful structure in understanding why differences occur so they can be created/predicted as needed

      - find useful structures like units/ratios between change causes (reasons to change) vs. reasons not to change to justify changing a standard solution (like a linear function) to find an optimal solution (a better-fitting function)
        - example: 
          - the reasons to change may include reasons like that 'a data point would be better predicted if the change is applied'
          - the reasons not to change may include reasons like that 'patterns of changes of other functions that avoided this change type performed better' or 'the data point is an outlier'
          - structures like ratios between these change causes can be useful if each change cause contributes equivalent certainty so they can be treated like units
          - this is useful bc change causes from a standard solution are a powerful structure to help optimize a solution - if there is a reason to change a structure, its likelier to be reflective of reality

      - find target solution structures that lead to problem-solving processes even if they dont solve the original problem, like a target position that leads to change in a direction toward the original intended solution, even if the destination isnt reached

      - find structures of difference between 'false rewards' & other useful error structures of falsehood & the error structures they correct to apply as structure to fulfill the 'error-correcting' problem-solving intent
        - usually real rewards can be found to incentivize finding/generating/deriving a solution if its correct, so this shouldnt be necessary, but it can be more efficient than identifying/using real rewards to incentivize a solution/optimization

      - find the structures of primary default interface structures that are most useful across interface queries & workflows & apply those as default components
        - example: change + direction, priority + potential field, variable + concept type are examples of structures of interface structures, but some in particular are more useful than others, like 'perspectives' (filter with priorities) bc they fulfill structures of usefulness like 'capturing high variation' and 'reducing complexity' and 'applying importance structures' which are useful for various interim & core functions like 'find important objects' and 'understand a system quickly' and 'find hub variables', so apply these metrics as filters of these structures of primary interface structures
        - workflow fit: this is similar to other workflows involving finding useful structures, but specifically filters them by which are useful for fulfilling intents of interim/core functions that are commonly used in interface queries' sub-intents

      - combine a partially implemented interface query with gaps in implementation left for variation, where the sections implemented are known to be optimal for various sub-intents of the interface query
        - the pieces that are implemented can be on different interaction levels of the interface query
        - generalization: 
          - this can be generalized to other interactions between problem/solution structures which have clearly optimal implementations of sections of the interaction
          - it can be generalized further to other structures than 'partial subset', such as known optimal 'sequences' of problem/solution interactions or known optimal 'combinations' of problem/solution interactions
        - simplification: this can be simplified to adding a variable, allowing variation in which subsets or other structures are implemented & which can be changed for various implementations

      - interface structures that are adjacent (immediately preceding/following) to a solution so as to be causative or indicative of a solution can be identified as predictors or generators or identifiers of solution structures
        - if there's a perspective, function, change, pattern, etc that is often found around solutions, those can be used according to their position as predictors/generators/identifiers
        - this is similar to 'applying the solution as a symmetry or interface around which changes are applied while still qualifying as a solution', but applying the solution as a base or center where other objects relevant to it are adjacent, which may or may not be solutions, as a merged interface structure involving a combination of multiple interfaces, although the surrounding structures may also qualify as solutions
        - adjacence can be determined by number of steps separating the structures (for example, separating a question/perspective/useful structure & a solution), number of interface structures separating them, distance determined by some similarity metric, or other definition
      
      - find a structure (such as a perspective/function or network with nodes arranged by a certain distance or similarity metric) that would make solving a problem much quicker (or fulfilling another solution metric, like using available resources) and aim for that structure as the solution target to generate (so the problem becomes 'generate this useful structure' instead of 'solve the original problem')
        - for example, when a function network is organized by similarity in impact, its easier to see which nodes are higher impact
        - this can be extended by applying filters to find useful 'solution-adjacent' or 'adjacently solution-finding' structures that make a solution obvious or guaranteed/inevitable
          - structures like a particular way of organizing a network by some distance metric can make solving a set of problems trivial, which makes it more useful than a network organized in a way that solves one problem, other things being equal
          - structures that 'make solving multiple problems trivial' are useful targets for solution automation workflows, as a problem-solving intent of 'find structures that make solving the problem trivial'
      
      - store the optimal interface queries associated with a particular solution automation workflow to convert the 'build interface query' task into a 'find interface query in database' task, or store generative functions to find the optimal interface queries if any are stored, or derive the interface query in a more efficient way than interface query design logic
        - generalization: can be generalized to associations between any problem/solution structures

      - identify structures of error structures & their interface structures like meaning, for use in 'predicting structures', which is an interim function, or 'predicting error/solution structures', which is a problem-solving intent
        - example: when an extreme set of errors of a particular type usually precedes finding an interface, that can be used to predict which error structures mean that 'an interface is about to be found' 
