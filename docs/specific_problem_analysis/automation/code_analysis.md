# Software Concepts


## Interface Analysis

  - interface analysis example with code components: 
    - usage: application, expectation/intention convergence, permission, error, interaction
    - change: difference/similarity types (difference in value, similarity in position), update, initialization, association/relation, removal, move
    - state, storage (database, distributed sync, cache, data structure), data
    - organization (index, business logic)
    - priority/intent/requirement
    - variable (parameter, attribute, input/output, type)
    - logic (function, fit, completeness, validity, match, gap, connection)
    - assumption: legitimate assumption (context) or false assumption (logic gap)
    - cause, responsibility, dependency
    - scope/relevance, system/context, meaning/integration (system context fit), understanding (state of application relative to intended/optimal state, given problem/intent/tech understanding)
    - interface analysis answers 'how do these concepts interact in a typical implementation', and 'what is the graph of their optimal interactions', with output like:
      - sub-intent of lines of code should match intents of code blocks, functions, & other larger units & structures of code
      - cause, intent, & meaning of code should align (the cause of a function call should match the intents supported by the function and the meaning of the function fit in the system context)
      - workflows & other larger structures of code usage shouldnt produce contradictory cause/intent/meaning/related objects (calling two functions in isolation shouldnt contradict the meaning of calling those functions in a sequence, all other things being equal - otherwise its a potential vuln)
      - the function lifecycle can start at an abstract set of filters or other function generators, then resolves to a structure containing logical tree structure, then resolves to a particular logical tree as more information about usage is gathered, then resolves to a set of core functions that are used to optimize that function tree rather than using more complex functions with potential side effects not already calculated (unlike core functions), then resolves to an input/output map once usage stops changing.
      - functions of an intent should be derived from general app intents & reduced into a core function set, before writing code for each function
      - problem types of code often involve conceptual or other interface mismatches, like a mismatch between responsibility & exit behavior, or a mismatch between types, or a mismatch in user intent & dev expectation, or a mismatch between function set intent & application intent
        - many problem types involve structural mismatches, like a sequence that should be a network, or a causal circuit that should be a node-to-node or interface connection
      - functions should have state (rather than being coded once at a particular abstraction level), and their state should change according to usage & integration with other functions & components
      - function-generating & function-deriving code should always be stored with an application in case the actual executed code is corrupted/deleted
      - probable contexts of an app or other components should be continuously re-generated & their integrations re-calculated and tested for, rather than a particular manually generated set of contexts
      - the organization of functions should also be continuously re-calculated according to the emerging meaning of an application (as it becomes more static in intent & usage, it should be transferred to a database rather than existing as a dynamically updated code-base)
      - the purpose of a function, app or other component should be to invalidate itself - so the final state of a function is erasing itself once the user doesnt need it
      - functions should be entitled to push back on general app or other containing structure intents, if they are capable of spotting a probleem that could cascade upward that the app or other structures cannot (just like an engineer can see problems that the organization or industry cannot bc of incentive conflicts, profit cycles, & other structures)

## Software stack

  - stack layers
    UI: templates, user event input processing, client (browser), config (browser settings), adjacent resources (active plugins), dependencies (SSL certs, keys, permissions, caches)
    Application server: handle (apply security config, namespacing, permissions, respond with error codes) & route user requests to application resources (code base, access, process/CPU/memory allowance)
    Memory layer: buffers, volatile vs. persistent memory, memory access, latency (request/response time difference)
    Process layer: process vs. thread
    Data store: store metadata (timestamps, indexes), state (cache), records (database rows), schema (database table design), references (key-value maps), objects (class instances, migration data)
    Infrastructure: Servers, Databases, Config, Pipelines, Environments, Containers, Virtual Machines, OS, Machine Images, Disks
    Networking layer: DNS, load balancer, proxies, VPN
    Environment Layer: debugging, sandbox, pentesting, dev/quality assurance/test/production
    Version Layer: data model governance (data versions, model versions), code versions, language versions, virtual environment versions, version sync/update/interaction strategy
    Security layer: encryption algorithms, key store, permissions, firewalls, gpg, hashing, signatures, certificates, ACL access control lists
    Rule Layer: protocols, functions, rule access (permissions), rule enforcement (type checking)
    System Layer: OS, config, code, change tools (auto-updates, package managers), compilers/parsers/interpreters, languages, processes, ports
    Isolation/Interaction Layer: competing/shared resources/processes, containers, cross-layer interactions, integration of code components, interaction of code & OS, interaction of processes
    Concept Layer: 
      Tests: 
        - concepts: clarity, responsibility, resiliency, necessity, scale, optimization, usage, extremes, standards, expectations, intent, meaning, cause, robustness
        - alignments/matching: user intention & dev expectation matching, risk/trust matching, code requirements vs. possible functionality matching

## Philosophies/paradigms
  
  - software dev life cycle:
    - initiation
    - system concept development
    - planning
    - requirement analysis
    - design
    - development
    - integration/test
    - implementation
    - operations/maintenance
    - disposition

  - 12 app factors (https://12factor.net/)

    I. Codebase: One codebase tracked in revision control, many deploys
    II. Dependencies: Explicitly declare and isolate dependencies
    III. Config: Store config in the environment
    IV. Backing services: Treat backing services as attached resources
    V. Build, release, run: Strictly separate build and run stages
    VI. Processes: Execute the app as one or more stateless processes
    VII. Port binding: Export services via port binding
    VIII. Concurrency: Scale out via the process model
    IX. Disposability: Maximize robustness with fast startup and graceful shutdown
    X. Dev/prod parity: Keep development, staging, and production as similar as possible
    XI. Logs: Treat logs as event streams
    XII. Admin processes: Run admin/management tasks as one-off processes

  - coding practices
    - keep it simple
    - dont repeat yourself
    - separation of concerns

    - code smells (reduce system/structural problem types)

      - structural problem types:

        - mismatches

          - intent mismatches

            - the intent of a function
              
              - is:
                - to capture unique logic (so it shouldnt be repeated but imported)
              
              - is not:
                - to be complex (so it should be only as complex as required)

      - examples: https://en.wikipedia.org/wiki/Code_smell

        Application-level smells:

            Duplicated code: identical or very similar code exists in more than one location.
            Contrived complexity: forced usage of overcomplicated design patterns where simpler design would suffice.
            Shotgun surgery: a single change needs to be applied to multiple classes at the same time.
            Uncontrolled side effects: very easy to cause runtime exceptions and unit tests can't capture it.
            Variable mutations: very hard to refactor code since the actual value is unpredictable and hard to reason about.
            Boolean blindness: easy to assert on the opposite value and still type checks.

        Class-level smells:

            Large class: a class that has grown too large. See God object.
            Feature envy: a class that uses methods of another class excessively.
            Inappropriate intimacy: a class that has dependencies on implementation details of another class. See Object orgy.
            Refused bequest: a class that overrides a method of a base class in such a way that the contract of the base class is not honored by the derived class. See Liskov substitution principle.
            Lazy class / freeloader: a class that does too little.
            Excessive use of literals: these should be coded as named constants, to improve readability and to avoid programming errors. Additionally, literals can and should be externalized into resource files/scripts, or other data stores such as databases where possible, to facilitate localization of software if it is intended to be deployed in different regions.
            Cyclomatic complexity: too many branches or loops; this may indicate a function needs to be broken up into smaller functions, or that it has potential for simplification.
            Downcasting: a type cast which breaks the abstraction model; the abstraction may have to be refactored or eliminated.[8]
            Orphan variable or constant class: a class that typically has a collection of constants which belong elsewhere where those constants should be owned by one of the other member classes.
            Data clump: Occurs when a group of variables are passed around together in various parts of the program. In general, this suggests that it would be more appropriate to formally group the different variables together into a single object, and pass around only this object instead.[9][10]

        Method-level smells:

            Too many parameters: a long list of parameters is hard to read, and makes calling and testing the function complicated. It may indicate that the purpose of the function is ill-conceived and that the code should be refactored so responsibility is assigned in a more clean-cut way.
            Long method: a method, function, or procedure that has grown too large.
            Excessively long identifiers: in particular, the use of naming conventions to provide disambiguation that should be implicit in the software architecture.
            Excessively short identifiers: the name of a variable should reflect its function unless the function is obvious.
            Excessive return of data: a function or method that returns more than what each of its callers needs.
            Excessive comments: a class, function or method has irrelevant or trivial comments. A comment on an attribute getter is a good example.
            Excessively long line of code (or God Line): A line of code which is too long, making the code difficult to read, understand, debug, refactor, or even identify possibilities of software reuse. Example: new XYZ(s).doSomething(buildParam1(x), buildParam2(x), buildParam3(x), a + Math.sin(x)*Math.tan(x*y + z)).doAnythingElse().build().sendRequest();



## Design patterns (relationship types of software components)

      - Creational patterns 
        - Abstract factory  Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
        - Builder Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.
        - Dependency Injection  A class accepts the objects it requires from an injector instead of creating the objects directly.
        - Factory method  Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
        - Lazy initialization Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. This pattern appears in the GoF catalog as "virtual proxy", an implementation strategy for the Proxy pattern.
        - Multiton  Ensure a class has only named instances, and provide a global point of access to them.
        - Object pool Avoid expensive acquisition and release of resources by recycling objects that are no longer in use. Can be considered a generalisation of connection pool and thread pool patterns.
        - Prototype Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum.
        - Resource acquisition is initialization (RAII) Ensure that resources are properly released by tying them to the lifespan of suitable objects.
        - Singleton Ensure a class has only one instance, and provide a global point of access to it.

      - Structural patterns 
        - Adapter, Wrapper, or Translator Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator.
        - Bridge  Decouple an abstraction from its implementation allowing the two to vary independently.
        - Composite Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
        - Decorator Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.
        - Extension object  Adding functionality to a hierarchy without changing the hierarchy.
        - Facade  Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
        - Flyweight Use sharing to support large numbers of similar objects efficiently.
        - Front controller  The pattern relates to the design of Web applications. It provides a centralized entry point for handling requests.
        - Marker  Empty interface to associate metadata with a class.
        - Module  Group several related elements, such as classes, singletons, methods, globally used, into a single conceptual entity.
        - Proxy Provide a surrogate or placeholder for another object to control access to it.
        - Twin allows modeling of multiple inheritance in programming languages that do not support this feature.

      - Behavioral patterns 
        - Blackboard  Artificial intelligence pattern for combining disparate sources of data (see blackboard system)
        - Chain of responsibility Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
        - Command Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations.
        - Interpreter Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
        - Iterator  Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
        - Mediator  Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to vary independently.
        - Memento Without violating encapsulation, capture and externalize an object's internal state allowing the object to be restored to this state later.
        - Null object Avoid null references by providing a default object.
        - Observer or Publish/subscribe Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.
        - Servant Define common functionality for a group of classes. The servant pattern is also frequently called helper class or utility class implementation for a given set of classes. The helper classes generally have no objects hence they have all static methods that act upon different kinds of class objects.
        - Specification Recombinable business logic in a Boolean fashion.
        - State Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
        - Strategy  Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
        - Template method Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
        - Visitor Represent an operation to be performed on the elements of an object structure. Visitor lets a new operation be defined without changing the classes of the elements on which it operates.

      - Concurrency patterns  
        - Active Object Decouples method execution from method invocation that reside in their own thread of control. The goal is to introduce concurrency, by using asynchronous method invocation and a scheduler for handling requests.
        - Balking Only execute an action on an object when the object is in a particular state.
        - Binding properties  Combining multiple observers to force properties in different objects to be synchronized or coordinated in some way.[22]
        - Compute kernel  The same calculation many times in parallel, differing by integer parameters used with non-branching pointer math into shared arrays, such as GPU-optimized Matrix multiplication or Convolutional neural network.
        - Double-checked locking  "Reduce the overhead of acquiring a lock by first testing the locking criterion (the 'lock hint') in an unsafe manner; only if that succeeds does the actual locking logic proceed.
        - Can be unsafe when implemented in some language/hardware combinations. It can therefore sometimes be considered an anti-pattern."
        - Event-based asynchronous  Addresses problems with the asynchronous pattern that occur in multithreaded programs.[23]
        - Guarded suspension  Manages operations that require both a lock to be acquired and a precondition to be satisfied before the operation can be executed.
        - Join  Join-pattern provides a way to write concurrent, parallel and distributed programs by message passing. Compared to the use of threads and locks, this is a high-level programming model.
        - Lock  One thread puts a "lock" on a resource, preventing other threads from accessing or modifying it.[24]
        - Messaging design pattern (MDP)  Allows the interchange of information (i.e. messages) between components and applications.
        - Monitor object  An object whose methods are subject to mutual exclusion, thus preventing multiple objects from erroneously trying to use it at the same time.
        - Reactor A reactor object provides an asynchronous interface to resources that must be handled synchronously.
        - Read-write lock Allows concurrent read access to an object, but requires exclusive access for write operations.
        - Scheduler Explicitly control when threads may execute single-threaded code.
        - Thread pool A number of threads are created to perform a number of tasks, which are usually organized in a queue. Typically, there are many more tasks than threads. Can be considered a special case of the object pool pattern.
        - Thread-specific storage Static or "global" memory local to a thread.


## Architectures

      - Service Oriented Architecture: can be implemented as web services, microservices
      - Event Driven Architecture
      - Space-based Architecture


## Tool examples

    - Protocols: 
      - protocol domains: communication, authentication/authorization, security, sweb service, electronic trading, instant messaging, email, bluetooth, automation, file transfer, network, routing
      - internet protocol layers
        - link layer
        - transport layer
        - internet layer
        - application layer

    - Web application server 
      - Apache Web Server
      - Apache Tomcat Server
      - IIS
      - NGINX
      - Jetty
      - Oracle/IBM HTTP Servers

    - Logging/Monitoring
      - Datadog
      - Logstash
      - AWS Cloudwatch

    - Authentication: Oauth, OpenID Connect, SSO, SAML, XACML

    - Formats
      - yaml, json, xml
      - rdf

    - API tools

      - API GUI: https://github.com/mermade/openapi-gui
      - API format: 
        - calls: curl/har/swagger
        - output: rdf/xml/json
        - spec: xsd, xml, swagger, raml
      - API code gen: swagger, api-map
      - API mapping: api-map (xsd, json)
      - API integration tools: informatica, talend, celigo smartconnectors, api-map, Swagger (OpenAPI spec), Apigee

      - API testing tools: jmeter (performance, load, functional)
        - testing (security, reliability)
          - structures: health check
          - performance
            - load testing
          - security: resources are not accessible to users that are not authenticated/authorized/identified
          - unit testing: check functionality of code units
          - functionality: check that required high-level functionality works
          - standards compliance:
            - open api spec
            - ws standard: WS-Addressing, WS-Discovery, WS-Federation, WS-Policy, WS-Security, and WS-Trust
          - interoperability: apps can access the API
          - pentesting: finding API vulnerabilities

    - Transaction Management
      - concepts
        - rollback/retry
        - ACID requirements

    - Connection Management
      - connection retry
      - request/response storage
      - interrupt handling

    - Process Management
      - process tracing
      - process restore/reboot behaviors

    - Debugging

      - system 

        - process debugging
          - terminal/bash: 
            - tracing probe markers: DTrace, SystemTap

          - python
            - sys.settrace(tracefunction) # trace a function
            - pdb.set_trace() # start tracing
            - traceback.print_exc() # print exception stack trace

        - code debugging
          - python
            - pdb:  python -m pdb script.py

          - exception debugging
            - python
              - printing stack trace
                  except: 
                      traceback.print_exc()

    - Testing

      - coverage testing: determine ratio of code tested by existing tests
      - code complexity
      - duplicated code
      - linting/standards testing
      - beta/user testing: users test the website
      - a/b testing: users test multiple versions of a website
      - automated website testing (selenium)
      - pentesting: automated attacks on a website
      - client testing (browser stack, cross browser testing, virtual machines)
      - regression testing: test functionality after a change
      - black box (functional) testing: test function requirements with input/output (type of black box testing)
      - white box (structure) testing: test structure of code rather than functionality
      - code testing
        - static code testing (white box): analyze code for vulnerabilities
          - data flow tracing (PumaScan, Fortify and Checkmarx): trace data through application (as is done in code with breakpoints) to identify risk/trust mismatches
        - dynamic testing: test running application in an environment
      - unit testing: test units of code
      - integration testing: test interacting units of code or system components like layers
        - API testing
      - hypothesis testing
      - deployment testing
      - system/structural problem type (code smell) detection: sonarqube, pmd, findbugs

    - Workflow Automation
      - concepts: workflows, processing, formats, conditions, error protocols
      - tools:
        - Airflow
        - Microsoft Flow
        - Zapier (task automation)

    - Optimization
      - website optimization analysis

    - Build tools

      - build/deployment/testing management/automation: Jenkins

      - Deployment Approval: Artemis

      - Config Management: terraform, ansible

    - Distribution tools

      - Scaling/Cluster Management: kubernetes

    - Package management: artifactory

    - Big data: 
      - compute: Spark, Hadoop
      - data warehouse: redshift, hive
      - data lineage/pipelines: Talend, SentryOne, Pachyderm, Logstash, Atom
      - querying/reporting (aggregation, structuring, dashboards, visualization): Splunk, Kibana
    
    - ETL (extract-transform-load) tools:
      - data integration (import/export/transform) automation: AWS Glue (data metadata store functioning as an etl engine & code generator)
      - Apatar

    - Streaming
      - Apache Kafka/Flink

    - Frameworks
        - app-building frameworks (laravel, symfony, react, angular, spring)
        - business application frameworks (for crm, erp, e-commerce, cms applications): drupal, sugarcrm, magento, wordpress, alfresco
        - js frameworks (angular, react, jquery, bootstrap, vue)
          - js dev cycle tools
            - webpack: package/dependency management
            - task runners: grunt, gulp
            - compilers: browserify
          - typescript: JS superset with extra features for compatability
    
    - IDE: atom, eclipse, intellij, pycharm, jupyter, xcode
    
    - Web site standards/regulations: wcag, 508, wai-aria

    - Database: 
      - relational database (mysql, db2, oracle, postgres, AWS Aurora (mysql + postgres compatible)
        - pl/sql: sql + procedure extension (from oracle)
      - multi-model database (oracle, db2)
      - object relational mapping (realm, multi-model databases)
      - data classes (for migration)
      - NoSQL (ElasticSearch, MongoDB) - https://en.wikipedia.org/wiki/NoSQL#Types_and_examples
      - key-value store (DynamoDB, Redis)
      - document store
      - distributed data store (Dynamo, BigTable, Mongo, Redis, Couchbase)

    - Cache tools

    - Encodings

    - Compression algorithms & tools

    - Quantum processors

    - Aggregate lists of good/opensource tools (like lists of free data sets or open source models)
        - https://github.com/jnv/lists#technical
        - programming 101 study guide: https://github.com/mtdvio/every-programmer-should-know

    - query languages
      - sql: queries relational databases implementing SQL support
      - sparql: queries RDF-formatted data, allows for a query to consist of triple patterns, conjunctions, disjunctions, and optional patterns
      - graphql: API query language

    - cloud providers: AWS, Google Cloud, Azure, Rackspace, IBM

    - browsers: brave, chrome, safari, firefox

    - OS: linux (ubuntu, debian, centos), windows, mac

    - Networking components:
      - DNS
      - load balancer
      - proxies
      - VPN
      - TCP/IP
      - SMTP
      - LDAP
      - HTTP, TLS, HTTPS, SSL
      - WAN, LAN
      - FTP
      - Internet, Intranet, Extranet
      - ethernet
      - packets/router/host/domain
      - throttling, bandwidth

    - isolation tools:
      - containers
      - virtual machines
      - hypervisor layer
      - remote desktop protocol (RDP)

    - data science & machine learning
      
      - computing tools (numpy, scipy)

      - optimization tools (cuda, cudnn, gpu)
      
      - data sanitization
      
      - math/statistical tools: partial differential equations, Markov processes (vs. recursive), probability distributions, trigonometric equations, matrix multiplication, eigenvectors, tensors, geometric progressions, regression, gradient descent for minimum-finding (cost-minimization)

      - Pre-trained open source ml models (lists of pretrained models, like GPT, BERT, AlphaGo, AlexNet)
        - https://modelzoo.co

      - tasks

        - neural networks
          - minimize cost
          - compare with threshold value
          - apply weights
          - aggregate inputs

        - data
          - sanitize
          - streamline (types, corrupt values, remove/merge duplicates)
          - regularize
          - format (as vectors, matrixes)
          - identify data components
            - irrelevant/redundant variables
            - patterns
            - missing data
            - corrupt data
            - extreme data (outliers, edge cases, error triggers, assumption contradictions, interacting extremes producing black swans)
            - structures (variable chains/alternatives)
            - data reductions
            - data classes (clusters in data set)
            - data cases
              - set of descriptive data cases needed to reduce data set to its variance
      
      - algorithms
      
        - core types

          - perceptron
          - feedforward
          - artificial neural net
          - deep learning algorithm

        - general types

          - supervised/unsupervised
          - recurrent
          - reinforcement
          - clustering
          - regression

        - specific use/method

          - decision tree


          - classification
            - clustering (nearest neighbors)

          - competition
            - genetic
            - GANs

          - data formatting
            - autoencoders for categorical data

          - dimensionality reduction
            - pca/ica
            - lda
            - svd
            - svm

          - data type
            - convolution
            - time-relevant:
              - LSTM

          - self-organizing map

      - components

        - parameters
          - weights
          - functions
          - metrics & threshold values
          - learning rate

        - metrics

        - network functions

          - learning
            - update strategy
            - node navigation function
              - input aggregation/weighting function
          - node activation function
            - cost function

          - network processes
            - weight initialization
            - node activation/navigation

        - machine learning methods
          - dimensionality reduction
          - feature selection
          - backpropagation
          - gradient descent
          - regularization
          - normalization
          - data augmentation

      - algorithm packages/tools
        - Apache MXNet, Singa
        - DeepSpeed
        - Dlib
        - Microsoft Cognitive Toolkit, ML.NET
        - PyTorch
        - Theano
        - ONNX
        - tensorflow
        - scikit-learn
        - caffe
        - keras
        - open neural networks (OpenNN)
        - deeplearning4j
        - ML lib

      - frameworks
        - fast.ai
        - open ai
        - h20 

      - AutoML
      - metrics
      - data visualization
      - model deployment/governance tools
      - machine learning IDEs
        - jupyter
        - pycharm
        - rstudio
        - visual studio
        - atom

- debugging

  - attack types
    - side channel attacks: info accessible by system implemenation, like how memory access is regulated/prioritized
    - input hacking (injecting code, taking advantage of missing input validation)
    - encryption algorithm hacking (reverse-engineering original input values to algorithms using rainbow tables/brute force calculations/possible parameter reduction/collisions)
    - machine learning algorithm hacking (training it to identify adjacent inputs, training it to make prediction errors, 

  - debugging attack points

    - connectivity (network access, firewall/port config, router/cable/server environment problem (electricity/temperature regulation/connection/unplugged))
    - dependency (versions, missing cache file/credentials/permissions/third party API service (like auth servers)/code library/different path after someone else updated tools on the server, CDN down, requesting/downloading prior/alternate versions of a resource since the expected one wasnt found, neglecting to update dependencies according to schedule from third party service provider before third party tool was updated, third party services havent fixed config/deployed updates like DNS propagation schedule, not patching code, hooking up added resources with existing resources)
    - prioritization of requests favoring other requests on server
    - lack of transaction management (failed requests arent re-tried, failed imports arent rolled back before re-import)
    - model (a common input is being identified as indicating a need to update the model, and the update action accidentally allows re-training from beginning)
    - browser/plugin (version has different support for or interaction with js libraries or other front-end features that dont have a backup code version available so the ajax call doesnt execute as expected, browser/plugin config optimizes for an intent like tab-navigation and overrides inputs having a certain pattern to make the inputs invalid)
    - lack of edge case/exception handling for infrastructure or other stack component (cluster configured to launch new components if one fails, copying new instance from a particular node, but doesnt specify what to copy from if the reference node is missing)
    - state/data structure (an operation becomes more performance in certain cases, like when a list is right under its threshold for allocating a new list and the entire list needs to be copied, and the time of this operation is below a web server config for returning certain error codes like a 60-second limit)
    - timing (expected vs. actual schedules, lack of integration of sequential prioritization in scheduling)
    - resources  (requests from users are above what infrastructure/configuration handles, so new components are being added to handle increased demand and copying/testing after addition is slowing down communication)
    - code (CPU/memory hogging code, unhandled inputs, unnecessary/incorrect assumptions, missing rules, re-running processes more than necessary like every time a function is called instead of the first time, not accounting for threading vs. process trade-offs like synchronicity/memory-sharing/interaction with full stack components, a particular common input is triggering logs that aggregate quickly and the large log files are slowing down requests)
    - maintenance (regular processes like running data imports or system optimization/tests occurring on a component of the stack)
    - system (other tools/apps on the server being updated/installed, env vars are rewritten by system process so code uses a previous language version that is slower on some operations or cant handle inputs or find dependencies of other version, a process wasn't configured to reboot itself if terminated or boot on server startup if a new server just added to the cluster is being called)
    - update conflict (priority of update requests ambiguous for conflicting versions - like sometimes one update source is executed first, sometimes another, and the update sequence has different results)
    - data (database lock/optimization, database process like optimization/import/procedures/replications running, data corruption, slow queries/indexing not accounted for)
    - access (lack of access to resources bc of other reasons - resources are being attacked, used by another process, accidentally deleted or otherwise missing, permissions were changed by an update or other admin/config process, config was overwritten by a self-fixing/reboot process after being interrupted)
    - misconfiguration (accidental like selecting an incorrect cron schedule/firewall rule/user group, or copy-pasting the wrong config, or default like auto-configurations applied on startup/installation/update)
    - attack (DDoS is keeping a resource busy and unable to handle incoming requests, ransomware changed file permissions)

  - debugging processes

    - dependency: set logs to debug, add logging statements/scripts from our team repo with process/stack tracing using pdb, sys trace & exception tracing and cli tracing to check running processes, check log aggregation/monitoring tools like datadog/cloudwatch/splunk, check healthcheck endpoints
    - infrastructure issue: look for config drift in cloud provider, check that components exist & are active/accessible, check for failed deployments & scheduling conflicts
    - server config/performance: check port access & firewall rules, check server/process logs, check which updates were executed recently, check for large files
    - code: check code tests for failing tests, run code with edge-case data values with request data if available
    - database: check logs, check for locks, recent permission changes, recent distribution/resiliency/transaction management config changes
