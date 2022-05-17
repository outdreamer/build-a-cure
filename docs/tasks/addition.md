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
		- variables like 'sequence', 'position', and 'adjacent position values' are relevant variables to addition
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

	- what operations cant be handled by a network?
		- circular loops (embedded input/output feedback loops within a network iteration)