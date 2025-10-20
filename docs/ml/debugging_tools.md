- create a table like this of symptoms, probable problem root cause, and tools/tests to use to identify whether that problem is relevant to the symptom
	
	- problem symptoms, probable problem root cause, tool to identify problem, successful test case, solution/fix
	    - website credentials being stolen, XSS, XSS scanning tool, check if pysa identifies an XSS in code, if it does then auto-escape output before including it in html and avoid using innerhtml/eval and use nonces in scripts 
	    - slow query, database lock, check for locks with a query, query returns results, run a query to fix the table with the lock

	- Example Symptoms and tests
		- Slow performance: check if CPU or I/O bound
		- Crashes: check for an out of memory error or race condition
		- Timeout: check for a deadlock or infinite loop

- tools by category

	| **Category**                  | **Tools / Commands**                                                		    | **Purpose**                                            
	| ----------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
	| **Network / Firewall**        | `ping`, `traceroute`, `mtr`, `netcat`, `curl`, `tcpdump`, `nmap`, Wireshark 	| Trace packets, connectivity, protocol and latency issues        				|
	| **System / Process**          | `top`, `htop`, `ps aux`, `lsof`, `ulimit`, `vmstat`, `strace`, `gdb`, `perf`  | Monitor CPU, memory, processes, file handles, syscalls          				|
	| **Application**               | APM tools (Datadog, New Relic, OpenTelemetry)                       			| Trace transactions, measure latency                    		  				|
	| **Threading / Concurrency**   | ThreadSanitizer, Valgrind Helgrind, AddressSanitizer, Java Flight Recorder 	| Detect race conditions, deadlocks, memory and concurrency bugs  				|
	| **Database / Concurrency** 	| `SHOW PROCESSLIST`, `pg_locks`, `EXPLAIN`, transaction logs, pg_stat_activity | Identify performance bottlenecks, diagnose locks/deadlocks, blocking queries  |
	| **Load Balancing**			| HAProxy stats, AWS ELB metrics   									  			| Identify traffic misrouting							   		 				|
	| **Logging / Observability**   | Centralized log tools (ELK, Grafana Loki, CloudWatch)               			| Correlate events and root causes                      		  				|
	| **Cache / Distributed**    	| Redis CLI, Memcached stats, ELK stack logs                   					| Debug stale or inconsistent caching         					  				|
	| **Security / SSL**         	| `openssl`, OWASP ZAP, Burp Suite, `curl -v`, SSL Labs        					| Inspect SSL/TLS certs and vulnerabilities   					  				|
	| **Cluster / Cloud**        	| `kubectl`, `aws logs`, Grafana, Prometheus                   					| Detect communication or scaling issues      					  				|
    | **Configuration** 			| `env`, `cat /etc/*conf*` 														| Inspect system configuration including environment variables 					|

- server diagnostic process

	Connection fails: check network layer                            Server reachable: check server performance
	     Run `ping <IP>` / `traceroute`                                   High load? Check CPU/memory.  
	     Ping fails: network/routing issue                                     High CPU: check `top`, `ps`  
	     Ping ok: DNS issue/firewall block                                     High memory: check `free`, `vmstat`
	     Check NIC & routes: `ip a`, `ip route`                           If CPU wait (iowait) is high, then Disk or I/O bottleneck: Run `iostat -x`, `iotop`
	     Check firewall: ufw/iptables                                     If CPU wait (iowait) is low, then CPU-bound issue: Check process threads, infinite loops, runaway app      
	     Check load balancer: `curl -v`, LB logs                          Check disk space: `df -h`, if disk full: clean logs, tmp, rotate logs, expand volume 
	     Check DNS: `dig`, `nslookup`: Verify DNS resolution path         Check database: slow I/O, locks, queries, indexes
	     Network / DNS fix: adjust routes, DNS records                    Fix root cause: optimize DB, tune cache, upgrade disks
	     Test app/service again: `curl`, `ss -tulwn`, etc
	     Still broken? Check logs: `/var/log`, `journalctl`
	     Fix service configuration: restart/rebuild/patch/rollback

- tools to identify vulns with AI
	- Almanax, Corgea, ZeroPath, Gecko, and Amplify

- Monitor Resource Usage tools
	- Memory leaks: track with valgrind, leaks, or runtime profilers
	- CPU bottlenecks: profile performance using perf, top, htop, py-spy, or IDE profilers
	- Disk/IO: check iostat, iotop, or SQL slow query logs
	- Threads/processes: monitor with ps, pstree, or strace

- Metrics to Check for I/O problems
	Metric				Meaning									Healthy Range
	- iowait			% of time CPU waits for I/O				Usually < 5–10%
	- await				Average wait time per I/O (ms)			< 10–20ms (SSD), < 100ms (HDD)
	- svctm				Average service time (ms)				Should stay low and consistent
	- util				% of device busy time					> 80–90% means saturated
	- tps				I/O transactions per second				Depends on hardware (HDD < 200, SSD > 10k)
	- read/write KB/s	Throughput								High is OK if latency remains low

- System Monitoring & Performance tools
	- top		View real-time CPU, memory, and process usage
	- htop		Interactive version of top with color, sorting, and process tree view
	- vmstat	Display system performance (CPU, memory, I/O, swap), shows blocked processes (b), wa column for I/O wait
	- iostat	Show CPU and disk I/O statistics — useful for diagnosing disk bottlenecks, shows detailed per-device I/O performance (latency, throughput, busy%)
	- sar		Collect and report system activity over time (CPU, memory, I/O, etc), shows historical I/O stats (if sysstat is installed)
	- free		Display free and used memory (RAM and swap)
	- uptime	Show system uptime and average CPU load
	- dstat		Combined statistics for CPU, disk, network, and I/O in real-time
	- mpstat	Show CPU usage per core
	- pidstat	Monitor per-process resource usage (CPU, I/O)
	- lscpu		Display CPU architecture and core information
	- iotop		Which processes are doing the most I/O

- Process & Job Management tools
	- ps				Show current running processes.
	- pstree			Display processes in a tree structure (parent-child relationships).
	- kill				Terminate processes by PID.
	- pkill / killall	Kill processes by name.
	- nice / renice		Adjust process scheduling priority.
	- jobs				List background jobs in the current shell.
	- fg / bg			Bring background jobs to foreground or send them to background.
	- nohup				Run a command immune to hangups (keeps running after logout).
	- screen / tmux		Persistent terminal multiplexers — manage multiple sessions.

- Disk & Filesystem Management tools
	- df				Show available and used disk space on mounted filesystems.
	- du				Display disk usage per file or directory.
	- lsblk				List block devices (disks, partitions).
	- fdisk / parted	Partition disks.
	- mount / umount	Mount or unmount filesystems.
	- find				Search for files or directories based on patterns or properties.
	- locate			Quickly find files using a prebuilt index database.
	- tree				Display directory structure as a tree.
	- stat				Show detailed file info (permissions, timestamps, size, etc.).
	- du -sh *			Summarize disk usage by folder in human-readable form.
	- file				Identify the file type (binary, text, executable, etc.).
	- smartctl			Check disk health (SMART data)
	- blkid				Identify filesystem type

- Networking I/O & Connectivity tools
	- ping						Test network connectivity to a host.
	- traceroute / tracepath	Show path packets take to reach a destination.
	- nslookup / dig			Query DNS records.
	- ifconfig / ip addr		View or configure network interfaces.
	- netstat					Historical connections, packet drops
	- ss						Active connections and socket states
	- telnet / nc (netcat)		Test TCP/UDP connections, debug open ports.
	- tcpdump					Capture and inspect network packets.
	- nmap						Network scanner — check open ports, services, hosts.
	- hostname					Display or set system hostname.
	- route / ip route			Show or modify routing tables.
	- iftop						Real-time bandwidth per connection
	- nload						Live upload/download stats
	- ethtool					NIC status and driver info
	- iperf 					Bandwidth and throughput testing

- User, Permission & Security Management tools
	- whoami			Display the current logged-in username.
	- id				Show user and group IDs.
	- sudo				Run commands as another user (usually root).
	- su				Switch user or become superuser.
	- groups			Show user’s group memberships.
	- umask				Set default permission masks for new files.
	- ufw / iptables	Configure firewall rules.

- System & Hardware Information tools
	- uname -a			Display kernel and system info.
	- lsb_release -a	Show Linux distribution version.
	- lscpu				Display CPU details.
	- lsusb				List USB devices.
	- lspci				List PCI devices.
	- dmidecode			Show hardware info (BIOS, memory, manufacturer).
	- dmesg				View kernel ring buffer (hardware/system messages), look for hardware I/O errors
	- who / w			Show logged-in users and their activities.
	- history			View command history.

- Logging & Diagnostics tools
	- journalctl	View systemd logs.
	- dmesg			View kernel and hardware logs.
	- tail -f /var/log/syslog	Follow system logs in real time.
	- last / lastlog	Show recent logins.
	- logger	Write custom messages to syslog.

- Development, Debugging & Profiling tools
	- strace	Trace system calls and signals — useful for debugging runtime behavior.
	- ltrace	Trace library calls.
	- gdb	GNU debugger — debug compiled programs.
	- perf	Analyze CPU performance and hotspots.
	- valgrind	Detect memory leaks and profiling.
	- gcc / clang	Compile C/C++ programs.
	- objdump / nm	Inspect binaries and symbols.
	- readelf	Display ELF binary information.

- System Control & Services tools
	- systemctl	Manage systemd services (start, stop, restart, enable).
	- service	Control SysV init services (legacy).
	- shutdown / reboot / poweroff	Manage system power states.
	- cron / crontab	Schedule recurring tasks.
	- at	Schedule one-time tasks.


- I/O Problems

	- Disk Saturation	
		- causes
			- Too many read/write ops, logs, DB writes	
		- symptoms
			- High disk util%, high await
		- solutions
			- Move data to SSDs or faster disks, use RAID 10, or shard storage

	- Slow Storage	
		- causes
			- HDD vs SSD, poor RAID setup	
		- symptoms
			- High latency per I/O
		- solutions

	- Filesystem Fragmentation	
		- causes
			- Poor layout on disk	
		- symptoms
			- Gradual slowdown
		- solutions

	- Swap Thrashing	
		- causes
			- Low RAM leads to excessive swapping
		- symptoms
			- High I/O wait, slow system
		- solutions
			- Add RAM, reduce memory pressure

	- Network Bottleneck	
		- causes
			- Saturated NIC or high latency	
		- symptoms
			- Delays in I/O over networked storage
		- solutions

	- Faulty Disk/Controller	
		- causes
			- Hardware degradation	
		- symptoms
			- Kernel “I/O error” messages
		- solutions
			- Replace disks, check SMART data

	- NFS/Remote I/O	
		- causes
			- Slow networked filesystem	
		- symptoms
			- I/O waits with normal local disk stats
		- solutions

	- network storage lag
		- causes
		- symptoms
		- solutions
			- Optimize NFS/iSCSI, improve bandwidth or reduce hops

	- Poor I/O configuration
		- causes
		- symptoms
		- solutions
			- Tune kernel parameters (vm.dirty_ratio, vm.swappiness)

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
		- High disk read I/O
	- causes	
		- Missing indexes
		- Poor query structure (SELECT *)
		- Inefficient joins or subqueries
		- Full large table scans
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
		- Fix DNS, IP, routes, firewall, or security groups settings
		- Restart networking services
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
		- Out-of-memory errors
		- Invalid input
		- Memory leaks
		- Race conditions
		- Dependency version conflicts
	- tools
		- Log analysis
		- Tracing (OpenTelemetry, Jaeger)
		- Debugger (gdb, pdb, Visual Studio)
		- Crash dumps or core dumps (kill -QUIT <PID> creates core dump of a running process)
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
		- Memory profilers (Valgrind)
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
		- High CPU usage under multithreading
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
		- Not closing file/socket handles, file descriptor leak
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
		- Kill zombie processes (pkill -9 or kill -9 <pid>)
		- Manage subprocess code
		- Call wait() after child exits

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

- Deadlock (Threads) / Race Conditions

	- symptoms
		- Random inconsistent results
		- Hard-to-reproduce bugs
		- Incorrect counters or data corruption
		- Occasional crashes under concurrency
		- System/app freezes but no crash
		- CPU idle
		- Threads or queries waiting indefinitely
	- causes
		- Shared mutable state accessed unsafely
		- Missing synchronization primitives
		- Improper use of threads/futures
		- Two or more processes/threads each holding resources the other needs
		- Circular lock dependencies
	- tools
		- Thread analyzers (ThreadSanitizer, Helgrind, Go race detector)
		- Logging with timestamps and thread IDs
		- Deterministic test frameworks
		- Thread dump (jstack, pstack)
		- lsof, strace for blocked syscalls
	- solutions
		- Use mutexes, locks, or atomic variables
		- Avoid shared mutable data
		- Design for immutability or message passing
		- Lock ordering discipline
		- Use timeout-based locking
		- Reduce resource coupling
		- Avoid nested locks
		- Use consistent lock order
		- Add synchronization

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

- SQL Query Plan Problems

	- Seq Scan on large table					No index being used					Create index on filter columns
	- Nested Loop with many rows				Bad join order						Rewrite join or create index
	- High sort cost							Sorting large results				Create index to match ORDER BY
	- Rows mismatch (estimated/actual)			Planner misestimation				Run ANALYZE or adjust statistics target
	- Recheck Cond								Partial index or bitmap recheck		Ensure full index coverage
	- Filter applied post-index					Not selective enough				Create composite index
	- Disk spill messages	(verbose plans) 	Not enough memory for sort/hash		Increase work_mem

- Database Index Problems

	- Slow queries despite having indexes							Wrong or missing index 								Create index or use index hints (FORCE INDEX, USE INDEX) or update stats
	- Sequential (table) scans on large tables						No usable index for WHERE/JOIN condition 
	- Index not used in query plan (EXPLAIN)						Wrong index/filter order 							Recreate index with correct order or composite key
	- Index not used from index mismatch							Data type mismatch or function on column			Use functional index or cast properly
	- High write latency or slow inserts							Too many indexes on a table 						Drop low-usage indexes
	- High disk usage												Unused or redundant indexes
	- Queries with “Using filesort” or “Using temporary” (MySQL)	Missing composite index for ORDER BY or GROUP BY
	- Large/bloated or fragmented indexes							Frequent updates/deletes without vacuuming 			Rebuild or reindex
	- “Index only scan not possible”								Index doesn’t include all needed columns
	- Index scan slower than expected 								Poor selectivity (index returns too many rows)		Add more selective column to composite index
	- Indexes not covering query									Query needs columns not in index					Create a covering index (INCLUDE clause or multi-column index)

	- tools/solutions
		- check if index exists on filter/join Columns, if not create it
		- check if data types of the column and filter are equal
		- check index usage statistics and drop unused indexes
		- check for index fragmentation/bloat and reindex 
		- check for redundant/overlapping indexes and drop/merge 

- Memory Corruption

	- preventing memory corruption
		- Hardware disk errors				Use RAID + ECC memory + S.M.A.R.T. monitoring
		- Power failures					Enable journaling (InnoDB, WAL) + UPS
		- Unclean shutdowns					Ensure graceful stop scripts
		- File system corruption			Use modern FS (ext4, ZFS, XFS) with journaling
		- DB Software bugs					Keep DB engine up-to-date
		- In-memory corruption				Use ECC RAM, validate caches
		- Overclocking or faulty RAM		Run memtest regularly

	- memory corruption tools/solutions
		- monitor for abnormal heap growth with pmap, top, smem, /proc/<pid>/maps
		- check system I/O logs: dmesg | grep -i "I/O error" for disk errors that can lead to database corruption errors
		- check for hardware memory errors: (memtest, fsck, smartctl, iostat, ECC RAM logs: dmesg | grep -i ecc, check /var/log/syslog for kernel memory errors)
		- check for memory boundary issues with dmalloc
		- check for memory corruption errors: random crashes, segmentation faults, “Invalid pointer”, “SIGSEGV”, “SIGBUS”, “Bus error”
		- check for memory allocator corruption errors: double free, heap corruption
		- check for disk/buffer cache corruption errors: slow performance or I/O errors in logs
		- check for race conditions causing corruption with ThreadSanitizer and use mutexes/atomic operations
		- check for buffer overflows with AddressSanitizer and use bounds checks
		- check for stack overflow and limit recursion depth
		- use valgrind to detect invalid reads/writes, leaks, use-after-free, double free and fix memory leaks and track ownership correctly
	
	- database corruption tools/solutions
		- check database error logs and core dumps, run consistency/integrity checks: check table or pg_verify_checksums
		- check for database corruption errors: checksum mismatch, database start fails, page consistency errors, unexpected NULLs, missing rows, or wrong data
		- fix hardware/disk issues before restoring, identify corruption isolation, then vacuum, repair or backup/restore, reindex, re-run integrity checks

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
		- Inspect cache stats (redis-cli info, Memcached stats, Cloudflare analytics)
		- Use cache logging/debug mode
		- APM to compare cache hit/miss rates
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
		- Expired/mismatched/missing/self-signed certificates
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
		- Partial results or partial data visibility
		- Writes succeed on some nodes only
		- Inconsistent data/replication
		- High latency on distributed queries
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
