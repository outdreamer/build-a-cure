python study guide

- questions

	- how to use python given limited memory
		- set memory limits for a program with the resource module, which can limit number of child processes, number of open files, CPU time or restrict the total address space, after which it will generate MemoryError exceptions when no more memory is available
		- optimize code for memory efficiency using generators/iterators, avoiding unnecessary copies, using numpy/pandas for handling large datasets, using ulimit or cgroups on linux to restrict memory usage for a python process, use tracemalloc to identify memory bottlenecks in code
	
	- heap memory
		- a private memory area used to store objects and data structures dynamically allocated during runtime
		- dynamic allocation: memory is allocated on demand when objects are created, objects like lists/dicts/user-defined objects are stored in the heap
		- garbage collection: the gc automatically frees memory no longer in use which prevents memory leaks, and generational garbage collection helps identify and clean up circular references
		- the GIL keeps memory management thread-safe so only one thread executes python bytecode at a time
		- python has its own memory manager that handles heap memory allocation/deallocation, using pools/arenas to optimize memory usage for small objects
		- python uses a special allocator for small objects (integer, strings) to reduce fragmentation and improve performance
		- larger objects are allocated directly from the heap
		- python tracks the reference count to an object, when it drops to zero, the object is eligible for gc
		- manage heap memory by avoiding creating unnecesssary objects, reusing objects wherever possible, using generators instead of lists, use gc and tracemalloc to debug and monitor memory usage, and delete references to objects when no longer needed
		- unlike stack memory which is used for static memory allocation and has a fixed size, heap memory allows for allocation of memory at runtime, so the size of the memory can grow or shrink as needed so its useful for storing objects whose size is not known at compile time
			- heap memory can be accessed from anywhere in the program, whereas stack memory is limited to be accessed by the function in which it was allocated
			- heap memory is more flexible but can be slower to access than stack memory bc of dynamic allocation/garbage collection overhead
	
	- detect a memory leak
		- memory leak: when objects that are no longer being used are not correctly deallocated by the garbage collector
		- identify memory leaks:
			- tracemalloc detects memory consuming lines in python, the code locations where the largest memory blocks are being allocated may indicate a memory leak
			- gc can identify objects that are not being collected
			- objgraph visualizes object references to find leaks by identifying objects being retained unnecessarily
			- memory profiler tracks memory usage line by line, identifying any areas of the code where the memory usage is significantly increasing which may indicate a memory leak
		- fix memory leaks:
			- identify when object references are not removed when not needed and remove them by setting them to None or deleting them
			- use weakref (weak references dont prevent deallocation by the gc), though weak references are useless once the object they reference has been deallocated so the code needs to handle that
			- identify large lists/arrays that arent needed all at once and use generators instead (use yield keyword) or iterators (implelment a __iter__ and __next__ method in the class)

	- whats are some similarities/differences between python and java
		- Java supports OOP, is compiled into bytecode and interpreted at runtime by the JVM, and statically typed and platform-independent
			- java is compiled into bytecode, then translated by the JVM into machine code and run on the Java Virtual Machine (JVM), offering better performance
			- JIT compilers identify frequently run code which they compile into machine code at runtime which is then cached and reused, compiling byte code into machine code like the JVM
			- the compilation step ensures portability, where the interpretation and JIT compilation ensure runtime performance
		- python supports OOP/functional/procedural programming, is interpreted and dynamically typed
			- python is compiled into bytecode which is then executed by the python virtual machine and interpreted at runtime
			- python is slower than java since it uses an interpreter, is executed line-by-line, and determines data type at run time

	- whats the difference between an interface and an abstraction
		- an abstract class is a blueprint for other classes, implemented with the abc module, which can have abstract methods without implementations and concrete methods with implementations, and cant be instantiated directly, where subclasses have to implement all abstract methods
		- an interface defines a set of methods that a class has to implement, typically interfaces are implemented with abstract classes having only abstract methods, which is useful for ensuring that behaviors are implemented without specifying how they should be implemented, and doesnt allow any implementations in the interface

	- __init__.py is for shared functions and variables across the package and creating packages, which is executed when a package is imported

	- passed by value/reference:
		- mutable structures are passed by reference, immutable structures are passed by value

	- scopes: local, enclosed, global, and built-in are the scopes in python
	
- libraries/tools
	- black for formatting
	- pylint/flake8 for PEP compliance
	- cprofile and line_profiler for profiling, use memory_profiler for profiling and identifying memory leaks, use psutil for identifying memory leaks
	- pdb for debugging
	- analysis tools
		- coverage analysis: coverage.py
		- linting/static analysis: mypy
			- static analysis identifies bugs in code without being run like XSS and SQL injection attack vectors, authentication bypass issues, and abstract injection points but can identify false positives
			- pysa improves on static analysis with data dependency and code context awareness to implement taint analysis and avoid false positives, identifying issues like XSS, SQL injections, path injections, OS command executions
		- dynamic analysis: dynapyt, pyinstrument, burpsuite, OWASP zed attack proxy, arachni
			- dynamic analysis is done on running apps but misses untested flows
		- interactive analysis: pytest and ipython
			- interactive analysis combines static flows with limited attacks, identifying for example authentication bypass issues and testing the login endpoint with sample parameters, but requires manual testing expertise to be valuable
		- security testing
			- veracode
			- bandit identifies injection attack vectors, cryptographic flaws, security misconfigurations, and credential management issues but cant do taint analysis (data flow issues like unused variables or multiple variable declarations or variables deallocated before usage)
			- pyt (pytaint) identifies XSS, SQL injections, path traversal attacks
		- unit testing: pytest or unittest
		- stress testing: stressor
		- load testing: locust
		- pentesting: scapy, nmap, impacket, pwntools, beautifulsoup, metasploit
		- regression testing: unittest, pytest-regressions
	- monitoring tools: prometheus with grafana, datadog, sentry, new relic, ELK stack, pyroscope

- version updates
	- 3.14: deferred evaluation of annotations, template strings, improved error messages, a tail-call-compiled interpreter, a C API for python runtime configuration
	- 3.13: advanced interactive interpreter, JIT compiler, and a free thread mode
	- 3.12: enhanced error messages, flexible f-strings, type parameter syntax, module improvement, syntactic formalization of f-strings
	- 3.11: enhanced performance by 10 - 60%, improved error messages, exception groups, exception notes
	- 3.10: parenthesized context managers, pattern matching for complex data structures
	- 3.9: offered string methods, dictionary merge and update operators, pattern matching, zoneinfo, improved type hinting
	- 3.8: new optimizations and features like positional-only parameters and the walrus operators
	- 3.7: improved performance, data classes to generate __init__ and __repr__ in classes, context variables to manage context-local state, ordered dictionaries by default
	- 3.6: formatted string literals, asynchronous generators, underscores in numeric literals
	- 3.5: type hints/annotations to function arguments and return values, added async, await
	- 3.4: asyncio and pathlib
	- 3.0: erased redundant constructs from 2.7, new syntax and semantics, removal of deprecated features, print function
	- 2.7: improved syntax, set literals, ordered dictionaries
	- 2.0: list comprehensions and garbage collection
	- 1.5: unicode support, enhanced standard library, facilitated internationalization
	- 1.0: exception handling, map, filter, reduce, improved code error management and exceptions

- optimizations
	- address reasons for bottlenecks (inefficient algorithms with polynomial runtime, memory consumption, IO operations, Global Interpreter Lock which limits concurrent execution)
		- use cprofile (cprofile.run('function_name')) and line_profiler and memory_profiler and timeit for timing function calls and pytest-benchmark for identifying bottlenecks
		- use pypy for JIT compilation
			- Just-In-Time (JIT) compilation is a technique used to improve the performance of Python code by compiling parts of the code into machine code at runtime. This allows Python programs to execute faster
			- use JIT compilation with numba which automatically compiles the function to machine code which boosts performance
				from numba import jit
				@jit(nopython=True)
		- work around the GIL to use multiple CPU cores and run multiple tasks simultaneously
			- use multiprocessing to create separate processes with their own memory space, bypassing the GIL which is useful for CPU bound tasks
				with multiprocessing.Pool(processes=4) as pool:
					results = pool.map(square_function, range(10))
			- use asyncio/coroutines for IO tasks like HTTP requests or database queries to perform concurrent tasks without blocking the main thread
			- use python 3.13 which comes with free thread mode

	- use match-case rather than if-else
	- use built-in functions which are usually optimized for speed and are often written in C
	- write generators to return one item at a time rather than all items at once
	- check membership of an item in a list with the in keyword
	- load modules only when needed
	- avoid recursion which takes up a lot of memory and instead use iteration
	- use cython (a superset of python) to speed up slow code, cython is compiled into c which makes it faster
		save file with pyx extension and use cythonize command on the file to compile it, after which it can be imported and used like a normal function
	- use vectorized operations and broadcasting with numpy
		- Broadcasting in NumPy allows us to perform arithmetic operations on arrays of different shapes without reshaping them. It automatically adjusts the smaller array to match the larger array's shape by replicating its values along the necessary dimensions. This makes element-wise operations more efficient by reducing memory usage and eliminating the need for loops
	- use pandas to manipulate data which is faster than standard python data structures
	- use sets and unions instead of loops where possible
	- use multiple assignment when possible
	- avoid global variables to help keep track of scope and avoid unnecessary memory usage, also local variables are faster to retrieve than global variables
	- use join rather than + to concatenate strings whch avoids creating a new string for each component
	- use while 1 for infinite loops
	- exit early (raise exceptions or exit first under failure conditions where possible to avoid executing code that will fail)
	- use itertools for combinations/permutations
	- use memoization like decorator caching such as with @functools.lru_cache(maxsize=100)
	- use keys for sorts using operator.itemgetter(): sorted(data, key=itemgetter(0))
	- dont use sets for conditions like checking membership of an item in a list, its not usually faster to change list format to a set
	- use linked lists which allocate memory as needed for frequent insertions/deletions, as linked lists avoid the overhead of resizing like arrays, each item in a linked list can be stored in a different location, although lookup times are slower in linked lists bc items are accessed sequentially, linked lists are faster at adding elements at the start of the linked list
	- use numpy arrays instead of lists for large data bc numpy arrays use less memory and are faster
	- use dicts to efficiently store and lookup data, and tuples to group values together
	- use tuples to consume less memory and access/create faster than lists
	- use lazy loading of data to only load data when needed, using generators, __getattr__, or functools.lru_cache
	- use hdfs or parquet formats to save data on disk and load only the parts that are needed
	- use scipy and numpy (implemented in c) for numerical operations which is much faster than lists for large-scale numerical operations
	- use list comprehensions which are faster than loops for creating a list
	- use map function which is faster than list comprehensions for function calls and large datasets: map(lambda x: x * x, range(1000000)) instead of [x * x for x in range(1000000)]
	- use zip function to iterate two lists of equal size

- other tips
	- use context managers to handle resources (files, sockets, db connections) in an efficient way by defining a context in which a resource is used and automatically open and close the resource
	- use try-except blocks to handle exceptions rather than failing
	- group errors with ExceptionGroup to handle them all at once
	- use the traceback module to see detailed error info: traceback.print_exc() or traceback.format_exc()
	- use TaskGroups to run similar tasks together as opposed to asyncio.gather which fails on the first exception
	- use decimal instead of float for calculations
	- use f"{value:.2f}" to control decimal places
	- use math module for square roots, logs, and trig functions
	- use numpy for faster, more complex operations like matrix operations, fourier transforms and statistical operations
	- use scipy for scientific operations, signal processing, optimization, interpolation, and integration
	- // is integer division which rounds down to the nearest integer, where negative results of integer division are rounded down toward negative infinity and where / is float division

- handlers for security bugs
	- log injection: validate inputs to logs
	- SQL injection: malicious queries/scripts inserted into sql created using unvalidated string input
		- fix: validate sql query input, use ORM like sqlalchemy with named parameters instead of query string building
	- XSS (cross-site scripting): injections of malicious scripts into trusted websites. These scripts are executed in the victim's browser, enabling attackers to steal sensitive information, manipulate website content, or perform unauthorized actions on behalf of the user
		- fix: validate http/user/database input/output, validate scripts in webpages with content security policies using nonces in scripts, escape output before including it in html to prevent execution of scripts with html.escape(user_input), use security headers like Content-Type, avoid using eval() or innerHTML without validation
	- ARP spoofing: associates the attacker's MAC address with the IP address of another host, causing any traffic meant for that IP address to be sent to the attacker instead. ARP spoofing may allow an attacker to intercept data frames on a network, modify the traffic, or stop all traffic. Often the attack is used as an opening for other attacks, such as denial of service, man in the middle, or session hijacking attacks
		- fix: static ARP entries, software to certify or cross-check ARP responses
	- MITM: https/arp/dns spoofing, ssl/tls stripping, email/session hijacking, man-in-the-browser, wi-fi MITM, replay attacks, fake certificate authority are MITM attack types
		- fix: mutual authentication, recorded attestments, HTTP public key pinning (pinning public key hashes provided by server), using signatures to authenticate DNS records
	- Cross-Site Request Forgery (CSRF): 
		- fix: use flask_wtf to create unpredictable CSRF tokens in forms which are verified by servers when requests are made, so that valid requests cant be forged
	- security tips
		- hash and salt passwords with bcrypt
		- set strict access controls
		- monitor query performance
		- log suspicious patterns
		- use environment variables for configuration
		- use structured logging, use logging level control, and avoid logging sensitive data
		- minimize dependencies
		- use precommit hooks with security scanning tools
		- use standard auth libraries like requests-oauthlib or Flask-Login
		- apply session management to expire tokens/sessions
		- rate limit API requests
		- validate emails
		- use whitelists to support valid requests
		- use prepared statements to send a query template and then send the values for fields in the template
			- a prepared statement is a feature where the database pre-compiles SQL code and stores the results, separating it from data, where the query can be executed later
			- a prepared statement takes the form of a pre-compiled template into which constant values are substituted during each execution
		- check hashes of downloads
		- have a secure backup strategy in case of database corruption or sql injection attacks
		- move credentials to .env files
		- use secret managers in prod
		- gitignore configuration files
		- patch dependencies regularly
		- rotate keys regularly
		- handle cookies securely
		- keep API tokens private
		- use APIs securely
		- use secure libraries
		- use SAST (bandit, veracode) and DAST tools (burpsuite, OWASP zed attack proxy, arachni)
		- use SSL/TLS connections, enforce HTTPS to protect against MITM attacks
		- avoid using root access
		- set file permissions (0 = none, 1 = x, 2 = w, 3 = w/x, 4 = r, 5 = r/x, 6 = r/w, 7 = r/w/x)
		- avoid eval(), compile(), exec(), input() without validation, pickle.loads(), subprocess.call() with shell=True
			- use ast.literal_eval() instead
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
			- use templating tools like string.template to format strings with parameters to avoid evaluating python statements, like how f-strings evaluate python statements

- sources
	https://wpexperts.io/blog/python-version-history/
	https://snyk.io/blog/python-security-best-practices-cheat-sheet/
	https://securecodingpractices.com/python-secure-coding-best-practices/
	https://www.programmingworld.tech/blog/optimizing-python-code-for-performance-tips-and-tools