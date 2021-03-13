  - example of identifying query-changing (invalidating, embedding, stopping) conditions during an interface query or interface query-generating query
    
    - queries are implementation of components of control flow (supply: decision/action/function, demand: problem/error/task/conflict/limit)
    
    - example: execute a query to find structures of 'high-variation' in a data set
      - identify relationships within a variable (across potential values for that variable)
      - identify relationships within a variable's state changes (across potential values for that variable across its lifetime)
      - identify relationships (interaction functions & types) between variables
      - identify relationships between variable structures (subsets, combinations, alternatives) & variables
      - identify variable types (proxies, root cause, interdependent)
    
    - query-changing conditions
      
      - standard control flow conditions

        - query-stopping condition is where its clear the data cant:
          - fulfill the optimization metric or fulfill it more
          - find the information or find any more
        
      - meta conditions

        - query-invalidating condition is where the data set invalidates the concept of variation or data 
          - when a query has identified type/relationship/pattern information invalidating the data
          - when the data is not a source of truth (state has changed but data has not & has no variation and is not data anymore, if data is a source of truth)
          - when a query has identified a function to reduce the variation/data without losing info
            - or create a function to do so
            - or identified a need to trigger an embedded query to create a function to do so
            - and has identified & organized resources to create that function or execute that query, after identifying its need for the function/query (AGI)
        
      - query interaction conditions
        
        - query-connecting condition is where the query identifies that another running or previously run query might have identified useful info relevant to its task

          - examples:

            - a query that identifies similar structures 'difference-reducing/increasing structures' or 'sismilarity-filtering structures (leaving just difference structures)' might find the high-variation structures quicker
              - this alternative query could be found by applying the concept of 'similarity' to the 'query' object, allowing for the possibility that the query was almost correct

            - a query to identify query metadata and apply those metadata variables to generate other alternative queries
              - query metadata examples: accuracy, side effects (like unintended functions built during processing)
                - generating more accurate or faster alternative queries by applying optimization structures (like alignment, info/function re-use, etc)

            - a query that identifies 'change-reduction' structures (like types or interfaces) could be more efficient than this query to find high-variation, which may miss embedded query opportunities for embedded structures of change in the data (data about variables/functions)
            
              - how could the original query know to check for such a query running in parallel?
                - identify problems with its own query metadata (execution, design, connectivity, progress, probability of success) & calling query to generate alternative queries that optimize on problematic structures like performance metrics (execution time vs. relevant info found)
                - identify problems in the original problem of the query (sub-problems of original problem, encountered problems like a missing function to derive)
                - apply structures of robustness by default, like apply 'alternative' to 'query' object to run alternative queries by default, filtering by difference or relevance to maximize probability of finding useful info
                - identify relevance structures that would be useful (such as useful for sub-problems identified initially or encountered during execution, or planned problem to solve later in original query)
                  - it could apply the concept of 'type' to itself (self-aware that it's a query) by abstracting the 'query' concept, identifying its type, and querying for other queries of that type
                    - identify that its processing was not finding info as quickly as typical queries asked to find structures of concepts like 'variation' 
                  - it could identify that there is another route to the info during its processing
                    - by examining data for variance, find a structure consistently causing/generating variance that relates to change reduction
                  - it could execute some of its processing using conceptual core structure analysis, creating combinations to identify concepts (related to query concepts like variation & data) like 'change reduction'
                  - it could identify that a query-invalidating condition that reduces the variation in the data set has been met in another query
                  - it could use concepts like 'equal' and 'opposite' to apply a counter-query to check for the opposite structures, which can be faster
                    - just like checking for a difference may be faster than checking for a similarity or vice versa, or checking for a limit/conflict may be faster than checking for a function
                  - it could apply concepts related to the definition of 'change' such as 'potential', and identify that potential increases with more change structures, particularly change-expanding structures, the opposite of what this query is looking for
                
                - then using the output of such analysis types that can supply relevance structures, applied at intervals or decision points during its own processing, it could check for a query running with intent (or inputs, side effects/outputs during/after processing) to:
                  - identify 'change reduction' structures
                  - generate a function to generate 'change reduction' structures
          
        - query-embedding condition is where an embedded query is required
          - in a data set is data about functions/variables, an embedded query might be used to find embedded variation in embedded function/variable relationships/structures
            - data about functions/variables would expand the possible variation in the data set within each column/variable, with change types (functions/variables) as data
    
    - condition types
      - invalidate query (compare & find alternative solution)
      - embed query (correct an info gap)
      - connect query (delegate processing to another query)
      - stop query (apply a metric)