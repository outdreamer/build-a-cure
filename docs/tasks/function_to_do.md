# to do

    - logic automation problem structures

      - connecting perspectives (interfaces with a goal like a priority or metric, which makes them by definition relevant to solutions) & solutions
        - by prioritizing different components (structures/attributes/interfaces), perspectives solve problem(s) in different ways, with different variables (problem origin points, solution metrics), and may solve different problem(s)
        - applying or integrating multiple perspectives can cover more problems solved or reduce the problems to solve, or it can create more problems depending on error types, like unnecessary abstraction or complexity added (in regard to complexity handled)
        - some perspectives are more useful than others for various intents
        - some perspectives need to be applied in structures (like sequences/combinations) with other perspectives
        - some perspectives will cause error types for an intent
        
      - problem perspectives with associated solution priorities/metrics

        - interface component perspectives

          - 'object' perspective identifying object changes/structures needed

          - 'state' perspective identifying state changes/structures needed

          - 'variable' perspective identifying which variables are required for solving automation task problem before changing existing system

          - 'function' perspective identifying which functions to write before implementing solution

          - 'test' perspective identifying which tests the solution needs to fulfill (enables finding solutions by iterating changes & checking changes to see if they fulfill test)

          - 'cause' perspective identifying causal network of system components and which causes need to be changed to complete automation task
            - cause of logic selection in existing solution may be the sequence & existence of queries, whether the logic functions are available, & whether the logic variables are populated, whereas the target cause of logic selection should be which logic exists in a data store & the sequence of queries to that data store

          - 'logic' attribute-connecting perspective (attributes like type-position) 

            - sub-queries about type attributes to solve problem of 'finding correct position of components to fulfill organization intent'
              - are certain types of logic better in different positions (validation in json dict, dependency changes in database triggers, parsing/testing in another position)
              - what other types apply to logic (configuration, filters, data, examples)
            
            - examples of logic attribute (type-position) connection functions
              - if a logic type is configuration, that should be in positions associated with configuration
              - if a logic type is changed more than other logic types, that may qualify as data
              - if a logic type is an example, that suggests a testing position

        - attribute-specific perspectives

          - 'optimization' perspective: identifying the most useful functions to write that optimize a metric (like 'flexibility') to the existing system (to support other intents), while fulfilling relevant problem-solving intents of the automation task problem

          - 'organized' perspective that integrates solution with existing system of solutions & finds/handles error types
            - apply interfaces to task & integrate interface objects into solution
              1. find variables of task ('inject logic for specific cases') first
              2. identify variable interactions & important error types to avoid with those variables
              3. design solution fulfilling foreseeable error types
              - variables of 'logic injection' function (solution to automation task of 'injecting logic in specific cases'): 
                - whether specific inputs have specific associated logic
                - whether logic variables are available/populated in input
                - whether logic functions in associated logic are available in execution context
                - whether logic inputs are validated
                - whether other specific cases are supported by 'logic injection' function
                - whether specific cases of multiple injected logic compoennts coordinate or contradict each other
                - whether outputs of injected logic components suboptimally change inputs of other injected logic components
                - whether injected logic components have a correct sequence and whether it aligns with injection sequence

          - 'efficient' or 'default' perspective with low learning curve (adjust existing logic & write tests, dont change anything that isnt necessary like rearranging components)
            - apply most granular change & add changes/logic as necessary to support future intents
              - apply most adjacent solution (add specific conditions to actual logic)

          - 'consolidated' perspective with low maintainence requirements
            - move logic to position with best available testing, validation, processing functions

          - 'reusability' perspective enabling future usage
            - keep logic in position enabling future usage intents

          - integrated 'consolidated' and 'reusability' perspectives
            - keep logic in position enabling future usage intents, but add function to convert to position with best functions to support those intents (testing, validation, processing functions)
        
        - structure perspectives

          - 'limit' perspective
            - identify limit of implementations & identify whether usage will converge to limit
              - implementation limits: 
                - will adding granular specific cases directly to existing solution ever hit a point where its sub-optimal
              - limit convergence:
                - are we near that point or will we be in the lifecycle of this solution

          - 'filter' perspective
            - identify which filters exist & how to change them to implement solution
              - existing filters: conditions, dependencies, constants, validations

          - 'interaction' perspective
            - identify how system components interact & how to change interactions to implement solution

      - apply solutions to various related & sub-problems to task automation problem

        1. problem of 'dependency' between logic components
          - apply 'dependency' definition
            - separate dependent variable logic & apply after initial logic once inputs are populated as constant independent inputs
        
        2. problem of 'dependency' between problem/solution components (solution steps)
          - solving problem 3 must occur before solving problem 4
        
        3. problem of 'selecting which implementation to use for primary automation task'
          - select between strategies
            - inject variable to store logic & apply if populated (store logic in database table)
            - embed logic in other logic (store logic in query logic)
        
        4. problem of 'selecting format to use once an implementation is selected'
          - select between logic formats
            - delimited format
            - actual logic format
            - logic standardized to executing language format (python)
            - logic standardized to common format (json dict) to be used as config vs. data in a data store

        5. problem of 'finding correct interaction level to apply solution at based on interaction interface'
          - interaction level: process, query, task, script, variable, function
          - interaction interface: usage interface, logic interface, input/output interface, state interface
        
        6. problem of 'finding intents supported by implementation options'
          - storing in database supports intent of 'fast initial querying & re-querying, & subsequent querying'
          - storing in python support intents of 'maintainability, modifications to add new logic, consolidate to process/step interface'
        
        7. problem of 'finding related & aligning intents of 'enable injecting logic in query logic' automation task'
          - testing logic correctness: 
            - determining difference in inputs/outputs, as aligning with differences applied in logic (input/output difference created by logic & input/output data difference)
          - testing updated logic:
            - determining difference in original/updated outputs (original data & updated data with new function to inject logic for cases)
          - a difference-determining function would be useful for both of the above intents

        8. problem of 'finding correct structures to approach problem'
          - 'organize problem components' intent
            - position (as an input to the 'organize problem components' intent)
              - find correct position of components
                - logic, input/output/interim/duplicate/index data, validation/generative functions
          - 'reduce solution space' intent
            - filters
              - apply organization intent with regard to solution filters (as an input to 'reduce solution space' intent)
                - tasks, processes, process variables, process steps, required inputs/outputs, and cost of implementing re-arrangements

        9. problem of 'finding functions to solve these problems & selecting the functions that solve the most problems to write the least code'
          - functions that solve the most problems out of problems 1 - 8 & fulfill the most perspectives (fulfill the most perspective-associated solution metrics)
            - function to determine (data/logic) difference
            - function to find required/similar logic/data
            - function to convert logic to a format
            - function to sort (logic/data) in sequence
            - function to apply logic based on variable (execute specific logic for an input, or a specific input to execute a process step logic)
          
    - add to reasons why variable or object network is insufficient
      - variable networks may illustrate attributes & direction of cause, but they dont illustrate:
        - why something is true
          - 'structure of an input' may cause a variable like the 'output of an interaction with another structure', but why is that true - bc:
            - structure enforces limits on interaction potential
            - structure allows similarities & alignments between fitting structures to interact
            - structure allows contradictory structures to damage other structures
          - these are system objects that arent displayed in a variable network with an arrow between an input structure & another structure, with an arrow leading to the side effects & other outputs of that interaction
        - you can add other layers to the variable network to show variables on other interfaces like cause to display reasons why something is true, other than a factual variable network displaying known interactions of components of facts, but this makes it not just a variable network, but a stacked/layered variable network, like how a state network has multiple layers and isnt restricted to one network
        - if you illustrate all interface interactions on one network, it might be unusable bc of the density of interactions
          - the above example has many patterns associated with it, many possible intents, many attributes/functions, many adjacent potential interactions & states & other interface objects
          - these objects can be indexed on the same network, but for quick queries, sorting through all of these objects may not be efficient
          - its also not efficient to store possible adjacent states of an object or its many sets of objects that can generate it or be generated by it in the same network
        - an object network is good for showing known interactions between objects, just like a variable network is good for showing known interactions between variables
        - the merging of all these networks is not efficient, for example when displaying an attribute like 'usefulness' 
          - this attribute may be a property of many objects, and it may be a property of structures of objects (like a system of objects)
          - the attribute also has definition routes associated with it
          - these interactions would be inefficient to display on the same network
          - the structure of the attribute definition routes (on a network of standardized concise definition components like concepts on a language network) would require different structures than objects with that attribute as a property
          - the structures of usefulness defined as the attribute's definition routes may not show up exactly the same on an object or other network 
          - a definition route of usefulness may interact with concepts like relevance & alignment, concepts that may not be displayed on a merged network in a clear way that shows the definition route
            - relevance & alignment are fundamental & therefore common concepts/structures that will show up frequently in a variable or other network, in structures that dont align with their definition routes
          - 'alignment' may involve pairs of objects that make up most of the network - showing how 'usefulness' is defined in terms of 'alignment' (connecting 'usefulness' to those pairs of objects indicating alignment structures) will look differently on that network than on the language network of definition routes
          - so a query to find 'alignment' in a merged variable/object network (that includes all interface components) would have to select between the language network version of 'alignment' (definition routes between concepts) and the structures of 'alignment' found on the object/variable network (pairs of objects), which is less efficient and clear than designing an interface query to select these sub-queries beforehand (like 'standardize object network to concepts & match concepts with alignment definition route')
        - a merged network implies that all possible useful info has already been generated & added to the network, whereas interface queries involve operations that can find/derive new info

    - make diagram of absolute reference connections with metadata structures like networks/paths

  - determine core graph variables (definition of adjacence/difference, connectivity, dimensions, info storage methods, interactivity of structures like sequences)

  - crypto as community consensus, where a decision can have value if backed by a community

  - interfaces that are important bc of generative concepts/structures
    - 'core' interface's generative concept 'simplicity' and related attribute 'composability'
    - 'interface' interface's generative concepts 'interactivity' and 'balance' (how does info from each interface integrate or interact to produce meaning, balancing influence of interfaces in a way thats indicates contribution)
    - 'cause' interface's generative concept 'power' (ability to trigger other components)
    - 'concept' interface's generative concepts 'uniqueness' and 'applicability'
    - 'info' interface's generative concept 'stability' producing info
    - 'intent' interface's generative concepts 'functionality' and 'direction' (functionality develops when there's a reason for it to develop, like a direction of change)
    - 'function' interface's generative concept 'connection' (connecting inputs/outputs)
    - 'pattern' interface's generative concepts 'similarity' (powerful patterns are repeated and patterns develop in similar ways, producing similarities across interfaces)
    - 'logic' interface's generative concept 'alignment' (aligning logical connections with info as a supportive foundation)
    - 'change' interface's generative concept 'difference'
    - 'structure' interface's generative concept 'info' (info about other interfaces with potential for structure)
    - 'potential' interface's generative concept 'adjacence' (what is probable is more adjacent)

    - the generative attributes (simplicity, interactivity, balance, power, uniqueness, applicability, stability, functionality, direction, connection, similarity, alignment, difference, info, adjacence) reflect core structures (unit, value, force, direction, equivalence, distance, rate, ratio, input-output, type, dependency, constant)

  - add to useful concepts

    - bitcoin and ai both benefit from integrating the concept of time into existing inventions (tx history, weight updates)
    - what other concepts could be equally powerful if injected into structures of existing inventions
    - why is time (or the structure of sequence) a powerful concept in those problem systems
      - historical info integrated into current & imminent info was a pre-existing gap in relevant info structures of the problem system
      - the usefulness of historical info wasnt identified or wasnt identified as integratable into existing inventions
      - the related concept of:
        - 'connection' could have served as a replacement, indicating relevance of previous info to new or derived info
        - 'position' could have also replaced 'time' or 'sequence', given the relevance of 'position' as a predictor of financial transactions and connecting one info state to another, given data that can access the destination from that origin
      - its also inherently relevant to know how space-times (states) connect (like in a sequence structure) in order to predict adjacent imminent space-times (or states) as imminent members of the sequence

  - structures like origin/destination points, loops, layers, boundaries, & paths for solving problems (like logistical resource allocation, adding variable to a function, or finding search path (sorting))
    - give examples of problems with relevant structures
      - a question/variable/cause pattern
      - a connected function sequence
      - a set of filters & limits

  - how to identify that more normal language is likelier to contain factual statements

    - multiple interrelated reasons, from the insight path
      1. facts often have simpler connections
      2. language patterns have intents
        3. agents apply language patterns to achieve intent
          4. linguistic intents are often to change meaning until its false (out of the full set of intents to 'communicate info')
          5. agent often over-think how to emphasize/reduce language components and it creates unnatural language patterns
          6. agent-changed language (newly created patterns) is rarely more efficient than normal language patterns (inherited patterns)
            7. when it is more efficient, it is quickly adopted until its normal
            8. more efficient language patterns are likelier to be true, bc of the normally simpler connection patterns of facts 
          9. it takes work to make a set of falsehoods or mix of falsehoods & facts seems like a fact, and the work has side effects like lack of normality (sounding unnatural in structure) or simplicity (using fewer resources to connect components)

    - relevant concepts
      - the concept of 'simplicity' interacts with connections 1, 5, 8, & 9
      - the concept of 'normality' interacts with connections 5, 6, 7, 8, & 9

    - these concepts can be used as almost interchangeable alternatives in generating the interface query generating this insight path

    - despite their differing definitions, simplicity & normality are connected by the concept of efficiency, because what is simple often becomes normal because of the efficiency of simplicity, so efficiency can be used as an interchangeable concept of both of these in some cases

    - interface query to generate the insight path to 'derive an attribute to identify facts'
      - apply concept interface
        - identify important concepts (simplicity, efficiency, emphasis, reduction, falsehood, change, connection, pattern, normality, agency) of the problem system of 'identify facts'
        - apply relevant concepts to problem system
          - agents change language to achieve intents
            - apply intent interface by mapping to intents ('change info' for intent of lying, or 'false similarity to fact')
              - connect intents to original relevant concepts
                - connect problem system component derived from intent interface of 'agent-changed language' to concepts of normality & falsehood

  - add to definitions
    - reason as source cause node ('this happened because of this causal factor')
    - intent as target cause node ('this happened because this intent was the goal used as a cause of the agent's decisions')

  - add to causation variables
    - ability to change (if a variable cant be changed, it is less causative for problem-solving intents)

  - add to problem type structures as 'indistinguishable cause'

    - multiple causes of the same variable

      - example: gravity (no agency, just granular intent of 'apply force to relevant objects') can cause an object to fall, just like throwing it down (concept of agency and intent to 'move object down' or 'move object to ground') can cause it to fall

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
            
