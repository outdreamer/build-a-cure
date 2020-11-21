
    - efficiency in calculation
      
      - why is finding a proxy value (that is a multiple of 10) of a multiplication value quicker at some multiplication problems?

        - because of the efficiency present in applying the definition of a digit (base 10), which may make multiplying 65 * 10 and subtracting 65 quicker than multiplying 65 * 9,
          - the operation 65 * 10 just involves moving 65 one digit to the left and adding a zero
          - subtraction is held to be less computationally expensive than multiplication
        
        - the definition of a digit positions multiplication output of base 10 in a sequence that allows indexing of values in comparison to 10 & degrees of 10
        
        - how to find the "definition of a digit' as a relevant object in all the objects of that space
          
          - filter: by noticing that:
            - multiplication changes positions of numbers in some cases
              - relevant concepts to number position
                - 'digit'
                - 'base'
            - multiplication preserves the original numbers in some cases
            - the original problem can easily be transformed into one of these cases (multiplying numbers rounded to an output of multiplying by 10), and easily converted back into the original problem (adding/subtracting remaining value)
              - these two operations may be less computationally expensive than the multiplication operation
          
          - query: in order to notice the above relevant objects, you can do the queries:
            
            - change interface: 
              - find variables of value changes and change types (value position change)
              - static/anti-change (apply 'not' operator or 'lack' problem type to 'change' concept):
                - find cases where change types dont apply (value position preservation and value preservation)
                  - find method of translating problem to case where work is minimized, if work-maximization conditions dont apply
                    - find secondary method to connect translated problem back into original format (with original parameters, meaning adding/subtracting remaining value)
            
            - intent interface:
              - intent of preserving values is to minimize work of calculation
                - find cases where work is maximized by preserving values
                  - filter by whether work-maximization conditions apply
                    - apply method of translating problem to case where work is minimized, if work-maximization conditions dont apply

        - in other words, the original question is 'why do value position & digit base produce calculation efficiencies in multiplication?'
          - because position (and emergent objects of position, like sequence) matters, as adjacent values have inherent relevance/meaning
            - 1000 has more meaning in some contexts than 1, and the second one in 1101 has more meaning than the 1 next to the decimal in some contexts, or in a default definition of 'meaning' as 'value' or 'distance from origin', except with definitions where the definition of meaning is a concept like 'clarity' or 'unit' or 'standard'
          - difference from base values is another way to measure relevance in values having position
          - the more different a multiplier is from 1, the more relevant these digit-based adjacent values become in optimizing the multiplication process
          - important metrics of relevance:
            - value position difference
            - non-zero value position difference (distribution of non-zero values in multipliers)
            - value difference from zero
            - value difference from adjacent digit base multipliers
            - difference in calculation operations between digit base multipliers (move position operation) & original multipliers (multiplication operation)

          - intent-matching:
            - intent-change
              - the intent is to change position of a value, there is an efficient operation to accomplish that intent (move value position) if the inputs qualify given the base standard
                - difference in multiplier value position = value position difference source, if difference between inputs & digit base requirements are negligible
              - this is how you can frame a math problem on the change interface, framing the differences needed (intents) with the input differences (variables) and other relevant differences (differences from standards)
              - an efficient solution is one that minimizes use of costly functions like transformation operations (maximizes use of adjacent resources or other efficient methods)
                - so the inputs to an efficient solution will minimize the difference type that is 'input differences'
                - efficiencies minimize differences/difference types needed to achieve an intent in general (an efficient alternate route may use fewer steps or lower-cost steps than the default route)

          - these differences align in a structure that clarifies the increase in value from using digit base multipliers followed by conversion to original multipliers
            - if a multiplier fulfills the threshold values of these operations on the difference types:
              - maximize (value difference from zero) + minimize (value difference from adjacent digit base multipliers) + minimize (non-zero value position difference)
                = minimal difference from efficient calculation (multiplying digit base multipliers)
            - the solution structure points to the alignment of these differences:
              - use methods (convert to digit base multipliers) that allow the use of position operations (move position) rather than more expensive operations (multiplication)

            - how could you derive efficiencies if you didnt already know that using a digit base multiplier was lower-cost than using the original multipliers?

              - you can apply definitions of objects to other definitions, and check for conversion adjacency to those objects
                
                - examples:

                  - find difference/change types (like differences in variables like bases, adjacent transforms)
                  - apply aligning structures of difference types
                    - difference from digit base multiplier (multiple of 10) aligning with value position difference operation (move)
                    - (difference from common base) combined with (difference from common base) = exponent addition/subtraction 
                  - apply a pattern to a parameter set
                  - apply an average operation to a function
                  - the points formed by factors of a number that align with the digit base form a pattern of efficiencies in multiplication intents for certain original multiplier sets
                  - apply transformation sequeence:
                    - standardize to common interface (in the form of a common base value)
                    - find derivative/slope
                    - this transformation sequence identifies the difference type of a constant difference between exponential values of a multiplier (4 ^ 0, 4 ^ 1, 4 ^ 2) once transformed to derivatives, constants being easier/more efficient to work with than other value/function types

                - youre looking for object intersections or object patterns that share resources in some way and reduce costs for each other by interacting
                  - this means you want to focus on combinations that increase the likelihood of interactions with other objects, just like the base number 10 has interactions with value position (digit definition) & the move operation, and multipliers having a common base having interactivity in their exponents
                  - youre also looking for shared spaces that can act as interfaces (common bases, formats, standards) where calculations are more trivial (addition rather than multiplication) because the values are already standardized
                  - operations may develop on these shared spaces, leading to efficient object interactions

              - you can also start with a set of unit or efficient operations and build functions out of them that iteratively fulfill higher & higher intents
              
            - how to derive efficient operations in the first place:

              - identify when there are alternate paths to an answer (65 * 10 = 650 * 1) while changing a minimum of other variables (having the same number types, like integers), and check if alternate paths are lower-cost, and in what cases (ratio of cases, common cases, etc)
                - a variant of this is identifying that multipliers share a common base, which has another calculation efficiency in the application of addition/subtraction to exponents instead of multipliers
                  - example: 64 * 16 = 4 ^ 3 * 4 ^ 2 = 4 ^ (3 + 2)
                  - if you dont need the result of the operation or can standardize other relevant values to that base, you can keep it in this format instead of executing the operation 4 ^ (3 + 2)
