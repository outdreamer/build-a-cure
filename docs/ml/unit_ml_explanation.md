- example of solution automation workflow applied to multi-layer perceptron example of xor function

  - xor function produces true if input a & b are different, and false if not

  - picture of multi-layer perceptron that can implement xor
    - https://en.wikipedia.org/wiki/File:XOR_perceptron_net.png

  - problem: create a function connecting the following format sequence from problem to solution
    
    - problem = 'find function that outputs true/false for inputs a & b which can have value 0 or 1, with 'true' output if a/b differ)' => 
    
    - solution = connect (inputs => all possible input combinations (problem space to filter) => all possible output solution metric values (solution metric space))
               = connect (inputs (a,b) => all possible input states of (a,b) => some interim function producing an interim state => some filter function to route all possible interim states to their correct final output state (true/false))
               = connect (a,b)         => (0,0), (0,1), (1,0), (1,1)         => some interim function producing an interim state => some filter function to route all possible interim states to their correct final output state (true/false)
               = connect (a,b)         => (0,0), (0,1), (1,0), (1,1)         => some set of all possible interim function states like (0,1,1,2) => some filter function to route all possible interim states to their correct final output state (true/false)
               = connect (a,b)         => (0,0), (0,1), (1,0), (1,1)         => 0, 1, 1, 2                                                      => false, true, true, false

    - the problem is:
      - 'converting the problem space of all possible inputs to the solution space of all possible outputs' (formatted as a function to generate outputs from inputs)
      - 'merging the problem space of all possible inputs with the solution space of all possible outputs' (formatted as a solution shape masking the problem space, indicating which possible input combinations are true & which are false)
    
    - the problem space has two primary possibilities:
      - the inputs a/b differ
      - the inputs a/b are equal
    
    - the solution space has two primary possibilities:
      - true/false
    
    - the interaction space between inputs/outputs has four possible input states (2 ^ 2, with two inputs a & b, having two possible states each: 0 & 1) that converge to two possible output states
      - two ways to differ (produce output true)
        - a is 0 and b is 1
        - a is 1 and b is 0
      - two ways to be equal (produce output false)
        - a is 0 and b is 0
        - a is 1 and b is 1
    
    - whats the minimum number of input/output-connecting interim nodes that can connect inputs/outputs non-linearly (not using an identity function or another linear combination of inputs)
      
      - the network depicted is not fully-connected, so inputs are routed only to adjacent nodes on the next layer
        - meaning inputs like x are not routed to all three nodes on the interim layer, just the adjacent two nodes on the interim layer

      - the interaction space would indicate 4 nodes to connect inputs/outputs - can this be reduced & how?
      
      - relevant structures
        - the inputs a & b can have a 'combination' (sum) structure in a network as the calculation moves to the next layer
          - why is the sum relevant? 
            - bc it can compress the info from the four possible input states and incorporate info about weights applied to inputs (although there will be overlaps with other sums created with different inputs/weights)
            - the sum of 0 + 0 = 0
            - the sum of 0 + 1 = 1
            - the sum of 1 + 0 = 1
            - the sum of 1 + 1 = 2
          - now we have three possible interim sum states created from the four possible input states
          - now we know that we require a network that can convert these three possible interim sum states to true when the sum is 1 (the inputs are different) and false when the sum is 0 or 2 (the inputs are equal)

      - in a logical function written with if/else statements & other functions, inputs can be routed to an existing comparison function that identifies structural meaning (in the form of equivalence) 

      - in a network, all inputs are routed to all nodes on the next layer for summation & comparison of the sum to a threshold value
      - in the example, the three-node interim layer has a node with a threshold that deactivates one weighted combination of inputs (1,1), and has two nodes that enable other weighted combinations of inputs (0,1 and 1,0)
        - it outputs zero if the threshold is not reached
          - the middle node of the interim layer would output 1 for equal state (1,1) which is then maximized to be negative
          - the middle node of the interim layer would output 0 for difference states (0,1) and (1,0)
          - the outer nodes of the interim layer would output 1 for all states except (0,0)
        - if the sum of the inputs is 1, the node is enabled (the inputs differ as one is 1 and one is zero), and if its 2, the node is disabled (the inputs are both 1)
        - the interim layer should filter out the equal state (1,1) by assigning the output of that equivalence-allowing node an extra negative weight (-2), and assigning difference-allowing nodes a positive weight
        - the extra difference-allowing node may function as an offset of the impact of the equivalence-allowing node
    
    - its useful to index nodes in a neural network by their functionality 
      - an 'equivalence-allowing node' may become an 'equivalence-preventing node' with particular input combinations, surrounding weights & activation thresholds

      - the activation functions of the network are assumed to 'output 0 if threshold is not reached', * indicates non-zero output value, parentheses indicates input value or threshold value

    
    - illustration of all possible iterations through the network, with four possible input states

        - for inputs (0,0), the inputs, thresholds, non-zero values (indicated by asterisk), & weights looks like this:            
            1 -2  1
          (1) (2) (1)      
            1  1  1
            (0) (0)
          
          - final total:  y = 0 + 0 + 0      y = 0

          - for these inputs (0,0), the trajectory of value sequences on each layer looks like this:
               0   0   0
              /    |    \
             0   0 + 0   0
             \    /\    /
              0  0  0  0

          - for these inputs (0,0), the trajectory of value sequences after each operation looks like this:
                   0
               0   0   0
          0*1     0*-2     0*1
   (0 if x<1)  (0 if x<2)  (0 if x<1)
           0       0       0
           0     0 + 0     0
          0*1 (0*1)=(0*1) 0*1
             \    /\    /
              0  0  0  0

          - in sequence format, where the sums of the last values equals the final total:

            - layer value sequence:
              0 -> 0 -> 0
              0,0 -> 0 + 0 -> 0
              0 -> 0 -> 0

            - operation value sequence:
              0   -> 0 * 1         -> 0 -> 0 * 1  -> 0
              0,0 -> 0 * 1 + 0 * 1 -> 0 -> 0 * -2 -> 0
              0   -> 0 * 1         -> 0 -> 0 * 1  -> 0

            - linear function requirement added by this input-output map (equivalent inputs (0,0) equal an output of zero)
              - 0 + 0 + 0 = 0


        - for inputs (0,1), the inputs, thresholds, non-zero values (indicated by asterisk), & weights looks like this:
            1 -2  1
          (1) (2) (1)*
            1  1  1
            (0) (1)*

          - final total:  y = 0 + 0 + 1      y = 1

          - for these inputs (0,1), the trajectory of value sequences on each layer looks like this:
               0   0   1
              /    |    \
             0   0 + 1   1
             \    /\    /
              0  0  1  1

          - for these inputs (0,1), the trajectory of value sequences after each operation looks like this:

                   1
               0   0   1
          0*1     0*-2     1*1
   (0 if x<1)  (0 if x<2)  (1 if x=1)
           0       1       1
           0     0 + 1     1
          0*1 (0*1)=(1*1) 1*1
             \    /\    /
              0  0  1  1

          - in sequence format, where the sums of the last values equals the final total:

            - layer value sequence
              0 -> 0 -> 0
              0,1 -> 0 + 1 -> 0
              1 -> 1 -> 1

            - operation value sequence:
              0   -> 0 * 1         -> 0 -> 0 * 1  -> 0
              0,1 -> 0 * 1 + 1 * 1 -> 1 -> 0 * -2 -> 0
              1   -> 1 * 1         -> 1 -> 1 * 1  -> 1

            - linear function requirement added by this input-output map (different inputs (0,1) equal an output of 1)
              - 0 + 0 + 1 = 1


        - for inputs (1,0), the inputs, thresholds, non-zero values (indicated by asterisk), & weights looks like this:
            1 -2  1
          (1)* (2) (1)
            1  1  1
            (1)* (0)
        
          - final total:  y = 1 + 0 + 0      y = 1

          - for inputs (1,0), the trajectory of value sequences on each layer looks like this:

               1   0   0
              /    |    \
             1   1 + 0   0
             \    /\    /
              1  1  0  0

          - for these inputs (1,0), the trajectory of value sequences after each operation looks like this:

                   1
               1   0   0
          1*1     0*-2     0*1
   (1 if x=1)  (0 if x<2)  (0 if x<1)
           1       1       0
           1     1 + 0     0
          1*1 (1*1)=(0*1) 0*1
             \    /\    /
              1  1  0  0

          - in sequence format, where the sums of the last values equals the final total:

            - layer value sequence:
              1 -> 1 -> 1
              1,0 -> 1 + 0 -> 0
              0 -> 0 -> 0

            - operation value sequence:
              1   -> 1 * 1         -> 1 -> 1 * 1  -> 1
              1,0 -> 1 * 1 + 0 * 1 -> 1 -> 0 * -2 -> 0
              0   -> 0 * 1         -> 0 -> 0 * 1  -> 0

            - linear function requirement added by this input-output map (different inputs (1,0) equal an output of 1)
              - 1 + 0 + 0 = 1


        - for inputs (1,1), the inputs, thresholds, non-zero values (indicated by asterisk), & weights looks like this:
            1 -2  1
          (1)* (2)* (1)*
            1  1  1
            (1)* (1)*

          - final total:  y = 1 + -2 + 1      y = 

          - for these inputs (1,1), the trajectory of value sequences on each layer looks like this:
               1   1   1
              /    |    \
             1   1 + 1   1
             \    /\    /
              1  1  1  1

          - for these inputs (1,1), the trajectory of value sequences after each operation looks like this:
                   1
               1  -2   1
          1*1     1*-2     1*1
   (1 if x=1)  (2 if x=2)  (1 if x=1)
           1       2       1
           1     1 + 1     1
          1*1 (1*1)=(1*1) 1*1
             \    /\    /
              1  1  1  1

          - in sequence format, where the sums of the last values equals the final total:

            - layer value sequence:
              1 -> 1 * 1 -> 1
              1,1 -> 1 * 1 + 1 * 1 -> -2
              1 -> 1 * 1 -> 1

            - operation value sequence:
              1   -> 1 * 1         -> 1 -> 1 * 1  -> 1
              1,1 -> 1 * 1 + 1 * 1 -> 2 -> 1 * -2 -> -2   
              1   -> 1 * 1         -> 1 -> 1 * 1  -> 1

            - linear function requirement added by this input-output map (equivalent inputs (1,1) equal an output of zero)
              - 1 + -2 + 1 = 0


          - initially, the program converts the two inputs x1 and x2 into three values: 
            - x1, a combination of x1 and x2, and x2

          - using one sequence that isolates each input, and one sequence that combines the different inputs using a sum, & applying weights at each layer to scale/change values, we convert the initial two values into three values (the first weights applied to inputs & input combinations), then another three values (applying the threshold function), then another three values (applying the second set of weights), then sums those three values to create one value

          - the system of linear equations that needs to be fulfilled according to this configuration is:

          - interim-final layer (sum of threshold outputs = final output)
            0 +  0 + 0 = 0
            0 +  0 + 1 = 1
            1 +  0 + 0 = 1
            1 + -2 + 1 = 0

          - interim-threshold operation (threshold applied to input weight sum = threshold output), with the successful condition
            (0 if input 0 < 1) + (0 if input 0 < 2) + (0 if input 0 < 1) = 0
            (0 if input 0 < 1) + (0 if input 0 < 2) + (1 if input 1 = 1) = 1
            (1 if input 1 = 1) + (0 if input 0 < 2) + (0 if input 0 < 1) = 1
            (1 if input 1 = 1) + (2 if input 2 = 2) + (1 if input 1 = 1) = 2

          - initial-interim layer (input weight sum = input weight sum)
            0*1 + (0*1 + 0*1) + 0*1 = 0 + (0) + 0
            0*1 + (0*1 + 1*1) + 1*1 = 0 + (1) + 1
            1*1 + (1*1 + 0*1) + 0*1 = 1 + (1) + 0
            1*1 + (1*1 + 1*1) + 1*1 = 1 + (2) + 1

            [0,0] -> [0*1,(0*1 + 0*1),0*1] -> [0,(0+0),0] -> [0,0,0] -> [0*1,0*-2,0*1] -> [0,0,0]  -> [0]
            [0,1] -> [0*1,(0*1 + 1*1),1*1] -> [0,(0+1),1] -> [0,0,1] -> [0*1,0*-2,1*1] -> [0,0,1]  -> [1]
            [1,0] -> [1*1,(1*1 + 0*1),0*1] -> [1,(1+0),0] -> [1,0,0] -> [1*1,0*-2,0*1] -> [1,0,0]  -> [1]
            [1,1] -> [1*1,(1*1 + 1*1),1*1] -> [1,(1+1),1] -> [1,2,1] -> [1*1,1*-2,1*1] -> [1,-2,1] -> [0]

          - the matrix operations need to produce the following matrix sequences:
            [0,0] -> [0,0,0] -> [0,0,0]  -> [0]
            [0,1] -> [0,0,1] -> [0,0,1]  -> [1]
            [1,0] -> [1,0,0] -> [1,0,0]  -> [1]
            [1,1] -> [1,2,1] -> [1,-2,1] -> [0]
            
          - so you can derive operations that would produce these sequences, once you identify this sequence of matrixes are useful for connecting inputs/outputs
          
          - or you can apply weighted sum operations to combinations of inputs & thresholds to get adjacent transforms of inputs, and see if those adjacent transforms can be connected to outputs using similar or the same operations, with a particular set of weights & deactivating threshold functions you would derive

            [0,0] -> weights applied to combinations of (0,0) according to a routing function -> sum of adjacent weighted inputs -> deactivating function that maps some of the weighted input sums to zero, according to some input threshold value -> weighted outputs of deactivating function -> sum of weighted outputs of deactivating function -> [0]
            [0,1] -> weights applied to combinations of (0,1) according to a routing function -> sum of adjacent weighted inputs -> deactivating function that maps some of the weighted input sums to zero, according to some input threshold value -> weighted outputs of deactivating function -> sum of weighted outputs of deactivating function -> [1]
            [1,0] -> weights applied to combinations of (1,0) according to a routing function -> sum of adjacent weighted inputs -> deactivating function that maps some of the weighted input sums to zero, according to some input threshold value -> weighted outputs of deactivating function -> sum of weighted outputs of deactivating function -> [1]
            [1,1] -> weights applied to combinations of (1,1) according to a routing function -> sum of adjacent weighted inputs -> deactivating function that maps some of the weighted input sums to zero, according to some input threshold value -> weighted outputs of deactivating function -> sum of weighted outputs of deactivating function -> [0]
            
            where the weights, threshold values, routing function, & deactivating functions would be consistent across each of the sequences above so the same network configuration can be applied to each of them

          - these summed values are the output of the interim layer (a weight applied to a filtering threshold, applied to the weighted output of the first layer (a weighted combination of inputs (which might include only one input))), and the value the sums equal is the required output according to the function definition

          - using matrix multiplication, we can derive various sequences of matrix transforms that would connect a 2-dimensional input like (1,1) into a 1-dimensional output like [0] for each of the input-output requirements

          - these matrix sequences can then be filtered by which sequences can be created with a weighted input sum according to an input routing function (route an output to all nodes on the next layer, or just adjacent nodes, or some other routing function), & a threshold function to convert some weighted input sums to zero

          - threshold functions are useful for transforming a value into another value that is required for the other parameters to be able to connect the inputs/outputs (in this case, transforming inputs into 1/0 values is useful for connecting inputs/outputs)

      - this indicates why three nodes can be used to map four possible input states to two possible output states
        
        - there are two ways to get to 0, and two ways to get to 1, just like in the mapping from four possible input states to two possible output states
        
        - the sum for each of the four possible input states (sums being the input to the activation thresholds in the interim layer) indicates three possible sums (0, 1, and 2)
        
        - assigning a weight of 1 to each of the two different-allowing sums (1 reached in two different ways, by 0 + 1 and 1 + 0) and a weight of -2 to the one non-zero equivalence-allowing sum (2 reached in one way, by 1 + 1) 
          - where an input of (0,0) would produce an output of zero because zero is output if thresholds are not reached and zero doesnt reach any threshold
          - allows the 1 in each (0,1) or (1,0) pair to retain its value and produce a 1 by following a single route in the network
          - allows the -2 output by middle node applied to the (1,1) input, offsets the 1 & 1 produced by the other outputs
