	standard_nns = ['cnn', 'mlp', 'gan', 'recurrent', 'ltsm']
	ensemble = ['adaboost', 'boosting', 'bagging', 'xgb', 'gradient_boosted_decision_tree', 'gradient_boosting_machine', 'random_forest', 'stacked_generalization']
	# unsupervised clustering with methods appropriate according to varying density measures
	clustering = ['knn', 'kmeans', 'dbscan', 'expectation-maximization', 'hierarchical', 'random_forest']
	# unsupervised
	unsupervised = ['hierarchical_clustering', 'gan', 'kmeans', 'mixture', 'dbscan', 'local_outlier_factor', 'autoencoder', 'deep_belief', 'self_organizing_map', 'expectation-maximization', 'pca', 'ica', 'nmf', 'svd']
	# supervised
	supervised = ['svm', 'knn', 'regression', 'decision_tree', 'naive_bayes', 'lda', 'learning_vector_quant']
	# dimensionality reduction
	reductions = ['dirichlet', 'pca', 'lda', 'svd', 'tsne', 'ica', 'nmf', 'mds', 'autoencoder', 'self_organizing_map'] # multidimensional scaling, non-negative matrix factorization
	regressions = ['linear', 'binary', 'mixed', 'nonparametric', 'nonlinear', 'polynomial', 'binomial', 'poisson', 'ordinal', 'logreg', 'gaussian_process', 'partial_least_squares', 'principal_components']
	anomaly = ['autoencoder', 'variational_autoencoders', 'local_outlier_factor', 'lstm', 'bayesian', 'hidden_markov', 'cluster_analysis_outlier_detection', 'knn', 'one-class svm', 'bagging', 'score_normalization']	
	# hierarchical_linear_models = ['random_effects'] # kernel_functions = ['radial_basis_function'] # function_approximation = ['radial_basis_function']
	

		'''
		- lasso
			- params: alpha=1.0, *, fit_intercept=True, normalize=False, precompute=False, copy_X=True, max_iter=1000, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic'
		'''
		'''
		- kmeans
			- fast
			- fails in local minima
			- If the algorithm stops before fully converging, the cluster_centers wont be the labels_ (means of each center)
			- labels_ are reassigned after last prediction
			attributes: cluster_centers (ndarray), labels (ndarray), inertia (float), n_iter (number of iterations run)
			variants: MiniBatchKMeans may be faster for large number of samples, does incremental updates of the centers positions using mini-batches
			methods: 
				- fit_predict(X[, y, sample_weight]) - Compute cluster centers and predict cluster index for each sample
				- has sample_weight param for its fit/transform/predict methods
			params: n_clusters=8, *, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='deprecated', verbose=0, random_state=None, copy_x=True, n_jobs='deprecated', algorithm='auto'
		'''
		'''
		- linear_regression
			- params: *, fit_intercept=True, normalize=False, copy_X=True, n_jobs=None
			- attributes: coef_, rank_, singular_, intercept_
			- methods:
				- has sample_weight param for its fit/score methods
		'''
		'''
		- elastic_net
			- params: alpha=1.0, *, l1_ratio=0.5, fit_intercept=True, normalize=False, precompute=False, max_iter=1000, copy_X=True, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')[source]
			- attributes: coef_, sparse_coef_, intercept_, n_iter_
			- methods:
				- has sample_weight param for its fit/score methods
				- path(X, y, *[, l1_ratio, eps, n_alphas, …]) - compute elastic net path with coordinate descent
			- variants:
				ElasticNetCV: Elastic net model with best model selection by cross-validation.
				SGDRegressor: implements elastic net regression with incremental training.
				SGDClassifier: implements logistic regression with elastic net penalty (SGDClassifier(loss="log", penalty="elasticnet"))
		'''
		'''
		PCA (n_components=None, *, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None)

		alt: KernelPCA

		method:
			- find top features explaining variance with eigenvalues of eigenvectors
		'''
		'''
		"TruncatedSVD/lsa (n_components=2, *, algorithm='randomized', n_iter=5, random_state=None, tol=0.0):
			- Contrary to PCA, this estimator does not center the data before computing the singular value decomposition. This means it can work with sparse matrices efficiently
			- truncated SVD works on term count/tf-idf matrices as returned by the vectorizers in sklearn.feature_extraction.text. In that context, it is known as latent semantic analysis (LSA)
			- supports two algorithms: a fast randomized SVD solver, and a “naive” algorithm that uses ARPACK as an eigensolver on X * X.T or X.T * X, whichever is more efficient
			- SVD suffers from a problem called “sign indeterminacy”, which means the sign of the components_ and the output from transform depend on the algorithm and random state.
			  To work around this, fit instances of this class to data once, then keep the instance around to do transformations."

		method:
			- select explanatory left features of output matrix, using:
				- singular-to-diagonal transform executed by multiplying:
				 	- orthogonal matrix U x * x, diagonal matrix D x * y, and orthogonal matrix V y * y that approximate original matrix A

		'''
		''' 
		LatentDirichletAllocation (n_components=10, *, doc_topic_prior=None, topic_word_prior=None, learning_method='batch', learning_decay=0.7, learning_offset=10.0, max_iter=10, batch_size=128, 
		evaluate_every=-1, total_samples=1000000.0, perp_tol=0.1, mean_change_tol=0.001, max_doc_update_iter=100, n_jobs=None, verbose=0, random_state=None)
		
		input: array-like or sparse matrix, [samples, features]

		output: doc_topic_distribution for X, shape= (samples, components)

		method: learns a model using variational bayes, then transforms to fit that model
		'''
	'''
		LinearDiscriminantAnalysis (*, solver='svd', shrinkage=None, priors=None, n_components=None, store_covariance=False, tol=0.0001) # solver = ‘svd’ (doesnt compute cov unless store_covariance is True), ‘lsqr’, ‘eigen’

		"A classifier with a linear decision boundary, generated by fitting class conditional densities to the data and using Bayes’ rule.
		The model fits a Gaussian density to each class, assuming that all classes share the same covariance matrix.
		The fitted model can also be used to reduce the dimensionality of the input by projecting it to the most discriminative directions, using the transform method."

		attributes:
		    coef_ - ndarray of shape (n_features,) or (n_classes, n_features) Weight vector(s).
		    intercept_ - ndarray of shape (n_classes,) Intercept term.
		    covariance_ - array-like of shape (n_features, n_features) Weighted within-class covariance matrix. 
		    	It corresponds to sum_k prior_k * C_k where C_k is the covariance matrix of the samples in class k. 
		    	The C_k are estimated using the (potentially shrunk) biased estimator of covariance. If solver is ‘svd’, only exists when store_covariance is True.
		    explained_variance_ratio_ - ndarray of shape (n_components,)
		    means_ - array-like of shape (n_classes, n_features) Class-wise means.
		    priors_ - array-like of shape (n_classes,) Class priors (sum to 1).
		    scalings_ - array-like of shape (rank, n_classes - 1) Scaling of the features in the space spanned by the class centroids. Only available for ‘svd’ and ‘eigen’ solvers.
		    xbar_ - array-like of shape (n_features,) Overall mean. Only present if solver is ‘svd’.
		    classes_ - array-like of shape (n_classes,) Unique class labels.

		method:
			- separate classes with line by mapping features into lower dimensional space (assuming means are far from each other)
				- calculate class means distance or inter-class variance 
					- calculate intra-class variance (distance between mean & sample)
						- construct lower-dimensional space maximizing inter-class variance
	'''	
		''' tsne (n_components=2, *, perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, 
			metric='euclidean', init='random', verbose=0, random_state=None, method='barnes_hut', angle=0.5, n_jobs=None)

			"converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.
			It is highly recommended to use another dimensionality reduction method (e.g. PCA for dense data or TruncatedSVD for sparse data) to reduce the number of dimensions to a reasonable amount (e.g. 50) if the number of features is very high"

			attributes:
				embedding_ - array-like, shape (n_samples, n_components) - Stores the embedding vectors 
	    		kl_divergence_ - float - Kullback-Leibler divergence after optimization.
				n_iter_ - int - number of iterations run

			output: Embedding of the training data in low-dimensional space

		'''

	kernel_functions = ['radial_basis_function'] # weighting
	ann = ['cnn', 'mlp', 'gan', 'recurrent', 'ltsm']
	ensemble = ['adaboost', 'boosting', 'bagging', 'xgb', 'gradient_boosted_decision_tree', 'gradient_boosting_machine', 'random_forest', 'stacked_generalization']
	clustering = ['knn', 'kmeans', 'dbscan', 'expectation-maximization', 'hierarchical', 'svm_clustering']
	unsupervised = ['hierarchical_clustering', 'gan', 'kmeans', 'mixture', 'dbscan', 'local_outlier_factor', 'autoencoder', 'deep_belief', 'self_organizing_map', 'expectation-maximization', 'pca', 'ica', 'nmf', 'svd']
	supervised = ['svm', 'nearest_neighbors', 'regression', 'decision_tree', 'naive_bayes', 'lda', 'knn', 'learning_vector_quant']
	reductions = ['dirichlet', 'pca', 'lda', 'svd', 'tsne', 'ica', 'nmf', 'mds', 'autoencoder', 'self_organizing_map'] # multidimensional scaling, non-negative matrix factorization
	regressions = ['linear', 'binary', 'mixed', 'nonparametric', 'nonlinear', 'polynomial', 'binomial', 'poisson', 'ordinal', 'logreg', 'gaussian_process', 'partial_least_squares', 'principal_components']
	anomaly = ['autoencoder', 'variational_autoencoders', 'local_outlier_factor', 'lstm', 'bayesian', 'hidden_markov', 'cluster_analysis_outlier_detection', 'knn', 'one-class svm', 'bagging', 'score_normalization']
	regularizations = ['ridge', 'lasso']
	parameters = []
	metrics = []
	limits = []
	assumptions = [
		'random variable', 'regression linearity', 'homogeneity of error variances', 'independence/normality of error terms', 'homogeneity of regression slopes', 'independence/orthogonality of variables'
	]
	problems = ['multicollinearity', 'bias', 'assumption', 'method_mismatch']
	efficiencies = [
		'similar structures like a boundary and a phase shift', 
		'phase shifts like when a change type converts to another', 
		'existing differences as an input/source of other differences'
	] # why some information is more adjacently mappable to other information
	all_intents = {
		'regression': {}, 
		'predict', 
		'classify': {
			'linear',
			'nonlinear with kernel function'
		}
		'normalize', 
		'regularize', 
		'detect outlier', 
		'identify clusters', 
		'differentiate clusters', 
		'combine'
	}
	alternatives = {}
	alternatives['cov_adjustments'] = ['ANCOVA', 'random_effects'] # analysis of covariance
	alternatives['dependent_mean_equality_across_independent_category_without_continuous_covariates'] = ['ANOVA/regression', 'ANCOVA']
	definition_schema = {
		'name': {
			'definitions': []
			'related_objects': {},
			'alternatives': [], # interchangeable or alternate methods, not variants of this method
			'assumptions': [],
			'variants': {
				'reason_why_it_varies_varied_attribute_or_variant_type': {
					'attribute_or_function': 'specific_variant'
				}
			},
			'types': [],
			'usage_intents': [], # used for, used in
			'problems': [], # problems are also indexed in intents::strategies, where intents include solving problems
			'intents::strategies': [
				'general_intent_or_priority': ['specific_intent'],
				'specific_intent': {
					'general strategy': 'specific strategy'
				}
			],
			'functional_reasons': {}, # this is reasons why a structure/method combination works, like why aggregating into an ensemble method is effective
			'insights': [],
			'method_steps': []
		}
	}
	methods = {
		'multidimensional_scaling': {
			'definitions': [
				'visualize similarity (pairwise distance) across data points in cartesian space', 
				'principal coordinates analysis', 
				'input pair-difference matrix & output coordinate matrix minimizing strain loss function'
			],
			'related_objects': {},
			'alternatives': [], 
			'assumptions': ['euclidean distance'],
			'variants': {
				'general': {
					'metricMDS': 'cost function is residual sum of squares'
				}
			},
			'types': [],
			'usage_intents': [],
			'problems': [],
			'intents::strategies': {},
			'functional_reasons': {},
			'insights': ["coordinate matrix x can be derived from b = x * x' with eigenvalue decomposition, and b can be computed from proximity matrix d with double centering"],
			'method_steps': [
				'find squared proximity matrix d',
				'apply double centering to compute b, using centering matrix J, with n as number of objects',
				'determine m largest eigenvalues & their eigenvectors of b, with m as number of target dimensions',
				'x is eigenvector matrix multiplied by square root of diagonal matrix of eigenvalues of b'
			],
			
		},
		'svm': {
			'definitions': [
				'non-probabilistic binary linear classifier',
				'assigns new data to one category or the other, given labeled data with two label categories',
				'maximizes difference between example data points of different categories, predicting category by side of gap'
			]
			'related_objects': {},
			'alternatives': [], # interchangeable or alternate methods, not variants of this method
			'assumptions': [],
			'variants': {
				'type': {
					'probabilistic': 'platt_scaling'
				},
				'unsupervised': {
					'clustering': 'support_vector_clustering'
				}
			},
			'types': [
				'supervised'
			],
			'usage_intents': [],
			'problems': [],
			'intents::strategies': [
				'classification': ['linear', 'nonlinear with kernel map to higher dimensional spaces'],
				'regression',
				'find_svm_classifier': {
					'descent': ['sub-gradient', 'coordinate']
				}
			],
			'functional_reasons': {},
			'insights': [],
			'method_steps': []
		},
		'kernel': {
			'definitions': [
				'method of mapping an input-output relationship to a space where different sets are linearly separable',
				'instance-based learner',

			]
			'related_objects': {
				'kernel_function': {
					'function': {
						'integration/aggregation': 'weighting function for a weighted sum', 
						'differentiation': ''.join([
							"function that calculates a weighted sum of similarities of new x' to origin data set x-values (similarities found with the kernel mapping x to x'),",
							"with weights applied to each origin input x-value's similarity to x' indicating importance of that origin input in determining y",
							"to find output y for each new x'"
						])
					}
				},
				'inner_product': {

				}
			},
			'alternatives': [],
			'assumptions': [],
			'variants': {
				'reason_why_it_varies_varied_attribute_or_variant_type': {
					'attribute_or_function': 'specific_variant'
				}
			},
			'types': [],
			'usage_intents': {
				'functions': [
					'compute differences with a lower-dimensional calculation',
					'convert function into a higher-dimensional function by replacing features with kernel function',
				],
				'neural networks': ['svm', 'kernel perceptron', 'gaussian_process', 'pca', 'canonical_correlation_analysis', 'ridge_regression', 'spectral_clustering', 'linear_adaptive_filters']
			},
			'problems': [],
			'intents::strategies': [
				'general_intent': ['specific_intent'],
				'specific_intent': {
					'general strategy': 'specific strategy'
				}
			],
			'functional_reasons': {},
			'insights': [
				'avoids computation cost of explicitly mapping a data set to another space with a feature map, using kernel functions to map to inner product spaces using existing variables'
			],
			'method_steps': []
		}

	}