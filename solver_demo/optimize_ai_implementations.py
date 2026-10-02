# Optimize AI implementations

# a script to 'generate changes to AI implementations' and 'filter those combinations, using the definition of relevance/optimality'
# generates ''combinations of insights' (to implement as AI implementations)
# filters those combinations using the definition of relevance/optimality
# specifies the filtered combinations to implement the insights as a new AI implementation

irrelevance_components = ['trivial', 'over-simple', 'incomplete', 'inefficient', 'invalid', 'impossible']
ai_implementations = ['activation function network of weights to identify a polynomial minimizing loss, applying chain rule to identify weights causing loss function changes']
general_optimizations = ['identify/merge similarly relevant structures', 'identify/remove less relevant structures in a set of opposing/contradicting/invalidating structures']
# identify that 'interface structures' can be applied to 'weights'
# identify that 'weights' can be connected to 'loss function changes' (as a 'core relevance structure' of the connection)
# identify that 'irrelevant' can be applied to the 'core relevance connection' between 'structures of weights' and the 'loss function changes'
# identify that 'weight structures with irrelevant impact on the loss function changes can be removed'
# identify that 'trivial' is a component of 'irrelevance'
ai_optimizations = ['identify "weight structures" causing "irrelevant/trivial loss function changes", so they can be removed']

# generate the above ai_optimization using a term from the original implementation (like 'weights') and a general optimization (like 'identify/remove irrelevant structures')
# by applying the 'definition of optimality' to generate an 'optimal structure of that term'