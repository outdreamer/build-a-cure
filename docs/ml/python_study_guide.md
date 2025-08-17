python study guide

- questions
	- AML typologies
		- unusual customer behavior, usage of large amounts of cash, smurfing (involving numerous transactions, people, accounts, high volumes of small transactions to avoid detection threshold reporting), unusual insurance claims, association with corruption, currency exchanges, purchase of portable valuable commodities, purchase of valuable assets, commodity exchanges, use of wire transfers, underground baning, trade-based money laundering, gaming activities, abuse of non-profit organizations, investment in capital markets, mingling with legitimate business, use of shell companies, use of offshore banks, use of nominees/trusts/family/third parties, use of foreign bank accounts, identify fraud, new payment tech, use of gatekeepers to obscure beneficiary identity and fund source
	- db normalization
		- eliminates insertion/update/deletion anomalies, improves data consistency, so one piece of data is stored in one place reducing the chances of inconsistent data
		- reduces data redundancy by dividing it into multiple related tables
		- improves query performance
		- but also increases complexity, reduces flexibility, and adds performance overhead by requiring joining tables
		- first normal form: each cell contains a single value and records are unique
		- second normal form: removes partial dependencies by separating tables, removes redundant data and places it in separate tables, requiring non-key attributes to be functional on the primary key
		- third normal form: ensures non-key attributes are independent of each other which eliminates transitive dependency
		- boyce-codd normal form: refinement of 3F that requires every determinant to be a candidate key
		- fourth normal form: addresses multi-valued dependencies, ensuring there are no multiple independent multi-valued facts about an entity in a record
		- fifth normal form (protection join): relates to reconstructing info from smaller, differently arranged pieces of data
		- sixth normal form: relates to temporal data (handling changes over time) by decomposing tables further to eliminate all non-temporary redundancy
	- data buffer: physical memory (often RAM) that temporarily stores data while being moved between different locations, which help synchronize data flow so components operating at different speeds can work together, and buffers optimize performance by reducing the number of I/O operations which are usually slower than in-memory operations, where buffers are used to read/write large files efficiently, networking data is buffered during transmission to optimize performance, and buffers allow slicing/manipulation of large datasets without copying
		- the buffer protocol allows objects to expose underlying memory to other objects which is useful for zero-copy operations where data is shared without creating copies, and objects like bytes/bytearray/memoryview implement buffers
		- buffers are useful to get more than one view on the data without holding multiple copies in memory
		- flush transfers data from the program buffer to the OS buffer or directly to file/disk, allows writing immediately as opposed to waiting for the automatic flusher to flush when the buffer is full or when the file is closed
	- how to use python given limited memory
		- set memory limits for a program with the resource module, which can limit number of child processes, number of open files, CPU time or restrict the total address space, after which it will generate MemoryError exceptions when no more memory is available
		- optimize code for memory efficiency using generators/iterators, avoiding unnecessary copies, using numpy/pandas for handling large datasets, using ulimit or cgroups on linux to restrict memory usage for a python process, use tracemalloc to identify memory bottlenecks in code
	- heap memory
		- a private memory area used to store objects and data structures dynamically allocated during runtime
		- dynamic allocation: memory is allocated on demand when objects are created, objects like lists/dicts/user-defined objects are stored in the heap
		- garbage collection: the gc automatically frees memory no longer in use which prevents memory leaks, and generational garbage collection helps identify and clean up circular references
		- the GIL keeps memory management thread-safe so only one thread executes python bytecode at a time
		- python has its own memory manager that handle heap memory allocation/deallocation, using pools/arenas to optimize memory usage for small objects
		- python uses a special allocator for small objects (integer, strings) to reduce fragmentation and improve performance
		- larger objects are allocated directly from the heap
		- python tracks the reference count to an object, when it drops to zero, the object is eligible for gc
		- manage heap memory by avoiding creating unnecesssary objects, reusing objects wherever possible, using generators instead of lists, us gc and tracemalloc to debug and monitor memory usage, and delete references to objects when no longer needed
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
			    def data_generator():
			        for i in range(10 ** 6):
			            yield i
			    result = sum(data_generator())

				class DataIterator:
				    def __init__(self):
				        self.current = 0
				    def __iter__(self):
				        return self
				    def __next__(self):
				        if self.current >= 10 ** 6:
				            raise StopIteration
				        self.current += 1
				        return self.current
				data = DataIterator()
				result = sum(data)

	- whats the difference between python and java
		- Java supports OOP, is compiled and statically typed and platform-independent
			- java is compiled into bytecode and run on the Java Virtual Machine (JVM), offering better performance
		- python supports OOP/functional/procedural programming, is interpreted and dynamically typed
			- python is compiled into bytecode which is then executed by the python virtual machine and interpreted at runtime
			- python is slower than java since it uses an interpreter, is executed line-by-line, and determines data type at run time
	- whats the difference between an interface and an abstraction
		- an abstract class is a blueprint for other classes, implemented with the abc module, which can have abstract methods without implementations and concrete methods with implementations, and cant be instantiated directly, where subclasses have to implement all abstract methods
		- an interface defines a set of methods that a class has to implement, typically interfaces are implemented without abstract classes having only abstract methods, which is useful for ensuring that behaviors are implemented without specifying how they should be implemented, and doesnt allow any implementations in the interface
	- what is the difference between a stack and a queue
		- stacks use LIFO where the last element added is the first to be removed, push/pop operate on the top element, uses list.append for push, list.pop for pop, stacks are useful for undo operations and function calls, where collections.deque can be used for a stack using collections.deque.pop
		- queues use FIFO where the first element added is the first to be removed, enqueue adds an element to the end and dequeue removes the element from the front, use collections.deque.append for enqueue and collections.deque.popleft for dequeue, queues are useful for task scheduling and buffering, queue can be implemented with lists using list.pop(0) to remove the first item
		- collections.deque is optimized for fast appends/pops from both sides of the deque, so its more efficient than a list which has inefficient pop(0) operations for queues as all the elements have to be shifted by one when popping from the front of the list

	- recursion
		- recursion is where a function calls itself to solve a problem by breaking it into smaller subproblems, such as calculations, tree traversals or divide-and-conquer algorithms
			def recursive(param):
				if base_case:
					return base_param_result # prevents infinite recursion with a stopping case
				if recursive_case:
					return recursive(modified_params)
		- tail recursion is where the recursive call is the last thing the function does so no more code is executed after it returns, which is sometimes implemented like a loop to save memory, like where multiplication happens in a parameter definition so the multiplication happens before the recursive call
		- non-tail recursion is where the function does more work after the recursive call returns so it cant be optimized into a loop, like where there is multiplication after the recursive call by being outside the function call
		- recursion is easier to implement when the problem is recursive like tree traversals
		- iteration involves loops (for/while) to repeat a block of code which is usually more memory efficient bc it doesnt involve multiple stack frames like recursion
		- avoid recursion when the problem can be easily solved with loops, when recursion depth is large which risks a stack overflow, when performance is critical and function call overhead matters
		- recursion is useful for simplicity and reduced code length, but increases memory overhead especially for deep recursion and has more function calls/returns so may have slower responses and risks stack overflow if the recursion depth exceeds the stack limit

	- stack overflow: occurs when the stack like a call stack (memory used to store active function calls) is full and an attempt to push an element on to it is made, which happens bc the stack has a fixed size or memory limit, which is a common issue in recursive functions where excessive function calls consume the call stack memory like with infinite recursion

	- SOLID concepts
		- Single Responsibility: a class should only have one responsibility
		- Open-Closed: entities should be open for extension but closed for modification (add functionality without changing the existing code)
		- Liskov Substitution: objects of a superclass should be replaceable with objects of its subclasses without changing program correctness
		- Interface Segregation: clients shouldnt depend on interfaces they dont use, suggesting splitting larger interfaces into smaller interfaces
		- Dependency Inversion: high-level modules shouldnt depend on low-level modules as both should depend on abstractions, and abstractions shouldnt depend on details, details should depend on abstractions
	- how to optimize sql queries
		- limit results, select specific fields, use indexes, identify bottlenecks in execution plans using EXPLAIN or EXPLAIN PLAN, avoid correlated subqueries and replace with joins/temporary tables
	- thread-safe:
		- functions correctly when accessed by multiple threads concurrently. In a multi-threaded environment, thread-safe code prevents unexpected behavior, race conditions, or data corruption
		- race conditions: when multiple threads access/modify shared data at once, leading to inconsistent results
		- fix: avoid shared state completely by re-entrancy (code can be safely interrupted and resumed as threads have their own local state), and immutable objects whose state cant be changed after creation so only read-only data is shared
			- synchronization mechanisms can be used when state has to be shared, like mutual exclusion (ensuring only one thread accesses data at a time using locks or mutexes), and atomic operations (using operations that are indivisible ensuring that shared data is consistent), though synchronization can lead to deadlocks and negatively impact performance bc it requires acquiring/releasing locks
	- passed by value/reference:
		- mutable structures are passed by reference, immutable structures are passed by value
	- encapsulation: bundles data/attributes and methods/functions in a single unit like a class, and restricts direct access to some of the components to protect data integrity and ensure control over how its accessed/modified
		- internal details of a class are hidden, access modifiers (public, protected, private) control visibility of class attributes and methods, and getter/setter methods allow controlled access to private attributes
		- public attributes/methods are accessible from anywhere, protected attributes/methods are prefixed with an underscore and are intended to only be accessed within a class/subclasses, private attributes/methods are prefixed with double underscores and not directly accessible outside the class but can be accessed with name mangling
		- encapsulation allows data security by preventing unauthorized access/modification, code maintainability, and flexibility allowing changes to internal implementation without affecting external code
	- polymorphism: the ability of a function/method/operator to behave differently based on the object its working with, allowing for flexibility and reusability in code and making it easy to work with objects of different types in the same way
		- method polymorphism is where different classes have methods with the same name with different functionality
		- operator polymorphism is where operators like + can perform different operations based on data types, either adding integers or concatenating strings
		- function polymorphism is where functions can handle arguments of different types like adding integers or concatenating strings
		- polymorphism with inheritance is where a child class overrides a method from its parent class, providing its own implementation
		- polymorphism is useful for code reusability, flexibility by extending functionality through adding new classes/methods, and readability
	- __init__.py is for shared functions and variables across the package and creating packages, which is executed when a package is imported

- libraries/tools
	- black for formatting
	- pylint/flake8 for PEP compliance
	- cprofile and line_profiler and memory_profiler for profiling
	- pdb for debugging
	- analysis tools
		- mypy for linting/static analysis
			- static analysis identifies bugs in code without being run like XSS and SQL injection attack vectors, authentication bypass issues, and abstract injection points but can identify false positives
		- dynamic analysis
			- dynamic analysis is done on running apps but misses untested flows
		- interactive analysis
			- interactive analysis combines static flaws with limited attacks, identifying for example authentication bypass issues and testing the login endpoint with sample parameters, but requires manual testing expertise to be valuable
		- security testing
			- bandit identifies injection attack vectors, cryptographic flaws, security misconfigurations, and credential management issues but cant do taint analysis (data flow issues)
			- pyt (pytaint) identifies XSS, SQL injections, path traversal attacks
			- pysa improves on static analysis with data dependency and code context awareness to implement taint analysis and avoid false positives, identifying issues like XSS, SQL injections, path injections, OS command executions
		- pytest or unittest for unit testing
		- stress testing: stressor
		- load testing: locust
		- pentesting: scapy, nmap, impacket, pwntools, beautifulsoup, metasploit
		- regression testing: unittest, pytest-regressions
	- monitoring tools

- version updates
	- 3.14: deferred evaluation of annotations, template strings, improved error messages, a tail-call-compiled interpreter, a C API for python runtime configuration
	- 3.13: advanced interactive interpreter, JIT compiler, and a free thread mode
	- 3.12: enhanced error messages, flexible f-strings, type parameter syntax, module improvement, syntactic formalization of f-strings
	- 3.11: enhanced performance by 10 - 60%, improved error messages, exception groups, exception notes
	- 3.10: parenthesized context managers, pattern matching for complex data structures
	- 3.9: offered string methods, dictionary merge and update operators, pattern matching zoneinfo, improved type hinting
	- 3.8: new optimizations and features like positional-only parameters and the walrus operators
	- 3.7: improved performance, data classes to generate __init__ and __repr__ in classes, context variables to manage context-local state
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
		- use dicts instead of lists for lookup operations
		- use list comprehensions which are faster than loops for creating a list
		- use map function which is faster than list comprehensions for function calls and large datasets: map(lambda x: x * x, range(1000000)) instead of [x * x for x in range(1000000)]
		- use zip function to iterate two lists of equal size
		- work around the GIL to use multiple CPU cores and run multiple tasks simultaneously
			- use multiprocessing to create separate processes with their own memory space, bypassing the GIL which is useful for CPU bound tasks
				with multiprocessing.Pool(processes=4) as pool:
					results = pool.map(square_function, range(10))
			- use asyncio for IO tasks like HTTP requests or database queries to perform concurrent tasks without blocking the main thread
			- use python 3.13 which comes with free thread mode
			- use multi-threading
			- use coroutines to create concurrent asynchronous code in python to perform multiple tasks simultaneously by creating simple lightweight threads
		- use scipy and numpy (implemented in c) for numerical operations which is much faster than lists for large-scale numerical operations
		- use JIT compilation with numba which automatically compiles the function to machine code which boosts performance
			from numba import jit
			@jit(nopython=True)
	- use match-case rather than if-else
	- use built-in functions which are usually optimized for speed and are often written in C
	- write generators to return one item at a time rather than all items at once
	- check membership of an item in a list with the in keyword
	- load modules only when needed
	- avoid recursion which takes up a lot of memory and instead use iteration
	- use cython (a superset of python) to speed up slow code, cython is compiled into c which makes it faster
		save file with pyx extension and use cythonize command on the file to compile it, after which it can be imported and used like a normal function
	- use vectorized operations and broadcasting
	- use pandas to manipulate data which is faster than standard python data structures
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
	- use numpy arrays instead of lists for large data bc numpy arrays use less memory and are faster
	- use sets to check if an item is in a group of items, dicts to efficiencly store and retrieve data, and tuples to group values together
	- use lazy loading of data to only load data when needed
	- use hdfs or parquet formats to save data on disk and load only the parts that are needed
	- use memory_profiler or psutil to identify memory leaks

- other tips
	- use context managers to handle resources (files, sockets, db connections) in an efficient way by defining a context in which a resource is used and automatically open and close the resource
	- use try-except blocks to handle exceptions rather than failing
	- group errors with ExceptionGroup to handle them all at once
	- use the traceback module to see detailed error info
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
		- fix: validate sql query input, use ORM with named parameters instead of query string building
	- XSS (cross-site scripting): inject malicious scripts into trusted websites. These scripts are executed in the victim's browser, enabling attackers to steal sensitive information, manipulate website content, or perform unauthorized actions on behalf of the user
		- fix: validate http input/output, validate database input/output, validate scripts in webpages with content security policies using nonces in scripts, validate user input, encode output before including them in html to prevent execution of scripts, use security headers like Content-Type, avoid using eval() or innerHTML without validation
	- ARP spoofing: associates the attacker's MAC address with the IP address of another host, causing any traffic meant for that IP address to be sent to the attacker instead. ARP spoofing may allow an attacker to intercept data frames on a network, modify the traffic, or stop all traffic. Often the attack is used as an opening for other attacks, such as denial of service, man in the middle, or session hijacking attacks
		- fix: static ARP entries, software to certify or cross-check ARP responses
	- MITM: https spoofing, ssl/tls stripping, arp spoofing, dns spoofing, session hijacking, man-in-the-browser, wi-fi MITM, email hijacking, replay attacks, fake certificate authority are MITM attack types
		- fix: mutual authentication, recorded attestments, HTTP public key pinning (whitelist of public key hashes provided by server), using signatures to authenticate DNS records
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
		- use SAST (bandit, veracode) and DAST tools (burpsuite, OWASP zed attack proxy, arachni)
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

- sources
	https://wpexperts.io/blog/python-version-history/
	https://snyk.io/blog/python-security-best-practices-cheat-sheet/
	https://securecodingpractices.com/python-secure-coding-best-practices/
	https://www.programmingworld.tech/blog/optimizing-python-code-for-performance-tips-and-tools