python study guide

- libraries/tools
	- black for formatting
	- pylint/flake8 for PEP compliance
	- security testing
		- bandit identifies injection attack vectors, cryptographic flaws, security misconfigurations, and credential management issues but cant do taint analysis (data flow issues)
		- pyt (pytaint) identifies XSS, SQL injections, path traversal attacks
		- pysa improves on static analysis with data dependency and code context awareness to implement taint analysis and avoid false positives, identifying issues like XSS, SQL injections, path injections, OS command executions
	- pytest or unittest for unit testing
	- cprofile for profiling
	- pdb for debugging
	- mypy for linting/static analysis
		- static analysis identifies bugs in code without being run like XSS and SQL injection attack vectors, authentication bypass issues, and abstract injection points but can identify false positives
	- dynamic analysis
		- dynamic analysis is done on running apps but misses untested flows
	- interactive analysis
		- interactive analysis combines static flaws with limited attacks, identifying for example authentication bypass issues and testing the login endpoint with sample parameters, but requires manual testing expertise to be valuable
	- pentesting
	- regression testing

- design patterns

- version updates

- optimizations
	- address reasons for bottlenecks (inefficient algorithms with polynomial runtime, memory consumption, IO operations, Global Interpreter Lock which limits concurrent execution)
		- use cprofile (cprofile.run('function_name'))
		- use dicts instead of lists for lookup operations
		- use list comprehensions which are faster than loops for creating a list
		- use map function which is faster than list comprehensions for function calls and large datasets: map(lambda x: x * x, range(1000000)) instead of [x * x for x in range(1000000)]
		- work around the GIL
			- use multiprocessing to create separate processes with their own memory space, bypassing the GIL which is useful for CPU bound tasks
				with multiprocessing.Pool(processes=4) as pool:
					results = pool.map(square_function, range(10))
			- use asyncio for IO tasks like HTTP requests or database queries to perform concurrent tasks without blocking the main thread
			- use python 3.13 which comes with free thread mode
		- use numpy (implemented in c) for numerical operations which is much faster than lists for large-scale numerical operations
		- use JIT compilation with numba which automatically compiles the function to machine code which boosts performance
			from numba import jit
			@jit(nopython=True)

	- use built-in functions which are usually optimized for speed and are often written in C
	- write generators to return one item at a time rather than all items at once
	- check membership of an item in a list with the in keyword
	- load modules only when needed
	- use sets and unions instead of loops where possible
	- use multiple assignment when possible
	- avoid global variables to help keep track of scope and avoid unnecessary memory usage, also local variables are faster to retrieve than global variables
	- use join rather than + to concatenate strings whch avoids creating a new string for each component
	- use while 1 for infinite loops
	- exit early (raise exceptions or exit first under failure conditions where possible to avoid executing code that will fail)
	- use itertools for combinations/permutations
	- use memoization like decorator caching such as with @functools.lru_cache(maxsize=100)
	- use keys for sorts using operator.itemgetter()
	- dont use sets for conditions like checking membership of an item in a list
	- use linked lists which allocate memory as needed, each item in a linked list can be stored in a different location, although lookup times are slower in linked lists, linked lists are faster at adding elements at the start of the linked list


- handlers for security bugs
	- cross site scripting
	- log injection
	- sql injection
		- use parameterized sql queries instead of string building
	- security tips
		- hash and salt passwords with bcrypt
		- set strict access controls
		- monitor query performance
		- log suspicious patterns
		- use environment variables for configuration
		- use structured logging, gitignore logs, use logging level control, and avoid logging sensitive data
		- minimize dependencies
		- use precommit hooks with security scanning tools
		- use standard auth libraries like requests-oauthlib or Flask-Login
		- apply session management to expire tokens/sessions, rate limit API requests, and validate emails
		- use whitelists to support valid requests
		- use prepared statements to send a query template and then send the values for fields in the template
		- check hashes of downloads
		- have a secure backup strategy in case of database corruption or sql injection attacks
		- move credentials to .env files
		- use secret managers in prod
		- gitignore configuration files
		- patch dependencies regularly
		- rotate keys regularly
		- handle cookies securely
		- set up Cross-Site Request Forgery (CSRF) protection by using flask_wtf to use unpredictable CSRF tokens in forms which are verified by servers when requests are made, so that valid requests cant be forged
		- keep tokens private
		- use APIs securely
		- use secure libraries
		- use SAST (bandit, veracode) and DAST tools
		- use SSL/TLS connections, enforce HTTPS to protect against MITM attacks
		- avoid using root access
		- set file permissions (0 = none, 1 = x, 2 = w, 3 = w/x, 4 = r, 5 = r/x, 6 = r/w, 7 = r/w/x)
		- avoid eval() (use ast.literal_eval()), compile(), exec(), input() without validation, pickle.loads(), subprocess.call() with shell=True
		- validate character encoding (unicode, ascii) or character sets and input length
		- use type annotations and linters to check types
			- for example, use the Literal type annotation to validate a string matches items in a static list and use type checking tools like linters to check that type annotations are followed
		- deserialize with caution
			- the pickle module is insecure, where a better alternative is json or PyYAML which allows serialization/deserialization to/from YAML, which should be used with yaml.SafeLoader to avoid attack vectors even though it cant load custom classes
			- use defusedxml to avoid xml security issues like DOS attacks or external entity expansion where an external source is referenced
		- sanitize external data
			- schema is a library that validates data structures like from config files, forms, external services or command line parsing or converted from JSON/YAML to python data types
			- bleach is a library that escapes or strips markup and attributes
			- jinja is a templating engine that auto-escapes to prevent XSS using markupsafe
			- use named parameters to prevent SQL injections instead of building a query string, or use object relationship mapping (ORM) tools like sqlalchemy
		- download packages cautiously
			- check package names for typos and check snyk advisor or use safety CLI or install pip audit or check github issues/dependabot alerts for known security issues with packages
			- use pip freeze to record environment-specific package versions
			- keep dependencies updated to use code with latest security fixes
		- review dependency vulnerabilities and licenses
			- avoid GPL, AGPL, LGPL, and EPL and use code with permissive licenses (MIT, Apache, BSD) where possible
		- dont use the system python version which is unlikely to be current
		- use virtual environments with venv to isolate projects (including python versions used, libraries, and scripts)
		- set DEBUG=False in prod to avoid publishing overly informative error messages
		- format strings cautiously
			- use templating tools like string.template to format strings with parameters to avoid evaluating python statements like f-strings evaluate python statements

- attributes
	- mutable structures are passed by reference, immutable structures are passed by value
	- dynamically typed
	- compiled to bytecode then interpreted at runtime

- sources
	https://www.geeksforgeeks.org/python/python-design-patterns/
	https://wpexperts.io/blog/python-version-history/
	https://snyk.io/blog/python-security-best-practices-cheat-sheet/
	https://securecodingpractices.com/python-secure-coding-best-practices/
	https://www.programmingworld.tech/blog/optimizing-python-code-for-performance-tips-and-tools