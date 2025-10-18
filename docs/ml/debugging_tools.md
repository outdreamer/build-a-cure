- identifying vulns with AI
	- Almanax, Corgea, ZeroPath, Gecko, and Amplify

- create a table like this of symptoms, probable problem root cause, and tools/tests to use to identify whether that problem is relevant to the symptom
	- problem symptoms, probable problem root cause, tool to identify problem, successful test case, solution/fix
	    - website credentials being stolen, XSS, XSS scanning tool, check if pysa identifies an XSS in code, if it does then auto-escape output before including it in html and avoid using innerhtml/eval and use nonces in scripts 
	    - slow query, database lock, check for locks with a query, query returns results, run a query to fix the table with the lock

	| **Category**                  | **Tools / Commands**                                                		    | **Purpose**                                            
	| ----------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------- |
	| **Network / Firewall**        | `ping`, `traceroute`, `mtr`, `netcat`, `curl`, `tcpdump`, `nmap`, Wireshark 	| Trace packets, connectivity, protocol and latency issues        |
	| **System / Process**          | `top`, `htop`, `ps aux`, `lsof`, `ulimit`, `vmstat`, `strace`, `gdb`, `perf`  | Monitor CPU, memory, processes, file handles, syscalls          |
	| **Application**               | APM tools (Datadog, New Relic, OpenTelemetry)                       			| Trace transactions, measure latency                    		  |
	| **Threading / Concurrency**   | ThreadSanitizer, Valgrind Helgrind, AddressSanitizer, Java Flight Recorder 	| Detect race conditions, deadlocks, memory and concurrency bugs  |
	| **Database**				    | `EXPLAIN`									                          			| Identify performance bottlenecks 					   		      |
	| **Database / Concurrency** 	| `SHOW PROCESSLIST`, `pg_locks`, `EXPLAIN`, transaction logs  					| Diagnose locks, blocking queries, deadlocks 					  |
	| **Load Balancing**			| HAProxy stats, AWS ELB metrics   									  			| Identify traffic misrouting							   		  |
	| **Logging / Observability**   | Centralized log tools (ELK, Grafana Loki, CloudWatch)               			| Correlate events and root causes                      		  |
	| **Cache / Distributed**    	| Redis CLI, Memcached stats, ELK stack logs                   					| Debug stale or inconsistent caching         					  |
	| **Security / SSL**         	| `openssl`, OWASP ZAP, Burp Suite, `curl -v`, SSL Labs        					| Inspect SSL/TLS certs and vulnerabilities   					  |
	| **Cluster / Cloud**        	| `kubectl`, `aws logs`, Grafana, Prometheus                   					| Detect communication or scaling issues      					  |


- DNS problems

	- symptoms	
		- Website not loading (e.g., ERR_NAME_NOT_RESOLVED)
		- Requests go to the wrong server or timeout
		- Email not being delivered
	- causes	
		- Incorrect DNS records (A, CNAME, MX, etc.)
		- DNS propagation delay
		- Misconfigured DNS resolver or nameserver
		- Cached old DNS entries
		- Expired domain
	- tools	
		- dig or nslookup to check DNS records
		- ping and traceroute to test network path
		- Online tools like DNSChecker.org
		- Check domain registrar & DNS provider dashboards
	- solutions	
		- Correct A/AAAA/CNAME records
		- Flush DNS cache locally (ipconfig /flushdns or sudo dscacheutil -flushcache)
		- Wait for DNS propagation (can take 24–48 hrs)
		- Fix nameserver entries at registrar
		- Use a reliable DNS host (e.g., Cloudflare, Route53)

- Database Problems

	- symptoms	
		- Web pages or APIs taking too long to load
		- Database CPU usage spiking
		- Lock contention or deadlocks
		- Timeouts in application layer
		- Queries hang or time out
		- Data inconsistency
		- “Lock wait timeout” errors
	- causes	
		- Missing indexes
		- Poor query structure (SELECT *)
		- Inefficient joins or subqueries
		- Large table scans
		- Lock contention
		- Slow queries
		- Unoptimized schema (no normalization or too much normalization)
	- tools
		- EXPLAIN or EXPLAIN ANALYZE query plans in SQL
		- Database slow query logs
		- Performance monitoring tools (e.g., pg_stat_statements, pg_locks / InnoDB status, New Relic, Datadog)
		- Index and schema inspection tools
	- solutions	
		- Add appropriate indexes
		- Optimize queries (avoid SELECT *, use WHERE conditions, use LIMIT, use indexed columns, avoid correlated subqueries)
		- Cache results (e.g., Redis)
		- Use pagination for large data sets
		- Archive or partition old data
		- Tune connection pool
		- Reduce transaction scope

- Security Vulnerabilities

	- symptoms	
		- Unauthorized logins
		- Unusual traffic from suspicious IPs
		- Reports of account takeover
		- Credential dumps found online
		- Data leaks
		- Alerts from scanners
	- causes	
		- SQL injection or XSS
		- Weak password hashing (MD5, SHA1)
		- No HTTPS
		- Compromised/outdated dependencies
		- Leaked API keys or database credentials in code
		- Lack of input sanitization
		- Insecure/weak crypto or storage
	- tools	
		- Web server and access logs
		- Intrusion detection tools (Wazuh, OSSEC)
		- Static analyzers (SonarQube, Snyk, Bandit)
		- Dynamic analysis (Burp Suite, OWASP ZAP)
		- Dependency scanners (Snyk)
		- Vulnerability scanners (OWASP ZAP, Burp Suite)
		- git-secrets or truffleHog for secret detection
		- SIEM (Security Information and Event Management) dashboards (Splunk, Datadog Security)
	- solutions	
		- Rotate all exposed credentials immediately and encrypt secrets
		- Enforce strong password hashing (bcrypt, Argon2)
		- Use HTTPS everywhere
		- Sanitize user input and validate parameters
		- Implement rate limiting and 2FA
		- Conduct security audits and penetration testing
		- Use prepared statements
		- Keep dependencies updated
		- Implement security headers and CSP

- Network / Connectivity problems

	- symptoms
		- Requests timeout or hang
		- “Host unreachable” / “Connection refused” errors
		- Packet loss
		- Slow SSH or HTTP
		- High latency
	- causes
		- Firewall blocking ports
		- Security groups
		- Incorrect IP routing
		- Misconfigured subnet, gateway, or DNS
		- MTU (Maximum Transmission Unit) mismatch (devices in a network have different MTU settings, leading to packet fragmentation or drops)
		- High latency links
		- Network congestion
	- tools
		- ping, traceroute, mtr (my traceroute) to trace paths
		- curl, netcat, tcpdump
		- netstat, ss, ifconfig, ip addr to inspect interfaces
		- Packet capture (tcpdump, Wireshark)
		- Check firewall rules (ufw, iptables, aws ec2 describe-security-groups)
		- Network logs
	- solutions
		- Fix DNS, routes, firewall, or security groups
		- Restart networking services
		- Correct DNS or IP settings
		- Optimize MTU, QoS, or TCP settings
		- Open correct ports
		- Use CDN or caching

- Load Balancer / Proxy Issues

	- symptoms
		- Some users see errors while others don’t or some users can’t connect
		- Uneven traffic distribution
		- High latency or 502/504 errors
		- Backend servers idle or overloaded
	- causes
		- Incorrect health checks
		- Sticky session misconfiguration
		- Wrong/unhealthy backend targets
		- SSL termination mismatch
		- Timeout mismatch: load balancer timeout shorter than backend response
	- tools
		- Check load balancer logs & metrics (AWS ELB, Nginx, HAProxy dashboards)
		- Use curl -I per node or ab (Apache Benchmark) to test responses per backend
		- Monitor request distribution
		- APM traces
	- solutions
		- Fix health check endpoints
		- Align timeouts with backend
		- Adjust load balancing algorithm (round robin, least connections)
		- Ensure all targets are registered and healthy

- Performance / Latency Issues

	- symptoms	
		- Slow page loads
		- High bounce rate
		- Long TTFB (Time to First Byte)
		- Rendering delays on frontend
		- High CPU or memory usage
		- Timeout errors
	- causes	
		- Unoptimized assets (large images, non-minified JS/CSS)
		- Inefficient backend APIs
		- Inefficient algorithms
		- No caching or CDN
		- Blocking JavaScript
		- Too many HTTP requests
		- Too many DB queries
		- Inefficient database or network latency
		- load balancer misconfiguration
		- excess log storage taking up memory
		- Blocking I/O
	- tools	
		- Browser dev tools (Network tab, Lighthouse)
		- GTmetrix, PageSpeed Insights
		- APM tools (New Relic, Datadog, Dynatrace)
		- Profiling (Chrome Performance Profiler, React DevTools, perf, Py-spy, pprof)
		- curl -w and ab (Apache Benchmark) for latency
		- top, htop
	- solutions	
		- Optimize and compress assets (WebP, gzip, Brotli)
		- Use CDN (Cloudflare, Akamai)
		- Enable caching (HTTP cache, Redis)
		- Lazy load images
		- Minify JS/CSS and bundle efficiently
		- Optimize backend response times and DB access
		- Optimize code paths
		- Batch DB calls
		- Use async/non-blocking I/O

- Application/server Crash / Exception

	- symptoms
		- Program stops unexpectedly
		- Stack traces in logs
		- 500 errors in web services
		- Service restarts or crashes
		- Log exceptions or segmentation faults
	- causes
		- Unhandled exceptions
		- Null pointers
		- Out-of-memory
		- Invalid input
		- Memory leaks
		- Race conditions
		- Dependency version conflicts
	- tools
		- Log analysis
		- Tracing (OpenTelemetry, Jaeger)
		- Debugger (gdb, pdb, Visual Studio)
		- Crash dumps or core dumps
		- Profilers (e.g., py-spy, perf, gdb)
	- solutions
		- Add error handling
		- Validate inputs
		- Fix logic errors
		- Increase memory / tune GC
		- Monitor memory usage and fix leaks
		- Add rate limiting and circuit breakers
		- Use version pinning in dependencies
		- Write integration and stress tests

- Memory Leaks

	- symptoms
		- Gradual performance degradation
		- OOM (out of memory) errors
		- Increasing memory footprint
	- causes
		- Unreleased objects/resources
		- Cyclic references
		- Poor GC tuning
	- tools
		- Memory profilers (Valgrind, heapdump analyzers)
		- Runtime metrics (Prometheus/Grafana)
		- Heap dumps
	- solutions
		- Free unused objects
		- Close resources
		- Fix cyclic references
		- Tune GC / increase memory

- Code Not Thread-Safe

	- symptoms
		- Random crashes or inconsistent data
		- Intermittent test failures
		- Race conditions or deadlocks
		- High CPU under multithreading
	- causes
		- Shared mutable state without synchronization
		- Improper locking
		- Non-atomic operations
		- Using non-thread-safe libraries
	- tools
		- Add logging around critical sections
		- Use thread analyzers (ThreadSanitizer, Valgrind’s Helgrind)
		- Reproduce under stress test (stress-ng, load test scripts)
		- Enable debug mode with logging for concurrency
	- solutions
		- Add locks, semaphores, or atomic data types
		- Avoid shared state (use message queues)
		- Use thread-safe collections or design patterns (immutable objects, producer-consumer)

- Filesystem / Resource Limits

	- symptoms
		- “Too many open files” errors
		- Disk full
		- App can’t write logs
	- causes
		- Not closing file handles
		- Log rotation missing
		- ulimit too low
	- tools
		- lsof, df -h, ulimit -n
		- strace system calls
		- OS metrics
	- solutions
		- Close files properly
		- Raise ulimit
		- Clear disk space
		- Rotate logs

- Too Many Open Files or Child Processes

	- symptoms
		- “Too many open files” (EMFILE) error
		- Resource exhaustion
		- Slow system or failing new connections
		- Zombie processes
	- causes
		- File descriptors not closed
		- Infinite loop spawning processes
		- Missing cleanup handlers
		- OS ulimit too low
	- tools
		- lsof to list open files
		- ps aux or htop to check process count
		- ulimit -n to check limits
		- strace -f to trace syscalls
	- solutions
		- Close files/sockets after use
		- Kill zombie processes (pkill -9 or kill -9 <pid>)
		- Raise file descriptor limits (ulimit -n 65535)
		- Fix code to reuse resources

- High CPU Usage / CPU Starvation

	- symptoms
		- Slow response times
		- System fan spinning hard
		- 100% CPU usage in top or htop
		- Processes “stuck”
	- causes
		- Infinite loops
		- Inefficient algorithm
		- Spinlock or busy-wait
		- High GC (garbage collection) activity
		- Background job overload
	- tools
		- top, htop, pidstat for CPU usage per process
		- perf top, strace -p <pid> to trace syscalls
		- Language profiler (Py-spy, Go pprof, Java Flight Recorder)
		- APM tracing (Datadog, New Relic)
	- solutions
		- Fix infinite loops / optimize algorithms
		- Use asynchronous or event-driven architecture
		- Add caching
		- Tune garbage collector or reduce unnecessary threads

- Software Update Problem

	- symptoms
		- Service fails to start after update
		- Dependency version conflict or missing dependency
		- Broken API calls
		- Config files overwritten or missing
	- causes
		- Missing backward compatibility
		- Library or OS version mismatch
		- Dependency not pinned
		- Migration scripts not run
		- Breaking API changes
		- Config drift
	- tools
		- Check logs (CI/CD, journalctl, application logs)
		- diff old/new config/dependencies
		- Package manager logs (apt history, npm ls, pip freeze)
		- Rollback deployment in CI/CD
	- solutions
		- Rollback to stable version
		- Reinstall or rebuild dependencies
		- Run migrations properly
		- Add version pinning in package files
		- Implement canary or blue-green deployments

- Race Condition

	- symptoms
		- Random inconsistent results
		- Hard-to-reproduce bugs
		- Incorrect counters or data corruption
		- Occasional crashes under concurrency
	- causes
		- Shared mutable state accessed unsafely
		- Missing synchronization primitives
		- Improper use of threads/futures
	- tools
		- Thread analyzers (ThreadSanitizer, Helgrind, Go race detector)
		- Logging with timestamps and thread IDs
		- Deterministic test frameworks
	- solutions
		- Use mutexes, locks, or atomic variables
		- Avoid shared mutable data
		- Design for immutability or message passing

- Segmentation Fault (Segfault)

	- symptoms
		- Program crashes with “Segmentation fault (core dumped)”
		- Memory corruption
		- Inconsistent behavior depending on input
	- causes
		- Dereferencing null or freed pointers
		- Buffer overflow
		- Stack corruption
		- Invalid memory access
	- tools
		- gdb or lldb to inspect stack traces
		- Core dumps (ulimit -c unlimited)
		- AddressSanitizer / Valgrind Memcheck
	- solutions
		- Fix pointer handling
		- Validate array bounds
		- Use smart pointers (C++) or managed memory
		- Enable compiler warnings and sanitizers

- Deadlock (Threads) / Race Conditions

	- symptoms
		- System/app freezes but no crash
		- CPU idle
		- Threads or queries waiting indefinitely
	- causes
		- Two or more processes/threads each holding resources the other needs
		- Circular lock dependencies
		- Missing synchronization
		- Shared mutable state
	- tools
		- Thread dump (jstack, pstack)
		- Thread analyzers (ThreadSanitizer, Helgrind)
		- Logging thread IDs
		- lsof, strace for blocked syscalls
	- solutions
		- Lock ordering discipline
		- Use timeout-based locking
		- Reduce resource coupling
		- Avoid nested locks
		- Use consistent lock order
		- Add synchronization
		- Refactor to avoid shared state

- Database Lock / Lock Contention

	- symptoms
		- Queries hang or time out
		- “Lock wait timeout exceeded” errors
		- High DB CPU / connection pool saturation
		- Data corruption
	- causes
		- Long-running transactions
		- Uncommitted changes blocking others
		- Poor transaction isolation or missing indexes
	- tools
		- Database lock monitoring (SHOW ENGINE INNODB STATUS, DB lock graph, pg_locks)
		- Slow query logs
		- APM traces
		- EXPLAIN to check access paths
	- solutions
		- Reduce transaction size
		- Add indexes
		- Use shorter locks (autocommit)
		- Change isolation level (e.g., from SERIALIZABLE → READ COMMITTED)
		- Kill stale sessions

- Zombie Process

	- symptoms
		- Processes appear as <defunct> in ps output
		- System resources slowly deplete
		- Parent process unresponsive
		- Resource leaks
		- System slowdown
	- causes
		- Parent process not calling wait() after child exits
		- Orphaned subprocesses from mismanaged subprocess code
	- tools
		- `ps aux | grep defunct`
		- top or htop for zombie count
		- strace parent process
	- solutions

- Infinite Loop

	- symptoms
		- 100% CPU usage
		- Application not responding
		- No output or progress
	- causes
		- Logical error in loop condition
		- Missing break condition
		- Network or retry loop without limit
	- tools
		- top, htop for CPU usage
		- Attach debugger (gdb, pdb, lldb)
		- strace or perf top to inspect syscalls
		- Add debug prints / timeouts
	- solutions
		- Add proper termination condition
		- Add loop counter / timeout
		- Use safe iteration boundaries
		- Implement circuit breakers for retries

- CPU Spikes

	- symptoms
		- 100% CPU usage
		- System lag or freezing
		- High power draw
	- causes
		- Infinite loops
		- Busy waiting
		- Thread starvation
	- tools
		- top, htop, pidstat
		- strace or perf top
		- Attach debugger
	- solutions
		- Add termination conditions
		- Use async waits
		- Optimize loops
		- Fix thread management

- Cache / CDN Issues

	- symptoms
		- Stale data
		- Incorrect results until cache cleared
		- Performance worse than expected
		- Cache misses too frequent
		- Performance drop
	- causes
		- Wrong TTLs
		- Cache not invalidated on data change
		- Cache key collisions
		- Cache key mismatch
		- Wrong cache layer (client vs server)
	- tools
		- Inspect cache stats (redis-cli info, Memcached stats)
		- Use cache logging/debug mode
		- APM to compare cache hit/miss rates
		- Cache CLI tools (Redis CLI, Cloudflare analytics)
	- solutions
		- Fix cache keys / TTLs
		- Implement proper invalidation on data change
		- Warm caches during deploy
		- Add versioning to cache keys

- SSL/TLS/HTTPS Problems

	- symptoms
		- HTTPS connection fails
		- “SSL handshake failed” or “certificate not trusted” errors
		- Insecure connection warnings
	- causes
		- Expired/mismatched/self-signed certificates
		- Missing intermediate certs
		- Protocol mismatch (TLS1.0 vs TLS1.2)
		- Wrong hostname (CN mismatch)
	- tools
		- openssl s_client -connect host:443 -showcerts
		- Browser DevTools network tab
		- curl -v https://...
		- SSL Labs test
	- solutions
		- Renew or reissue certificates
		- Install full chain (intermediate + root), add the CA certificate into client trusted root store
		- Match CN/SAN to domain
		- Enforce modern TLS versions (≥1.2)

- Firewall / Security Group Issues	

	- symptoms
		- Connection refused / timeout
		- Service unreachable from specific networks
		- Ping or SSH blocked	
	- causes
		- Port blocked by OS firewall or cloud security group
		- Wrong inbound/outbound rules
		- NAT or routing misconfigured
	- tools
		- nmap, netcat (nc), or telnet to test open ports
		- Cloud security dashboards (AWS, GCP, Azure)
		- iptables -L, ufw status
	- solutions
		- Open required ports
		- Fix inbound/outbound rules
		- Adjust NAT or routing tables
		- Apply least privilege principles

- Distributed / Shards / Partition Problem

	- symptoms
		- Partial data visibility
		- Writes succeed on some nodes only
		- Inconsistent replication
		- High latency on distributed queries
		- Inconsistent data
		- Partial results
		- Replication lag
	- causes
		- Network partitions
		- Misconfigured cluster topology
		- Inconsistent replication settings
		- Schema/Version drift between nodes
		- Shard imbalance
	- tools
		- Cluster logs and health checks (e.g., mongostat, nodetool, kubectl logs)
		- Distributed tracing (Jaeger, Zipkin)
		- Network monitoring tools
	- solutions
		- Reconfigure cluster consistency
		- Resync or rebalance nodes/shards/partitions
		- Ensure same schema and version across nodes
		- Implement retry and idempotency logic

- Configuration / Environment Errors

	- symptoms
		- App works locally but not in production
		- Missing env variables
		- Startup failure
	- causes
		- Wrong config paths
		- Missing secrets
		- Inconsistent versions
	- tools
		- Compare configs
		- Log env vars
		- CI/CD environment diff
	- solutions
		- Fix configs / env vars
		- Version pinning
		- Use config management (Vault, dotenv)
