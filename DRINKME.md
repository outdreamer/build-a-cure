# Examples

## Intro Example

	This project is intended to automate interface analysis (a method to solve problems automatically), to produce solutions to input problems. This tool is based on a core concept of organizing information in a way so that solutions to problems are retrievable or buildable with a query set. Organized information is information that has had structure applied to it, so queries with this tool are applying structures (like filters, limits, or networks) to input information to create solution structures (like requirements, metrics, foundations, solution-generating methods, or the solutions themselves). 
	The problem in this case can be seen as a scaffold (like a network) and the solution is the content filling the scaffold (like an optimized route in that network).
	This program would take the problem statement:
		- "build a tool to detect & display bacteria in a room"
	and output possible solutions such as:
		- "grow bacteria until it's more measurable"
		- "use an animal model in an air-conditioned building (when people aren't in it like at night) that would quickly show signs of infection if the virus was live and present"
		- "display points on an AR interface with magnified bacteria attributes, or applying other data visualization rules to indicate attributes"
	along with other solution metadata like probability of success, sufficiency of information to select the optimal solution, and which solution is optimal, given which sets of resources are available.
	Another example input problem statement:
		- 'preventing infections from pathogens'
	would have possible solution output:
		- 'create artificial or hybrid pathogen to fight the deadlier pathogen'
		- 'remove deadly components of the pathogen on the structure (surface or protein or genetic) interface that is within 3 causal or system nodes'
		- 'point deadly pathogen at harmful cells like cancerous cells'
		- 'create a cell that will generate antibodies on demand'
		- 'calculate all harmful pathogens and install antibodies for each of them or their most common attributes'
		- 'calculate the stressors that will produce which antibodies'
		- 'calculate which stressors will produce evolution to handle the pathogen stressor'
		- 'create more filters to validate edits done to genes'
		- 'create more backup copies of original DNA to help the system remember which copy to use for comparison during validation'
		- 'create a pathogen to propagate original DNA after any infection'
		- 'calculate benefits of various pathogens and apply them to add functionality to the bio system'
	and other solution metadata.
	Another example problem statement:
		- 'build an optimal thermometer'
	would have possible solution output including:
		- 'automatically shut off the thermometer when optimal temperature is adjacent or reached'
		- 'have backup energy sources for emergencies'
	and other solution metadata.

## Example of applying intent interface to automate logic selection (code finding & building)
  - intent matching example
    - sequence structure (
        split.iterate.replace operations
      )
      - splitting, then iterating, and replacing in iterated strings, would be useful if 'the split delimiter has a string in common with the string to replace, but has different wrappers'
    - sequence structure (
        replace.iterate.split operations
      )
      - replace.split would eliminate a string that could interfere with the splitting or make it sub-optimal in another way (reducing whitespace to avoid later strip operations)
    - how would you identify these matches between use case (reasons to use a function, or general function intent) and the structure/operation intents automatically?
      - apply system interface
        - apply system object 'efficiency'
          - apply an 'efficiency' definition, such as 'intent alignment for resource-sharing'
            - alignment of intent between: 
              - the general problem statement: "generate a 'replace' function with intent to remove one string in param1, which has a string in common with another string to keep, but different wrappers"
                - actual problem statement or function intent may not have this much information, such as specifying that other strings may contain the string to replace but shouldnt be removed, which may need to be inferred
              - the structure & operations: "sequence(split.iterate.replace)"
              have a structural intent in common, so their directions are aligned (once they have a similar structural level on the same interaction layer)
            - use case: the intent of (reason to use) a particular structure/operation (like split.replace)
            - the goal is to link the use case with the structure/operation, by finding an interaction space where their metadata can be checked for a match, like an intent alignment, since the 'compare' operation embedded in an equivalence check requires similar inputs:
            - problem statement: 'find code to fulfill use case intent' or 'find use case intent that could use the code' (code meaning specific structure/operations)
              - standardized problem format:
                - equate use case intent with structure/operation intent
                  - equivalence check
                    - sub operations:
                      - compare
                        - compare operation requirement: similar inputs
                          - solution format: find a dimension set (structural interaction layer) where use case intent and structure/operation intent have sufficiently similar structures that their intents can be checked for equivalence
                            - solution structure: apply structure to use case intent and structure/operation intent until they can be compared (differentiated/equated)
                              - solution structure: function with intent to "replace 'the' but not 'tithe' in input string"
                                - apply solution formatting filter 'generalize' to structure 'function inputs'
                                  - generalized solution structure: function with intent to "replace 'string_to_replace' but not 'containing_string' in input string"
                                    - solution: subset = filter(input_string.split("tithe"), lambda x: x.replace('the', ''))
            - use case for sample input:
              - sample input string "if condition applies to the tithe, keep the objects"
              - string to replace = "the", 
              - function intent "replace 'the'" in input string
              - apply tests for system objects & common problem types like "false similarities"
                - find false similarity in the form of "similar strings in input"
                  - without assumed resources like the concept of a "word" wrapped with whitespace, or a "string to replace" param including the whitespace, we can operate with just the string/subset/wrapper concepts
                  - one should be kept, one should be replaced
                    - difference is wrapper of string in common
                      - objects: keep string, replace string, string in common, wrapper
                  - to remove one but not the other:
                    - 1. remove the string to keep first, retaining its position
                      operation: "split"
                    - 2. remove the string to remove, from output of split (either iterate or join with alternate delimiter)
                      operation: "replace"
                    - then the pieces can be joined if not already joined, with the original string to keep, if required by the function
                    - given that one operation needs to be done before the other (remove "tithe" as split delimiter before removing "the"), we need a sequence structure
                      - the intent of removing "the" is: reduce words that dont substantially change meaning of sentence
                      - the intents of removing "tithe" include: remove object identifier, making if condition incomplete
                      - given the difference in intent, we may be able to match the intent of either removal, depending on general function intent (like "reduce sentence to important words")
                      - this is how we can identify which word should be kept, if not explicitly stated
              - given this derived use case metadata in a generated or input list of possible use cases, we can match this set of requirements with the sequence(split.replace) intents
                - derived use case metadata (intent): "replace 'the' but not 'tithe' in input string"
                - structure/operation metadata (intent): "sequence(split.replace)"
              - the structural match we can find from this information is in the input/output map for both intents
              - the structure/operation may be generated, or filtered by common metadata matching the input metadata, to reduce the combinations to check for a match with the derived possible input metadata
              - we now have a generated function for the use case intent: subset = filter(input_string.split("tithe"), lambda x: x.replace('the', ''))
              
              - additional processing can be done with intents based on applying the logic interface to string metadata:
                - the intent of removing 'the' as the delimiter (removing both ' the ' and 'the ') would be to leave 'ti' in the 'tithe' word and to remove ' the '
                - the intent of removing 'tithe' as the delimiter (removing only 'tithe' but keeping 'the') would be to do further processing on 'the' or to remove 'tithe' temporarily to avoid processing 'tithe'
                - given that using 'the' as the delimiter would alter both words, including the word to keep, we would remove the word to keep as the delimiter first, since the string to remove is a subset of the string to keep
                - this is another way to give us the sequence of operations in our generated function, other than finding structures/operations matching general function intents like "reduce sentence to important words"
              - other ways include:
                  - fulfilling priorities like 'avoid possibility reduction (maximize potential)', which would exclude logic that assumed acceptable removal of possibilities like the usefulness/relevance of the word 'tithe'
                  - applying insights like:
                    - 'when removing a string, check for false similarities like strings that the string to remove is a subset of, and remove those first before removing string to remove, then re-add them in original positions after removal of string to remove'
                    - "an equivalence of type 'subset' is not an indicator of relevance"
            - this is the application of the problem-solving workflow: 'find a dimension set where problem types/system objects like intent alignments can be clearly identified/differentiated'
              - meaning apply structure to the use case input (abstract object) and remove structure from the structure/operations (concrete object) until you find an interim interaction space where they can be checked for equivalence in intent (matching intent)
  - function interface metadata example
    # code                                # intent                         # meaning                                                        # cause
    structure & operations                usage of structure/operations    system fit of structure/operations                               requirement for structure/operations
    # code                                # intent                         # meaning                                                        # cause
    def finding_function(numbers):        intending "filter" (test/change) means "find relevant items (relevance determined by filter)"     because "a set contains irrelevant items to remove"
    # code                                # intent                         # meaning                                                        # cause
    for i in range(0, len(numbers)):      intending "index iteration"      means "apply structure to all in integer index sequence"         because "a structure (like a filter/change/test) is needed"        
    # code                                # intent                         # meaning                                                        # cause
      subset = filter(numbers[i], func)   intending "filter list by func"  means "apply filter structure to items in list"                  because "a subset structure is needed"        

## Example of applying an interface to a classification problem (classify images as having a dog vs. cat)
  - applying structural interface to a data set's variables
    - applying sequence structure (time sub-interface)
      - does a dog ever become a cat? 
        - apply similarity interface
          - apply problem interface
            - apply problem type: false similarity:
              - does a dog image ever seem to become a cat?
        - apply permutation interface (explore all possibilities, such as by swapping variable positions)
          - does a cat ever become a dog?
    - applying combination structure (interaction/group sub-interface)
      - does a dog image ever contain a cat as well?
        - apply similarity interface
          - apply problem interface
            - apply problem type: false similarity
              - does a dog image ever seem to contain a cat as well?
        - apply change interface
          - apply change type interface
            - apply change type: base distortion
              - apply intent interface
                - whats the intent of a base distortion 
                  - apply change interface to components (DNA, evolution, regulation function)
                    - whats the intent of a base distortion from the DNA base
                      - missing/gap in/failure of regulation function
                      - handle a different change type than change types handled by DNA base 
                        (encountered on an interacting interface to the interface where the base distortion occurred, for example a problem like climate change produced a stress signal that was communicated to the DNA layer or an input layer, or selected for animals that already had access to temperature-handling functionality or inputs to those functions)
                      - randomness (interactions with structurally damaging compounds, by operating on same interaction layer)
          - apply structure interface
            - apply 'match' structure to environment (in background of image) & species feature ('inferred/proxy' variable of genes & 'interface' variable linking genes-environment) 'cluster' structures (types)
              - produces concept of 'evolution' to describe inherited changes from previous environments, reflected in features
                - apply similarity interface to output of application of change type interface
                  - would a dog ever evolve in the same way or evolve the same features as a cat?
       
## Example of applying an interface to identify problem types
      - automatic problem type identification
        - structural problem types:
          - mismatches
            - intent mismatches
              - the intent of a function
                - is:
                  - to capture unique logic (so it shouldnt be repeated but imported)
                - is not:
                  - to be complex (so it should be only as complex as required)
          - now youve identified two rules to use when evaluating function quality, using their intent metadata
        - generative query of automatic problem type identification
          - apply problem interface
            - apply structure interface
              - structural problem types:
                - mismatches
                - apply intent interface
                  - intent mismatches
                    - apply function interface
                    
                      - the intent of a function
                        - apply concept interface
                          - apply concept 'equivalence'
                            - is:
                              - to capture unique logic (so it shouldnt be repeated but imported)
                            - apply concept 'difference' or 'inequality' or 'contradiction' or 'invalidation/neutralization' or 'opposite'
                              - is not:
                                - to be complex (so it should be only as complex as required)

## Example insight path
  - an example of an insight path including questions to reduce a diagnosis search space quickly:
    - questions that rule out conditions (most-filtering questions first with least info)
      - questions that minimize 'minimum required info to answer'
      - questions that have 'minimum required info to answer' in common with other questions
      - questions that rule out low-variation conditions first (high-variation conditions are likelier to apply to difficult-to-diagnose conditions)
      - questions that require minimal changes to diagnose (a condition has a state that, when triggered by eating a glucose tablet, is very quick to diagnose)
      - questions that rule out common problem types first (mismatches, over-prioritization, structural damage, dysfunction/dysregulation cascades, false signals, interaction that shouldnt happen, conflicts, lack of resources/competition), given that complex conditions are likelier to have more unusual/complex problem types (such as structures of common problem types, like combinations/injections)
      - questions that focus on unusual symptoms/metrics to reduce solution space
      - questions that focus on symptoms/metrics with unique/unambiguous causes (vs. systemic variables that could be caused by many things)
      - questions that rule out similar conditions
        - questions that rule out conditions that are more common (prioritize more common conditions)
        - questions that rule out conditions that are more commonly mistaken for this condition (prioritize ruling out common mistakes)
        - questions that rule out conditions that are deadly (prioritize examining deadly conditions first)
        - questions that rule out conditions that are untreatable/undiagnosable (prioritize avoiding time analyzing untreatable/undiagnosable/idiopathic conditions, relegating them to research)
      - questions that rule out causal conditions
        - conditions that cause kidney damage, which would make kidney damage diagnosis more likely if they cant be ruled out
        - conditions that are caused by kidney damage, which would make kidney damage diagnosis more likely if they cant be ruled out

## Example interface queries to generate an invention
  - example of specific queries for a cnn
    1. start with the pattern interface
      - check for patterns in interface structures of the problem system, like variables, incentives, intents, priorities, questions:
        - find pattern 'features usually have a certain size'
          - identify relevant objects to pattern, including false requirements/assumptions, like:
            - input space needs to include all inputs
              - apply relevant interface structures to false requirement, like 'subset' on the structural interface
                - test if subset of inputs includes more relevant information
    2. another way to generate this invention:
      - start with system, then function interface, identifying functions governing problem system object relationships, like aggregation
        - match pattern of input-to-label aggregation with subset-to-type aggregation pattern
          - apply associated structures of one pattern (subset) to another (inputs)
    3. start with conceptual interface
      - start with fundamental concepts, like the concept of 'relevance'
        - relevant information to differentiating between types takes the form of the regions where differences aggregates
          - regions inherently mean a section rather than a whole
            - arrive at the subset object, and apply it to any complete/whole sets in the problem (neural net) system structure
    4. start with intent interface
      - identify intent of all problem system relationships
        - intent of 'using all inputs' is to 'capture all information'
          - apply change opportunities from other interface queries, like the 'input subset' change, and re-calculate the intent
            - intent of 'using subset of inputs' is to 'capture information of a particular size'
              - identify opportunities where that intent is relevant (where information has a size similar to the subset size, like variables that have aggregated into differentiating features between types)
                - check if that opportunity is relevant to the problem of 'differentiating types'
    - interface queries like these can be abstracted to insight paths to solve problems:
      - start with the pattern interface without other information
      - start with fundamental (either foundational, important, causative, generative, descriptive/compressing, determining, or core objects) cross-system objects without other information
      - systematize or structurize the problem first, where possible
      - false objects like false requirements are important for identifying opportunities for change, so identify false problem types in the form of information mismatches when looking for relevant changes
      - intent alignment is a good way to detect solution types like change (innovation/optimization) opportunities, in the form of mis-alignments between existing problem system intents and problem-solving intents (mis-alignments representing change opportunities)

## Example interface query to generate an insight (problem type: find relationship between concepts)
    - apathy & stupidity query example:
      - stupidity structural definitions:
        - short-term thinking
      - apathy structural definitions:
        - indifference to others' well-being
        - egotism
        - selfishness
      - connecting link:
        - short-term thinking is related to the concept of 'local bias'
        - local bias is a component of selfishness (bias toward nearest individual)
      - once you standardize to the structural interface (applying structural metrics to definitions, like: distance to find the nearest individual, and short-term thinking & local bias),
        you can connect these two concepts with a query to find similar structures (short-term thinking is related to local bias, which happens to be a component of selfishness)
      - this is an example of how to arrive at an insight about which concepts are related by applying the structural interface, and insight paths (insight paths like 'find similar objects, as a way to find relevant objects, when looking for connections between components')

## Example insight path: to generate comical statements (in the form of a word choice or response), you can execute the insight path:
    
    - step 1: find objects of types such as:
      - relevant (directly relevant objects like functionality/interactions, as well as structures like system contexts in which meaning occurs, prior patterns or references, integration structures)
      - related (inputs, outputs, requirements, assumptions, alternatives)
      - interface (causal objects, vertex objects, like core/hub objects, determining/causative/generative variables, etc)
      - unlikely (improbable objects given a system context)
      - similar (objects with core (fundamental), explicit (known) or multiple (correlation) similarities)
      - required (known related objects)
      - invalidating (known contradictory objects, which contradict the existence of an object)
    - alternative/chainable step 2:
      - change required objects until theyre invalidating (change required object like intent to 'protect self' into an invalidating object) or vice versa
      - change similar/likely objects until theyre different/unlikely or vice versa
      - change related objects until theyre unrelated or vice versa
      - change relevant objects (meaningful) until theyre irrelevant (nonsensical) or vice versa
    - alternative/chainable step 3:
      - position the altered object with an emphasizing context, or alter the context to emphasize the original object ('emphasize' meaning 'maximize its difference')
      - position the altered object with a relevant context, or alter the context to make the original object relevant ('relevant' meaning 'structurally connected')
    1. on the use of the word 'help' vs 'convince/trick':
      - help: give someone what they need (act in someone else's interest)
      - trick: get something out of someone against their own interest (act in your interest, against someone else's)
      - invalidating object:
        - trick themselves
        - not helping themselves
      - missing object: 
        - you shouldnt have to trick someone into helping themselves (act in their own interest)
        - the missing object is the 'intent to help themselves', which is assumed as a default related object to an agent's decision
      - emphasizing context:
        - if a person is against against their own interest, you will not be able to help them trick themselves into acting in their own interest
    2. on the response 'so true' to a negative factual statement about them:
      - invalidating object: a negative factual statement (invalidates an agent portraying themselves falsely)
      - related objects:
        - agreement
        - argument/contradiction
        - counterattack
      - unlikely object:
        - the agreement of an agent with a self-invalidating object (a negative factual statement that invalidates their false statements)
      - missing object: 
        - the missing object is the 'intent to help themselves', which is assumed as a default related object to an agent's decision
      - emphasizing context:
        - someone saying a negative statement, and responding in a sincere, extremely validating (such as 'reassuring' or 'complete agreement') way
    - alternative insight paths:
      - to generate example 1 above, you could also generate the question 'why would you have to help someone act in their own interest', a question that uses the path:
        - pull standardized verbs & iterate
        - retrieve related words (by association, 'help' => 'obligation') & synonyms of related words: 'need', 'responsibility', 'have to'
        - iterate default question types: why/how
        - execute core operations (combine, differentiate, identify, filter, replace)
          - combine the two above: 'why have to'
          - inject concept of 'agent': 'why would an agent have to'
          - add original verb 'help': 'why would an agent have to help'
          - inject concept of 'agent': 'why would an agent have to help an agent'
          - identify the one system context where 'help' would not be required: in theory, you wouldnt have to help someone in the context of 'helping themselves' (act in their own interest)
          - apply not-required context: 'why would an agent have to help an agent help themselves'
        - this question clarifies the ridiculous nature of the combination, by associating an 'obligation' verb with a not-required context (uniting the two with the common concept of 'requirement')
        - from this question, you can identify a comical word choice of 'help' to replace a word like 'trick' or 'convince', in the context of 'help them realize theyre better off'

## Example of a common system filter, permuting assumptions like system position (position swaps, where position can refer to node identity or system position)
	- investment risk allocation vs. capital allocation (swap objects allocated)
	- battery ion vs. base metal (swap a variable on top of a foundation to the foundation position)
	You can predict which system filters will be useful based on system priority
	    - a system prioritizing efficiency will find similarities more useful, and similarities will be more causative & likely to occur in that system
	    - a system prioritizing stability will prioritize & generate more limits, to prevent change types
	You can also predict which system filters will be useful across systems, based on system intent ('find' benefits from gaps & inefficiencies, 'build' benefits from efficiencies)
	The inputs to this system are:
		- a set of core definitions
		- a way to discover information to feed into the system 
			(this means internet access so API queries & searches can be done, if the specific system of the problem space isn't an input, formatted as a system network definition)

## Example of problem-solving workflows this project will automate:
		1. how to solve the problem of automating the generation of info objects (summaries, explanations, perspectives, etc)
			- specifically, how to 'explain a complex concept in a concise way' (which is a 'mapping' problem type, mapping expert keywords to concise keywords):
				- explaining ml as 'exploring different combinations of embedded weights on input feature data & weight paths, using filters to determine which weighted feature combinations contribute to incremental prediction function updates' involves:
					- standardizing the concept of an artificial neural network using its concise definition
					- identifying the right objects that are most important to include (combinations, weights, weight paths, features, filters, learning, prediction function)
					- modifying & connecting these objects using the right functions
					- mapping structural objects like weights & filters to a semantic structural definition involving key concepts like learning rate & prediction function
					- explaining why you'd use the mechanics of the system, not just how
				- theres a gap in usual explanations between 'a set of combinations, weights, layers, & filters to update learning rate' and important interim objects like 'weight paths' and the semantic reason of why a set of combinations, weights, layers, & filters would produce a good prediction function, as opposed to standard regression (good for standard or preliminary relationship analysis) or starting from a function of theorized important variables from pca and making incremental adjustments across the most different data points (good for weight initialization)
					- the reason is that adding extra weights in a path (node in a new layer) allows the previous weight state to be changed again, allowing it to be tuned to data & add extra complexity, generality, or accuracy, which helps fit a function to data
						- a visual is small boundaries/gates representing the generality of a theorized function, positioned around the correct function, preventing the function from getting beyond them
					- other important objects in the ML space:
						- errors: the lack of built-in error handling is a reason for regularization layers - other error types can be caught with system/variable pattern layers
						- causal structures: after initial data analysis, the network has the potential to identify other causal structures/levels missed when removing correlated variables that is not exploited
						- function network: the network has the potential to identify an output function network as opposed to one prediction function, where functions can be used under data conditions or to represent anticipated changes to the function
						- system fit: given the inferred system the function occupies, missing or future variables (what did data set likely miss given the noise, despite lack of clear impact of missing variables), error types (what problem types occur), & application intents of the function (used in what decision types) can be theorized
					- these objects can have a map to adjacent objects of a prediction function
						- node layers can represent subset function tangents that are reduced in length to generate a curve
					- 'a set of combinations, weights, layers, & filters' => 'to update learning rate' => 'to get prediction function'
						- origin: weights, layers, & filters
							- semantic: importance, change types, contribution rate
						- interim: weight paths
							- semantic: type paths, attribute sets, causal clusters
						- aggregate: function variant
							- semantic: accurate subset prediction function, general subset cluster prediction function, type specific prediction function, & other variants
						- final: prediction function
							- function generated by network of prediction function variants (with regularization & other extra processing determining which variants & components of them make it to the final function)
					- the ML mechanics of weight paths or regression problem of fitting a curve are similar to the mechanics of deciding which subsets to use when calculating area under the curve 
						- do you use the successively largest shapes that reduce the remaining area to be calculated
						- do you evenly split based on the best subset that mimics the curve the most
						- do you use adjacent functions & their metadata (like area) & the transformations of their metadata, given the transformation of the adjacent function to the original
						- do you match pieces of the function that would create larger or more measurable shapes
						- do you match change rates with change rates of metadata (area)
						- 'a set of combinations, weights, layers, & filters to update learning rate' maps clearly to 'a set of sums, sizes/shapes, scale/accuracy, & split function to update change rate metadata (area) calculation'
						- to map ML to this problem (finding fewest or best objects to use when calculating the area under a particular function), you could assign:
							- feature variation to component (subset or adjacent function) shape
							- feature weight to component (subset or adjacent function) size
							- weight paths to various strategies to split/aggregate, transform/distort, compare/map:
								splitting functions, adjacent function transformation functions, metadata transformation functions (when x & y change in function1, how does metadata change, and how does that relate to how x & change in function2 & how function2 metadata changes), change rate distortion metadata functions (as more sides are added to a polygon to create a curve, how does area change), or subset matching functions to reduce calculations
							- prediction function to best calculation route to determine area under a curve
						- why would you map ML to this problem instead of using a ML network? so you could apply methods of solving the area under the curve to the prediction function
							- using 'subset aggregation' & 'change rate distortion of metadata' to determine the best version & method of combining feature weights to get their aggregate object (weight set, or prediction function), which is area in the other problem space
						- thats the problem expanded by a dimension (to focus on different metadata with an extra dimension, which is aggregation of a different type (shapes of 2-dimensional orthogonal change) than aggregating change rates to form the curve)
							- whats the problem reduced by a dimension? finding the right length of a line for a target intent
							- the next lower dimension problem is finding the right position
							- whats the map of the lower dimensional problem (finding length) to the higher dimensional problem (calculating area)
								- does it cross any metadata of the interim dimension problem (fitting prediction function), such as constants, exponents, coefficients, inflection points, change rate patterns, etc
								- how do change rate & type interaction spaces differ as dimensions are added
				- this explanation can be generated using system analysis (the system interface on the interface network)
			
		2. how to solve the problem of automating insight generation & discovery in an efficient way
			- using the pattern interface, identify that insights occur in patterns as people discover levels of detail & complexity in a field
			- identify questions as a key input to insights, especially insights that shift a paradigm (epiphanies)
			- frame questions as a source & destination node on a network, where the standard answer is the path connecting them
			- identify question path patterns across insights
			- use these patterns to jump to the correct insight quicker than normal discovery times
			- using insight paths, question shortcuts, & filters, you can skip ahead in designing an optimal solution, such as:
				- building a tool in the best way first, rather than waiting to discover errors or efficiencies & building them later
				- finding an accurate prediction function network that adapts the best to change
				- how to guess the existence of a sub-system in the absence of information or ability to measure the sub-system
					- for example, if you were a doctor in the 19th century, how would you guess the existence of DNA:
						- given that:
							- you know that families have traits in common, but not why
							- you know about the standard set of organs because you're a doctor & you had to do autopsies to learn how to do surgeries
						- an insight path to generate a theory of the existence of DNA:
							- check known objects for contribution ('if someone is missing an organ, has nerve damage or a brain injury, or drinks a lot of alcohol - do their traits change?')
								- look for counterexamples to any apparent contributions to the output
							- check related types for similarities & similarity source location ('are there other species like humans with similar abilities? is there anything functional they have different? where are these functions stored?')
							- check for related functionality under changing conditions & permuted assumptions ('when a trait (like hair) is damaged, what happens? some traits are repaired')
							- given lack of known object (organ/nerve) impact on traits, change layer or scale (infer that there may be a sub-system we cant see)
							- change causal direction/structure ('if organs dont change traits, do traits change organs? is there another causal node leading to both of them or in between them?')
							- apply insights
								- 'changes tend to cascade up in scale'
								- 'complex systems with high variation tend to have many layers & objects'
								- 'if something is damaged & is repaired, there is usually a set of instructions to repair it'
							- apply question shortcuts
								- 'is blood composed of discrete units, like water is composed of drops' (infer existence of cells)
								- 'do blood units differ from liver units, such as by intended function' (infer different cell types)
								- 'are there units with intent/function' (infer existence of microorganisms, match it to medical conditions)
								- 'do some units have intent to give or take functionality from people (make them healthy or sick)' (infer existence of harmful microorganisms)
								- 'could these units be in food or tools we use' (find different examples of resources with microorganisms, like plant fungus & bacteria in dairy)
								- 'would a harmful unit for one species harm another species' (infer high variation in microorganisms)
								- 'does high variation in microorganisms imply smaller inputs generate them' (infer existence of sub-system generating microorganisms & cell types)
								- note: how would you arrive at blood as an object to focus on in the first place, in the above question path?
									- insights like:
										- 'constants can form a platform for change to occur' (noting that blood characteristics dont change much across patients
									- find importance of blood by noting that:
											- lack of blood causes death (implying it's important)
											- that leeches sometimes remove symptoms of illness (implying that blood is related to illness, which can distort traits)
											- that blood circulates through the whole system (implying it's a hub node)
										- so 'important, relevant hub nodes' are a good place to start a question path within an insight path
							- apply testing/filtering insights (to narrow down the possible set of implementations/structures that could explain trait differences & behavior)
								- identify 'mixing bacteria colonies' as the best test, because this tests functionality emerging from combining microorganism species ('does it kill the same plants')
									- if it doesnt kill the same plants as the other pathogen, this supports the theory of smaller inputs than the microorganism layer
								- extrapolate conclusions implied by each inferred relationship output by previous queries
									- if it explains most differences between species, it must be flexible, with many possible versions (infer a set of combinations)
									- if it explains functionality, it must be related to needs (infer stressor as an input to evolution)
									- if it's used as instructions to repair, it must be stored in various places, otherwise anyone without combinations of components would lose the ability to repair
							- the next logical conclusions after these testing filters may be:
								- the repair instructions are stored in units of components that are repaired (hair, nails)
								- the function (change unit) instructions are stored elsewhere, and not in organs that youve seen patients with severe damage or without (brain, kidney, appendix, etc)
								- there are units with intent that create functions (confirmed by experiments with pathogens from milk & plants)
								- pathogens have functions & units with intent, and they dont have organs that we cant live without (so its not in brain, kidney, appendix, blood, etc)
								- the units with intent may be located wherever else they are needed to create functions
								- the units may contain function or repair instructions
								- repair is a function
								- the units may contain instructions to create function instructions (function instructions like 'send pain' or 'pump blood')
							- then you could apply more insights given good system design insights or other optimization insights, to guess the likeliest implementation of 'units that contain instructions':
								- 'the safest place to store extra copies of instructions is at every possible location, in case one location is damaged'
									- this would lead to inferring that the units containing instructions each contain all instructions
						- chaining these insights/questions/tests/conclusions enables converting a question ('what explains trait differences') into a theory ('theres a sub-system that contains instructions'), which can be narrowed down with queries, filters, & insights
						- linking these objects requires:
							- having an object in common with a previous point
							- applying core functions like 'given condition', 'apply edge case context', 'remove assumption', 'change variable', etc
							- changing stage (testing/system discovery/filtering, applying question/insight path), according to distance to target (theory of sub-system to explain trait differences)
						- this is one of many insight paths to generate this theory, given a doctor's perspective from that problem space & its technology
							- there are more concise versions based on plant trait inheritance in a garden, or observing plants/animals in different environments evolve different traits, given the faster evolution, or through studying particles/matter state changes with technology or heat sources
							- there are also more abstract paths
								- using system insights like:
									- 'noise appearing in high variation outputs with minimal functionality are often generated by interference in communication between high-variation inputs on a sub-system or other layer'
								  which explains noise (mutations) that cause trait differences, you can cover almost the same cognitive distance as the above example insight/question/filter chain, but with one insight (not covering non-mutation trait similarities)
					- another example: how would you automate identifying gravity without advanced measuring tech or information that makes it obvious, & without someone telling you there's something to figure out or telling you what to focus on:
						- meaning in the absence of a set of coincidences + prior exposure to similar patterns, like:
							- coincidental free time from industry & resource access, a natural object in a location providing an attribute useful as protection
								- with a coincidental useful side effect that becomes apparent when you use it for the protection (tree producing shade with a side effect of apples)
							- exposure to other similar patterns like natural processes happening without human interference 
								- adjacent to the concept of defaults or initial/origin values, or stability/equilibrium
						- adjacent/obvious sources of the insight:
							- sun/weather/shadow patterns
							- invisible rules explaining changes like pathogens follow or generate
							- object interaction patterns in contexts outside of counter-examples (even when interfering force is applied, objects stabilize on the surface)
						- reason/intent to focus on it:
							- something broke or broke something else when it fell (something important like a building or delicate like medical tool)
							- building a machine to use accessible/costless/self-sustaining resources to power it 
								(a ball falls with similar force if dropped from a high enough position as someone throwing it)
							- building a machine to fly (get something at top of trees, construct large buildings, travel faster using wind once airborne)
							- make a ball that bounces higher
							- prevent domino effects from falling (objects knocking each other over)
							- make things lighter to carry
							- looking for fundamental forces
							- explain nature
						- queries to generate a theory of an invisible force governing some motion:
							- useful objects/attributes/functions common in other patterns
								- default behavior (any automatic process could be useful if you can chain/organize/link them in some way that produces an intent you can use)
									- adjacent concepts to default like 'origin' or 'initial value'
								- stabilization (a process that self-restores can be useful as an energy source or a boundary or a constant)
								- equilibrium (a source of balance, or a point to base distortions on)
								- emergent attributes at rest, as prediction tools
							- insight paths
								- system: there are core functions that determine most complex systems that are not in flux from variance injection
								- type: there are different types of forces, such as forces between specific objects, forces that are created by other object forces, input forces, core forces
								- scale: if the earth is relatively big, why would it have similar rules to objects that are small, like animals & buildings have different rules (phase shift)
									- similarly, there may be contexts of different scales where gravity doesnt apply
								- interface: changes happen on the earth surface bc it provides a foundation for those changes to occur
									- those changes dont seem powerful enough to damage the foundation
									- the foundation must have more powerful forces than the changes produced on it
								- variable type differences: given that gravity appears to be constant & universal, and that generally there are different variable types than just constants in a system, it would make sense for gravity to be a constant and for other variables to vary
									- constants tend to be inputs/assumptions, like fundamental forces
								- change: if gravity wasnt a constant or fundamental force, other things would be changing faster or in different ways than they are
								- potential: given that if something has the potential to change, it would be changing with these core distortion functions (combine, merge, split, move, intersect), there would be evidence of those distorted versions of the force if it wasnt a constant or a fundamental force
							- pattern insights
								- usually if a pattern appears in many circumstances in a system of interacting objects, it's because there's a function generating it, not because it keeps happening by accident
						- then apply filters to reduce solution space of possible theories as to the specific function:
							- filtering out counter-examples:
								- objects carried by wind: gravity applies to denser/heavier/higher mass objects
								- objects that float rather than sink to the surface: water has other forces like boundary & chemical rules
							- filtering out immeasurable sources of the insight
								- stars: cant measure how far away they are without tech or math methods or historical information (given slow rate of change of cosmic events), so developing a theory of gravity using star movements is non-adjacent
									- it's possible if they become focused on shadow/weather movement patterns, from which they could infer:
										- sun & earth rotation and gravity from the fact that the rotation repeats
											- which implies one of them is circling the other but not getting significantly closer
												- given historical mentions of similar weather patterns
		3. how to solve the problem of selecting between alternative solutions
			- specific solutions:
				- select between solutions for recycling unused waste resources (research enzymes, research using it as fuel, burn it, leave it in space, build new products with it)
				- select between solutions for determining area under a function (add area of subsets, estimate area from adjacent function transforms, transform it until it's composable with known values)
				- select between routes 
			- solution selection abstraction:
				- select metrics (specificity, testing, uncertainty reduction, cost assessment, completeness, success, intent, requirements)
				- select starting point for queries on interface network
				- select starting structures (problem/solution definition, object model)
				- select starting abstract core function (filter, derive, build, change)
		4. how to solve an information problem
			- convert it into sub-problems (missing information, info asymmetry, randomness, ambiguous alternatives)
			- query for solutions to those sub-problems (determine missing information, distribute information, test randomness as equivalence of possible outcomes & remove, find attributes that can break ambiguity)
			- find the sub-problem solution sets that cooperate & select one that fulfills solution requirements
		5. how to design a product that will prioritize a concept (like anonymity, trust, relevance, equality, distributed power, or checks on power)
			- find structures with those associated concepts (just like the concept of power could have the structure of a hub node in a network), or find conceptual network path building those concepts
			- apply filters to the structures found, testing combinations for the concept based on its definition, or apply filters to the conceptual network path until it has structure

## Example of mapping concept to structure
	- diagram:
		- https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/concept.svg
	- example: 
		- create a program that checks if a system is robust automatically, regardless of which system
		- what would a concept like 'robust' mean for a system?
			- given the definition route to 'robust' as 'strong enough to withstand various circumstances'
				- you can infer that if a system is robust, it can retain its structure despite application of various change types
				- so query for change types in that system
				- then check which change types break the system & the ratio of (change types handled/total change types)
				- assign a ratio to 'strong' adjective
				- check if the change type handled ratio is above or below the strong ratio
				- if above, the system is 'robust'

## Example of mapping problem to structure (asymmetry, conflict, lack, mismatch)
	- for a conflict like vectors aiming at a corner of a closed shape (where the shape is formed by the intersections of limiting attributes), the structural way to solve that problem is:
		- reducing the angle of the corner 
			which reduces the difference between corners (and the incentive to aim for a corner) & adds extra alternatives
			- the solution is an example of 'false limit' - the limit of there being a finite supply of corners or the limit of one route occupying a position at a given time can be surmounted with extra resources
		- reducing incentive to aim at corners
			- if the shape has fewer corners, there will be less incentive for internal vectors to aim there
		- reducing motion
			- if the shape has a stable state, the motion of the internal vectors can be reduced or staggered at intervals for resource-distribution
		- adding motion
			- use types of motion to distribute the vectors so they aim at different corners
	- you could apply these methods of solving the structural problem to the original problem 
		(a conflict like competition or overflow or false limit or false alignment if the vectors dont need to aim for the same corner)
	- the way to assign 'conflict' problem type to the closed shape structure with internal vectors is by aligning attributes 
		(incentives that organize motion to create an oversupply of resources (motion vectors) that cant be supported by a resource (position))
 
## Problem-solving Insight Paths 

Insight paths can take the form of finding & applying the right questions to ask in a system, to reduce time to solve a problem (see example filters as problem-reducing questions)
In the patterns from system_analysis.json, you have example filters to use when reducing a problem before trying specific methods to solve it.
These are the objects to look for in order to quickly:
- identify causes of system error
- identify vertices (determining/generative/causal/description-compressing variables) of a system
- understand a system quickly
- optimize a system
All systems will have core abstract concept implementations:
"concept_structure_map": {
	"power": "position",
	"balance": "equivalent",
	"efficiency": "path",
	"change": "distance",
	"potential": "unoccupied accessible adjacence",
	"relative change": "ratio",
	"base/standard/interface": "origin change",
	"symmetry": "origin",
	"information": "structure",
	"truth": "match",
	"priority": "direction",
	"intent": "output",
	"position": "input"
}
But specific concepts evolve within a system, given unique combinations of core objects.
- example:
	- a "signal joint" evolves as a concept in the gene system because it's an output of an important combination of core processes that is not matched with an equivalent handler, so it can cause further complexity bc its allowed to interact with other systems instead of decomposing it after it's used.
	- an "improvisation" is a change given a starting position and new problem information that doesnt match an existing solution
	- cause cant be traced when:
		- inputs/system/measurement tools decays/changes before it can be measured
		- change/decay outputs dont follow patterns or have multiple alternative possible patterns
- when a system is totally unknown, you should diversify across all interfaces at first - example of finding value in a set:
	- finding value in a set - analyze a set from:
		- core interface: what core functions determine set generation/selection/aggregation/interaction/organization
		- causal interface: what functions were used to generate the set
		- intent interface: what is this set for
		- structure interface: randomness, endpoints, subsets/split
		- potential interface: what are the limits on this set, what is the set of possible outcomes
		- change interface: where is the change concentrated/distributed in the set from a standard set
		- pattern interface: what patterns do sets in this position (determined by attributes or sample subset) normally follow
		- function interface: what functions are adjacent to the set if it has a sequence or clear function map
		- concept interface: 
			- what specific tradeoffs/mismatches/alignments/symmetries/combinations/interactions are inherent to the problem/problem space? (specific concept filter) 
			- where is the power distributed in the set? (abstract concept filter)
		- system interface: what variance injection points are in the set generation/selection/aggregation/interaction/organization
	- then when you find a pattern match on an interface set, you can restrict the search to those
	- key concepts of this problem (like the "tradeoff of search start point/split function/organization vs. performance", "subset gains", "pattern matching", and "potential worst/best case scenario of solution") should be found quickly from various interfaces:
		- structure interface: 
			- position (sequence in the set problem space) is a determinant of adjacence/distance
			- adjacence between start search position and final found value position is a key metric
			- start-found adjacence can be maximized by changing input (number of start points)
			- limits on number of processes involve ability to read a value at a given position at a time
			- maximizing start-found adjacence requires more work (higher search processes) to produce a possible metric "lower search time"
			- "search time" and "start point count" have a tradeoff structure
		- potential interface:
			- the set of possible outcomes (possible positions of value) is equal to the set's positions (indexes)
			- how do you reduce the set of possible outcomes if the possible outcomes are an integer sequence equal to the set length
			- subsets are a potential interim unit (based on the value count attribute) between the outcome data type (one value index) and the input data type (set)
			- the potential of subsets of equivalent length to contain the value could be equally likely (adding randomness to search)
			- potential injection point for pattern interface: skipping equivalent valued subsets could reduce solve time (if subsets with a certain split follow patterns as determined at search time)
			- best case scenario in standard search (random or endpoint) is the first value in the set is the target value
			- does subset search offer gains to random search?
			- best case scenario of unit solution type (iterate check of value)in subset search is first value after first subset split (split in half) is the target value
			- next best case scenario type (if the unit solution type best case scenario doesnt occur iteratively) is pattern found & used to reduce solution/search space
			- splitting requires multiple processes
			- pattern logging/searching requires multiple processes
			- depending on set, either can reduce solution space with extra work
			- there is a trade-off between work invested in pattern-checking, subset-splitting & solution space reduction potential
