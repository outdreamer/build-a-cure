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
            Downcasting: a type cast which breaks the abstraction model; the abstraction may have to be refactored or eliminated.
            Orphan variable or constant class: a class that typically has a collection of constants which belong elsewhere where those constants should be owned by one of the other member classes.
            Data clump: Occurs when a group of variables are passed around together in various parts of the program. In general, this suggests that it would be more appropriate to formally group the different variables together into a single object, and pass around only this object instead.

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


# Best practices

    - CICD:

      - continuous integration (CI): merging all developers' working copies to a shared mainline regularly
        1. run tests locally
        2.a compile code & run tests in other environments
        2.b deploy artifact
      - Continuous delivery: checks that software is always deployable to users
      - continuous deployment: automates deployment process

      - CI/CD best practices

        - Maintain a code repository
        - Automate the build
        - Everyone commits to the baseline every day
        - Every commit (to baseline) should be built
        - Every bug-fix commit should come with a test case
        - Keep the build fast
        - Test in a clone of the production environment
        - Make it easy to get the latest deliverables
        - Everyone can see the results of the latest build
        - Automate deployment