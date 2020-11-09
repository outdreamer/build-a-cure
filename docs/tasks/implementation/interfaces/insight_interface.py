'''

  - definition: 
    - uses patterns in network structures & insight paths to predict: 
      - probable missing pieces of networks 
      - insight path of a route type (optimal/realistic) 
      - insight path trajectory for a particular assumption set 
  
  - attributes: 
    - reusability (insights can have a limited opportunity of applicability, and may have scope beyond their host system) 
  
  - functions:
    - apply/derive an insight path, shown in FIG 20 (Insight path application)
    - link insights
    - identify insight

  - objects:

    - rule structure (combination of rules, sequence of rules, position of rules) 

    - units of insight paths include core functions to produce insights, such as:
        - change/split/merge type
        - change attribute value/set
        - apply limit/intent/priority/function/pattern from one part of system to another part of system
        - insert interim/sub-system
        - insert variance
        - insert conflict
        - derive common attributes/rules
        - combine objects that haven't been combined yet
        - check similar objects for common cause or symmetry
        - remove/add assumption/requirement/dependency/connection

  - structures: 

    - insight path: a reusable cross-system pattern, usually built out of core functions from a general interface filter (type, intent, function, structure), that allows generation of insights. 
        It can be as simple as a function like differentiate, a standardizing attribute like relevance, or involve a standard object like a simplifying question. 
        It does not refer to specific strategies unless those strategies can be used to generate insights. 
        Insight paths usually consist of abstract or structural rules like 'match structure' or 'identify type'.

  - concepts: 
    - predictive power (an insight is true & may be powerful in predicting across systems) 

  - examples:
    - a unit example is 'trial and error' or 'statistical regression' or 'break up the problem into smaller problems & solve them separately, then aggregate solution output' - these are standard abstract rule sets/sequences to apply when discovering new insights in a system, which can be used across systems. You can call these specific strategies, but they can also be considered insight-generators or solution-filters, as they can reduce the solution space when narrowing down possible insights describing a link to the correct linking rule. These examples are not always ideal/efficient so they're not top priority methods, but they're a good example of what position an insight path occupies in a system. 
    - an actual useful insight path would solve a common, abstract difficult problem, like 'generating the idea of regression', which would be something like:
      - query for concept adjacent to balance/equivalence in the context of a data set output (average)
      - apply the concept of average to indicate a general average distance within output range specified by input format (point subsets) in an input (data set)
      - find a definition of 'average between output ranges of point subsets' that matches the change type you're aiming for (ie, least squares)
      - find a definition of the format 'point subsets' that matches your average definition (adjacent points with euclidean distance definition, in subsets of the data set with a particular change rate)
      - format the input (calculate the data set subsets) using the 'point subsets' definition
      - apply the definition for 'average between output ranges of point subsets' to the formatted input (calculated data set subsets)
    - As shown in the top section of Fig. 19 in the section titled 'Averaging/Standardizing Function' depicts example implementation of the function, involving sub-functions to connect input A and output B are depicted, with varying number of steps, usage of core functions, direction, probability & complexity.
    - Applying an insight path like 'functions requiring more distortions are less likely' may automate the assignment of levels of probability to prediction functions, given the 'Averaging/Standardizing function' implementation structures depicted.
    - The section of Fig. 19 titled 'Interface Object Insight Path' depicts an example of an insight path that is a trajectory of objects on the interface network, which has some objects in common as the system path because of the cross-over in definitions of a system and an interface. These objects may be object/attributes/rules of an interface (or combinations/other core functions applied to them), maps between interfaces, or filters used to generate an interface.
    - The section of Fig. 19 titled 'Structural Insight Path: Function Pattern' depicts an example structure to frame common distortion patterns as alternate routes from function input to function output, which are a very useful subset of insight paths to generate insights across fields.

    - joke insight path examples

        - expectations
          - inevitabilities/incentives/assumptions as a source of expectations
          - hypothetical questions & question chains ('what if x') to generate assumptions
            - what if function x normally associated with object 1 is instead in object 2, which shows no evidence of function x
          - assumptions & assumption chains
            - not just "that inanimate object x has feelings" but also "and has tried to manage them but fell for a sock anyway" to fulfill an 'explanatory alternate route' intent of "how it got stuck"
            - permuting the assumption that a gender will be classified as an object of the gender classification system rather than an object of a different classification system, like race or social status or species
              https://www.twitter.com/alienbot1/status/1053376572558852100
        - intent
          - missing the point
            - the point of preventing animal cruelty is not "so they dont have obvious evidence to point to when justifying organizing criminal enterprise against humans"
          - invalidating the point
            - protesting animal cruelty using signs & bumper stickers made with glue made out of dead animals
          - making a point in an unexpected route
            - preventing animal cruelty so they taste better
        - structures
          - switching positions/structures
          - relevance cycles
          - efficiencies
          - similarities
            - differences can be found in:
              - attribute value, attribute structure, attribute metadata
              - adding/removing variables, variable structures (sets, sequences, networks)
              - identifying variables likely to change
              - identifying variables & patterns likely in a system/context
              - interfaces (priorities, abstract attributes like relevance/meaning/sense, logic)
            - difference types:
              - absence of object
              - combined object in a set
              - distorted object
              - filtered/subset object
              - ambiguous/alternative/interchangeable object
              - new object type
              - developed object with new functionality/attributes
              - deconstructed object
              - formatted object
              - object generator/effect
              - illusory/implied difference
              - reference vs. structural vs. systemic difference
          - extremes
          - bases
            - maintaining a base of reality is useful for highlighting differences
              - "reverse-engineering how an idiot came to a conclusion without the assumption that a cult got to them"
          - paths
            - alternate routes are a place to inject assumptions

        - logic
          - validity
            - illogical connections are a plact to inject assumptions
            - system has to make sense (have some organization) to maximize impact

  - answers questions like:
    - what rules are useful across systems?
    - what rules are derivable given a set of structures that commonly appear in systems?
    - what are common rules used for previous insights, and how can they be optimized (shortening an insight path with a set of simplifying/standardizing questions)

  - dependencies
    - this function relies on the apply_structure function and the find_format_for_metric.py function 
    
  - visuals
    FIG. 19. 'Insight path application' illustrates insight path examples and an example of applying an insight path. 

'''