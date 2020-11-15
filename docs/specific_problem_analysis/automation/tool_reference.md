## Tool examples

    - software stack layers
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


    - Architectures
      - Service Oriented Architecture: can be implemented as web services, microservices
      - Event Driven Architecture
      - Space-based Architecture

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

      - concepts: clarity, responsibility, resiliency, necessity, scale, optimization, usage, extremes, standards, expectations, intent, meaning, cause, robustness
        - alignments/matching: user intention & dev expectation matching, risk/trust matching, code requirements vs. possible functionality matching

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

    - CICD: Travis, GitLab, Jenkins, AppVeyor

    - Build tools

      - build/deployment/testing management/automation: 
        - Jenkins
        - Gradle
        - Maven

      - Deployment Approval: Artemis

      - Infrastructure Config Management: 
        - Terraform
        - Ansible
        - Vagrant
        - Puppet
        - Chef  
        - AWS CloudFormation

    - Orchestration tools
      - automated systems/software configuration, coordination, & management, specifically to:
        - integrate a variety of disparate applications and systems
        - assemble end-to-end processes

    - Distribution tools

      - Scaling/Cluster Management: kubernetes
      - Computing: MapReduce, HDFS

    - Package management: artifactory

    - Big data: 
      - compute: Spark, Hadoop
      - data warehouse: redshift, hive
      - data lineage/pipelines (perform workflows of operations on data, like validate/transport/aggregate/distribute): Talend, SentryOne, Pachyderm, Logstash, Atom
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
      - graphql: API query language, allows querying of multiple databases, microservices, and APIs with a single endpoint

    - cloud providers: AWS, Google Cloud, Azure, Rackspace, IBM

    - message broker: helps app communicate using messaging protocols

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

    - hardware

    - semiconducters: https://www.investopedia.com/ask/answers/042115/what-are-main-types-chips-produced-semiconductor-companies.asp#:~:text=The%20Main%20Types%20of%20Chips%20Produced%20by%20Semiconductor,Chips%20%28Commodity%20ICs%29%205%20Analog%20Chips.%20More%20items

        - chip functionality type

            - Memory Chips
                - store data and programs on computers and data storage devices
                - Random-access memory (RAM) chips provide temporary workspaces
                - flash memory chips hold information permanently unless erased
                - cannot be modified
                    - Read-only memory (ROM)
                    - programmable read-only memory (PROM) chips 
                - can be changed:
                    - erasable programmable read-only memory (EPROM)
                    - electrically erasable read-only memory (EEPROM) chips 

            - Microprocessors: 
                - contain one or more central processing units (CPUs)
                - Computer servers, personal computers (PCs), tablets and smartphones may each have multiple CPUs
                - The 32- and 64-bit microprocessors in PCs and servers are based on x86, POWER, and SPARC chip architectures
                - mobile devices typically use an ARM chip architecture
                - Less powerful 8-, 16- and 24-bit microprocessors turn up in products such as toys and vehicles.
                - microprocessor types:
                    - Graphic Processing Units (GPUs)
                        - renders graphics for display on an electronic device
                        - can perform many calculations simultaneously
                        - When used in conjunction with a CPU, a GPU can increase computer performance by taking on some computationally-intensive functions, such as rendering, from the CPU

            - Standard Chips (Commodity ICs)
                - used for performing repetitive processing routines
                - Produced in large batches, these chips are generally used in single-purpose appliances such as barcode scanners
                - If an IC is made for a specific purpose, it is called an ASIC, or application-specific integrated chips

            - SoC (System on chip)
                - all of the electronic components needed for an entire system are built into a single chip
                - The capabilities of a SoC are more extensive than those of a microcontroller chip, which generally combines the CPU with RAM, ROM, and input/output (I/O)
                - In a smartphone, the SoC might also integrate graphics, camera, and audio and video processing. Adding a management chip and a radio chip results in a three-chip solution.

        - chip circuit types

            - most computer processors currently use digital circuits
                - digital circuits usually combine transistors and logic gates
                - sometimes, microcontrollers are added to digital circuits
                - Digital circuits use digital, discrete signals that are generally based on a binary scheme
                - Two different voltages are assigned, each representing a different logical value.

            - Analog Chips
                - mostly replaced by digital chips (except in cases like optionally with power supply chains, wideband signals, and sensors)
                - voltage and current vary continuously at specified points in the circuit
                - typically includes a transistor along with passive elements (inductor, capacitors, and resistors)
                - more prone to noise (small variations in voltage) which can cause errors.

            - Mixed Circuit Semiconductors

                - typically digital chips with added technology for working with both analog and digital circuits
                - A microcontroller might include an analog-to-digital converter (ADC) for connecting to an analog chip (such as a temperature sensor)
                - A digital-to-analog converter (DAC), conversely, can allow a microcontroller to produce analog voltages for making sounds through analog devices

    - isolation tools:
      - virtualization: 
        - VirtualBox
        - VMware Player
        - Vagrant
        - containers: Docker, ECS
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