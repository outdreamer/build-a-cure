- date of international search report: 01/05/2021

- general comments
	- nearly every program involves an equivalence check of some sort, where an explicit data type check or an implicit state/process check or other input metric
		- 'having an equivalence check' that doesnt make it equivalent to my method of 'comparing any structure with any other structure after standardizing it to a custom primary interface which is a standardizing filter with a special meaning that indicates it can be used to solve any problem', but I understand why someone who isnt good at comparing things would have trouble identifying the difference between the two
	- none of these programs do anything other than:
		- apply machine-learning algorithms to identify patterns, generate content, identify entites in unstructured data, etc
		- apply known existing functions to process data, for example to create summaries of data with a 'summarize' function or identify topics/entities in data with an 'identify entities' or 'identify topics' function
		- apply input-output function sequences of known existing functions, which can be replaced with a sql select statement & an iteration of the results to create a nested list connecting inputs/outputs
	- my invention provides a method to automate problem-solving by applying solution structures like interface queries, which use interfaces ('standardizing filters that make comparison of inputs trivial', so that problem/solution structures can be compared & connected)

- relevant other inventions in category Y: documents considered to be relevant, invalidating novelty when combined

	- US 2007/0156748 A1 - Emam IBM
		- https://patents.google.com/patent/US20070156748A1
		- paragraphs: 48, 93 - 99, 138 - 141, 144, 145, 147
		- abstract
			"The present invention is directed to the field of electronic content management and more particularly to a method, system and computer program for automatically generating electronic content based on a user designed table of contents and a desired final content form. Language identification and automatic machine translation technologies are also used to broaden the sources of information, The method comprises the steps of: extracting from the unstructured data, information related to one or a plurality of preselected topics; consolidating the extracted information in a structured form; localizing the consolidated information according to a selected environment; generating content according to a specified form."
		- differences
			- their invention can convert an e-book or a web page into a set of keywords or a different e-book or web page with synonyms replacing the original words, but it cannot convert it into an insight-generating algorithm like my invention can
			- their invention determines relevance on a single metric 'similarity', which is the default metric of relevance/usefulness/meaning used by thousands of other algorithms, and is only one structure used in my system which uses thousands of other useful structures & identifies new useful structures as needed
			- their invention requires user configuration of a text-generating algorithm
			- their invention solves an entirely different problem of 'generating example content given a domain reference network & an output template', whereas my invention solves the problem of 'automating problem-solving'
			- their invention depends on trivial combinations of known machine-learning & data processing methods, whereas my invention relies on definitions of interfaces on which any problem can be solved (intent, cause, potential, meaning)
			- this invention in general has the intent of 'apply a pattern to a topic to make it relevant to that topic', which amounts to functionality like:
				- 'apply a number pattern like a function to a specific number set'
				- 'find an example of a pattern in this system'
				- 'apply a route from one system network to an equivalent position in another system network, having nodes in the same/similar position to enable finding the equivalent position to apply the route to'

				which is functionality that is insufficient to complete any other task than the general function of 'apply a structure from one system to another system', which is not implemented in this invention, because this invention is too specific to fulfill that general function, and instead only implements a specific version of 'applying a structure to a particular topic', for the specific problem of 'converting input to a user-specific language or other user-specific network'.
		- similarities to my & other inventions
			- there are many thousands of programs that generate content in a specific form based on an input template specified by the user, which is a minor detail of my invention that is dynamically generated, rather than being a statically defined function to do nothing other than fulfill a template
			- there are many thousands of standardization algorithms, none of which standardize information to a structure even remotely similar to that used as input to my invention
			- there are many thousands of feature-extraction, relation-extraction, and filtering methods in the machine-learning domain, none of which are similar to my invention
			- there are many thousands of similarity-calculation algorithms, none of which use interfaces to highlight differences & make comparison trivial, nor do they use interface structures like problem/solution structures or cause/intent structures to determine similarity, they just use comparison of vector angles/magnitude or some other well-known method or trivial adjustment to it
			- there are many thousands of entity-extraction tools because its an extremely trivial & standard known process with a known solution

	- US 2015/0106156 A1 - Adobe Systems Incorporated
		- https://patents.google.com/patent/US20150106156A1
		- paragraphs: 68, 73, 81, 82, 85, 86, 88 - 90, 107
		- abstract
			- "A contextual analysis engine systematically extracts, analyzes and organizes digital content stored in an electronic file such as a webpage. Content can be extracted using a text extraction module which is capable of separating the content which is to be analyzed from less meaningful content such as format specifications and programming scripts. The resulting unstructured corpus of plain text can then be passed to a text analytics module capable of generating a structured categorization of topics included within the content. This structured categorization can be organized based on a content topic ontology which may have been previously defined or which may be developed in real-time. The systems disclosed herein optionally include an input/output interface capable of managing workflows of the text extraction module and the text analytics module, administering a cache of previously generated results, and interfacing with other applications that leverage the disclosed contextual analysis services."
		- differences
			- their invention is basically 'apply AI to extract features/entities & tag text with categories/topics/entity labels' which has been implemented countless times by many people in very similar ways as their 'invention'
			- the structure of a 'direct acyclic graph' is used for a workflow to 'connect the input information with the output structured topical information', rather than a workflow to automate problem-solving or generate workflows to automate problem-solving
			- their use of the term 'interface' means 'web page' or 'desktop app view', rather than my invention's definition of the term, which is 'standardizing filter useful for comparing structures in a way that allows the solution of any problem on the interface'
			- their invention applies the 'input-output sequence/graph' as the only method to connect a specific problem input with a solution output, to solve the specific problem of 'converting a text input to another text format using existing known tools that implement those conversion functions'
				- my invention identifies many useful structures like 'format sequences', 'input-output sequences', 'assumptions', 'contradictions', 'efficiencies', 'trade-offs', 'cost-benefit analysis' and primary interfaces on which any problem can be solved like information/meaning/math/potential/cause/intent/change/patterns, as well as problem/solution attributes like 'solution success cause' as being particularly useful in not only solving original problems but also solving the problem of 'generating solution structures like interfaces, solution automation workflows, insights, problem/solution core interaction functions, insight paths, and interface queries on-demand', and can apply these structures to solve any solvable problem (meaning there is sufficient information available to solve it)
		- similarities to my & other inventions
			- this involves 'nodes' that perform specific logic to complete a task like 'analyze this attribute of the input', which could refer to any function, and indeed they admit that almost any function can be plugged into this system, so the only value added is the directed acyclic graph organizing the functions called from resources, which is so trivial it can also be created with a sql query & a database of functions indexed by input/output
			- their invention allows specifying a workflow to process data using existing functions, but so do countless other inventions
				- my invention involves new functions to process data in extremely useful ways that enable automation of problem-solving, not just 'applying processing functions in a sequence to extract attributes like summaries or entities using known methods like entity extraction accessed by calling existing known functions'
				- anyone could write a query like 'select input, output, function_name from functions where type = "processing_function" and output = "user_specified_output"' and sort the functions by input/output equivalences and replace their invention
				- if there are no equivalent input/output functions available, their invention fails to fulfill the user request, whereas my invention would derive the structure of what the user meant by their problem statement & build a function to fulfill that user intent
			- 'caching of solutions' is called 'memoization' and is not unique to this invention, nor are any of their other tools used, whereas my invention not only assembles tools in a new way, but defines sub-inventions in the form of new terms, new tools & new analysis structures, types & rules used to fulfill the overall invention
			- the relevance scoring system they describe is so common its surprising it ever made it into a patent application, let alone that it was approved

	- US 2011/0093452 A1 - Jain, Oath
		- https://patents.google.com/patent/US20110093452A1
		- paragraphs: 22, 23, 30, 32, 33, 36, 50 - 54
		- abstract
			- "Web search engines are often presented with user queries that involve comparisons of real-world entities. Thus far, this interaction has typically been captured by users submitting appropriately designed keyword queries for which they are presented a list of relevant documents. Embodiments explicitly allow for a comparative analysis of entities to improve the search experience."
		- differences
			- their invention is to 'determine if known similarities/relationships are relevant to a search query', whereas my invention is to "determine a way to convert a problem into a solution by applying interfaces (which are a 'standardizing filter that formats input in a way that make comparisons trivial' so that any problem can be solved on that interface)"
			- their invention is basically 'apply a similarity-calculating function like cosine similarity to determine if "a query is similar to another query involving a product version comparison" or if "a keyword in the query has a related object it is often compared to"' with intent to suggest alternate queries the user might want to run instead or suggest content matching the 'compare related product versions' intent, and apply machine-learning techniques to identify patterns between related objects & queries to help improve search query keyword & search result content recommendations
			- my invention doesnt just fulfill a 'search' intent (referenced as 'find' function), it also has functionality that can support 'build' and 'derive' and 'change' intents to adjust/derive/build solutions where an existing solution is not found
			- their use of the word 'comparison' is irrelevant and can be replaced with synonyms like 'similarity' or 'relationship', compared to my use of the concept of 'comparison' as a 'process to be executed, once inputs are standardized to an interface to identify their differences, as a sub-process of an interface query involving possibly multiple interfaces to fulfill problem-solving intents or solution automation workflows to solve any problem'
			- what they are comparing is 'objects related to search keywords' like 'product versions', whereas my invention standardizes structures to compare structures like 'definitions of the problem/solution', 'inputs & outputs', 'functions/intents/causes', 'sub-problems & sub-solutions' or 'formats in a format sequence' or a 'format required by a solution automation workflow and an origin problem format', so that these compared structures' interaction functions (relationships) can be determined & they can be positioned correctly inside a solution automation workflow to solve a problem
		- similarities
			- their definition of 'comparables' is a synonym for 'similarities', which countless search algorithms & tools implement a method of automatically identifying
			- their definition of 'meaningful' means 'different', which countless search algorithms & tools implement a method of automatically identifying
			- identifying patterns using machine-learning is implemented in so many other applications it can safely be ignored as a possible source of innovation

