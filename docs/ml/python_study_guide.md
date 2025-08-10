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

- handlers for security bugs
	- cross site scripting
	- log injection
	- sql injection
		- use parameterized sql queries instead of string building
	- security tips
		- use type annotations
			- for example, use the Literal type annotation to validate a string matches items in a static list and use type checking tools like linters to check that type annotations are followed
		- deserialize with caution
			- the pickle module is insecure, where a better alternative is json or PyYAML which allows serialization/deserialization to/from YAML, which should be used with yaml.SafeLoader to avoid attack vectors even though it cant load custom classes
			- use defusedxml to avoid xml security issues like DOS attacks or external entity expansion where an external source is referenced
		- sanitize external data
			- schema is a library that validates data structures like from config files, forms, external services or command line parsing or converted from JSON/YAML to python data types
			- bleach is a library that escapes or strips markup and attributes
			- jinja is a templating engine that auto-escapes to prevent XSS using markupsafe
			- use named parameters to prevent SQL injections instead of building a query string, or use object relationship mapping tools like sqlalchemy
		- scan code with tools like bandit
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
