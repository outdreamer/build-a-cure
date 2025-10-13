- identifying vulns with AI
- Almanax, Corgea, ZeroPath, Gecko, and Amplify

- create a table like this of symptoms, probable problem root cause, and tools/tests to use to identify whether that problem is relevant to the symptom
- problem symptoms, probable problem root cause, tool to identify problem, successful test case, solution/fix
	    - website credentials being stolen, XSS, XSS scanning tool, check if pysa identifies an XSS in code, if it does then auto-escape output before including it in html and avoid using innerhtml/eval and use nonces in scripts 
	    - slow query, database lock, check for locks with a query, query returns results, run a query to fix the table with the lock
- make sure each unknown symptom is in the table as a problem as well
- make sure there is a tool/solution for each cause/symptom


- general problems

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


- specific problems

- dns not routing correctly

	- symptoms	
		- Website not loading (e.g., ERR_NAME_NOT_RESOLVED)
		- Requests go to the wrong server or timeout
		- Email not being delivered
	- causes	
		- Incorrect DNS records (A, CNAME, MX, etc.)
		- DNS propagation delay
		- Misconfigured DNS resolver
		- Cached old DNS entries
		- Expired domain or misconfigured nameserver
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

- slow sql queries

	- symptoms	
		- Web pages or APIs taking too long to load
		- Database CPU usage spiking
		- Lock contention or deadlocks
		- Timeouts in application layer
	- causes	
		- Missing indexes
		- Poor query structure (SELECT *)
		- Inefficient joins or subqueries
		- Large table scans
		- Unoptimized schema (no normalization or too much normalization)
	- tools
		- EXPLAIN or EXPLAIN ANALYZE in SQL
		- Database slow query logs
		- Performance monitoring tools (e.g., pg_stat_statements, New Relic, Datadog)
		- Index and schema inspection tools
	- solutions	
		- Add appropriate indexes
		- Optimize queries (avoid SELECT *, use WHERE conditions)
		- Cache results (e.g., Redis)
		- Use pagination for large data sets
		- Archive or partition old data

- stolen credentials

	- symptoms	
		- Unauthorized logins
		- Unusual traffic from suspicious IPs
		- Reports of account takeover
		- Credential dumps found online
	- causes	
		- SQL injection or XSS
		- Weak password hashing (MD5, SHA1)
		- No HTTPS
		- Compromised third-party library
		- Leaked API keys or database credentials in code
	- tools	
		- Web server and access logs
		- Intrusion detection tools (Wazuh, OSSEC)
		- Vulnerability scanners (OWASP ZAP, Burp Suite)
		- git-secrets or truffleHog for secret detection
		- SIEM dashboards (Splunk, Datadog Security)
	- solutions	
		- Rotate all exposed credentials immediately
		- Enforce strong password hashing (bcrypt, Argon2)
		- Use HTTPS everywhere
		- Sanitize user input and validate parameters
		- Implement rate limiting and 2FA
		- Conduct security audits and penetration testing

- networking problem

	- symptoms
		- Requests timeout or hang
		- “Host unreachable” / “Connection refused” errors
		- Packet loss
		- Slow SSH or HTTP
	- causes
		- Firewall blocking ports
		- Incorrect IP routing
		- Misconfigured subnet, gateway, or DNS
		- MTU mismatch
		- High latency links
	- tools
		- ping, traceroute, mtr to trace paths
		- netstat, ss, ifconfig, ip addr to inspect interfaces
		- Packet capture (tcpdump, Wireshark)
		- Check firewall rules (ufw, iptables, aws ec2 describe-security-groups)
	- solutions
		- Fix routes, firewall, or security groups
		- Restart networking services
		- Correct DNS or IP settings
		- Optimize MTU, QoS, or TCP settings

- load balancer misconfiguration

	- symptoms
		- Some users see errors, others don’t
		- Uneven traffic distribution
		- High latency or 502/504 errors
		- Backend servers idle or overloaded
	- causes
		- Incorrect health checks
		- Sticky session misconfiguration
		- Wrong backend targets
		- SSL termination mismatch
		- Load balancer timeout shorter than backend response
	- tools
		- Check load balancer logs & metrics (AWS ELB, Nginx, HAProxy dashboards)
		- Use curl -I or ab to test responses per backend
		- Monitor request distribution
	- solutions
		- Fix health check endpoints
		- Align timeouts with backend
		- Adjust load balancing algorithm (round robin, least connections)
		- Ensure all targets are registered and healthy

- poor performance

	- symptoms	
		- Slow page loads
		- High bounce rate
		- Long TTFB (Time to First Byte)
		- Rendering delays on frontend
	- causes	
		- Unoptimized assets (large images, non-minified JS/CSS)
		- Inefficient backend APIs
		- No caching or CDN
		- Blocking JavaScript
		- Too many HTTP requests
		- Inefficient database or network latency
		- load balancer misconfiguration
		- excess log storage taking up memory
	- tools	
		- Browser dev tools (Network tab, Lighthouse)
		- GTmetrix, PageSpeed Insights
		- APM tools (New Relic, Datadog, Dynatrace)
		- Profiling (Chrome Performance Profiler, React DevTools)
		- curl -w and ab (Apache Benchmark) for latency
	- solutions	
		- Optimize and compress assets (WebP, gzip, Brotli)
		- Use CDN (Cloudflare, Akamai)
		- Enable caching (HTTP cache, Redis)
		- Lazy load images
		- Minify JS/CSS and bundle efficiently
		- Optimize backend response times and DB access

- server crash

	- symptoms
		- 500 internal server errors
		- Service restarts or crashes
		- Log exceptions or segmentation faults
	- causes
		- Unhandled exceptions
		- Memory leaks
		- Race conditions
		- Dependency version conflicts
	- tools
		- Application logs (with structured logging like JSON)
		- Tracing (OpenTelemetry, Jaeger)
		- Crash dumps or core dumps
		- Profilers (e.g., py-spy, perf, gdb)
	- solutions
		- Add robust exception handling
		- Monitor memory usage and fix leaks
		- Add rate limiting and circuit breakers
		- Use version pinning in dependencies
		- Write integration and stress tests

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
		- Dependency version conflict
		- Broken API calls
		- Config files overwritten or missing
	- causes
		- Missing backward compatibility
		- Library or OS version mismatch
		- Dependency not pinned
		- Migration scripts not run
	- tools
		- Check logs (journalctl, application logs)
		- diff old/new config
		- Package manager logs (apt history, npm ls, pip freeze)
		- Rollback deployment in CI/CD
	- solutions
		- Rollback to stable version
		- Reinstall or rebuild dependencies
		- Run migrations properly
		- Add version pinning in package files
		- Implement canary or blue-green deployments

- Database Lock / Lock Contention

	- symptoms
		- Queries hang or time out
		- “Lock wait timeout exceeded” errors
		- High DB CPU / connection pool saturation
	- causes
		- Long-running transactions
		- Uncommitted changes blocking others
		- Poor transaction isolation or missing indexes
	- tools
		- Database lock monitoring (SHOW ENGINE INNODB STATUS, pg_locks)
		- Slow query logs
		- APM traces
		- EXPLAIN to check access paths
	- solutions
		- Reduce transaction size
		- Add indexes
		- Use shorter locks (autocommit)
		- Change isolation level (e.g., from SERIALIZABLE → READ COMMITTED)
		- Kill stale sessions

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

- Deadlock (Threads or DB)

	- symptoms
		- System freezes but no crash
		- CPU idle
		- Threads or queries waiting indefinitely
	- causes
		- Two or more processes/threads each holding resources the other needs
		- Circular lock dependencies
	- tools
		- Thread dump (jstack, pstack)
		- SHOW ENGINE INNODB STATUS or DB lock graph
		- lsof, strace for blocked syscalls
	- solutions
		- Lock ordering discipline
		- Use timeout-based locking
		- Reduce resource coupling
		- Avoid nested locks

- Zombie Process

	- symptoms
		- Processes appear as <defunct> in ps output
		- System resources slowly deplete
		- Parent process unresponsive
	- causes
		- Parent process not calling wait() after child exits
		- Orphaned subprocesses from mismanaged code
	- tools
		- `ps aux | grep defunct`
		- top or htop for zombie count
		- -strace` parent process

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

- Cache Misconfiguration

	- symptoms
		- Stale data
		- Incorrect results until cache cleared
		- Performance worse than expected
		- Cache misses too frequent
	- causes
		- Wrong TTLs
		- Cache not invalidated on data change
		- Key collisions
		- Wrong cache layer (client vs server)
	- tools
		- Inspect cache stats (redis-cli info, Memcached stats)
		- Use cache logging/debug mode
		- APM to compare hit/miss rates
	- solutions
		- Fix cache keys / TTLs
		- Implement proper invalidation
		- Warm caches during deploy
		- Add versioning to cache keys

- SSL/TLS/HTTPS Problems

	- symptoms
		- HTTPS connection fails
		- “SSL handshake failed” or “certificate not trusted” errors
		- Insecure connection warnings
	- causes
		- Expired or self-signed certificates
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
		- Install full chain (intermediate + root)
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

- Code Security Vulnerabilities

	- symptoms
		- Unauthorized access
		- Data leaks
		- XSS / SQL injection alerts
		- Strange input causing errors
	- causes
		- Lack of input sanitization
		- Insecure crypto or storage
		- Hardcoded credentials
		- Outdated libraries
	- tools
		- Static analyzers (SonarQube, Snyk, Bandit)
		- Dynamic analysis (Burp Suite, OWASP ZAP)
		- Dependency scanners
	- solutions
		- Sanitize and validate inputs
		- Use prepared statements
		- Rotate credentials and encrypt secrets
		- Keep dependencies updated
		- Implement security headers and CSP

- Poor Communication Between Shards / Partitions

	- symptoms
		- Partial data visibility
		- Writes succeed on some nodes only
		- Inconsistent replication
		- High latency on distributed queries
	- causes
		- Network partitions
		- Misconfigured cluster topology
		- Inconsistent replication settings
		- Schema drift between nodes
	- tools
		- Cluster logs and health checks (e.g., mongostat, nodetool, kubectl logs)
		- Distributed tracing (Jaeger, Zipkin)
		- Network monitoring tools
	- solutions
		- Reconfigure cluster consistency
		- Resync or rebalance shards
		- Ensure same schema and version across nodes
		- Implement retry and idempotency logic