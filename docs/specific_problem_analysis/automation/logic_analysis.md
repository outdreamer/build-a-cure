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

    - example of applying core interface to logic interface includes generating core logic component combinations:

        - apply ([assumption1 + priority 2 + condition 3], function 4)
        - permission defined as a combination of core components: access to (or valid input of) 'activation' sub-function of a function object
            - function object with metadata like:
                - inputs/outputs
                - alternate implementations
                - current implementation logic
                    - conditions
                    - assignments
                    - iterators
                - system objects
                    - optimization points
                    - vertexes
                - types: input/output data types, condition/assignment/iterator types, memory types
                - sub-functions: activate, inject, import, compile, standardize, optimize, etc

## Debugging

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


Testing

Overall testing strategy

    test for each source of variance that can hold embedded assumptions (inputs/outputs, conditions, function & stack metadata such as permissions/context)

Test concepts

    - concepts like relevance are important in security: is there a 'need to know'
    - key concepts: interconnectivity, integration, feedback, regret, importance, relevance, coherence, state, channel, scalability, responsiveness, performance, optimization, resilience
    - health checks, polling, latency, caching, breakpoints, concurrency, multi-threading, bandwidth, throughput, 

Integration test

    calculating interaction of all objects in code requires analyzing not just classes & functions but:
        system context (permissions, installed tools, browser settings, antivirus software, firewall configuration)
        emergent properties
        implicit assumptions
        consecutive exploits using gaps in multiple chainable objects
        agent actions/resources (info about stack being used)

Standard test questions

    'how will program resolve selection between two alternative resources based on tech stack'
    'how can functionality/inputs be mimicked'
    'how will this user action interact with this user-exposed function'

Non-standard test questions

    'how will this object1.function interact with object2.function under edge conditions'
    'can object1.function be tricked into interacting with object2.function'
    'how will tool design limits conflict with developer intents'
        can a query expose information because of how the query tool is designed
        if there are assumptions embedded in tool design to account for specific priorities (latency, accuracy, latest data, resilience), will that produce unexpected query results under certain conditions
            if so which conditions
        do embedded assumptions carry hidden advantages for various agent positions
            does prioritizing most recent data have un/intended advantages, and how could those be exploited

Existing testing tools

    code generation tools (generate API) to standardize code
    analyze dependencies & context
        'if a third party tool makes this mistake, how will that impact our system'

Custom testing tools

    intent-matching
        'what is the possible & likely reasons for this action'
            'why would someone make a request to a third-party site with injected javascript - how could retrieved resource be exploited'
            'what previous/future user actions based on their intent/decision profile could make this resource a security hole'
    test generation
        parsing code assumptions & generating unit tests by variance/assumptions

Code optimization tools

    identifying code snippets with repeated logic (on various interfaces, not just raw code repetition) or too much variance
    identifying assumptions in code that can be exploited
    identfiying optimal logic order:
        if variable exists condition should precede variable use
        condition with return should usually precede conditions without return
        conditions with common assumption should be preceded by condition testing that assumption
        list metadata (location of an item) should be stored during list definition if possible to avoid iteration later
        over-restrictive conditions that reduce later choices should be carefully examined for necessity
        if conditions should be in an if/else block rather than consecutive if conditions, if they should never happen concurrently

Test Generation

- unit testing:

  - assumptions
  - inputs/outputs
  - conditions
  - intents/use cases

- integration testing: 

  - function chains
  - system context
  - user decision history (visited insecure website/cleared cache)

- identify objects that need to be mocked bc of security/deployment constraints

- generate assert statements, conditions, and mock objects as needed

- Error types

    - problem types include assumptions (unenforced limits on future state)

    - identifying app structure of code base

        function units
            function names

        function workflows
            integrating function units (function sequences, hub functions, alternative function routes)

        conditions
            if/while
            types
            tests
            sample/test data
            best/worst case scenario & relationship to sample/test data
            variables

        inputs
            structural
                function params
                global vars
                config
                file reads
                open ports
                listeners
                events
                data (data variation, data state, data integrity, data processing)
            assumptions
                strings
                validation
                state (subnet is not right below its limit so that another application requesting an ip doesnt interfere with your app resources getting one when auto-scaling)
                components (with no generation function, indicating their existence is assumed)
            anti assumptions
                components that can be re-generated
                standardization
                alternative routes
                auto-error correction
                integrated analysis (not assuming one change will not produce changes for adjacent applications/resources)

    - dont need to focus on unplanned changes so much as permuted assumptions/expectations, if your assumption index has correctly identified the important inputs

        index assumptions as all important process inputs, from app inputs like user events, down to the os level like available memory

    - third party assumptions are another big error source, bc their assumptions may be invisible until theyve generated problems, but their assumptions can be derived using assumption patterns/types/variables

    - what types of data can help in automation of code debugging

        saved snapshots of application state (track progress within application to find anomaly patterns)
        assumption data
            assumptions about state, process sequence, data values, data/config variation, and other params

- example of how to predict the errors that will occur from a particular unplanned assumption change

        find inputs
            find dependencies/required inputs (and input combinations & other input structures)
                find problematic assumption types
                    best/worst case combinations
                    single-chain function sequence (with no alternative routes) depending on one input of initial function
                    core structure changes (paths, permissions, ports)
                        find assumptions matching assumption type structures
                            check if change impacts those assumptions

        find assumption/input-invalidators
            find invalidating states of assumptions (inputs)
                what states would invalidate the application intents/assumptions
                    find states that can invalidate required inputs
                        find requirement invalidating states that this change will bring application/env closer to

        find changes
            find changes that will cause many other changes
                find alternative changes that wont cause many other changes
                    find difference between those alternatives & original change
                        find if difference adds value in reducing total changes needed (assumptions/components interacted with)

        find problem types
            find problem types involving related objects of change, changed components, and their dependencies
                find unplanned changes
            test state produced by change for problem type structures

        find error-triggering state changes
            filter by state changes similar to this change
                check if those state changes resulted in rollbacks/alarms/errors

    - create problem flow chart automatically by permuting problem types or alternatively assumptions

        problem types: dependency/input of condition is not populated, condition is inadequate to handle input, condition is not applied

        assumptions: variable is not populated

        inject structure 'boolean' to component 'variable'
            variable is populated
                inject structure 'process'
                    variable checking process
                    variable resolution process
                        variable type is incorrect
                        variable type is irrelevant
            variable is not populated

  - data processing error types
          - intersections/processes with obvious error opportunities:
            - data splitting
            - data merging
            - data indexing & caching
            - computation indexing & caching (false positions to answers, false answers)
            - computation timing
            - computational order error (non-commutative)
            - connectivity

          - non-obvious error opportunities or lack of optimization
            - organization method of distributed datasets allows for random or specific task optimization, rather than absolute optimization 
              (multiple indexes for same dataset or storage of metadata properties & locations in each dataset so many organization methods can be used on same dataset)
              - theres a lot of room for pre-computing, pre-indexing, & pre-combining within & across data set combinations
            - lack of relationship metadata between datasets 
              (which dataset contains more items of type c, etc)
            - identifying key vertices (factors on an analytical layer) to split the data set beforehand and creating multiple clusters split in different ways likeliest to be needed
              - identifying key splitting order & intervals at query time

- example of a system analysis function: identify a system object (error) in the problem space system

    - general method: pull error cause types, error types caused, identify known possible information problem types, match error types with info problem types by applying structure, find matching solutions for error types once linked to info problem types

    - function to generate/identify errors in a solution (function set, host system) within a problem space formatted as a system

      - identify error root cause types using combinatorial core analysis

        - find components
          - structural mis/matches
            - intent mismatch between function combinations across layers 
          - unnecessary structures
          - missing structures
        - apply components
          - apply combinations
            - combine components in various structures
              - inject componeents into other components
          - apply changes
            - remove/add limits/rules/assumptions
            - use alternate paths
            - switch expected with unexpected components
        - build components
          - function sequences granting access

      - find error types caused by those cause types
        - structural mismatches cause:
          - lack of system/context-function fit (function-scope mismatch)
          - lack of rule enforcement (function/responsibility mismatch, expectation/usage mismatch)
          - lack of intent restriction for using a function (intent mismatch)

      - filter caused error types by which generated errors would cause information problem types (process failure, access vulnerability, corrupt data)

      - identify specific errors of filtered caused error types, organized by interface
        - lack of intent restriction for using a function
          - malicious function sequences matching validation requirements
          - breaking input/output sequence for later functions
        - lack of system/context-function fit: 
          - incorrect permissions for context
        - lack of rule enforcement
          - unhandled function inputs
          - granting cache access to unauthorized scripts

      - match specific interface (intent, structural) error types with information problem types (apply information interface to error types)
        - lack of intent restriction
          - breaking input/output sequence for later functions
            - injecting function with less validation in function chain

      - match specific interface (intent, structural) error types with solution types
        - intent mismatch: align intent
        - lack of intent restriction: reduce intents supported by function (re-organize logic, add validation)
        - incorrect permissions for context: scope permissions, generate permissions for a context/intent & check for a match before executing
        - breaking input/output sequence: check that all valid/supported function sequences are maintained
        - lack of rule enforcement: check that all rules & rule structures (like sets or sequences) determining resource access are enforced, or rule gaps where error/attack types could develop are closed
      
      - reduce by solution types that cover the most error types without contradicting other solution types or creating additional unsolved problem types
        - intent-matching covers multiple structural error types
        - system-fitting or structure-matching as a superset of intent-matching
      