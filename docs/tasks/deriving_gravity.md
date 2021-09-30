  - why does a ball thrown in the air have the shape of a parabola with varying height/width, with respect to distance from original position (x-axis)?
    
    - how to derive the function of the trajectory of a thrown object, given just a limited subset of (x,y) values, or just (original position, direction of movement, & propulsion force)

    - specifically, why would the function of x have a x^2 term?
      - what is the meaning of the parabola?
    
    - if the ball isnt thrown vertically, it will have another dimension of change in the form of a 'direction of movement', represented by x
    - if the ball fulfills the following conditions, it will drop to the ground again once after the initial throw:
      - isnt caught but allowed to reach its highest vertical position given the force it was thrown with
      - doesnt encounter other forces keeping it above the ground
      - doesnt bounce
    - the x^2 component just happens to represent the trajectory of an object that is thrown semi-vertically, the trajectory having a peak height and returning to its original height as momentum of the original force is reduced, excluding other influences that could have changed its motion, like wind or someone catching the object, where momentum has an impact of exponentially changing slope (change rates) as its impacted is reduced by interaction with gravity
    - so the parabola isnt meaningful outside of the similarities in its shape to the connection between variables 'direction of movement' x & 'height' y on its own, but it does imply the following structures in the physics system:
      - the existence of a propulsion force incentivizing change in the upward direction
      - the interaction between the propulsion force & gravity
      - the reduction of this force as it interacts with another force (which happens to be gravity)
      - the limit on this force, which is reduced to zero at a particular height, at which point momentum begins to incentivize motion in the opposite direction in response to gravity
      - the upper limit on its possible vertical position y
      - the lack of interfering variables that could have changed the parabola's shape (to another polynomial, a shifted/scaled version of the function because of influences other than initial force & direction of motion & gravity, or to a function with a linear component or a minimum value other than zero, etc)
    
    - how would you derive the parabolic structure, given these initial known variables (x,y) values, or (propulsion force, direction, gravity) and the other relevant structures of the system?
      - these structures represent requirements of the connecting function (the parabola):
        - the limiting & reducing effects on:
          - the propulsion force when opposed by gravity, which incentivizes downward motion in general, leading specifically to:
            - increasing momentum on the downward slope
            - reduction of its upward motion to zero
          - the maximum & minimum possible height
            - the minimum being zero assuming no interfering structure
            - the maximum being determined by the propulsion/gravity force interaction
        - and given that we know the info (or assume as a proxy of info):
          - the number of bounces (1)
          - the origin position (height of propulsion initiator)
          - the lack of interfering structures
          - the non-vertical motion (the direction of movement) resulting in a dimension that changes with time x
        - given that we know the maximum, minimum & general shape as determined by the limits/reductions, and the given input info variables, we know we need a function that:
          - has one peak
          - has decreasing change rate at first that reaches zero, then has increasing change rate until it reaches height y = 0
          - has similar or equal decreasing/increasing change rate change rates (the parabola is roughly or exactly symmetric)
        - so we can infer that x^2 is an adjacent operation of x that can be used as a standard structure to adjust with adjacent operations (like shifts/scaling/inversion) and known required variables like propulsion force (ignoring interference structures)
        
    - the 'meaning' of the parabola does not have 'physical' system definitions, but it has interface definitions (such as 'structural' or 'change' interactions) in that:
    
      - an initial change type ('propulsion force' & 'direction of movement') changes at a decreasing change rate until its change rate is zero (peak), then changes at an increasing change rate until its output variable ('height') is zero, creating a 'symmetry' at its peak
        - the initial change type component (the 'propulsion force') has limited power in response to its interaction with another change type ('gravity') that is stronger, because when the propulsion force distorts a component of an object's state (height), gravity can force it back into one component of its original state (height), in a system with a lack of interference structures
        - the constant multiplier of x^2 and x^2 represent the relative strength of the opposing force of the initial force
          - the constant multiplier represents the ratio of relative strength (degree of relative strength)
          - the x^2 term represents the fact that no matter how hard the ball is thrown (the parameters of the propulsion force), gravity can overpower it every time (higher absolute relative strength)
        - there are no limits or other structures preventing these change types, the coordination of these change type components, or their interactions in the system
        - this is a common standard interaction structure partly bc it can be generated with adjacent transforms of the input x, and adjacent operations are more common
        - given that its a common structure, the system where this structure occurs must have two opposing interaction forces
        - constant change is less common than exponential change, because most of the time, constant change requires a very simple closed system, and that is a very rare condition in the 'physical' system (physical reality, created by the lack of structures preventing a system where interfaces are allowed to interact as is useful for other interface structure interactions), and conditions enabling other possible generators of constant change are even rarer)
          - given the complexity of systems (with many variables, many possible neutralizing/interference & opposing structures, many limits & requirements, many structures that can store energy, many possible interactions given lack of limits enforcing non-interaction, etc), this means 'more complex change types are more probable'
          - this is a very useful rule to understand systems, that can be used to infer & connect with other useful rules like:
            - if inputs are complex, outputs are likely to be complex, as the internal connecting structures of inputs/outputs are unlikely to be capable of storing/reducing complexity unless specifically designed to do so, which is uncommon
          - deriving the rules 'more complex change types are more probable' and 'inputs are likely to be similar to outputs in some conceptual system attribute like complexity' from the initial set of (x,y) values can be done with interface queries:
            - applying the change interface to identify change types like 'unit change type', 'constant change type', 'increasing/decreasing change type', 'opposing change type', 'componding change type' at which point the 'complexity' attribute will become clear in the 'difference' between the 'increasing/decreasing change type' and the 'constant change type'
            - applying the common useful function 'connect inputs-outputs' to connect input interface structures (concepts like 'complexity') with output interface structures (concepts like 'complexity')
              - identifying the 'structural similarity' useful interface structure between the inputs/outputs:
              - applying the concept interface's useful function 'abstracting' to derive the rule 'inputs are likely to be similar to outputs in some conceptual system attribute like complexity'
            - applying the probability-concept interface to check for the 'commonness' of various conceptual attributes like 'simplicity' (or 'complexity') across known systems to identify their 'probability'
            - applying the system-structure-probability interface to check for 'requirements' or 'limits' enforcing a 'simple' or 'complex' system, and the 'probability' of those structures across known systems

      - contextual meanings can include other change types when applied to the contextual host system (the 'physical' system), including variables like:
        - substitute variables of gravity (the input 'mass of host object' leading to the output of the 'gravitational force' leading to the observed change rates applied to the thrown object's position in relation to the host object (planet))
        - the system where these variables can interact in this way ('standard physics model where change occurs over time')
        - the change type interactions & components indicated in the parabola are unlikely to retain their simplicity in a physical system where assumptions like 'lack of interference structures' are not enforced, but it can be used as a standard/base solution to start applying transforms to in order to fit actual data & detect relevant interference structures in place
        - why is x (change in horizontal position) multiplied by itself useful for determining vertical position:
          - its only useful in that it describes a general shape of motion in systems like the 'physical' system where there are two interactive opposing forces (propulsion & gravity forces), one of which is stronger, where there is a change in 'direction of movement' that can be mapped to the x-axis
          - so another meaning is that:
            - 'in a system with two interactive opposing forces (where their relative power means one consistently overwhelms the other, but does not prevent all functionality of the other), where a direction of movement applies to the force (propulsion force) initiating change from a stable state (original position), the direction of movement applied to itself may be a useful general structure to identify change in other positional components (height) of the object acted on by the forces'
            - the 'change in area x^2' created by 'direction of movement x applied to itself' is relevant to determining how change in direction of movement determines change in another position dimension y where movement is not prevented or is incentivized/initiated by a force
              - change in movement x is not the only relevant variable to determine y - the previous position y also matters to determine the change in y that a particular change in x will create
              - 'how square area changes when direction of movement x is the side length of the square' determines the general shape of the interactive forces and other positional dimension of change y
                - 'some energy is invested in changing x and some energy is invested in changing y, where change in y follows a "squared area" change pattern applied to x'
                - why is a square a relevant structure? bc:
                  - squaring a number produces a symmetry
                  - squaring a number produces a one-peak structure
                  - the overlap of these symmetry & peak structures aligns with the 'two opposing interactive forces having different power' and the standard x^2 change type, where y increases exponentially (with 'componding' change) in a way that reflects the physical process of momentum creating compounding change (the change type of 'change creating an increase in change')
                  - squaring a number produces a change type progression (increasing increasing change in y => high increasing change in y) that has a structural similarity to 'interactive opposing forces without other interference/neutralizing structures'
                    - where the 'change type progression' is: 'constant positive change in x' => 'high increasing change in y => decreasing increasing change in y => increasing decreasing change in y => high decreasing change in y'
            - this is ignoring spin & other variables which may add movement in dimension z

      - the 'gravity' variable isnt specified in the original variables (x,y) values of the data set, but can be inferred by the slowing change rate on the upward slope
        - meaning: some 'structure' is 'interfering' with an 'increase in upward change' and 'constant upward change', which 'opposes' the 'initial change type' of 'upward change'

      - why are direction of movement x and vertical movement y related at all (or specifically in this way, where a change in x applied to itself can adjacently produce a change y) bc they are:
        - 'interactive': 
          - they are both position variables and their interaction cant be prevented in the 'physical' system, which is by definition the 'interaction space' of positional dimensions & time
        - 'required' to interact: 
          - this is bc 'its required that if an object's x-value changes or if it has a value at all, it must also have a y & z value (they are required to interact)'
        - 'probable' to interact: 
          - any change in x is also likely to produce associated changes in y & z (rather than y & z being constant while x changes), given how constant change is difficult to create bc its a simple structure & maintaining simplicity in a complex system is a high-cost operation
        - 'structurally similar':
          - exponential (squared change) in x maps adjacently to change in y
        - 'systematically compliant':
          - the general system structure of 'an interaction of opposing forces where one (the change-inhibiting force) is absolutely stronger to a non-absolute degree (not enough to prevent all functionality of the change-initiating force) and where there are no neutralizing structures, resulting in a compounding change structure (like that created by momentum)' matches the physical system structure 'gravity & propulsion force interaction, connecting a change in both direction & height' & also matches the 'inverse of the shape (parabola) created by the adjacent unit compounding change structure (x^2)'
          - they represent a common interaction function across systems
          - change of one type (change in 'width' position component) impacts changes in related/similar/equal types (change in 'height' position component) on the same interface ('position') when 'required' to 'interact' bc these changes are not just interactive bc of the requirement, but they are also adjacent:
            - 'if change in one position component is prevented, change can accrue to another position component to create a minor/adjacent state change, without requiring impossible, unlikely, or extreme state changes, given change type interaction requirements like continuity' (change in dimension set or extreme position change like non-continuous position change)

      - so the question 'why would the position trajectory of a thrown object have an x^2 term' is answered by structures like:

        - 'structural similarity with adjacent shift/inversion operations between one-peak compounding change & object speed change based on object position x (momentum)'
        - 'structural similarity between opposing interactive forces where one is stronger, forcing any change initiated by the weaker force to be neutralized (so y returns to base position of zero) & object speed change based on object position x (momentum)'

        - where structures like:
          - 'one-peak' are relevant structures injected into the interface queries producing these interface structures bc of known requirements (like 'no bouncing'), meaning 'bc of the structural similarity between the requirement (no bouncing) and the structure (one-peak)'
          - 'final y position of base y position zero' is a relevant structure to symmetry structures (like those found in various compounding/exponential change structures), where change from the base is allowed to occur but it should return to the base by the end of the function trajectory

        - if it wasnt these structures indicating 'gravity', what other structures could have explained the interaction?
          - 'gravity' exerts an 'opposing force' structure, which acts like a 'boundary', 'barrier', 'limit', or other 'requirement' structure, so other structures resulting in those structures could also have explained the interaction, if the physical system rules/structure were different
            - a 'set' of vertical forces exerting an upper limit or downward force at various points on the upward slope, and a lack of propulsion forces allowing it to fall back to zero on the downward slope
            - a force acting on the z-dimension whose outputs cascade to other dimensions
            - a 'circular' structure indicating a return to an origin value (y = 0)
            - a 'set of barriers' acting like a 'set of tangents' that limit the upward change rate
            - a 'repulsive force' in the position above the peak
            - a 'gravitational force' of an object around the peak, slowing motion (like a planet)
            - a 'set' of augmenting forces at various heights or along various trajectories that keep change compounding or increasing up to a limit
            - a 'set' of connecting forces ensuring objects in various positions are connected adjacently to other positions (like motion in a particular direction or with continuous speed change)

      - so we have arrived at a structure ('opposing force interaction') indicating gravity, which occurs bc of the referenced requirements/limits & the resulting allowed interactions, common/adjacent/unit structures, structural similarities (like between complex inputs/outputs), interaction types, & change structures (like bases/symmetries) and change types (like compounding change) in the physical system and across systems in general
        - this allows another way to calculate the trajectory of the ball, if it was sub-optimal to use the other inputs like (x,y) values or (origin position + direction of movement + propulsion force), such as 'calculate the change that gravity applies to other interactions in the physical system and predict the output using that change pattern between inputs/outputs of functions where gravity is an input'
        - gravity acts like a 'complexity preserving/adding' function (as opposed to a 'complexity reducing' function like a derivative or regularizer) and a 'change reversing function' in this physical system, which can be applied as needed in other interactions
        - in this way, we have derived the concept of 'gravity' without traditional numerical math