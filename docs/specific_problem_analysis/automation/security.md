- security methods

    - create https temp server/cert for request sessions on sites that arent https already, after filtering content for immediate malware/attacks on temp server

      - invariant vs. symmetry

      - applying 'combination' structure to type patterns:
        https://www.technologyreview.com/2020/10/30/1011435/ai-fourier-neural-network-cracks-navier-stokes-and-partial-differential-equations/

      - energy stored in information/structures has stability physics, where information in a certain structure can support other information of different structures, including structures allowing variation in change/potential

      - config manager that allows specifying conditions/processes (check for approval from Artemis), data source (url or queries) & UI components/graphs (template or queries) to build apps/pipelines  automatically
      
      - migration/integration automation using app architecture/code/config search: searching other stack resources (application code, API, data store, resources, security & pipelines) in a repository of stack resources of existing or optimal applications, to test the original app test cases to see if a particular codebase/database/config/pipeline will work for the users' needs, without having to manually code a migration or integration to another stack (either migrating code, cloud, pipeline, data store, security tools, or all of the above), and using incremental tuning of the application code (mixing in code components, injecting dependencies, executing adjacent transforms, etc)
        - the primary work involved on the dev side would be ensuring the test cases covered all user needs
        - the migration/integration logic would involve search filters in the form of exit conditions that would skip to the next resource stack if a particularly important test doesnt pass, rather than trying to fix the resource stack that is clearly too different from user needs to be adjacently useful
        - it could also start from a standard set of application resource stacks in various stack combinations and add logic/config/schema until it fulfills the test cases
        - identifying probably successful transforms of code/config can be done with code queries if indexed by intent, or by translating code to the currently iterated resource stack given pre-defined mappings


    - vms, servers, networks, encryption algorithms with intent & approved actions (browse web, email, edit doc, test software)
    - approved workflows: use components like approved action sequences of previous sessions as the site matches requested actions
    - centralized data store: if you go to a site for 'change your address intent', it retrieves or infers & confirms your updated address with an address storing server/network that picked it up from an original update you submitted with authorization procedures, rather than you having to update it everywhere
    
    - code changing per request: once code-generation is automated, generate slightly different site code for each request (swap out dependencies, use alternative functions or workflows that have ambiguous/neutral impact on intent & execution)
    
    - request demand-supply matching: 
      - assign cause (demand/need/requirement or reason for intent) to each intent (I have to go to the car insurance site bc the insurance provider submitted a request to pay a bill to a third party request tracker that approves site access requests)
        - example: does a site dev want the site to be tested? then it can accept 'test' intent workflows, otherwise request patterns similar to test request patterns & no other request patterns will be assumed to be illegitimate
    
    - intent-based navigation & configuration (generate config for a particular priority set like 'safety first, then functionality, then performance' or intent like 'protect my system from all third parties' or 'ask me for permission to train a model to filter external requests')

      - browser user error-config form to generate site options
        - they can specify what kind of errors they make (clicking on wrong thing) or features they want (auto-scroll on articles at their pace)
        - these configurations can be stored by the browser to adjust site content (as a list of info, formats, priorities, & relationship functions between them) to be displayed & usable in a way that fits customer configuration (preventing their error types & adjusting site UI/events/updates according to customer config, so the UI is always customizing itself to their needs if specified, rather than a particular design (replaced with site info/formats/priorities/etc from server, which can act as the default)

      - intent-permission integration: 
        - context metadata for permissions-granting, so that certain info can only be accessed if certain system processes & conditions occur matching or associated with the valid intents, rather than if a user knows a password
        - similar for updates, update metadata like priorities has to match 'user-specified' or 'default system' or 'generated for intent' priorities & other metadata to be downloaded & installed
        - similarly for user behavior across requests, frequenting/giving permissions to sites from the same funder should alert the user of potentially dangerous permissions combinations, in usage data & legal terms (accepting cookies on this site & enabling location tracking on this app & accepting these terms gives this entity access to this cache, which has this sensitive data)

    - usage error prediction algorithm: predicting errors based on system usage
      - using a site with a recommender algorithm configured to over-prioritize user history in generating recommendations will produce errors of homogeneity in content, which can be predicted from the priority, the lack of self-correction/balancing potential once a priority/preference is set, the use of history data as model training input (embedded assumption that preferences wont change), the assumption that users will know every variable (source of difference) in content theyll want to see (so if they want to see content contradicting their derived priority/preferences, they have to look it up themselves, instead of the algorithm being able to infer these variables using contextual data, like info exposure or education/socialization trajectory, so the algorithm can infer 'what music a nascar fan will like' without having nascar fan data, just using objects like the structural similarity in content variation & other contextual data)

    - use predicted content as a backup in case of connection/traffic disruptions (without allowing prediction algorithms to access input to other algorithms such as over-requesting it to make it inaccessible, which would give them the ability to force their bad predictions to be true for those inputs, without evaluating system context/impact of that change)

    - changing encyption algorithms on server & client according to a function with ambiguities built in (following a particular algorithm with different algorithms for example)
    
    - traffic algorithms applied to internet requests, so (like scheduled commuter groups to leave at different times) that a user set can request a resource at a scheduled time, and the content can be pre-delivered to temp storage on local servers & updated with update requests if they miss their scheduled time, which can be done in bulk for data requested commonly & frequently in a community

    - context-fitting & request metadata matching: 
      - one person couldnt execute two simultaneous processes, so check for computations done on computer that would preclude a particular process
      - one person couldnt execute two simultaneous requests without software (verifying requests across sites with anonymizing functions), so check for approved 'bot developer' intents
      - people dont usually just infer that they should change a configuration on a site, it usually happens after they receive information about that configuration (verify information across requests at different sites to establish request legitimacy)
      - apply request/communication patterns, like that info objects such as conclusions usually follow other info objects like news articles, and actions follow conclusions
      - predictability of requests is an identifying feature and a way to generate probable data (like a probable conversation or headline, given new information queried) but also a security flaw, as it can be mimicked easier when its more predictable
      - explanation of their cause/intent for a request wont usually differ drastically from previous explanations/intents/causes without exposure to information (request change rate metadata)
      - match intents across processes/context: if a user is checking their email, its highly unlikely they also suddenly simultaneously want to encrypt all their files and show a popup with a skull on it asking for credit card information
        - similarly with info security: a person who typically uses an app to exchange updates with family or do science research (fact-based usage) is unlikely to suddenly be interested in fake news, logical  fallacies, emotional language, or want to find out about antivax cults they can join (conspiracy-based usage)
        - deriving intent from context: if they use dark web tools, like degrading content, or are poor in some way, they are likelier to be interested in using email spam automation software, intents which can be tested with fake site generation to test if they would download it
        - if a set of funds have been requested, are those funds verified, and can the payment be allocated after verifying network path & in pieces according to path traversed so far (adding trustless design) - with an associated purchase, allocating the payment across product shipment trajectory & damage checks or other quality tests
    
    - reducing requests needed by deriving code on-demand rather than pulling it, and aligning intents across code bases to identify code that can be shared/reduced
      - example: running bug-spotting/fixing programs locally & testing in a local vm rather than installing updates, running installed updates in a local vm with extra security until typical period of attacks has passed
    
    - computation network: calculating whether a request like 'have you calculated this & cached result' or 'calculate this' is the more efficient operation with calculation server networks
