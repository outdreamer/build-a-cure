# Solution Automation using Interface Analysis

## Intro 

	This is a tool to automate problem-solving, specifically to translate problem tasks, such as 'optimize a system', 'create a robust system', 'create a way to execute transactions without trust', 'find a compound to treat this condition' or 'find a variable relationship' into solutions, insights, and other relevant information, automatically.

## Invention Relationship

	- Solution automation is:
	  	- a problem-solution format connection method that uses interfaces, putting components from interface analysis together in a way that allows users to submit problems & receive solutions
	  	- the main program implementing problem-solving workflows, API service, UI, & product
	  	- the program that specifically converts problems into solutions, using generated problem-solving workflows & interface queries
	  	- fulfills high-level user tasks like 'match the input problem with a solution'
	- Interface analysis is:
	  	- a task-completion (format connection) method that defines interfaces
	  	- configuration of logic which is also accessible by API, and info objects like imported insights/functions are the content/data
		- the logic executed on each interface, including how to design an interface query to retrieve the requested relevant information
		- fulfills granular interface operation tasks like 'find a structure on an interface that matches input' 
	- Solution automation uses components defined in interface analysis, and interface analysis contains input configuration to solution automation (including definitions & rules used to implement interfaces & interface queries)

## Definitions

1. Interface
	- a standard for comparison (like the causal interface, conceptual interface, pattern interface, structural interface, etc) that is useful for solving various problem types
    - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/interface.svg
2. Interface query
	- a way to apply interface standards to convert the input info format (like a problem statement) to the output info format (like a solution space, or solution set)
3. Insight path 
	- a way to speed up the acquisition of insights, from standard methods like 'trial & error'
4. Problem space
    - its the space where youd graph all the info relevant to a problem - the context allowing a problem to exist
    - I often use tech as a key determinant of a problem space bc which tech you have often determines which available resources like strategies you can use, but it includes all the other resources you might have access to (info, potential, energy, physical assets, etc).
5. Object model
  - this is the standard object-function-attribute model you encounter in programming, applied to systems
  - by attribute, I mean an inclusive set of terms including parameter, variable, input, output, & property
6. Abstract network
  - this is the network of abstract concepts which are based on core structures (power, balance) 
7. Conceptual math
  - this is an example of the logic executed on an interface, specifically the concept interface
  - an example of conceptual math is applying the concept of 'meta' to the concept of 'game' and getting output of the operation like 'a game where games can be created by agents inside the game' or 'a game to design games', given similarities between attributes/functions of objects in the definition & relevant spaces
  - its useful to think of it like conceptual light (information) that can be combined with other concepts given trees of structural layers applied, where the concept is embedded, reflected, or absorbed on the way to the final structural layer - so the computation would be a trajectory on that tree linking the two concepts being combined
 Interfaces

## Limitations

  - depends on queryable information (the system must be discoverable) and definitions (for efficiency, although the definitions should be derivable if the system information is accessible)
  - the set of dictionaries used may need updating to build the right queries (there may be more core functions or interfaces to add) but it will discover that during the query
  - some query sets/chains will be more efficient than others, but that will become clear with meta-analysis of queries after its used, so query analysis needs to be done regularly to update query-building logic
  - it will generate possible solutions as it runs and the first generated solution is unlikely to be the most optimal
  - some calculations may need to be made before query can be run (minimum information to solve a problem, relevant insight paths to select interface trajectories, problem solving cost analysis) which can add to solve time
  - some problems are inefficient to solve (resources should be allocated elsewhere bc solving the problem is too costly or efficiencies are imminent in the host system)
  - standard queries (example filters) may beat custom queries for some problems but it may be clear after, so both may be optimal to run

## Useful Diagrams

  - system diagram  
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/system.svg
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/variance.svg
  - function diagram
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function.svg
  - problem diagram
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg
  - insight path
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg
  - info problem type
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg
  - intent of alternate paths
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/cause.svg
  - intent organization
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/intent.svg
  - causal structures
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/cause.svg
  - variance gaps
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/variance.svg
  - perspective
    https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/perspective.svg
  - core functions
    - layer diagrams involve applying layers of chained transforms to core functions to generate new object combinations through paths on these diagrams
    - these diagrams can be applied to objects/attributes/systems, which can be framed as a function
      - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/solution.svg
      - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg
  - graphing solution for a problem space
    - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function_map.svg
    - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/map.svg
    - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/prediction.svg
    - https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg

## Components

  - This invention involves several key components like:
    - a network of interfaces
    - information formats (applying definitions to get structures of information like a meme like a joke template, or a problem like an info imbalance, or a concept like relevance)
    - a definition of problem-related objects - like intent, problem space, solution, & meaning (the meaning interface is a meta-interface to connect the other interfaces in a way that is relevant to the problem intent)
    - the concept of insight paths & problem-solving workflows & interface traversals
    - interface-specific definitions of concepts (like a structural definition of the concept 'cause')
    - a language to standardize & connect these components using as few terms as possible
    	- functions of core verbs like find/build/apply/derive
    	- components like interface/problem/context
    	- formats like intent/cause/system/concept/structure
    - solution automation workflows (which are interface queries & insight paths that connect a problem & a solution)
    - database schema (storing definitions, interface analysis rules, insight paths, patterns, functions, concepts, prior interface queries & interface query stats, etc)
    - core interface query operations (find/apply/build, representing core 'intents' to solve 'problem types')
    - interface query logic that comes with defaults built-in (such as 'query the pattern interface to handle missing information or to find common information')
    - interface-specific configuration to include useful logic & structures specific to each interface given its definition, like common problem types/formats or problem-solution matching logic
	    - example of interface analysis logic 
			- interface analysis rules are configuration of the program, which are:
			    - stored in a database (in a 'functions' table)
			    - can be derived from applying other interfaces
			    - can be derived by applying definitions to identify the rules from raw data
			    - the analysis rules are generatable from the core & object interfaces, using the system layer graph that generates all the possible structures (like causal trees or loops or combinations) of a defined interface object (like cause)
			    - the analysis rules are somewhat trivial compared to the invention - the invention is the implementation & assembly of the components:
			      - solution automation workflows
			      - database schema (including indexes for interface objects like functions, patterns, structures, systems, concepts, etc)
			      - definitions (of core input objects like interfaces, alternative definition routes for important concepts, etc)
			      - interfaces (including primary interfaces & analysis rules used to implement them, as well as logic for interface queries & finding new/specific interfaces)
			      - interface queries
			      - core query operations (find/apply/build, representing core 'intents' to solve 'problem types')
			- for example, the causal interface implements causal standardization & analysis, which involves analyzing structures of causation (like dependencies & causal direction)
			   	- a sample rule applied on the causal interface, stored in the functions table, might be something like:
				    - 'hub causes, which cause many other causes, are typically associated with metadata like causal direction having a value of "all or most possible outward directions"'
				- this rule might be applied once a problem is standardized to the causal interface as part of an interface query to generate a solution, to find important/direct causal structures of the problems (since another causal analysis rule 'direct causes are usually more solvable than root causes' may apply)

## Summary

	Much of this project automates the problem-solving methods & structures I use mentally - so it can be viewed as meaning, information organization, solution or intelligence automation. Other components of this project include important specific functions, like predicting/finding/using important system filters & finding useful problem type-agnostic insight paths.
  These components can be used to solve problems like "predicting system behavior more efficiently", by:
    - applying a problem-solving workflow, like 'break into sub-problems, solve independently, aggregate & integrate sub-solutions & test aggregate solution'
      - breaking it into sub-problems, like 'optimize predictions', 'increase prediction accuracy' & 'optimize learning', with a corresponding interface query to link the problem with a solution using info formats (to break into sub-problems & integrate the sub-problem solutions) & a metric to evaluate them
      - identify key components of the problem system 'learning', like 'bias'
      - applying relevant structures, like an insight path having a relevant supported intent like "find & describe change rules of identified key components of the problem system to optimize"
      - retrieving/deriving & applying insights about the mechanics of bias
      - organizing the retrieved information (including bias insights & bias patterns) to fulfill intent 'optimize predictions', with other intents 'increase prediction accuracy' & "make 'learning' system more efficient".
  You can see how these components - once standardized to the meaning (relevance to problem-solving intent) interface - are formatted with the structures of relevance.
  - problem intent: optimize learning
    - apply structure: find object in the learning system that is measurable (predictions)
    - problem intent: optimize predictions
      - apply structure: find object in the learning system that allows specific measurements of predictions (prediction metrics, like accuracy)
      - problem intent: increase prediction accuracy
  You can derive key components like 'bias' in the 'learning' system with various methods, including:
    - interface-specific definitions:
      - structural definitions of bias include 'applying a rule out of context' 
        - matching this structure or its abstraction (insight path of this structure, like 'identify structures having the mismatch problem type between core/important components') to a structural format of the problem system would enable identifying other alternative structures matching this structural definition (to build the abstract insight path if it doesnt already exist in the database)
    - core analysis:
      - generating important components from core components
        - (rule) x (rule change type, or change type that can be applied to rules) x (system that doesnt support that change type) = 'irrelevant rule'
        - (rule) x (system change type, or change type that can be applied to systems, where the system may not support that change type) = 'irrelevant rule'
    - interface-specific analysis:
      - applying a problem type format like 'enforcement gap' or 'variance injection point' would allow components of one system to enter other systems, which might not benefit from those components in the same way due to their different structure
    - common components analysis:
      - apply common important interface objects
        - apply the important 'relevance' concept
          - 'out of context' maps to 'relevance', so if you apply important concepts & other interface objects like relevance to core components like 'rules', you can arrive at the structural definition another way
            - 'irrelevant rules' maps to 'applying a rule out of context'
        - apply important problem types
          - common problem type is a 'mismatch'
            - apply this problem type to important learning objects, like 'context' on the system interface & 'rule' on the function interface
              - 'a mismatch of context & rule' maps to the structural definition 'applying a rule out of context'
  - the 'prediction accuracy' is the relevant object to optimize, which can be derived from the original problem statement 'predicting system behavior more efficiently' once broken into sub-problem problem-solving intents like 'optimize learning' with the same structure-application process.
