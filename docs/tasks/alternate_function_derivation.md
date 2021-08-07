  - how would you derive the function for the area of a circle

    - applying the known version of the area function for a standard shape
      - r^2 is the unit formula of an area of a standard square shape
      - identify differences between r^2 and the area of a circle with radius r
        - multiply r^2 * 4 and subtract basic differences (like increasingly smaller fractions) until the area approaches the actual circle's area
      - alternatively, find neutralizing structures to combine differences into differences that are more computable
      - alternatively, compute a different difference and apply the resulting ratio of difference to the original difference
        - rather than finding difference between square & circle, find differences between square & hexagon, or unit area (r^2) and the associated quarter of the circle's area (which is pi/4, but without knowing pi yet)
        - given the ratio of difference between the square & hexagon in relation to their difference types, identify the likely difference ratio between the hexagon & the circle, or the square & the circle
          - given the square area/hexagon area ratio, in relation to the difference types (side count, angle count, distance from standard, distance from sub-structures like angles/corners, difference in operations & operator values like powers, composable component structures like triangles) between the square & hexagon shapes, calculate the square/circle area ratio, or the hexagon/circle area ratio, in relation to their difference types
        - apply a sequence that converges at pi (not known from the beginning, but by generating a sequence of terms that approach the circle's area, like the following, and finding a generative function to create that sequence in such a way that it converges to pi)
          - 4, 3, 3.5, 3.125, 3.15, 3.14, 3.1415
          - then connect the sequence's generating function to the area calculation by compressing the sequence's formula (to reduce steps from the first value in the sequence 4 to the final converged value pi)
    
    - by observing attributes of circles, like their dimensions, such as width/height
      - by applying adjacent transforms of these dimensions, like basic operations like multiplication/addition (half, power of 2)
        - half * width = radius 
          - radius ^ 2 = r^2
            - area / r^2 = pi
      - once you identify adjacent relationships (like area = pi * (1/2 * width)^2), check if these hold across other examples
      - if the formula holds across other examples, meaning it:
        - fulfills the 'probability of success' & 'accuracy/precision' solution metrics
        - matches a useful structure like 'common or repeated interaction patterns', which in this case is the pattern between width & area
      - it can be considered a likely candidate for a solution the more metrics it fulfills

    - apply 'standard' interface to 'solution' structure
      - apply a 'standard solution' structure 
        - identify differences (errors) in target solution & applied standard solution output
        - identify functions that could reduce these differences (errors)
          - create interim structures that are more computable & calculate difference types & difference in area in relation to those interim structures, then apply the formula to derive the area difference from those difference types  to the origin-target difference or interim-target difference
            - apply ratios of difference types based on other calculated differences/difference types
          - apply a sequence that gravitates around pi as a symmetry (value converged to by the sequence) that eventually arrives at a term that is equal to pi
          - apply a sum of a sequence of decreasing values that when added eventually converge to pi
          - what type of curve has an area that converges quickly to circle or circle-adjacent shape areas? (simple exponential, polynomial, log)
            - what equivalences exist between the area patterns of a circle or circle-adjacent shapes, as opposed to the area patterns of other shapes
            - what is another unit or lower-dimensional equivalent of the problem
              - 'unit' structure applied to number of dimensions meaning 'calculating length of a curved vs. linear line' instead of 'change type' unit r^2

    - apply 'attribute' interface
      - apply 'change' interface or apply 'adjacent change' useful structure
        - generate connection functions between input structures (objects/attributes/functions) by connecting transformed structures with the target variable ('area') predicted by the solution function
          - filter generated connection functions ('pi * r^2') by which connection functions fulfill:
            - solution metrics like 'prediction success probability'
            - useful structures like 'common interaction pattern'

    - apply 'meaning' interface
      - why do 'unit' values like 3, 4, 6 relate to other 'unit' values like pi & e and 'unit' operations like addition/multiplication/powers and resulting unit components created by structures of unit structures (like primes)?
        - bc of the definition of 'relevance' based on 'similarity' (meaning 'similar structures are often relevant/useful for determining important info'), as these are 'structural similarities'
          - they are similar:
            - to each other in value
            - similar in value to primes
            - similar in value to absolute unit values like 1
            - similar in adjacent transformations from primes (1 is similar by multiplication, 6 is similar by addition & multiplication)
            - the square of a value means 'multiply something by itself once' which is relevant to the concept of a prime (factor of itself & 1), where taking the power of 2 is 1 higher than taking the power of 1
              - so the square is a relevant operation when determining relationships between primes
          - the area created by shifting r by r units (r^2) is related to the area created by rotating r (pi * r^2)
            - how is the 'shifting' operation related to the 'rotation' operation (without using pi) & why is it explainable with pi?
              - transform 'shift' into 'rotation' operation
                - shift operation = fix 'position' of endpoints of vertical line, but allow 'position' of vertically aligned endpoints (line with length r) to be variable
                  - vary the number of endpoints that are fixed (add an 'endpoint position' variable)
                    - rotate-possible operation = fix 'position' of one endpoint at an origin value, but allow other endpoint to be variable
                      - apply all possible variable values of new variable
                        - rotate operation = fix 'position' of one endpoint at origin value, but apply all possible values of other endpoint 'position' value
              - so the transforms applied are:
                - add a variable in the form of number of endpoints that have a 'fixed' position
                  - apply 'one' as the value of this variable ('one endpoint position is variable')
                    - implicit is the filter here that the length of r is still not variable, so the endpoint position can only vary with one type of operation, 'rotation'
                      - apply all possible values of the new variable, while fulfilling other filters (like 'fixed length of r' and 'fixed other endpoint position')
                        - only one operation is possible to vary the position of one endpoint while holding r & the origin constant
                          - now we've arrived at the rotation operation
                - this only applies one variable & all possible values of it to generate a change type (rotate), so its an adjacent transform of the original change type (shift)
          
          - why would 'adding an endpoint position variable (or endpoint fixed count variable) & applying all possible values given the new change type' be the connection (pi) between r^2 and pi r^2, which are the area values generated by these operations?
            - each quarter of the circle falls short of another area unit (r^2)
              - what is the power/coefficient of r that you could use to create each quarter of the circle, other than pi/4 * r^2 - are there any other adjacent transforms of r to create this value without referencing pi directly but by an alternate route? its unlikely given that pi is the exact definition of this relationship, but there could be alternate paths that are good approximations
                - meaning 'how does r^3 relate to the area of the circle', 'how does r^1/2 relate to the area of the circle', etc

          - what is the distribution in difference between the changes you would need to make to r as you rotated it in order to generate the area of the square instead?
            - sequence of r-values to generate the circle as you rotate r: r r r r r
            - sequence of r-values to generate the square as you rotate r: r, r + 0.1y, r + 0.2y, r + 0.3y, r + 0.2y, r + 0.1y
            - alternate methods:
              - find two opposing sequences on different sides of the circle and compute their average
              - find sequences that when summed would equal the default r sequence

          - what is the equivalent relationship between square/circle but applied to the circle/x (such as a triangle), and what is the difference in area between those shapes?
            - add another variable to the 'rotate' operation in the form of 'variable r' or add another variable to the 'shift' operation like 'variable power' to generate the equivalent x-generating operation
            - connect the triangle's area to r instead of connecting the circle's area to r (this is the same as calculating the ratio of difference/difference types between the hexagon/circle)
              - calculating the area of a circle using triangles is adjacent given the trigonometric relationships connected to pi
            - is the fact that the hexagon & square have more symmetries (no clear up/down orientation indicating a difference between top/bottom of the shape) than the pentagon (and the triangle is the first possible unit 3-d shape) a relevant fact to explain why 3/4/6 are more relevant in calculating constants & circle metrics like e & pi than 5 is?
              - why is 5 more relevant than 3 in some cases like finding primes (definition of commonness/repeatability of factors between 3/6)
          - what sequence of unit structures like triangles would approach pi r^2 (or the quarter area, pi/4 r^2)?
            - fractal triangles of some sequence would generate a quarter of the circle once an arc of the curve is established by another triangle
          - determine relevance of adjacent terms like 3 ^ 1/2
            - 4 is the number of unit r^2 area units to create the square bounding the circle pi * r^2
              - 4 ^ 1/2 = 2, indicating the number of r^2 units that would be multiplied by the same number to generate the square of 4 r^2 forming a boundary outside of pi * r^2
              - 3 ^ 1/2 would be the lower limit to generate the inner square of 3 ^ 1/2 r^2 units multiplied by 3 ^ 1/2 r^2 units to generate the inner square

    - apply 'requirement' filter structure
      - define initial adjacent upper limit: 
        - by definition, the coefficient of the area unit for a circle's area will be less than 4, bc 4 * r^2 is the square bounding the circle that exceeds its area
      - define initial adjacent lower limit: 
        - by definition, the coefficient of the area unit for a circle's area will be greater than 3, bc 3 * r^2 fits inside the circle
      - identify remaining structure allowed by initial limits: 
        - the remaining factor explaining the difference in area will be a fraction, and a smaller one closer to zero than 1, bc the circle's area is nearer to 3r^2 than 4r^2
      - apply 'equivalence' change to position the 'circle area' as the 'average' structure
        - identify a structure more equidistant to the circle (compared to 3r^2) than the square is, to use as the next upper limit (octogon, hexagon) and find the area of that shape, then average with the area of 3r^2, which is likelier to be closer to the circle's area than the average of 4r^2 and 3r^2

  - summary of operations used to determine the relationship between square area & circle area (or between the area unit r^2 and the circle area)
    - connect difference types between these structures
      - add variables to connect the structures
        - connect adjacent versions of these structures
          - connect the units of these structures
            - connect adjacent units of these structures
          - calculate difference in area added by a particular change type (difference in variability or value) to a standard shape and format the difference between that difference and the circle's area in terms of that change type
          - apply differences to variables (connective angle, generative function, side count, side length) of the origin/target shape (square/circle) or adjacent shapes (line, triangle) and find the area of the different shapes, then connect the area to the original shape's area using a transformed version of the differences relevant to the area
            - example: once you change the side count, how does that change the area calculation?
        - connect interim versions of these structures (difference between circle/hexagon/triangle area vs. circle/square area, or triangle/square area)
        - connect opposing versions of these structures
          - like 'average an equidistant larger value & a smaller value' or an 'equidistant higher-dimensional (square) vs. lower-dimensional value (triangle)' once you know the difference in area between these values, compared to the circle's area
      - connect structures of differences between these structures
        - connect ratios of adjacent/interim versions of these structures
    - connect components of these structures
      - patterns of line length changes, as a line becomes more curved (like changes from x ^ 1 to x ^ 2)
      - sequences of decreasing triangles/squares or other unit shapes can be used to calculate area of curved shapes
    - connect generative functions of these structures
      - generative functions of shift/rotate
      - generative sequences of area as convergence/sum values
        - factorials/fractals as decreasing sequence structures
        - sequence of area differences in exponent sequence functions (patterns of difference in areas of x^1/2, x^1, x^2)
    - connect neutralizing/coordination structures
      - sum of sub-structure areas that are easier to compute than original area structure
    - connect alternate/approximate versions of these structures
    - connect relevant structures like constants to these structures
    - connect definitions/meaning of these structures

  - related questions & notes from applying known rules & adjacent transforms

    - these adjacent distortions are similar to trigonometric identity coefficient ratios (2, 3, 4, 6)
        e = 2.71828183
        pi = 3.14159265
        e / 2 = 1.35914091
        pi / 2 = 1.57079633
        e / 3 = 0.906093943
        pi / 3 = 1.04719755
        e / 4 = 0.679570458 (~2/3) - 4 is relevant to process above used in determining area of circle
        pi / 4 = 0.785398163 (~3/4) - 4 is relevant to process above used in determining area of circle
        e / 5 = 0.543656366
        pi / 5 = 0.628318531
        e / (e + pi) = 0.463880555
        pi / (e + pi) = 0.536119445
        e / 6 = 0.453046971 (~1/2)
        pi / 6 = 0.523598776 (~1/2)

      - sums are approximately 6, 2.9, 2.0, 1.45, 1.17, 0.97
        - solution metric question              (halting condition of increasing adjacent transforms of denominator)
          - at what point of increasing denominators do the sum of their ratios equal 1?
        - at denominator = 6, their sum is 0.976645747
        - pi + e = 5.85987448
        - e/4 = 0.679570458
        - pi/4 = 0.785398163
        - (pi + e)/4 = 1.46496862
        - pi/(pi + e) = 0.536119445
        - 4/(pi + e) = 0.682608478
        - (4 - pi)^2 = 0.736863172
        - (4 - pi) ^ 1/2 = 0.92650275
        - (4 - pi) / 4 = 0.214601837            (difference in each area unit (r^2) from the corresponding 1/4 section of the circle)
        - if you use (pi + e) as the denominator, their sum equals 1
          - e + pi / e + pi = 1
        - you can arrive at this by a roundabout method of applying adjacent transforms (like adding one to the denominator or adding relevant objects like pi & e), or by applying known operations like adding fractions
        - relations between 53/46 occur a lot in these comparable adjacent transforms involving pi + e

      - this applies the intents:
        - identify unit area (r^2)
        - identify coefficient or constant to connect unit area & adjacent circle area (square area formed by 4 * r^2)
          - 4 - pi = 0.858407346
          - pi/4 = 0.785398163
          - 4/pi = 1.27323954
          - 4 ^ 1/2 / pi ^ 1/2 = 1.12837917
            (4 ^ 1/2 / pi ^ 1/2) / 4 = 0.282094793
            4 ^ 1/2 - pi ^ 1/2 = 0.22754615
          - 4 - 3, pi - 3                          (difference from common number like 3, which standardizes one of the terms to 1)
                1, 0.14159265
                1/1, 1/0.14159265 = 7.06251329     (4 is 7.06251329 times as different from 3 as pi is different from 3)

      - what intents are missing to connect 4 * r^2 to the area of a circle?
        - identify difference types causing ratio of difference between 4 * r^2 and pi * r^2
          - identify difference types between 4 and pi (integer/decimal data type, rational/transcendental number)
            - examine question of producing integer like 4 by multiplying an irrational number like pi by another number 
              - what kind of number would the other number have to be & is this possible using either of these data types or adjacent versions of them?
          - once difference types are identified, identify functions to reduce those differences (one or more differences at a time) & apply them

      - other adjacent transforms with associated meaning
        2 ^ 1/2 = 1.41421356
          1 / (2 ^ 1/2) = 0.707106782     (unit used to create 2, with the negative unit exponent of 2, meaning (x^-2) = 2 where x = 0.707106782)
        e ^ 1/2 = 1.64872127
          1 / (e ^ 1/2) = 0.60653066      (unit used to create e, with the negative unit exponent of 2)
        3 ^ 1/2 = 1.73205081
          1 / (3 ^ 1/2) = 0.577350268     (unit used to create 3, with the negative unit exponent of 2)
        pi ^ 1/2 = 1.77245385
          1 / (pi ^ 1/2) = 0.564189584    (unit used to create pi, with the negative unit exponent of 2)

        1/e = 0.367879441                 (unit negative power of e)
        1/pi = 0.318309886                (unit negative power of pi)

        - adjacent approximate connection
          1/e + 1/pi (0.686189327) ~ e / 4 (0.679570458)
    
    - find out if other more adjacent coefficients (like 3 ^ 1/2) are related
    - why is the derivative of 1/2 * width^2 = 1 * width - is that relevant as a unit of area?
    - find out how factorials are related to decreasing growth (in terms of calculating area)
    - is it significant that the numbers 1, 2, 3, 4, 6, 2^1/2, 3^1/2, pi, and e are similar in value? their ratios are near 1 because they were already similar in the first place, which is all their ratios' similarity to 1 means
