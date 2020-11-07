# Medical app


## schema

		- diagnosis
		- test
		- treatment
		- metric
			- Identify the processes & bio markers related to the condition as you go through search results so you can do secondary searches
				- target metric to inhibit/increase
				- cooperative metrics: synergistic compounds that enhance the effect of drugs without debilitating side effects
					- search for these & the stressors that deactivate/activate them
						Example: MUC1 - bacteria exposed to a split tail activates it
				- antagonistic metrics: any compounds that can neutralize the drug & the supplements/foods that contain them
					- get these inhibitors by looking up existing treatment pharmacokinetics/dynamics & interactions
						- search for inhibit, induce, substrate
						- check for synergistic effects & any effects that prevent the drug from being metabolized, which may be required to activate it
						- once you find a treatment, you need to check it against context provided by user to filter the list of treatments or style it differently
				- metrics further up the causal stack 
					- if you decrease hunger, diabetes doesnt happen, which is also a treatment (fasting)

		- protocol
		- decision
		- interface objects (insights/systems/strategies/errors/assumptions/synergies)

		- condition object

			- searching for a condition brings up related information like:
				- standard medical info:
					- differential diagnoses
					- symptoms/states/stages
					- tests/metrics
				- recovery protocols
				- diagnosis protocols (including tests/questions/metrics)
				- variables
				- questions
				- requirements (inputs, precursors)
				- related conditions (caused by & causative of)
				- related systems (immune, circulatory)
				- related functions (damaged/missing/unavailable functions, like 'regulate structure')
					- inputs to related functions to check for (when examining specific causes for a particular patient & for use in diagnosing to test if a patient has a certain important function input/output that can be reported/measured)

		- system object

			- abstract interfaces

				- functions
				- structures (position, surfaces, interaction layer)
					- components (sub-structures)
				- interactions (expected/handled/accidental, layer/function-based interactions)
					- interaction space
				- change/potential
					- alternatives
				- problems
					- conflicts/competition (like conflicting structures)
					- missing components (given the current set of useful combinations like those producing enzymes/proteins/genes, what other useful combinations arent being used or are adjacent)
				- systems
					- functional systems (protective, restorative, filtration, update)
					- efficiencies like sharing resources for common intents
					- context/conditions/assumptions
				- intents
					- protect sub-system vs. protect system (a problematic conflict that allows auto-immune conditions to develop)
					- trigger function vs. check for prioritization (a competition conflict for shared components that considers prioritized processes)
				- strategies
					- aligning neutralizing side effects (negative outputs used as inputs to a function in same interaction space)
					- positioning functionality for task delegation (using DNA-propagating structures to restore damaged DNA)
					- positioning functionality for relevance (position functionality at point-of-usage like at cellular level or in blood stream rather than a particular system/organ for quick responses to problems)
					- positioning problems by handling function (deploy functionality to find relevant system, contain & move problems to a system that can handle them)

			- specific interfaces

				- input
					- energy

				- structures
					- barriers: blood-brain barrier
					- filters: skin/kidney/liver
					- position: 
						- adjacent components (healthy/dysfunctional, genes, cells)
						- adjacent combinations (if merged with next similar component, what structures/components/functions can be formed)
						- containing environment (organ, tumor, nerve, cell)
						- interaction layer (molecular, blood, chemical, electrical, inflammatory)

				- function
					- testing/comparing/finding/filtering
					- regulation/limiting
					- repair/recovery
					- evolution/stressor handling
					- reduction/destruction/increase/inhibition/triggering/propagation/creation

				- component
					- info components: instructions, memory, networks, filters, regulations, markets, interactions, processors, functions, resources, energy
					- enzyme
					- protein
					- cell
					- gene
					- tasks/pathways/workflows (where directed processes happen & interact with other tasks/processes relevant to the directed trajectory)

## protocols

		- add diagnosis protocol

			- questions & tests/metrics/symptoms to look for to resolve questions

			- start with most-reductive questions first

				- prioritize:

					- questions that rule out the condition (most-filtering questions first with least info)

						- questions that minimize 'minimum required info to answer'

						- questions that have 'minimum required info to answer' in common with other questions

						- questions that rule out low-variation conditions first (high-variation conditions are likelier to apply to difficult-to-diagnose conditions)

						- questions that require minimal changes to diagnose (a condition has a state that, when triggered by eating a glucose tablet, is very quick to diagnose)

						- questions that rule out common problem types first (mismatches, over-prioritization, structural damage, dysfunction/dysregulation cascades, false signals, interaction that shouldnt happen, conflicts, lack of resources/competition), given that complex conditions are likelier to have more unusual/complex problem types (such as structures of common problem types, like combinations/injections)

						- questions that focus on unusual symptoms/metrics to reduce solution space

						- questions that focus on symptoms/metrics with unique/unambiguous causes (vs. systemic variables that could be caused by many things)

						- questions that rule out similar conditions
							- questions that rule out conditions that are more common (prioritize more common conditions)
							- questions that rule out conditions that are more commonly mistaken for this condition (prioritize ruling out common mistakes)
							- questions that rule out conditions that are deadly (prioritize examining deadly conditions first)
							- questions that rule out conditions that are untreatable/undiagnosable (prioritize avoiding time analyzing untreatable/undiagnosable/idiopathic conditions, relegating them to research)

						- questions that rule out causal conditions
							- conditions that cause kidney damage, which would make kidney damage diagnosis more likely if they cant be ruled out
							- conditions that are caused by kidney damage, which would make kidney damage diagnosis more likely if they cant be ruled out

		- add protocols for different symptom sets/stages in interaction space
			- add info for different stages (including recovery protocol, adjacent causal/caused conditions, tests to take, symptoms to look for to indicate progression/recovery)

		- add decision protocol

			- diagnosis
				- stage identification
				- considering alternate causes
				- testing selection & evaluation

			- treatment
				- selecting supplements
				- selecting treatments based on priority (less invasive, higher success, lower risk, fewer side effects, higher impact, prevents other problems, more researched/tested)
				- recovery protocol to avoid/invalidate other treatments (like maintaining/palliative treatments)

			- checkup
				- scheduling
				- testing
				- updating info (new habits/symptoms, changes to protocol followed)
				- return to other decisions for re-evaluation
				- evaluation for progression/regression (and associated stages/symptoms/conditions)


## info format search result filter (to allow selection of info formats by intent/advantage)

		- advantages:

			- function format
				- you can see how organizing info by function clarifies the similarity between the reduce & prevent functions, which can both be used to accomplish prevention of the condition that compound 2 prevents

			- component format
				- this format narrows the focus to a particular object for quick, short-term fixes, which is useful for emergency situations like preventing destruction of important/rare resources

			- type format
				- this format clarifies the connections between similar objects, to quickly compared & find alternatives with the necessary similarities/differences

		- by function (find impact/interaction of a function)

			- reduce

				- reduce damage
					- compound 1
					- compound 2

				- reduce occurrence of condition
					- compound 2

			- prevent

				- prevent condition
					- compound 2

		- by component (find related objects of a particular component)

			- compound 1
				- reduces damage

			- compound 2
				- reduces damage
				- prevents condition

		- by type (find similar/different alternatives)

			- component type

				- compound A
					- compound 1

				- cmopound B
					- compound 2
					- compound 3

			- function type (types organized by function metadata)

				- function type: has a particular input type
					- reduce damage
						- compound 1.reduce damage
						- compound 2.reduce damage

				- function type: has a structure
					- compound 1.reduce damage

				- function type: has a side effect
					- compound 2.reduce damage

				- function type: in a system
					- compound A.reduce damage

				- function type: for an intent
					- compound 1.prevent condition

		
## automatically finding inputs (triggers, requirements, inputs, dependencies) of a component (function/side effect/change/state)

	- out of this set of functions for each substance, derive the following indexed info & search patterns to find substances for an overall "immune system".function-enhancing effect:

	  - search terms:

	    - components:

	      - primary component (cell) type: t-cell, b-cell, nk cell, neutrophil, macrophage, lymphocyte - white blood cell, cytokine, antibody, antimicrobial peptide, endogenous antibiotics
	        - primary component function/input
	      - host system (immune response) type: adaptive, innate, stress
	        - host system function/input
	      - sub-system type: intestinal, spleen, connective tissues, genes, beneficial bacteria, bone marrow, inflammation, stress
	        - sub-system function/input
	      - positive components: immune cells, bacteria, adaptive/innate immune response, anti-inflammatory, communication, response
	      - negative components: stress, stress response, inflammation, pro-inflammatory, phagocytes, bacteria, microbes, pathogens

	    - synonyms:

	      - input: fuel
	      - output: effect
	      - immune: anti-inflammatory, protective, pro-
	      - reduce: regulate, lower, destroy, fight, kill, -cytic, -cidal, anti-
	        - conditions: regulate expression
	      - increase: build/synthesize/produce/proliferate, help/promote/enhance, synergistic, induce/enable/activate/catalyze/stimulate/trigger
	        - conditions: stimulate/induce production, reinforce, strengthen integrity, enhance immunity/activity
	      - change:
	        - conditions: shift toward

	    - functions

	      - negative change types
	        - reduce count/function/input of positive components
	        - increase count/function/input of negative components

	      - positive change types
	        - increase count/function/input of positive components
	        - reduce count/function/input of negative components

	    - aggregate terms:
	        - component: function, attribute (type, input, output), sub-component
	        - component set: primary component or sub-system or host system

	    - search patterns:
	      - increase positive primary components (t-cells)
	      - reduce negative sub-system type components (stress signals, proinflammatory expression)
	      - increase positive sub-system type components (intestinal protection/barrier, bone marrow production function)
	      - component.name [immune response type, cell type, cell function] input
	      - increase positive component set

	- sample output should include: vitamin c, echinacea, astragalus, zinc
	- subsequent queries can chain inputs (find input of input of component to enhance, find input of component with functionality of component that cant be produced, etc)

	- this is an application of the interfaces to the immune system
	  - interface application:
	    - information interface (conditions)
	      - object interface (components, functions, attributes)
	        - abstract interface (types rather than specific implementations)
	          - change interface (condense similar synonyms)
	            - function interface (input/output (fuel/effects/functionality))
	              - intent interface (positive/neutral/negative)
	    - generate aggregate terms used for injecting multiple options (component)
	    - identify relevant combinations (increase positive resources/effects/processes/states, reduce negative resources/effects/processes/states)
	    - generate relevant patterns with aggregate terms

	  - to produce an output on the pattern interface, to generate the set of queries to find the compounds that will fulfill the original input intent 'enhance the immune system functionality'
