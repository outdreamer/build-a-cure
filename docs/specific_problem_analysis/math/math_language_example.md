# problem-solving automation example with math proof 

## math-language conversion example 
	
	- original proof, with problem-solution connecting formats
		- definition of variable
			x = 0.999 (continuing digits to infinity)
		- definition of variable, distorted to be more adjacent to solution output format of 'integer' (numbers having factor of 1)
			10x = 9.999
		- definition of variable, distorted by core operation to make one side more adjacent to solution output format of 'integer', without decreasing the other side's adjacence to integers
			10x - x = 9.999 - .999
		- definition of variable, standardized to integers
			9x = 9
		- definition of variable, standardized to unit coefficient of variable (1 * x)
			x = 1

	- format both sides with coefficients
		1 * x = 0.999 * 1
		10 * x = 9.999 * 1
		(10 - 1) * x = (9.999 - .999) * 1
		9 * x = 9 * 1
		x = 1

	- format both sides with variable a as coefficient in place of 1
		1 * x = 0.999 * a
		10 * x = 9.999 * a
		(10 - 1) * x = (9.999 - .999) * a
		9 * x = 9 * a
		x = a

	- format both sides with equivalent integer coefficients
		1 * x = 0.999 * a
		(1 * 10) * x = (.999 * 10) * a
		(1 * 10 - (1 * 10)/10) * x = (.999 * 10 - (0.999 * 10)/10) * a
		9 * x = 9 * a
		x = a

	- format both sides with language
		coefficient * x = adjacent_coefficient * a
		(coefficient * number giving other side an integer accessible with a fraction subtraction) * x = (adjacent_coefficient * number giving other side an integer accessible with a fraction subtraction) * a
		(coefficient * (number giving other side an integer accessible with a fraction subtraction - the fraction of itself based on this number, to give other side an integer)) * x = (adjacent_coefficient * (number giving other side an integer accessible with a fraction subtraction  - the fraction of itself based on this number)) * a
		integer produced by integerizing number (* 10) and subtracted fraction (/10) * x = integer produced by integerizing number (adjacent_coefficient * 10) and subtracted fraction (9 + adjacent_coefficient)/10 * a
		x = a

## example of problem-solution mapping on various interfaces

	- general insight path: 
		- what operations can you do to b that would produce b on one side and an adjacent operation on 1 (10 - 9) on the other side

	- specific insight path:
		- find a number b (9.999) so that 1/n of itself is equal to the original adjacent_coefficient (0.999) so an adjacent integer (9) divisible by the repeating digit (9) to produce the target integer (1) (after moving one decimal to produce the integer) can be achieved by subtracting the adjacent_coefficient, given that 1/n of b will be the decimal after the integer, where n is a coefficient of the other side of the equation indicating only a multiplication operation has been done (requiring that no change has been done to the number type of the other side, as multiplying 1 by an integer = an integer)
			- b * 1/n = adjacent_coefficient = (b - adjacent_coefficient) * 1/n * (infinite sequence of 1/(10 ^ 0), 1/(10 ^ 1), 1/(10 ^ 2) ...)
			- 9.999 * 1/10 = 0.999 = (9.999 - 0.999) * 1/10 * (infinite sequence)
		- find a number b & n so that 1/n of itself (b/n) is equal to the original repeating decimal (adjacent_coefficient) so an adjacent integer divisible by the repeating digit x in adjacent_coefficient to produce the target integer can be produced by subtracting the adjacent_coefficient from b
			- b/n = 0.xxxxx = adjacent_coefficient
			- b - adjacent_coefficient = (n - 1)/b

	- apply specific insights

		- apply the insight:
			- 'to determine if two values are equal, find a relationship using one value (10 - 9 = 1) and substitute the other value (10 - 9 = 0.999) to see if other operations produce the same output with the substituted alternate equal value'
				- find a number y (10) with an integer difference equal to the posited equal value of 0.999 (1) between x & the original adjacent_coefficient, once adjacent_coefficient is standardized to an integer (9), so that the integer difference of 1 can be used to equal the subtracted adjacent_coefficient (0.999)
					y - 9 = 1
					y - (9.999 - 0.999) = 1
					y = (9.999 - 0.999) + 1 = 10
				- we aim for 10 bc its one theorem value away (1) from an adjacent integer of the other supposedly equivalent value in the theorem (0.999)
					- so if 1 = 0.999, then the substitute equivalent value also holds (10 - 9 = 0.999), which we can adjacently check

		- apply the insight: 
			- 'find common base & standardize to compare objects'
				- standardize to the common base as the infinite series (10)
							1 = 10 - 9 = 10 - (10 * 0.999 - 0.999) = 0.999
					        1 = 10 - 0.999(10 - 1) 
					        1 = 10 - (0.999 * 10) + 0.999
						   -9 = 0.999 - (0.999 * 10)
							9 = 0.999 * 10 - 0.999 
							  = 0.999 (10 - 1)
							  = 0.999 (9)
							1 = 0.999
				- the key is that ((10 * 0.999) - 0.999) is an adjacent way to get to a non-1 integer from 0.999 
					- we dont want to find an adjacent route to the integer of 1, using operations like adding (1 - 0.999) to 0.999 to get 1, which 
						- ignores the theorem to prove and uses an equivalence achieved by addition/subtraction that doesnt use external information to the theorem
						- assumes the theorem is irrelevant, otherwise using 1 - 0.999 would be pointless if the theorem is true (if 1 = 0.999, then 1 - 0.999 = 0, and subtracting zero is pointless here & assumes the theorem is false, otherwise there would be no need to subtract anything to get from 1 to 0.999 bc theyre equal)
					- we want to get from 0.999 to 1 by a circuitous route that uses operations other than adding/subtracting zero, just to prove that other operations dont change the fact of the theorem but rather confirm it by the fact that their attributes & relationship functions hold to the extent that they can be used as a foundation of the theorem

	- apply intent interface (problem metadata including sub-problems with metadata like 'intent' and 'functions') & the solution automation workflow insight path 'break problem into sub-problems & merge sub-solutions'

		- apply insight to generate query on intent interface 'if two objects are equal, their components are also equal'
				- components
					- functions
						- connecting functions
							- a = object1.function * b (connects a and b using object1 function)
							- output a should be produced by applying object1.function to b
								- the same should hold for object2 - you should be able to produce the same outputs using the same inputs, with the other object's corresponding function
									- a = object2.function * b (connects a and b using object2 function)

		- apply general query on intent interface 'connect a & b, once indexed by intent for comparison':
			- intent: equalize objects:
				- intent: compare
					- intent: standardize to common core structures
						- base
						- coefficients
						- number types
				- intent: connect once comparable (standardized)
					- intent: find adjacent operations producing route from source to target value
						- intent: filter adjacent operations by restrictions
					- intent: substitute source with target value (or vice versa in another relationship) to highlight equivalent properties of source/target values
						- output: value produced by adding a-difference (1) between integerized value (9) from b (0.999) where the other side equals b

		- apply general query to specific problem 'connect 0.999 and 1, once indexed by intent for comparison'
			- equalizing intent
				- comparison intent
						- standardize (reduce difference)
							- base
								- each repeating digit is an element with the same numerator coefficient in an infinite sequence of formula 9/(10^n), so 10 is a relevant number by default
									0.999 = 9 * [1/(10 ^ 1) + 1/(10 ^ 2) + 1/(10 ^ 3) ...]
									0.999 * 10 = 9 * [1/(10 ^ 0) + 1/(10 ^ 1) + 1/(10 ^ 2) ...] = 
											   = 9 * 1/(10 ^ 0) + [1/(10 ^ 1) + 1/(10 ^ 2) + 1/(10 ^ 3) ...]
											   = 9 + [1/(10 ^ 1) + 1/(10 ^ 2) + 1/(10 ^ 3) ...]
								    9.999      = 9 + [1/(10 ^ 1) + 1/(10 ^ 2) + 1/(10 ^ 3) ...]
								    0.999      = [1/(10 ^ 1) + 1/(10 ^ 2) + 1/(10 ^ 3) ...]
							- coefficients
								- of infinite series: the repetition of the numerator indicates a value that can be extracted as a coefficient of the series, so the numerator can be standardized to 1
								- for coefficient value difference reduction intent, for comparison intent
							- number types for value difference reduction intent, for comparison intent
								- dont use division to change values, unless the output is an integer to keep values in integer number type (as target value to achieve from source value 0.999 is an integer, 1)
						- isolate variables on either side (after optionally framing 1 as variable a)
				- connect comparable values once standardized
						- find adjacent operations producing target number type or value
							- producing an integer 9 on the x side is adjacent with multiplication, and doesnt involve a number type change to the other side with either multiplication or subtraction, just a scalar change, which keeps it as an integer
							- producing an integer 9 on the x side is adjacent with multiplication & subtraction, and does involve a number type change at the subtraction operation
						- filter adjacent operations by restrictions
							- dont use division or operations that change to a decimal rather than an integer

		- alternate query on intent interface
			- intent: show that 0.999 and 1 are equal
				- sub-intent: equalize coefficient of x and coefficient of 1 (a)
					- sub-intent: equalize one side with integer (9)
						- sub-intent: show coefficients of both sides
						- sub-intent: find coefficient (10) that will equalize the side with repeating digits to an integer + original quantity with repeating digit (0.999)
							- this has to be a number (10) that will produce an integer (9) from the fraction 0.999, after a subtraction of itself (- 0.999), by moving the decimal one place
						- sub-intent: equalize both sides to an integer (subtract 0.999)
							- sub-intent: find x value in remaining formula (9x = 9)