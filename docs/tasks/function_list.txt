Terms:
- objects: a data set, function set, attribute set, class definition, type hierarchy
- attribute value: value held by the attribute like True/False
- attribute property: conceptual metadata property of the attribute like unique, identifier, static, etc
- decisions:
	- choosing to execute one section of code over another; 
	- for example a conditional statement, design patterns, emergent usage/behavior 
		of user/system, bugs, assumptions, & possible input values are decisions since
		they may result in calling different code
- relationship types: sub-type, causal factor, cooperating equal, different version
- strategy: rule used to make decisions, possibly for a particular context
- solution: strategy implemented for a particular context & problem type

Abstract functions to code:
1. identify an attribute of an object (lookup definition of attribute, create logical tests based on definition)
2. identify & list all attributes of an object (database table fields)
3. identify & list all rules related to an object (entries in 'functions' database field)
4. determine if an attribute is new or fits into an existing attribute & whether its an ancestor or descendant of other attributes
5. add an attribute to a list of attributes of an object (add column to table)
6. identify all possible values of an attribute (alphanumeric, numbers, a value from a list)
7. identify all rules defining the list of possible values of an attribute (max length, string data type, contains limited characters)
8. identify all possible properties of an attribute (static/regularly changed, required, unique, identifier, causal, determines other attributes)
9. identify attribute/rule/type/object relationship rules (attribute A is used to calculate how attribute B should be updated or deleted)
10. identify rank/priority of attributes used to make decisions like classification in entity group, identification of unique entity
11. classify a field as a particular type (by category or data format or other identifying or deciding attribute having multiple possible values)
12. build a class definition 
	- retrieve any known rules describing the object's interactions
	- build a list of probable attributes which could be inherited from type ancestors or shared with other objects interacted with in rules
	- retrieve the type hierarchy position based on attribute/rule similarity to ancestors/descendants
	- filter possible attributes by which attributes can be used to identify it, which will be tagged with the 'required' property
		- identifying attributes are those that maximize variance
	- retrieve the values for these attributes required to qualify as an instance of the class
	- assemble attribute-identification functions for each attribute if not already in database table 'functions'
	- derive any additional interaction rules to describe interactions with other objects (if interaction data is available)
13. convert data from one format to another
	csv/graph to database, csv to graph/functions, functions to patterns/objects, log to csv/database
14. identify data relevant to the same object
15. prioritize which version takes precedence over other versions (updated more recently, better design, etc)
16. determine intent (of data, function, design, convention, protocol, decision, change)
17. identify a change that should be entered into the 'functions' table as:
	- a 'conversion' function type, which converts from one usable format to another
	- a granular 'operation' function type doing a single operation on an input
18. identify a pattern 
	to store in the 'functions' table as a 'pattern' function type
19. identify which operation or combination of operations can convert one object into another
	to know which linking changes to look for when trying to connect two objects
20. derive a relationship using list of possible operation sets that convert an object into another or explain their interaction rules
	- identify if one object is a sub-type, causal factor, cooperating equal, different version, etc of the other object
21. identify if a relationship fits into an existing network or if it contradicts a relationship in the network
22.identify if a strategy is a good fit to compress a problem & addresses its causal metrics without causing bigger problems
23. compare two input objects & return a list of similarities & differences,
	 as well as possible inferred similarities based on network position with probability,
	 and a list of ordered functions to convert one object into the other
	 - raw % difference between attribute values & attribute properties
	 - weight of attribute value differences based on attribute priority
	 - create attribute-rule network graph for each object & calculate raw degree of difference
	 - identify equivalent attributes & weight degree of difference between them & their corresponding relationships across graphs
	 - check equivalence of composite scores
24. identify minimum information needed to make a decision (identify required inputs to make the right decision 100% of the time)
25. identify operations to attain minimum required information (generate required inputs for decision)
26. optimize code (spot inefficiencies in code & fix them automatically, like redundant conditions)
27. identify field usage/query requirements in UI, request data, & code base
	ex: 'code commonly queries by name field so create a separate index for that'