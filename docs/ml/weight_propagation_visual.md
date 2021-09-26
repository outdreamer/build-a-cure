- why is a change in weights able to update the neural network in such a way that the resulting prediction function it represents is more accurate?
	- bc the neural network is essentially performing the corresponding operation to an 'average' operation where some inputs are weighted
	- similar to how multiple inputs of the individual networks in an ensemble network are weighted to change the impact of their contribution on the final score, the multiple components of the neural network can be weighted to produce a prediction function that is more accurate bc of the weight update

	- what are these 'multiple components'?
		- the weights are associated with multiple connections between node/threshold/activation units on one layer & node/threshold/activation units on the next layer, according to the routing/propagation function that determines which inputs are forwarded to which nodes on the next layer
		- so each weight can be said to be applied to either:
			- a node/threshold/activation unit's inputs from connected node/threshold/activation units
			- a node/threshold/activation unit's outputs
		- the set of weights creates changes to apply to the outputs of a layer's nodes
			- these changes differ by which node the output is being routed to
		- so a differently weighted variant of the previous layer's nodes' outputs is sent to each node in the next layer (in a fully connected network)
		- these differently weighted variants of the previous layer's nodes' outputs are the core unit structure that a weight is applied to
		- but the next (third) layer in the layer sequence has different inputs bc of these weights 
			- weight1 * activation (differently weighted inputs variant 1 of the previous layer's nodes' outputs) + weight2 * activation(differently weighted inputs variant 2 of the previous layer's nodes' outputs) + ...
		- a node in the next layer has a 'weighted inputs variant' of 'weighted inputs variants', rather than a 'weighted inputs variant'
			- weight x01 * activation(differently weighted inputs variant 1 propagated to previous node 1) + weight x02 * activation(differently weighted inputs variant 2 propagated to previous node 2) +  ... 

		- if you extend this to the final layer where outputs of a layer are pooled or otherwise aggregated/selected, further iterations are wrapped around the initial layers' outputs:
			weight y1 * (weight x01 * activation(differently weighted inputs variant 1A propagated to previous node 1) + weight x02 * activation(differently weighted inputs variant 2A propagated to previous node 2) +  ...) + 
			weight y2 * (weight x11 * activation(differently weighted inputs variant 1B propagated to previous node 1) + weight x12 * activation(differently weighted inputs variant 2B propagated to previous node 2) +  ... ) 


									operations						    description


layer4	2 *  1(1x + 3y) + 			4 *  1(1x + 3y) + 
input	   	 2(2x + 2y + 2z) +			 2(2x + 2y + 2z) +

	    1 *  5(1x + 3y) + 			3 *  5(1x + 3y) + 			5 *  5(1x + 3y) + 
			 3(2x + 2y + 2z) + 			 3(2x + 2y + 2z) +			 3(2x + 2y + 2z) +
			 6(3y + 1z)				 	 6(3y + 1z) + 				 6(3y + 1z) + 

			 						9 *  4(2x + 2y + 2z) + 		6 *  4(2x + 2y + 2z) + 
			 							 y(3y + 1z)					 y(3y + 1z)



weights3		 2 4         	      		1 3 5        		   		9 6
																			

																					layer 3 inputs are:
																						- differently weighted sums of different layer 2 outputs
																						- these could also be called:
																							- differently weighted sums of (differently weighted sums of original inputs)
																							- 'summed weight variants of summed weight variants of layer 1 outputs'

																					- differently weighted input variant sum (differently weighted input variant sum 1x + 3y) + (differently weighted input variant sum 2x + 2y + 2z)

layer3	      1(1x + 3y) + 	   		 	 5(1x + 3y) +						    
input		  2(2x + 2y + 2z)     		 3(2x + 2y + 2z)     		 4(2x + 2y + 2z)
							       		 6(3y + 1z)		   			 7(3y + 1z)

weights2		 1 5         	      		2 3 4        				6 7

																					- layer 2 inputs are:
																						- differently weighted sums of original inputs
																							- where coefficient of some terms is zero if its a fully connected network, meaning:
																								(1x + 3y) = (1x + 3y + 0z)
																						- these could also be called 'summed weight variants of layer 1 outputs'
																						
																					- differently weighted input sum (1x + 3y) varies on weights compared to differently weighted input sum (2x + 2y + 2z) and differently weighted input sum (3y + 1z)

layer2	       (1x + 3y)   	 		    (2x + 2y + 2z)    	  	 	  (3y + 1z)	    
input

weights1		 1 2       		  			3 2 3         				2 1

layer1			  x        		    	 	  y           				 z
feature 
outputs


- another visual example with weight routing for a network like this:
	e f g h
	a b c d 
	x y z


- would be:

	e 											   f 										   g 											  h
	|         \       \          \		/          |       \          \		/         /        |         \		/          /       /          |
	a          b 	   c          d 	a          b 	   c          d 	a          b 	   c          d 	a          b 	   c          d
	| \ \     /|\     /|\     / / |     | \ \     /|\     /|\     / / |     | \ \     /|\     /|\     / / |     | \ \     /|\     /|\     / / |
	x  y z   x y z   x y z   x y  z 	x  y z   x y z   x y z   x y  z 	x  y z   x y z   x y z   x y  z 	x  y z   x y z   x y z   x y  z

	     x         y        z 			     x         y        z 				 x         y        z   			 x         y        z

- so you can see how the weights differ across the combinations of weight variants, and each layer adds another layer of recursion, where it's applying another 'sum of weights' operation on 'input combination variants'
- in the diagram above, (1x + 3y) is a weight variant, and (2x + 2y + 2z) ia a weight variant, etc
- this is why you might call the inputs to each node a 'tree of trees'


- so we get 'emergent weights' resulting from these iterations of a 'weighted sum of inputs' operation

- in the above diagram for the first node on layer 4, we have the resulting weighted sum:
	2 *  1(1x + 3y) + 			
	   	 2(2x + 2y + 2z) +			 
	1 *  5(1x + 3y) + 			
		 3(2x + 2y + 2z) + 			 
		 6(3y + 1z)	

	- which reduces to: 
		10x + 14y + 8z

	- where the previous layer3 sum for the first node would be: 
		 5x + 7y + 4z

	- and where the previous layer2 sum for the first node would be:
		 1x + 3y + 0z

- the second node on layer 4 would reduce to a differently weighted sum of the original inputs, etc

- so multiple options of 'differently weighted sums of original inputs' are being presented to the final pooling/selection layer
- the pooling/selection layer chooses between different alternate functions produced by:
	- 'different weight trees'
	- 'recursive differently weighted input sums'
	- 'differently weighted sums of (differently weighted sums of (differently weighted sums of original inputs))'

