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

    - how do you figure out that (0, 1, 1, 2) is a useful output of the interim layer to combine with a mapping/filtering function that can assign 'false', 'true', 'true', 'false' to those outputs, thereby implementing the xor function?
      - you can derive increasingly specific requirements of the function as mentioned below, then find a combination of weights/nodes/thresholds that fulfills the most specific requirements you can derive
      - you can also derive the structure of the function & their interactions as mentioned below, then find variables that fulfill the structural interactions
    
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

              x = 0             x = 0
            1 -2  1
          (1) (2) (1)      
            1  1  1
            (0) (0)

              x = 1             x = 1
            1 -2  1
          (1) (2) (1)*
            1  1  1
            (0) (1)*

              x = 1             x = 1
            1 -2  1
          (1)* (2) (1)
            1  1  1
            (1)* (0)

              x = 1 + -2 + 1    x = 0
            1 -2  1
          (1)* (2)* (1)*
            1  1  1
            (1)* (1)*

      - this indicates why three nodes are required to map four possible input states to two possible output states
        
        - there are two ways to get to 0, and two ways to get to 1, just like in the mapping from four possible input states to two possible output states
        
        - the sum for each of the four possible input states (sums being the input to the activation thresholds in the interim layer) indicates three possible sums (0, 1, and 2)
        
        - assigning a weight of 1 to each of the two different-allowing sums (1 reached in two different ways, by 0 + 1 and 1 + 0) and a weight of -2 to the one non-zero equivalence-allowing sum (2 reached in one way, by 1 + 1) 
          - where an input of (0,0) would produce an output of zero because zero is output if thresholds are not reached and zero doesnt reach any threshold
          - allows the 1 in each (0,1) or (1,0) pair to retain its value and produce a 1 by following a single route in the network
          - allows the -2 output by middle node applied to the (1,1) input, offsets the 1 & 1 produced by the other outputs

      - how to derive this network

        - identify increasingly specific requirements & find variables that fulfill those requirements

          - this network can be derived by the following 'requirement' structures:

            - basic input/output requirements
              - possible inputs (0,1) and (1,0) must have an output of 1
              - possible inputs (0,0) and (1,1) must have an output of 0

            - basic function requirements
              - the output must be zero for inputs (1,1) and (0,0)
                - output of interim nodes allowing sum of 2 from (1,1) must be offset by output of interim nodes allowing sum of (1) from (1,1) (there must be two nodes allowing the sum of 1 from the input (1,1) to offset the -2 from the node allowing sum of (1,1) to output a 1 value (which is then multiplied by the -2))
                - output of all interim nodes allowing sum of 0 from (0,0) must always be equal to zero

              - the output must be one for inputs (0,1) and (1,0)
                - output of interim nodes allowing sum of 1 from (1,0) must be equal to one and there must be only zero outputs of other interim nodes
                - output of interim nodes allowing sum of 1 from (0,1) must be equal to one and there must be only zero outputs of other interim nodes

            - from the basic input/output requirements, we've derived the requirements for the functions connecting them
              - there are other requirements that could connect the inputs/outputs (fulfill input/output requirements), but this is a way that requires minimal nodes
              - now we know what the outputs of the interim layer should be
              - the other variables include options like:
                - how layers are connected (fully connected, or just adjacent nodes, or another way)
                - how many nodes are in the interim layer (how many weight combinations of activated nodes produce the outputs) & their weights to produce the correct outputs
                - whether other layers can be added to reduce/relocate other operations to add value for another metric

        - identify structural interactions & variables that fulfill those interactions

          - given that:
            - the nodes only interact with two adjacent nodes on the interim layer
            - weights are summed in each interim layer node
            - inputs have four possible states, of which there are two meanings (true/false)
            - sums produce three different values given the two-adjacent node interaction

          - what other variable values can combine to produce the input/output mapping:
            - what second weight set & interim layer node count combinations could produce the final conversion between sums & true/false outputs, given that the other interactions like sums & two-adjacent node interactions are already defined?
            - can the weights applied to the initial input layer (first set of weights) be changed to optimize the other parameters?
            - what other adjacent node interaction types (like fully connected layers, as opposed to two-adjacent-node interactions) would combine with weight & interim layer node count & interim layer count variable values to produce the same input/output mapping as the xor function?
