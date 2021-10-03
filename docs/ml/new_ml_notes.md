
      - concept of 'comparative features': features that were enough to differentiate a category in the training set but not in test, bc they have too many overlaps with other category feature sets
        - adding sub-parameters allows variation within these overlaps to be identified/differentiated, using any remaining differentiating features that are still available in inputs but dont change overall input/output connections (change direction, average change rate, etc)
          - https://www.theregister.com/2021/09/02/imaginary_numbers_help_ais_solve/

      - examine 'wave' and 'symmetry' structures in weight paths/trees where 'adjacence' of features is preserved or magnified to some degree (leading to incremental change in adjacent node outputs)
        - concept of 'cost-sharing' among various contributing weight paths/trees to avoid over-specificity
        - https://spectrum.ieee.org/what-is-deep-learning/particle-17

      - 'kernel function acts like a mapping useful to calculate a difference without converting to the whole space'
        - other examples: regularizers can act like 'activation functions', similar to how randomizers can act like 'averagers'

      - give examples of optimizations/derivations applied to standard ml process
      - give examples of formatting ml in different formats (variable network, tree, sequences, etc)
      - give examples of errors produced by compressing algorithmic input/output connection logic
      - give an example of why to choose position of a function in data pre-processing vs. in an algorithm (lack of certainty, such as 'lacking an insight generating a reason why the structure should be applied')
      - give example of a sequences & networks' interactions with time (like reducing computations over time, applying operations chronologically, interacting with prior data, adapting over time)

      - backpropagation corrects weights based on 'differences' between expected/actual values (a standard error definition structure)

      - for a data point, change in weight for various node types (normal, hidden) can be calculated based on using gradient descent for determining the weight change that would minimize the 'output node error degree'

      - plain language version of weight update function:
        - output node error degree     = difference between target & predicted value
        - all output node error        = mean least squares applied to (output node error degree)
        - (normal) weight change       = - learning rate                                                       *        derivative of all output node error with respect to weighted input sum for output node         * previous node output
                                       = - learning rate                                                       *        change in all output node error with respect to change in weighted input sum for output node   * previous node output
                                       =   learning rate * output node error degree * derivative of activation                                                                                                         * previous node output
        - (hidden) weight change       =   learning rate                            * derivative of activation * sum of derivative of all output node error with respect to weighted input sum * weight(output node k) * previous node output
