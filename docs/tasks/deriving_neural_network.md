- how to generate existing solutions for the 'find a prediction function' problem

	- to connect the default structure (one degree of difference to data points) of 'adjacent point connections' and the solution of 'regression':
		- the default structure on a graph of data points is 'connections between adjacent points'
			- apply core functions like 'compare'
				- to implement 'compare', its necessary to standardize comparisons of these connecting lines between adjacent points, you would 'align' them vertically or horizontally
				- once they are aligned vertically, there would be a clear trend connecting the 'common' area crossed by the lines
				- the concept of 'average' would be derived by finding the most 'common' points across all the adjacent-point connecting lines
		- this gives a 'standard' solution of a constant-sloped line to predict data points
			- this standard solution is sub-optimal when the variation about the average is high, where the average represented by the regression line will be highly inaccurate for most values
	
  - to get to the 'regression' solution to the 'find a prediction function' problem

		- a set of connected 'subset' lines to better represent 'local averages' would reduce this 'inaccuracy' problem of 'one general average'
		  - the 'extreme' version of this is infinitely many subset lines (forming a curve), which would reduce the 'inaccuracy' problem for a data set
		    - so now we know we need non-linearity in the prediction function
			
    - an interface query for structures that could produce non-linearity in the prediction function:
				- start with a unit problem, like solving a way to map inputs/outputs of a known unit function, for example XOR
					- the standard solution is one of the following:
						- 'sum the two inputs and if its even, output 0, otherwise output 1'
							- [0,0, 0,1, 1,0, 1,1] -> [0, 1, 1, 2] -> [0, 1, 1, 0]
						- 'find the difference between the two inputs, and output the difference'
							- [0,0, 0,1, 1,0, 1,1] -> [0, 1, 1, 0] -> [0, 1, 1, 0]
					- these represent the state sequence between input -> interim state -> output of these functions
					- the prediction function should be able to connect each input/output example, like:
						- [0,0] -> [0] -> [0]
						- [0,0] -> [0 + 0] -> [0] -> if 0 = 0, output 0 -> [0]
					- we know that simple functions like the XOR arent enough to represent a curved line, we need other operations to connect these data points in a curved line

					- how would you represent these state changes for each input/output example in another way, given that we know existing operations arent enough to connect them?
						- other structures include thresholds (activations) & coefficients (multiplication)
							- a function using a threshold outputs a value with no impact on future operations (0) if the input is below/above a certain threshold value, 'deactivating' it
							- a coefficient multiplier scales values, changing their value, but not their data type or format, and not changing them to zero (relevant to threshold functions) if coefficients are non-zero
						- can thresholds & coefficients be used to represent the function another way?
							- can thresholds be used to change a value to zero, when coefficients cant be used to do so
							- can coefficients be applied in a consistent way that scales values in a way to trigger thresholds in a useful way
							- apply an adjacent change:
								- if you change the 'variable count' attribute by 'adding a variable' using sums/weights, is the resulting set of values capable of being transformed in a way that results in the required outputs for all inputs
							- can the 'adjacent changed state' be connected to the output state
								- can you multiply the 'augmented inputs' vector by a coefficient vector to create the outputs for all inputs?
									- mapping 2 inputs to 3 interim values to one output value (as in the XOR function example implemented with a multi-layer perceptron) offers a way to convert the problem of 'find a structure to add nonlinearity to a summarizing/predicting line of a set of input/outputs' into 'find coefficients for this vector of 1/0 values that would produce 0 or 1 as needed, given the inputs associated with each vector of 1/0 values'
										- the solution in that example is the coefficients [1, -2, 1] for that configuration of network parameters, including weights/node layers/numbers/connectedness/thresholds
									- the vector of 1/0 values represents an interim state of the inputs after initial weights/sums/thresholds have been applied, but for now we're just solving for the connection function between the next-to-last state (vector of 1/0 values) and the last state (output of 1/0), specifically the coefficients of that connection function
									- the initial connection function between inputs and the interim state vector can be solved for first or second, to apply unit/adjacent weights as coefficients & available operations like sums to find the possible unit/adjacent interim states
										- 'what are the unit/adjacent coefficients/constants & operations that could convert inputs into an interim vector of 1/0 values that could be mapped to one dimension (0/1 value) as needed'
									- this converted problem can be implemented for many combinations of parameters & sample inputs/outputs of the data set
										- 'what are the coefficients that could turn this vector of 1/0 values into the outputs as needed, given the inputs associated with the vector & the threshold function'
									- next or alternatively, the integration of the input-interim and interim-output connection functions:
										- 'what are the coefficients & thresholds that could convert the 2 inputs of 1/0 values into 3 interim 1/0 values and 1 output 1/0 value, given how those two pairs of values (input-interim, interim-output) can be connected'
									- the solution of two vectors of weights/coefficients & sums applied to inputs is different from the standard representation of the XOR function, which finds the difference between the two inputs and outputs 1/0 according to whether the difference is 0 or 1 (which in ml would be called 'data pre-processing', by using the 'difference between inputs' as the input, instead of the original inputs)
					
					- other interface queries could have asked questions like:
						- 'what structure aligns with the non-linear prediction function structure of incremental state changes between input (constant regression line) and output (curved line)'
						- 'what structure aligns with the state sequence converting a term of (constant multiplier * x) into a term of (x ^ exponent)'
						- these queries would have produced other structures aligning with state sequences, like vector operations applied to vector sequences (used for solving for systems of linear equations)
							- noting how similar solutions are to the target value without removing any terms, they might come up with the 'threshold' structure by applying the structure interface to apply an 'adjacent operation' of 'removing' the terms preventing the solution from being reached, and a way to tell which values to remove (threshold function mapping deactivated values to zero), that would consistently produce accurate solutions across all inputs/outputs

				- in this way, we could derive the structure of a 'neural network' (or sequences of vector operations applied to create an output vector from an input vector) to solve the problem in a different way
					- with this structure, we have a way to transform inputs into higher-dimension outputs that can be mapped to outputs in another way, using sums/weights
					- how do we apply it to get non-linearity of the prediction function, either from a vector of the original x-values, or the averages represented in the constant regression line?
						- the impact of the network has to be that of operations including an exponent (multiplying the input by itself to some degree)
							- so the 'vector sequence' has to reflect a net change that equals exponential change of some degree
								- now we are asking the question:
									- 'how could sums/weights/deactivations be applied in a sequence to create exponential change applied to the input x' (resulting in y)
									- we can derive this sequence either:
										- starting from combinations of thresholds/weights/sums assigned to different positions in the network & finding combinations that map inputs to outputs
										- connecting adjacent states, then connecting those connections, as indicated above
										- deriving what operations produce exponential change (self multipliers) and mapping those structures to the network operations (what weights/sums/thresholds produce self-multiplication to the required degree)
										- linearly mapping operations known to be adjacent to the target prediction function to combinations of structures like layers or adjacent node/weight paths in the network
										- applying pre-processing to the data so the network can be used to learn weights of input terms of the prediction function polynomial, bc inputs are transformed with exponents & other operations whose structures arent supported by the network
                    - starting from other 'enabling function/structure' & 'requirement' pairs (like a 'required level of accuracy' and an 'approximation function')
                
                - other relevant questions include:
                  - 'why can a network learn a non-linear function', which is the same reason it can learn other function types
                  - 'why apply a neural network instead of a logic function network' (a set of if/then statements, or a set of specific processing functions for each task or a query on a general function network amounting to the same)
                    - the neural network implements the logic in a different format, encoding conditional operations ('if/then') with thresholds/weights, offering alternate nodes for different localized 'if/then' input-output mappings to develop, allowing for incremental change connecting local input-output mappings (local subset functions)
                    - an 'if/then' function network can also be learned by a neural network
                    - bc a neural network can learn complex functions at scale for many inputs & operation types once inputs are formatted correctly
                    - many operations can be represented by the combination of weight/sum/deactivation operations
                  - 'what structures in the network map to structures relevant to the input/output prediction function'
                    - input sums, adjacent network nodes, weight vectors, weight path patterns, & node/operation trees may represent function subsets, local averages, or locally relevant sums/coefficients/operations
                      - in this sense, the neural network may be supporting a customized prediction function for structures of inputs/outputs (like pairs of inputs/outputs), optionally with overlaps in common with other prediction functions
						
						- non-linearity of a function implies the 'combination of many subset functions' and the 'combination of many random variables' and requires 'exponential change types'
						- the difference between coefficient multipliers & integer exponents can be thought of as 'guaranteeing a change type of a particular rate', where coefficients can be less than constant change and exponents (of integer values) reflect greater than constant change
						- 'combining many subset functions' or 'combining incremental state changes' to create a function aligns with the network structure of 'vector state sequences'
						- the structure of 'local averages' can be reflected in the neural network architecture of the sum/weight operation used to find the output value of each node
						- 'multiple routes between the same inputs/outputs' is a structure that is embedded in the 'neural network' structure
							- 'multiple routes between the same input and different outputs' would be useful for predicting functions for structures like circles
						- the corresponding neural network applied to a data set would solve the problem of 'convert this vector of x values into this vector of y values' or 'convert this x value into this y value' or 'convert this x value in this vector that is otherwise zeros into this y vector that is otherwise zeros' (or some variant with non-zero values for adjacent features)
						- first it would create a vector of higher dimension than the input using sums/weights
							- then it would apply thresholds, deactivating some of those interim values (converting them to zero)
								- then the outputs of that deactivation would be multiplied by weights found to generate the y-value for that input x-value
						- why would you 'deactivate' some inputs? bc theyre not relevant to generating the output using available operations (multiplication, sums)
							- if your input is the entire vector of x-values, youd want to deactivate the other x-values that are not relevant to the output y-value for the x-value youre trying to predict (adjacent values could be considered relevant)
							- if your input is the interim vector produced by the thresholds to deactivate some values, youd want to deactivate the values that cant contribute to the output y-value, using coefficients & sums

						- why is non-linearity useful & how is it connected to a neural network structure
							- it provides multiple alternate routes between inputs/outputs, in case an alternate version of an input (like a different position) should produce the same output (like a category label) but requires a different route to do that (compared to another input that should also produce that output)
							- the fact that an exponential (polynomial) function can have incremental continuous change, where an input has very similar output to an adjacent input, is a parallel reason why non-linearity is useful, as a similar input should produce the approximately same output in those cases, where the 'approximate equivalence' of these adjacent outputs of adjacent inputs benefits from multiple routes between inputs & an output value (the opposite is true for adjacent inputs with very different outputs like on a steep part of a curve)
							- in some non-linear curves, very different inputs will produce the same output, like for a curve shaped like a wave (which in these cases is a problem of lack of pre-processing the data, which would reduce the x variable to a term with the interval component removed)
							- the main benefit of non-linear curves is that different change types are allowed in the same function (high change rate & low change rate, as in 'tangent slope')

						- what type of neural network could fit an infinite random sequence to an infinite random sequence (to create a 'randomizing' function)

						- what type of problem would benefit from mapping an input to multiple possible outputs (like 'deriving possible inputs')

						- what is the benefit of the neural network vs. deriving which change types are necessary, which function terms can produce those change types (optionally filtering for maximally different terms with 'spaces having no surprises' or 'determined spaces' connecting them), and applying multiple quick convergence/testing methods to find parameters of the function producing those change types
							- example: for the 'find a prediction function' problem, this could take the form of change types such as:
								- functions that intersect with or have m ratio of error for n points in the data set
								- parabolic functions for functions with a clear complete curve having complexity in the exact parameters of the curve
								- functions connecting a set of 'average' or otherwise 'representative' points in the data set
								- high change rate in one input range and a low change rate in another input range
							- reducing the data points to a 'function range' is trivial
							- finding a 'representation' or 'error/cost-calculation' metric is trivial
							- finding a standard function that fulfills the representation or error/cost calculation metric to some non-trivial degree, is trivial
							- finding parameters that optimize a function across several metrics may be non-trivial

						- how do the various functions in the 'find a prediction function' problem space interact:
							- how does the 'neural network to find a prediction function' structure interact with the 'convergence' structure
								- the neural network is fulfilling the same abstract intent as the convergence structure (to find optimization points), & may use the convergence structure to find points representing weights to optimize its errors
							- how does a 'convergence structure' (like sum of infinite series that converges quickly or an efficient method of gradient descent) interact with a 'test' structure (to quickly determine if a solution prediction function is successful enough to stop searching)
								- a convergence structure can be an alternative to a test structure (to determine solution success, whether contextually or absolutely) when the convergence structure is called by a function with intent to 'find an optimization point of a function' (whether locally or globally)

						- if a neural network has node-threshold-weight or node-threshold-weight path combination units that prevent certain outputs & allow certain inputs, those units may map to various structures on the same space as the function
							- these units may be represented as subset lines acting as boundaries preventing the prediction function from moving in a particular direction as it converges (like a pinball machine has barriers preventing motion in some directions or from reaching some positions)
								- what is the net graph produced by these subset lines corresponding to these units? does it look like a range/area or a 'tangent bundle' structure across various points

