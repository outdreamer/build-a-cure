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
    Security layer: encryption algorithms, key store, permissions, firewalls
    Rule Layer: protocols, functions, rule access (permissions), rule enforcement (type checking)
    System Layer: OS, config, code, change tools (auto-updates, package managers), compilers/parsers/interpreters, languages, processes, ports
    Isolation/Interaction Layer: competing/shared resources/processes, containers, cross-layer interactions, integration of code components, interaction of code & OS, interaction of processes
    Concept Layer: 
      Tests: 
        - concepts: clarity, responsibility, resiliency, necessity, scale, optimization, usage, extremes, standards, expectations, intent, meaning, cause, robustness
        - alignments/matching: user intention & dev expectation matching, risk/trust matching, code requirements vs. possible functionality matching

- philosophies/paradigms
  
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

- tool examples

    - Web application server 
      - Apache Server
      - Tomcat Server
      - IIS

    - Streaming
      - Apache Kafka

    - Logging/Monitoring
      - Datadog
      - Logstash
      - AWS Cloudwatch

    - Reporting (aggregation, structuring, dashboards):
      - Splunk
      - Kibana

    - API Management
      - Swagger

    - Deployment Management
      - Artemis

    - Config Management
      - Terraform
      - Ansible

    - Cluster Management
      - kubernetes

    - Transaction Management
      - rollback/retry
      - ACID requirements

    - Connection Management
      - connection retry
      - request/response storage

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

    - Workflow Automation
      - Airflow

    - Optimization
      - website optimization analysis

    - Database: 
      - relational database
      - object relational mapping
      - data classes (for migration)
      - NoSQL (ElasticSearch, MongoDB)
      - key-value store (DynamoDB, Redis)
      - document store
      - distributed data store (Dynamo, BigTable, Mongo, Redis, Couchbase)

    - query languages
      - sql: queries relational databases implementing SQL support
      - sparql: queries RDF-formatted data, allows for a query to consist of triple patterns, conjunctions, disjunctions, and optional patterns
      - graphql: API query language

    - API integration tools
      - informatica
      - talend

    - cloud providers: AWS, Google Cloud, Azure, Rackspace, IBM

    - Networking components:
      - DNS, load balancer, proxies, VPN

    - isolation tools:
      - containers
      - virtual machines
      - hypervisor layer
      - remote desktop protocol (RDP)

    - data science & machine learning
      
      - computing tools (numpy, scipy)
      
      - data sanitization
      
      - math/statistical tools: partial differential equations, Markov processes (vs. recursive), probability distributions, trigonometric equations, matrix multiplication, eigenvectors, tensors, geometric progressions, regression, gradient descent for minimum-finding (cost-minimization)

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
        - perceptron
        - deep learning
        - autoencoder
        - genetic
        - supervised
        - unsupervised
        - recurrent
        - reinforcement
        - convolution
        - classification
        - feedforward
        - self-organizing map
        - LSTM

      - components

        - parameters
          - weights
          - functions
          - metrics & threshold values

        - metrics

        - processes
          - weight initialization
          - node activation/navigation

        - functions
          - learning
            - update strategy
            - node navigation function
              - input aggregation/weighting function
          - node activation function
            - cost function

      - methods
        - feature reduction
        - feature selection
        - backpropagation
        - gradient descent
        - regularization
        - normalization

      - algorithm packages
        - tensorflow
        - scikit-learn
        - caffe
        - keras
        - open neural networks
        - deeplearning4j
      - frameworks
        - fast.ai
        - open ai
        - h20 
      - AutoML
      - metrics
      - data visualization
      - model deployment/governance tools
      - machine learning IDEs

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
