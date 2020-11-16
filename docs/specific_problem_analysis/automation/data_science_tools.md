# Statistical tools


# Concepts

	- matrix
	- vector
	- eigenvector/eigenvalue
	- sparsity
	- orthogonal
	- variables
		- random
		- gaussian/normal
	- degrees of freedom
	- jacobian
	- hilbert space
	- lie algebra
	- hessian matrix
	- neumann series
	- taylor series
	- homomorphism
	- topology
	- manifold
	- soft thresholding operator: translates values towards zero, making them exactly zero if they are small enough
	- hard thresholding operator: sets smaller values to zero, leaving larger ones untouched
	

# Functions

		- loss/cost/objective/penalty
		- kernel
		- norm: function from a real/complex vector space to the real numbers that commutes with scaling, obeys the triangle inequality, and is zero only at the origin


# Tasks

	- backpropagation
	- action/policy/state/reward
	- finding local maxima/minima, where function has equality constraints (like that equations have to be satisfied by the chosen variable values)
		- derivatives (slope is zero indicating a curve maximum/minimum or saddle point)
		- lagrange multiplier
			- convert a constrained problem into a form so the derivative test of an unconstrained problem can be applied
			- Lagrangian function: 
				- to find the maximum/minimum of the original function:
					- find the lagragian function: 
						- original function - lagrange multiplier * g(x), where equality constraint is g(x) = 0
					- find the stationary points of the lagrangian function
						- find the saddle points within the stationary points
							- find the optimizing saddle point of the bordered hessian matrix (having definiteness)
				- the lagragian uses a reformulation of original problem, using the relationship between the gradients of the function & constraints
				- allowing optimization without using constraint parameterization
		- gradient descent


# Rules
		- coefficient estimates do not need to be unique if covariates are collinear
	

# Statistical models
		- linear models
		- generalized estimating equations
		- proportional hazards models
		- M-estimators
		- anova
		- arima


## Probability distributions

		- normal (gaussian)
			- logit-normal
			- truncated-normal
			- wrapped normal
			- folded normal
			- half normal
			- log normal
		- poisson
		- binomial 
			- bernouilli
		- uniform
		- weibull
			- exponential
		- gamma
			- chi-squared (used in goodness of fit tests)
		- pareto
		- levy
		- cauchy
		- laplace
		- t-squared

	- distribution types/attributes
		- joint
		- conditional
		- generalized
		- continuous/discrete
		- negative
		- geometric
			- hypergeometric
		- beta
		- stable
		- logarithmic
		- truncated
		- raised
		- half
		- bi
		- phased
		- mixture
		- combination
		- shifted
		- unique
		- convex
		- wrapped
		- folded
		- noncentral
		- inverse
		- scaled

	- probability density functions
		- pdf
		- cdf (cumulative)

	- other functions
		- delta function


# Metrics

	- recall
	- accuracy
	- precision
	- change detection (metrics: false alarm, misdetection, detection delay)


# Algorithms

	- regression

		- linear
		- logistic
		- poisson
		- bayesian probit regression
		- generalized linear regression: version of linear regression, where:
			- output/dependent variables can have non-normal error distribution models
			- the measurement variance magnitude is an output of its predicted value
			- it uses a function to link the linear model & dependent variable (linking the linear model to a mean of the outcome distribution function)
		- lasso regression: involves variable selection & regularization
		- ridge regression
		- best subset selection regression

	- artificial neural network

	- categories

		- reinforcement learning

			- deep reinforcement learning
			- inverse reinforcement learning
			- safe reinforceement learning

			- specific reinforcement algorithms: 

				- https://en.wikipedia.org/wiki/Reinforcement_learning#Comparison_of_reinforcement_learning_algorithms

				Monte Carlo:		Every visit to Monte Carlo
				Q-learning:			State–action–reward–state
				SARSA:				State–action–reward–state–action
				Q-learning-Lambda:	State–action–reward–state with eligibility traces
				SARSA-Lambda:		State–action–reward–state–action with eligibility traces
				DQN:				Deep Q Network
				DDPG:				Deep Deterministic Policy Gradient
				A3C:				Asynchronous Advantage Actor-Critic Algorithm
				NAF:				Q-Learning with Normalized Advantage Functions
				TRPO:				Trust Region Policy Optimization
				PPO:				Proximal Policy Optimization
				TD3:				Twin Delayed Deep Deterministic Policy Gradient
				SAC:				Soft Actor-Critic

		- unsupervised

			- clustering

		- supervised

			- classification

			- regression
			
			- structure prediction (selecting a structure from a set of structures of a particular format, like a logic tree version)

				- example: sequence tagging (using hidden Markov model or conditional random field to predict next word based on conditional probability given previous word)
				Probabilistic graphical models 
					- Bayesian networks
					- random fields (conditional random field)
				- inductive logic programming
				- case-based reasoning
				- structured SVMs
				- structured k-Nearest Neighbours
				- Markov logic networks
				- constrained conditional models
				- Recurrent neural network, in particular Elman network

	
	- specific problems

		- generalizing (avoiding/reducing overfitting)
			- cross-validation
			- regularization

		- data changes
			- data augmentation
			- alternate data set generation
			- missing value imputation

		- loss function
			- square loss
				- mean square
			- hinge loss

		- standardization: framing values in standard range like 0 - 1 or -1 to 1

		- regularization (generalizing to prevent over-fitting to a specific data set, adding a cost to optimization function to penalize over-fitting) 

			- classification

			- lasso regularization (least absolute shrinkage and selection operator)

				- forces sum of the absolute value of the regression coefficients to be less than a fixed value, so that certain coefficients are zero, effectively choosing a simpler model excluding those coefficients
				- standardization by centering variables around the mean
				- shrinks the magnitude of all the coefficients, but sets some of them to zero
				- translates coefficients towards zero by a constant value, setting them to zero if they reach the constant value
				- linear regression, where coefficients have Laplace prior distributions
				- find the minimum of {{ averaged * [mean squared (meaning y - xB)] - lagrangian multiplier * (B) }}
					min {{ 1/N * ||y - xB|| - L * ||B|| }}

				- isolates components of B that are zero (such as the corners of the lasso norm square), for certain objects that are tangent to the boundaries of the norm shape, to help with removing those components
			
			- ridge regularization

				- forces sum of the squares of the coefficients to be less than a fixed value, which shrinks the size of all coefficients (not setting any of them to zero)
				- improves prediction error by shrinking large regression coefficients in order to reduce overfitting
				- shrinks the magnitude of all the coefficients
				- scales all of the coefficients by a constant factor
				- linear regression, where coefficients have normal prior distributions
				- methods
					- Tikhonov-regularized least squares
			
			- early stopping: training until error on validation set stops decreasing

			- other regularizers
				- signal noise reduction: 
					- total variation regularization

			- regularizers for sparsity
			    - Proximal methods
			    - Group sparsity without overlaps
			    - Group sparsity with overlaps

			- regularizers for semi-supervised learning

			- regularizers for multitask learning
			    - Sparse regularizer on columns
			    - Nuclear norm regularization
			    - Mean-constrained regularization
			    - Clustered mean-constrained regularization
			    - Graph-based similarity

		- selecting model from a model ensemble

			- Bayesian learning methods make use of a prior probability that (usually) gives lower probability to more complex models
			- Akaike information criterion (AIC)
			- minimum description length (MDL)
			- Bayesian information criterion (BIC)

		- dimensionality reduction

			- feature selection: selecting variables for use in the model
				- stepwise: useful only when a few variables have a strong relationship to dependent variable
				- lasso

		- anomaly detection

		    - Density-based techniques
		    	- k-nearest neighbor
		    	- local outlier factor
		    	- isolation forests
		    	
		    - Outlier detection
		    	- subspace
		    	- correlation
		    	- tensor
		    	- cluster analysis 
		    	- fuzzy logic

		    - SVM (one-class)

		    - Replicator neural networks

		    - Autoencoders
		    	- variational autoencoders

		    - Long short-term memory neural networks

		    - Bayesian networks

		    - Hidden Markov models (HMMs)

		    - Deviations from association rules/frequent itemsets

		    - Ensemble techniques
		    	- feature bagging
		    	- score normalization
		    	- different sources of diversity