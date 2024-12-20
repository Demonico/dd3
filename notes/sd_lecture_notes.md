# Outco System Design Lecture Notes

## Lecture 1: How to System Design

### Who gets asked these questions?

L4+

- L4/mid-level
    - essentially a pulse check
- L5/senior
    - working solution
    - 1-2 deep dives
- L6/Staff+
    - 3-4 deep dives into design

### What's the point of the system design interview?

- Check your fundamentals
- Problem solving

### How to answer a SD question

Important sounding off-handed statements

- Suggested times are estimates and vary by interviewer.
- Have a working solution before you go into optimizations.
- No strict order between micro-service diagram, data schema, or calculations
    - Cover them in the order you feel will communicate your design in the most efficient way
    - This depends on the problem
- Don't present data schema as API schema
    - you want to encapsulate your deb rather than surface it to the user
- For front end design questions
    - Should be similar
    - Replace data base schema with local state discussion
- Make a note of deep dive topics to come back to e.g. caching
- Driving the interview is a positive signal

Written in the lecture video

- Resuirements gathering (< 10 min)
    - Functional reqs
        - Use Cases, what the user asks for
        - Prioritization and feature scoping
            - list a lot of features, and scope out the unimportant ones
        - What is the problem the system will solve (IMPORTANT)
            - Suggest features instead of asking for them
            - jr engineers ask for features
        - Write down the sentences (technique from OOP design)
            - Verbs become and API
            - Nouns -> entities
            - Adjectives -> types
        - Visual diagram
            - Put yourself in the shoes of the user
        - Time management
            - Ask for a hint "Did I miss anything? vs. What are the reqs?"
    - Non-Functional reqs
        - What can break your system
        - Examples
            - Scalability
                - \# of users
            - Security
            - Availability
                - 99.999% uptime
            - Consistency
                - Freshness latency
            - Latency
                - ms
            - Reliability
            - Durability
            - Stability
            - Maintainability
            - Fault tolerance
            - Fairness (important for queing systems)
            - Spikiness (traffic)
            - Global (userbase)
            - Devices supported
            - CAP Theorem mistake
                - CP
                - AP
                - Which part of the system is CP or AP
                - Still need to discuss the missing acronym

- Working solution (< 20 min)
    - **Agree with interviewer on basic design**
    - **Draw a High Level Diagram as soon as possible**
        - Main communication point with the interviewer
        - Draw the communication links between microservices you identified
        - **Draw the user flow**
            - Read path
            - Write path
            - Make sure to address all the actions described in functional requirements
    - Capacity
        - Do these throughout the interview
        - How can you calc throughput QPS if you don't know what the API looks like?
        - How can you calc storage requirements if you don't know the schema?
        - Intuition of where the bottleneck will be
        - Math with a purpose
        - Bottlenecks (4 types of resources)
            - CPU
                - Capacity
            - RAM
                - Capacity
            - Disk
                - Capacity
                - Bandwidth/Throughput
                - Latency
            - Network
                - Connections
                - Bandwidth/Throughput
                - Latency
    - API Schema
        - RESTful (usually public facine)
            - Resource driven design
            - focus on nouns
            - \<HTTP Method\> \<Resource\> \<queryParams\>
                - GET /newsfeed/?startDate= { userAuthToken: 12345}
        - gRPC (internal between services)
            - Service driven design
            - focus on actions
            - getNewsFeed(uid, startDate, endDate)
        - Websocket
            - STOMP protocol
    - Microservice and High Level Diagram
        - Group features by data or functionality
        - **Security patterns**
            - _HINT_: If there is a payments DB, that should be a separate microservice.
                - this helps isolate security issues better
        - Organizational barriers
            - example: separate catalog from shipping
    - Data Schema
        - Tables
        - Access patterns/query patterns
            - these drive the data and storage decisions
        - Data Models
            - PrimaryKey
            - SortKey
            - ShardingKey
            - Indexing
        - Storage Tech
            - File System
            - Relational
                - Row based
                - Column based
            - NoSQL
                - Key Value
                - Document
                - Wide Column
                - Graph (not common)
- Deep dive section (< 20 min)
    - Tabulate all future deep topics, and pick the top few to discuss
    - 3 deep dive topics per question you are in good shape
    - Format for deep dives
        - Identify the problem (below)
        - Prove the problem exists
        - List out possible solutions
        - Discuss the trade offs
        - Suggest a solution and how you will deal with the cons
    - Ways to come up with deep dive topics
        - Non-Functional reqs
            - Scale
                - what happens when one machine can't handle all requests
            - Availability
                - what happens when a system goes down
                - how do you maintain availability
            - Caching
                - cache policy
                - what to cache
                - cache misses
            - Load balaancing
                - load balancing algo
                - availability
            - Queueing
                - Message semantics
                    - At least once
                    - At most once
                    - Exactly once
                - Microservices stability / resilience patterns
                - Geographic distribution
                - DB configurations
                - Sharding
                - Reapplication
                - Concurrency
                - Thundering herds / stampede
            - Monitoring
                - Read and write QPS
                - Read and write latency
                - Resource capacity
                - Data retention
                - Data freshness
                - \# of live connections
                - Cache hit rate
            - Alert
                - Queue Length
- Wrap Up section (~ 5 min)