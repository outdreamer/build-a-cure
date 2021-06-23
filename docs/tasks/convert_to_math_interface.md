    - standardize solution automation workflows to a high-certainty interface (like the math interface) using default structures like cross-interface mappings (like 'mapping a conceptual difference type to a particular mathematical difference type') to check if the solution is computable without additional interface queries to apply the solution automation workflow

      - apply a solution automation workflow like a sequential connection between problem & solution:
        - identify isolatable differences between problem & solution
        - map differences to numerical differences (like cosine or other difference)
        - identify conversions that reduce differences in a sequence

      - example with prediction function (using a 'sequential connection' solution automation workflow insight path)
        - identify isolatable differences between problem (data set) and solution (prediction function)
          - data set is a collection of points
          - prediction function is a connection between points
        - map differences to numerical differences (numerize non-numerical data)
        - identify a function to connect a collection of points (reduce differences between points & point-connecting function) - and the format sequence to connect in order to convert points to a function
          - possible format sequences:
            - data set => points => variables => variable operations & structures (like set) => various possible prediction functions => integrated format (like average) of various possible prediction functions => prediction function
            - data set => points => various point-connecting functions (like average/regression) => integrated format (like average) of various point-connecting functions => prediction function        

      - another example with finding the solution to a function:
        - problem 'convert x to y'
          - list differences between x and y
          - list functions to neutralize those differences
          - apply solution metric filter: 'is x == y?' or solution metric filter to test for progress (similarity to solution) 'is new x value nearer to y than previous x?'

        - once youve mapped a problem to a high-certainty interface like the math interface, you can query for available functions that resolve the differences between input/output, either all the differences at once, or resolving one subset of differences at a time when applied in the correct subset structure (like sequence, combination, or integration/aggregation structure)

        - example: map a problem like 'generate a poem' to the math interface
          - apply solution metric filters of a successful poem:
            - show vs. tell: does it use structures of meaning or does it use common words that have become meaningless to cheaply evoke a response
              - math interface variable A: how many structures of meaning does it use vs. how many common cheap trick words
            - response: does it have a probable similar emotional response or does it not consider emotional response of audience at all
              - math interface variable B: what is the adjacence value in emotional response 
            - relevance: does it have relevance structures
              - math interface variable C: how many relevance structures does it have, and do these align with (relate to) the intent structure vector
          - some function f(A + B + C) = y poem success
            - now we have to find operations (multipliers, combinations, powers, opposites) of these variables to predict a successful poem
              - then with that prediction function, we can generate or filter poems accurately for solution metric filters

          - or apply an error-prone algorithm and apply distortion function mapping error output to successful output

      - this format connection sequence can be derived by definitions of 'point' and 'line':
        - identify the intents to connect the problem & solution
          - general intent: 'predict y given x'
            - sub-intent: 'convert points into a line'
        - identify the format sequence to implement intents:
          - implement intent 'convert points into a line': connect points to convert them into a line
          - implement intent 'find component to connect them': 'lines' component can be used to connect them
        - solution metric filter: does the line have to connect every point?
          - no but it should be as near as possible to as many as possible points
        - solution metric filter: in what sequence should points be connected?
          - connections should be made in increasing adjacent order, from x origin to highest value of x, unless some points can be connected quickly by skipping points once priority points are identified, like when there's a clear inflection point or maximum/minimum
        - solution metric filter: does the line have to be composed of lines directly connecting one or more points?
          - no because the general intent is predict position of y given x, not to connect the points
        - solution metric filter: can the line be composed of subset/alternate connecting lines, like subset-connecting lines or various average lines?
          - yes, if an integration operation (like average) is applied to create one continuous line (with no angles)
            - why does it have to be continuous & free of angles? it doesnt, but a discrete line set is less likely to occur in real life (isolated variable subsets predicting y for different ranges) which would ignore the pattern interface, but it may be more relevant with missing data or variables

      - how to derive solution metric filters:
        - identify variables of solution once solution format is identified ('point-connecting line')
          - direction
          - prioritization of points
          - inclusion of points
          - point subsets
            - point subset/set approximations
            - point subset-connection methods
          - integration method of subset connections
          - point-connection methods
        - generate solution metric filters by framing solution format variables as questions

      - how to find answers to solution metric filter questions to determine required solution metric filters
        - the answers to the filter questions must align with the intents of the solution ('derive/improve/approximate a prediction function')
          - points can be prioritized according to adjacence to the average or to subsets of other points if clusters are identified, so the function is predictive
          - direction of point connections matters for some point-connection methods (like 'connect each point pair with their own line, in increasing order'), but not others (like 'find important points & connect them, then integrate/average their connections')
          - points can be included based on metrics (like importance in representing other points, or adjacence to average, as a way of adding value to prediction)
          - point subsets can be selected based on representative samples (a predictive subset) or alternatives (alternate predictive subsets) or integrations (subsets to integrate to form an integration structure like aggregate/average)
            - point subset approximations can be used in place of the entire set, just like the data set points can be approximated with a subset
            - point subset connections can be direct (connect each adjacent pair, connect priority points, connect/average point subset-connecting lines), or indirect (use point to determine value of a possible prediction function)
          - integration method of subset connections have varying value in predicting y (average, weighted average, aggregate, connect)
          - point-connection methods have varying value to improving a prediction function

      - how to determine function interaction structures like 'sequence'
        - for some functions, there are requirements & limits on what other functions they can interact with, in what structures
          - example: for 'compare' and 'standardize' intents, examples of basic interactions are:
            - sequence: standardize, then compare
            - sequence of subset/total: standardize systems components to compare systems
        - the cause of the function sequence requirement for an intent like 'compare to find differences' is that the standardization (when applied first) reduces irrelevant differences, so the relevant differences are clearer & easier to identify
        - the concept of a common base/standard that both objects have is associated with the definition of 'compare', as a way to anchor calculations, to reduce differences in calculations (calculations of difference will be more accurate & easier when the calculation can start from the same position & take the same steps in both objects)
        - the above intents are relevant to functions like 'compare' to improve accuracy of metrics:
          - 'reducing differences in calculations of a function (like compare)'
          - 'reducing irrelevant differences' or 'isolating relevant differences'
        - apply opposite structure
          - if standardization was not applied, an equivalence check could not be reliably executed without using abstractions like input-output patterns or other metadata than mapping the inputs/outputs themselves
        - apply related functions
          - 'equate' is a similar function to 'compare'
            - standardization is a useful function for both equalizing & comparing objects
