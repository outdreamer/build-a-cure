- description of learning operations like 'addition' using neural networks ('patterns of differences to create correlations') vs. interface structures ('requirements', 'similarities', 'patterns', 'units', 'sequences', 'repetitions', 'replacements')

	- addition requirements
		- the function to generate whatever differences accurately describe the differences between input added numbers and output number resulting from addition

	- addition variables
		- number of digits
		- identity of digits

	- if AI can learn a pattern of differences, it can learn to generate a few difference types based on the patterns of differences it sees during training
		- these difference types might include operations like:
			- 'add 50', 'add 100', 'combine digits in the same position', 'move extra value to next digit in sequence as another value to be added'

	- the over-specificity or over-generalization tendencies of AI might create a situation where differences are applied where they shouldnt be 
		- example of suboptimal differences a network might learn:
			- 'move a value two digits over and add it there instead'

	- default addition operations include:
		- add values in equivalent positions
		- if their combined value cant be stored in that position (greater than 9), keep the rightmost value (2 in a result of 12) resulting from that operation in that position and add the leftmost value (1 in a result of 12) to the next left digit in the sequence

	- other operations that might be learned other than default addition operations
		- test if the likely result of an addition will probably be higher than 9

	- insights that a network could identify which are basic & required to create the accurate/complete operation of addition
		- variables like 'sequence', 'position', 'combine (add, as in combine without overlap or dimension change)', and 'adjacent position values' are relevant variables to addition
		- functions like 'add extra value of previous operation to next left digit, in addition to existing values in that digit position' are also required for addition

	- insights that a network could identify which are useful to create the accurate/complete operation of addition
		- variables like potential value (what values each digit can store), meaning of each digit (the tens digit has different meaning than the ones digit, it represents 'ten of whatever is in that digit' so it can store more value than the ones digit) are also relevant/useful to create the addition operation
		- these are useful for times when the 'basic required operations/variables' arent inferred by a network trained to learn addition, to limit irrelevant/meaningless/useless patterns a network might learn if it doesnt learn those basic required operations/variables
		- the 'relevance' of 'similar positions (digits)', the 'sequence and sequential direction of the addition operations' and the "value limit of -1 and 10 on each digit's value (a number higher than 9 cant be embedded in one position, each digit can only hold one integer between 0 and 9 and cant be negative" are interface structures that can adjacently generate addition
		- focusing on 'changes to the ones and tens digit' in training examples is the most useful structure to focus on when learning addition, as its the core unit input/output example which could most adjacently produce learning the operation
		- learning a 'repetition with replacement', as in 'repeating the learned ones/tens operation' but 'applying it to the next item in the sequence' (tens and hundreds digits) by replacing the inputs/outputs is another operation that networks could identify that would more adjacently produce addition
			- this can be learned by keeping the 'difference created by the operation' (repeating the operation on 'adjacent digits') but changing the input/output (repeat the operation on the 'next digit in the sequence to get the second next digit in the sequence'), by adjacently applying interface structures like 'differences', 'adjacencies', 'sequences', and 'input/output' structures
		- learning an association between non-adjacent digits before learning the association between adjacent digits is possible bc non-adjacent digits can influence each other (if a sequence like '999' occurs, the rightmost nine influences the value of the leftmost digit bc its so high)
		- learning that 'higher digits have more impact on more non-adjacent digits' is another insight that a network can use to adjacently derive addition
		- 'having another variable to store side effects' (like extra values above 9) is another useful structure a network can use to adjacently derive addition
		- identifying that the 'extra value should subtract the resulting rightmost digit (whatever value is stored in the original digit should be left there) rather than carrying the whole value to the next digit' is another required structure to use in adjacently deriving addition
		- a network would likely be confused by adding numbers that cancel each other out, like negative and positive numbers with equal value, unless it had already identified the required operations/variables for addition
		- these confusing examples are likely to produce incorrect learned patterns unless theyre introduced after the less confusing examples when the requirements are likely to be already learned, as the core operation of addition is simple but being able to learn subtraction (adding a negative number to a positive number)
			- this is the operation of 'finding the input to addition with the opposite of the negative number that could create the original inputs', as in '-1 + 4' is equal to 'find x that could be added to 1, the opposite of the negative number (-1), that could create 4', which both have '3' as an answer, thereby converting the operation of '-1 + 4' into an addition operation of 'x + 1 = 4' which is likelier to be possibly answered by the network, if its trained with random regularization leaving out some inputs in some examples
			- finding the connection between '-1 + 4 = x' (or '4 - 1' = x) (formatted as an addition of differently signed values, requiring learning subtraction) and 'x + 1 = 4' (formatted as an addition of positive values, requiring learning addition) is useful in cases where the operation can be converted into an addition operation of positive values and where inputs have been regularized to handle the problem of 'input inference', as opposed to learning what the '-' symbol means, which is an alternative option for the network to learn
			- learning this requires applying an adjacent change to switch the position of 4 from an input (number being added) to be an output (result of addition), since the value of -1 can be interpreted as 'distance from the other number being added (4)', as the answer is 'one integer (unit) away in the negative direction' (3)
			- learning that values being added represent 'distances on a number line' where positive/negative signs represent 'direction of distance' is another useful structure for the network to learn, even if it doesnt help with learning addition operations in other number spaces

	- rather than asking a network to learn every possible input/output difference or difference type in addition (which would just be a list of all numbers that can be added), using interface structures such as 'sequences', 'side effects', and 'adjacencies' to connect input/output values is more useful
		- an interesting question for a network to try to solve is 'what numbers cant be added' and see if it can generate other number types that cant be added by identifying and removing properties of numbers that can be added

	- what operations cant be handled by a network?
		- circular loops (embedded input/output feedback loops within a network iteration)