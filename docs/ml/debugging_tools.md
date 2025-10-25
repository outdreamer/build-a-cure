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

- debugging strategies

	- Binary search over time: use log timestamps and checkpoints to narrow the moment an anomaly began
	- Instrumentation and tracing: use distributed tracing (OpenTelemetry), eBPF probes, or perf counters
	- Deterministic replay: tools like rr, time-travel debugging, or VM snapshots
	- Correlation analysis: compare metrics (CPU, memory, latency, error rate) to find related patterns
	- State dumps: capture core dumps, thread dumps, or tcpdumps for offline analysis

- server diagnostic process

	Connection fails: check network layer                            Server reachable: check server performance
	     Run `ping <IP>` / `traceroute`                                   High load? Check CPU/memory.  
	    	Ping fails: network/routing issue                             	High CPU: check `top`, `ps`  
	     	Ping ok: DNS issue/firewall block                             	High memory: check `free`, `vmstat`
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
	- ping						Test network connectivity to a host, test latency
	- traceroute / tracepath	Show path packets take to reach a destination, detect routing issues
	- nslookup / dig			Query DNS records/resolution
	- ifconfig / ip addr		View or configure network interfaces.
	- netstat / ss				Historical/active connections, packet drops, socket states, listening ports
	- telnet / nc (netcat)		Test TCP/UDP connections, debug open ports.
	- tcpdump / wireshark		Capture and inspect network packets.
	- nmap						Network scanner — check open ports, services, hosts.
	- hostname					Display or set system hostname.
	- route / ip route			Show or modify routing tables.
	- iftop						Real-time bandwidth per connection
	- nload						Live upload/download stats
	- ethtool					Check and configure NIC speed, duplex, and offload settings, check driver info
	- iperf / iperf3			Bandwidth and network throughput testing
	- ip a, ip route, ip link	Inspect and modify network interfaces and routes
	- mtr						Continuous traceroute with packet loss statistics.

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

- System, Hardware and OS-Level Problems

	- Heisenbugs in distributed systems: Only appear at scale or under race conditions between nodes.	
		- symptoms
			- Random consistency or latency issues
		- solutions
			- Use tracing (Jaeger, OpenTelemetry), distributed logs, and replay testing
	
	- Clock skew / time synchronization drift: Nodes disagree on time, breaking distributed coordination or SSL.	
		- symptoms
			- Authentication failures, data inconsistency.	
		- solutions
			- NTP/PTP monitoring, log timestamps, use monotonic clocks
	
	- Data corruption across layers (app → OS → storage): Data silently changed by drivers, firmware, or FS caching.	
		- symptoms
			- Hash/checksum mismatches, “phantom writes.”
		- solutions
			- End-to-end checksums, fsck, ZFS, RAID scrubbing
	
	- Eventual consistency anomalies: Data in distributed system lags behind expectations
		- symptoms
			- Reads return stale data intermittently
		- solutions
			- Tune replication lag, add quorum reads/writes, audit data repair jobs
	
	- Non-deterministic startup order bugs: Dependent services start in random order
		- symptoms
			- Intermittent boot failures
		- solutions
			- Use dependency managers (systemd units with After=), health checks, retries.

	- Bit flips / cosmic ray soft errors: Random hardware bit error in RAM or cache.	
		- symptoms
			- Random crashes, corrupted computations, checksum failures.	
		- solutions
			- ECC memory, error detection codes, redundancy, memtest86+
	
	- Power supply instability: Voltage fluctuations causing random resets or data corruption.	
		- symptoms
			- Random restarts, sudden crashes.	
		- solutions
			- Use UPS, monitor voltage rails, replace PSU
	
	- Intermittent hardware faults: Occur randomly, not reproducible.	
		- symptoms
			- Random kernel panics, ECC errors, I/O failures.	
		- solutions
			- Swap components (RAM, NICs, disks) to isolate; use smartctl, dmesg, or IPMI logs
	
	- Bus contention / signal integrity issues: Improper termination, crosstalk, or grounding.	
		- symptoms
			- Unreliable data transmission, high CRC errors.	
		- solutions
			- Use oscilloscopes, logic analyzers, and PCB design verification tools
	
	- Firmware / microcode bugs: Hard to update and diagnose; often vendor-specific
		- symptoms
			- Kernel or BIOS errors, device misbehavior.	
		- solutions
			- Check firmware updates, apply vendor patches, analyze with fwupdmgr, or downgrade temporarily

	- Infinite Loop / 100% CPU

		- symptoms
			- Process hangs with 100% CPU and no I/O activity
				top
					PID USER  %CPU %MEM COMMAND
					1234 root 99.8  0.3  myapp
			- Application not responding
			- No output or progress
		- causes
			- Logical error in loop condition
			- Missing break condition
			- Network or retry loop without limit
		- tools
			- top, htop for CPU usage
			- Attach debugger (gdb, pdb, lldb)
			- strace or perf top to inspect for repeating syscalls
			- Add debug prints / timeouts
		- solutions
			- Add proper termination condition
			- Add loop counter / timeout
			- Use safe iteration boundaries
			- Implement circuit breakers for retries
			- debug control variables.
			- Attach debugger:
				strace -p 1234
				- Seeing repeated syscalls like the following indicates unbounded loop, fix control condition.
					read(3, "", 0) = 0	

	- High CPU Usage or CPU saturation/starvation/spikes

		- symptoms
			- 100% CPU usage in top or htop, perf top shows hot function
			- System lag or freezing, slow response times
			- High power draw
			- System fan spinning hard
			- Processes “stuck”
		- causes
			- Infinite loops
			- Busy waiting
			- Thread starvation
			- Inefficient algorithm
			- Spinlock or busy-wait
			- High GC (garbage collection) activity
			- Background job overload
		- tools
			- top, htop, pidstat for CPU usage per process
			- perf top, strace -p <pid> to trace syscalls
			- Attach debugger
			- Language profiler (Py-spy, Go pprof, Java Flight Recorder)
			- APM tracing (Datadog, New Relic)
		- solutions
			- Add termination conditions
			- Use asynchronous or event-driven architecture
			- Fix infinite loops / optimize algorithms
			- Fix thread management
			- Throttle processes or use a load balancer to distribute the load evenly
			- Add caching
			- Tune garbage collector or reduce unnecessary threads
			- Identify the process responsible:
				ps -fp 1234
				strace -p 1234
			- Restart service: sudo systemctl restart myapp.service
		
	- Disk Errors or Hardware Failure

		- symptoms
			- Disk or disk partitions fail to mount
			- Errors in logs about I/O failure or device errors
			- Unusual noise or slow disk performance (if using HDDs)
		- causes
			- Bad sectors on the disk or SSD wear
			- Faulty cables or connections
			- Filesystem corruption
		- tools
			Check disk health: Use smartctl (SMART data for HDD/SSD) (sudo smartctl -a /dev/sda)
			Run filesystem checks: fsck /dev/sda1 for ext4 and xfs_repair /dev/sda1 for xfs
		- solutions
			- Replace the disk if physical failure is detected
			- Ensure RAID redundancy if applicable, and replace failed disks immediately

		- Failing Disk
			- symptoms: 
				sudo smartctl -a /dev/sda
					- SMART overall-health self-assessment test result: FAILED
			- solutions: Backup immediately, replace drive.

		- Disk Full
			- symptom:
				- df -h shows 100% use; du -sh * reveals large dirs
					df -h
						Filesystem      Size  Used Avail Use% Mounted on
						/dev/sda1        50G   50G     0 100% /
			- causes: Root filesystem full.
			- tools: df, du
			- solution: 
				- Clean /tmp, rotate files, or extend volume.
				- Clean logs:
					sudo journalctl --vacuum-time=7d
					sudo rm -rf /var/log/\*.gz
				- Find large files:
					sudo du -ahx / | sort -rh | head -20
		
		- Disk I/O Bottleneck
			- symptom:
				- iostat -xz 1 shows high %util and %iowait; e.g. %util=99%
					iostat -xz 1
						Device:  %util
						sda       99.5
			- causes: Disk is saturated — I/O bottleneck.
			- tools: iostat, vmstat, dstat
			- solution: 
				- optimize queries or add faster storage, or use async I/O
				- Disk overloaded: Tune queries, optimize disk layout, use SSD, or balance load.
		
		- Disk I/O errors
			- symptom: dmesg shows: blk_update_request: I/O error, dev sda
			- tools: dmesg, smartctl
			- solution: Failing disk. Replace hardware.

		- Bad Disk Sector
			- symptom:
				dmesg | grep -i error
				blk_update_request: I/O error, dev sda, sector 123456
			- causes: Bad disk sector.
			- solution: Run SMART test and replace disk if failing.
				sudo smartctl -t short /dev/sda

		- Faulty Disk/Controller	
			- causes
				- Hardware degradation	
			- symptoms
				- Kernel “I/O error” messages
			- solutions
				- Replace disks, check SMART data

		- Disk Saturation	
			- causes
				- Too many read/write ops, logs, DB writes	
			- symptoms
				- High disk util%, high await
			- solutions
				- Move data to SSDs or faster disks, use RAID 10, or shard storage

	- Thermal throttling or overheating: System performance varies with temperature.	
		- symptom:
			- Performance degradation under load
			- sensors shows temp near limit; /proc/thermal_zone*/temp high
				sensors
					Core 0: +95.0°C (high = +80.0°C, crit = +100.0°C)
		- causes: CPU overheating, throttling possible.
		- tools: lm-sensors, ipmitool
		- solution: 
			- Clean dust, replace thermal paste, improve cooling, lean heatsinks, monitor sensors (lm-sensors, IPMI), replace/clean fans, ensure proper ventilation.

	- ECC Memory Errors
		- symptom:
			- dmesg logs “EDAC MC0: CE memory read error”
				dmesg | grep -i edac
					EDAC MC0: 1 CE memory read error on CPU#0Channel#0_DIMM#0
		- causes: Correctable ECC memory error.
		- tools: dmesg, edac-util
		- solution: Monitor frequency; replace faulty RAM if recurring.

	- Power supply fluctuation
		- symptom: ipmitool sdr shows voltage out of range
		- tools: ipmitool, BIOS logs
		- solution: Replace PSU or fix power source.

	- Network interface errors
		- symptom: ethtool -S eth0 shows high RX/TX errors
		- tools: ethtool, dmesg
		- solution: Bad cable, duplex mismatch, or faulty NIC.

	- System won’t boot (GRUB error)
		- symptoms: grub rescue> 
			- error: file '/boot/grub/i386-pc/normal.mod' not found
			- Cause: GRUB corrupted or missing after disk changes or updates.
		- solutions: 
			- Boot from live CD/USB
				sudo grub-install --boot-directory=/mnt/boot /dev/sda
				sudo update-grub
			- If /boot partition was moved, mount it first:
				sudo mount /dev/sda1 /mnt/boot

	- Kernel Panic
		- symptoms: 
			- /var/log/kern.log or serial console shows “kernel panic – not syncing VFS: Unable to mount root fs"
		- causes: Missing or corrupt initramfs or kernel modules.
		- tools: dmesg, console logs
		- solutions: 
			- Hardware fault, bad driver, or corrupted kernel module. Reboot, update kernel, run memtest.
			- Boot into recovery or previous kernel from GRUB.
			- Rebuild initramfs:
				sudo update-initramfs -u
			- Reinstall kernel if necessary:
				sudo apt install --reinstall linux-image-$(uname -r)

	- File Permissions Broken
		- symptoms: Permission denied
		- solutions: 
			sudo chown -R username:username /path/to/files
			sudo chmod -R 755 /path/to/dir
			- For system directories, check /etc/fstab mount options.

	- Interface Missing
		- symptoms: ip link show
		- solutions: 
			- Check driver module:
				sudo lshw -C network
				sudo modprobe <driver_name>
			- Re-enable interface:
				sudo ip link set eth0 up

	- Locked Package Manager
		- symptoms: 
			- Could not get lock /var/lib/dpkg/lock
		- solutions: 
			sudo rm /var/lib/dpkg/lock-frontend
			sudo rm /var/lib/apt/lists/lock
			sudo dpkg --configure -a

	- Service Not Starting
		- symptoms: sudo systemctl status nginx
			- nginx.service - failed (code=exited, status=1/FAILURE)
		- solutions: 
			- View logs:
				sudo journalctl -xeu nginx
			- Port already in use → sudo netstat -tulnp | grep 80
			- Bad config → nginx -t

	- Cron Jobs Not Running
		- symptoms:
			- Check logs:
				grep CRON /var/log/syslog
		- solutions: 
			- Ensure cron service running:
				sudo systemctl status cron
			- Use full paths in scripts (/usr/bin/python not just python).

	- “Authentication failure” (sudo)
		- solutions: 
			- Unlock account:
				sudo passwd username
			- Check sudoers:
				sudo visudo
			- Add:
				username ALL=(ALL) ALL

	- SSH Login Denied
		- symptoms:
			- Logs:
				tail -n 20 /var/log/auth.log
		- solutions: 
			- Check permissions:
				chmod 700 ~/.ssh
				chmod 600 ~/.ssh/authorized_keys
			- Ensure sshd is running:
				sudo systemctl restart ssh

	- Missing Drivers
		- symptoms: 
			lspci -k | grep -A 3 -i network
			- If “Kernel driver in use” is empty → missing driver.
		- solutions: 
			sudo apt install linux-firmware
			sudo modprobe <driver_name>

	- Kernel Module Fails to Load
		- symptoms: 		
			- modprobe: ERROR: could not insert 'nvidia': No such device
		- solutions: 
			- Reinstall module package.
			- Check compatibility with uname -r.
			- Rebuild modules:
				sudo dkms autoinstall

	- USB Devices Not Detected
		- symptoms: dmesg | grep usb
		- solutions: 
			- Reload USB modules:
				sudo modprobe -r usb_storage && sudo modprobe usb_storage

	- Repeated Errors in syslog
		- symptoms: 
			sudo journalctl -p 3 -xb
				- kernel: EXT4-fs error (device sda1): ext4_find_entry:1453: inode ...
		- solutions: Check disk (fsck), filesystem mount options, and hardware.

- I/O Problems

	- Slow Storage	
		- causes
			- HDD vs SSD, poor RAID setup	
		- symptoms
			- High latency per I/O
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

- Database Problems

	- symptoms	
		- Web pages or APIs taking too long to load
		- Database CPU usage spiking
		- Lock contention or deadlocks
		- Timeouts in application layer
		- Queries hang or time out
		- Data inconsistency
		- “Lock wait timeout” errors
		- High disk read I/O or high disk utilization.
	- causes	
		- Missing indexes
		- Poor query structure (SELECT *)
		- Inefficient joins or subqueries
		- Full large table scans
		- Lock contention
		- Slow queries
		- Unoptimized schema (no normalization or too much normalization)
		- Overloaded or under-configured database resources (CPU, memory, disk).
		- Corrupted database or corrupted indexes.
	- tools
		- EXPLAIN or EXPLAIN ANALYZE query plans in SQL
		- Database slow query logs
		- Performance monitoring tools (e.g., pg_stat_statements, pg_locks / InnoDB status, New Relic, Datadog)
		- Index and schema inspection tools
		- run checks for database corruptioni
	- solutions	
		- Add appropriate indexes, rebuild indexes if fragmented
		- Optimize queries (avoid SELECT *, use WHERE conditions, use LIMIT, use indexed columns, avoid correlated subqueries)
		- Cache results (e.g., Redis)
		- Use pagination for large data sets
		- Archive or partition old data
		- Tune connection pool
		- Reduce transaction scope
		- Increase buffer pool size (InnoDB buffer)
		- Adjust query cache or memory parameters

	- Missing Index / Slow Query
		- symptom:
			- EXPLAIN shows Seq Scan on large table
				EXPLAIN SELECT * FROM orders WHERE customer_id = 123;
					Seq Scan on orders  (cost=0.00..45832.00 rows=1200 width=80)
	  				Filter: (customer_id = 123)
		- causes: Sequential scan means no index used.
		- tools: EXPLAIN, EXPLAIN ANALYZE
		- solution: Create index:
			CREATE INDEX idx_col ON table(col);
	
	- Database Connection Exhaustion
		- symptom:
			SHOW STATUS LIKE 'Threads_connected';
			Threads_connected: 200
			- “Too many connections” error; 
		- causes: All available connections in use.
		- tools:
			- DB logs, DB console
		- solution: 
			- Increase pool size or close connections in app or use connection pooling middleware.
			SET GLOBAL max_connections = 500;
	
	- Corrupted Database Table
		- symptom:
			- CHECKDB or pg_verify_checksums or mysqlcheck reports errors
			mysqlcheck mydb -c -u root -p
				mydb.users
				error    : Table is marked as crashed and should be repaired
		- tools: 
			- DB internal check utilities
		- solution: 
			- Restore from backup or use page repair.
			mysqlcheck mydb --repair -u root -p

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

		- Deadlock
			- symptom:
				- Database logs show ERROR: deadlock detected; pg_stat_activity shows waiting queries
					SHOW ENGINE INNODB STATUS\G
						LATEST DETECTED DEADLOCK
						TRANSACTION (1): waiting for lock on record
						TRANSACTION (2): holding lock on the same record
			- causes: Circular lock dependency.
			- tools: DB logs, pg_stat_activity, SHOW ENGINE INNODB STATUS
			- solution: Shorten transaction scope, reorder transaction locks, acquire locks in consistent order.
		
		- Lock contention
			- symptom: pg_locks shows multiple transactions waiting
			- tools: SQL monitoring views
			- solution: Reduce lock duration, add retry logic, or use lower isolation level.

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

- Security Vulnerabilities

	- symptoms	
		- Unauthorized logins
		- Unusual traffic from suspicious IPs
		- Reports of account takeover
		- privilege escalation
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
		- fuzzing (AFL, libFuzzer), sandboxing
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
		- Network-dependent services (e.g., web or database) are not reachable.
	- causes
		- Firewall blocking ports or security groups misconfiguration
		- Incorrect IP routing
		- Misconfigured subnet, gateway, or DNS
		- MTU (Maximum Transmission Unit) mismatch (devices in a network have different MTU settings, leading to packet fragmentation or drops)
		- High latency links
		- Network congestion or bandwidth issues
		- Hardware failure (e.g., faulty network interface card or cables)
	- tools
		- ping, traceroute, mtr (my traceroute) to trace paths
		- curl, netcat, tcpdump
		- netstat, ss, ifconfig, ip addr to inspect interfaces
		- Packet capture (tcpdump, Wireshark)
		- Check firewall rules (ufw, iptables, aws ec2 describe-security-groups)
		- Network logs
		- Check for high latency using traceroute or mtr
		- Use netstat or ss to see open connections and troubleshoot blocked ports:
	- solutions
		- Fix DNS, IP, routes, firewall, or security groups settings
		- Restart networking services
		- Optimize MTU, QoS, or TCP settings
		- Open correct ports
		- Use CDN or caching
		- Replace or repair faulty hardware (NIC, cables) if identified

	- Asymmetric routing: Request and response take different network paths.	
		- symptoms
			- Works intermittently, packets dropped by firewalls on return path.	
		- solutions
			- traceroute, NetFlow logs, route analysis on both ends
	
	- Network partition (“split-brain”) in clusters: Nodes in a distributed system can’t communicate but still think they’re primary.	
		- symptoms
			- Data inconsistency, dual writes, corrupted state.	
		- solutions
			- Use quorum-based replication, monitor health checks, design for partition tolerance (CAP theorem)
	
	- NAT traversal / firewall state timeouts: Stateful firewalls or NAT devices silently drop idle connections
		- symptoms
			- Random disconnections after idle period.	
		- solutions
			- Tune TCP keepalives, increase NAT session timeout, or use UDP hole punching

	- No Internet Connectivity
		- symptoms
			ping -c 3 8.8.8.8
			ping -c 3 google.com
			- IP reachable but not domain → DNS issue.
			- Nothing reachable → routing or interface down.
		- solutions: 
			sudo systemctl restart NetworkManager
			sudo dhclient eth0
			- Check routes: ip route

	- Port not listening
		- symptom: netstat -tulnp or ss -lntp shows no process on port
		- tools: ss, netstat
		- solution: Service not started or misconfigured. Start or check service binding config.

	- Asymmetric routing / firewall drop
		- symptom: tcpdump sees SYN sent but no SYN-ACK returned
		- tools: tcpdump
		- solution: Return path blocked or misrouted. Tracepath from both directions, check routing tables.
	
	- Network congestion or bufferbloat
		- symptom: ping -f latency spikes; iftop shows interface saturation
		- tools: ping, iftop, nload
		- solution: Shape or rate-limit traffic; increase queue size or use QoS.

	- Firewall/security group blocking traffic	
		- symptom:
			- Services unreachable (e.g. SSH, HTTP) from specific networks; connection refused/timeout
			- Ping or SSH blocked
			- iptables -L -v -n shows DROP policy or rule for target port
				sudo iptables -L -v -n | grep 443
				DROP       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:443
		- causes: 
			- Inbound HTTPS traffic (port 443) is being dropped by firewall rules.
			- Port blocked by OS firewall (iptables or ufw rules blocking ports) or cloud security group/firewall (AWS, Azure, etc.)
			- Wrong inbound/outbound rules
			- NAT or routing misconfigured
		- tools
			- sudo ufw status, sudo iptables -L -n -v, nc -zv <host> <port>	
			- nmap, netcat (nc), or telnet to test open ports
			- Cloud security dashboards (AWS, GCP, Azure)
			- nft list ruleset
		- solutions
			- Check cloud security groups and fix inbound/outbound rules
			- Adjust NAT or routing tables
			- Apply least privilege principles
			- Remove or change rule for the port:
				sudo ufw allow 22/tcp 
				sudo iptables -I INPUT -p tcp --dport 443 -j ACCEPT
				sudo service iptables save

	- Packet Loss
		- symptoms:
			- Poor performance
			- Intermittent disconnects or dropped SSH sessions	
			- Intermittent packet loss / latency spikes: Occur only under certain traffic conditions, may be due to physical layer, congestion, or faulty NIC
			- ping shows dropped packets; tcpdump shows TCP retransmissions ([RST], [Dup ACK], [Retransmission])
				ping -c 5 8.8.8.8
					5 packets transmitted, 3 received, 40% packet loss, time 4006ms
				$ sudo tcpdump -i eth0 -n 'tcp port 80'
					15:03:40.123456 IP 10.0.0.1.34567 > 10.0.0.2.80: Flags [S], seq 1000
					15:03:41.123789 IP 10.0.0.1.34567 > 10.0.0.2.80: Flags [S], seq 1000 (retransmission)
		- causes:
			- faulty link between host and gateway, faulty NIC, faulty hardware/cable
			- SYN retransmission means lost packet or blocked port.
			- Congestion, MTU mismatch	
		- tools: ping -c 100 <host>, mtr, tcpdump -n -i eth0, wireshark
		- solution: 
			- Use mtr to isolate hop: run mtr 8.8.8.8 to find the hop where packets are dropped
			- check/replace hardware/cables
			- check router/switch config/logs
			- Tune MTU (ip link set mtu 1400 dev eth0)
			- Use iperf3, tcpdump, ethtool, and time-correlated metrics. Capture packets on both ends

		- SYN Retransmissions
			- symptom:
				sudo tcpdump -i eth0 -n 'tcp port 80'
					15:03:40.123456 IP 10.0.0.1.34567 > 10.0.0.2.80: Flags [S], seq 1000
					15:03:41.123789 IP 10.0.0.1.34567 > 10.0.0.2.80: Flags [S], seq 1000 (retransmission)
			- causes: Server not responding — possibly port blocked or packet dropped.
			- solution: Check service status, firewall, routing.
		
		- TCP Retransmissions (Loss)
			- symptom:
				sudo tcpdump -nnvvv -i eth0 'tcp and port 443'
				[Retransmission] Seq=12345 Ack=67890 Win=2048
			- causes: Packets lost or delayed, network congestion.
			- solution: Use mtr to find bad hop, or adjust TCP window.
		
		- Duplicate ACKs
			- symptom: [Dup ACK 42#1] Seq=12345 Ack=67890
			- causes: Indicates packet loss or reordering.
			- solution: Check NIC errors: ethtool -S eth0 | grep error

	- DNS resolution failure	
		- symptoms
			- Website or host unreachable (ping: unknown host, curl: Could not resolve host)	
			- Website not loading (e.g., ERR_NAME_NOT_RESOLVED)
			- Requests go to the wrong server or timeout
			- Email not being delivered
			- dig example.com shows wrong or no A record; ping fails by name but works by IP
				dig example.local
					;; connection timed out; no servers could be reached
		- causes
			- Misconfigured DNS resolver or nameserver (/etc/resolv.conf)
			- Wrong DNS server
			- DNS cache poisoning: Wrong IP resolved, service unreachable intermittently
			- DNS server outage	
			- Incorrect DNS records (A, CNAME, MX, etc.)
			- DNS propagation delay
			- Expired domain
		- tools
			- nslookup, dig, host, resolvectl, systemd-resolve --status	to check DNS records
			- ping and traceroute to test network path
			- Online tools like DNSChecker.org
			- Check domain registrar & DNS provider dashboards
		- solutions
			- Check /etc/resolv.conf entries
			- Test with public DNS: 8.8.8.8 or 1.1.1.1
			- Restart systemd-resolved
			- Correct A/AAAA/CNAME records
			- Wait for DNS propagation (can take 24–48 hrs)
			- Fix nameserver entries at registrar
			- Use a reliable DNS host (e.g., Cloudflare, Route53)
			- verify upstream DNS
			- Check cat /etc/resolv.conf and update with:
				nameserver 8.8.8.8
			- DNS cache poisoning / stale records: Cached incorrect or outdated DNS entries; Use dig +trace, flush DNS caches, verify TTLs	
				- Clear local DNS cache: sudo systemd-resolve --flush-caches or ipconfig /flushdns or sudo dscacheutil -flushcache

	- Network interface down
		- symptoms	
			- No network connectivity; ping fails even to gateway	
		- causes
			- Interface disabled
			- Cable unplugged
			- NIC driver issue	
		- tools
			- ip a, ethtool eth0, nmcli dev status	
		- solutions
			- Bring interface up: sudo ip link set eth0 up
			- Reconnect cable
			- Restart NetworkManager
			- Check NIC drivers

	- IP address conflict
		- symptoms	
			- Random disconnects; “Duplicate IP address detected”	
		- causes
			- Two hosts on same network with same IP	
		- tools
			- arp -a, ip neigh show, nmap -sn <subnet>	
		- solutions
			- Assign unique static IP or enable DHCP
			- Clear ARP cache: sudo ip -s -s neigh flush all

	- Routing problem	
		- symptoms
			- Can reach local network but not internet	
		- causes
			- Default gateway missing or wrong route
			- Misconfigured routing tables	
		- tools
			- ip route, netstat -rn, traceroute <ip>	
		- solutions
			- Add correct default route: ip route add default via <gateway>
			- Fix gateway settings in /etc/netplan/ or /etc/network/interfaces

	- Slow network / high latency	
		- symptoms
			- Lag, slow file transfers, timeouts	
		- causes
			- Network congestion
			- Faulty cable/switch
			- Duplex mismatch
			- Bandwidth throttling	
		- tools
			- ping, mtr, iperf3, ethtool, ifconfig	
		- solutions
			- Replace bad cable
			- Match duplex/speed: ethtool -s eth0 speed 1000 duplex full
			- Use QoS or traffic shaping
			- Upgrade link capacity

	- MTU mismatch (Fragmentation Needed)/ packet fragmentation
		- symptoms	
			- Large packets dropped silently due to mismatched MTU or misconfigured PMTU discovery.
			- Works for small requests, fails for large ones (e.g., HTTPS).		
			- VPN drops, incomplete file transfers, slow HTTPS	
			- ping -M do -s 1472 <host> gives “Frag needed and DF set”
				ping -M do -s 1472 8.8.8.8
					From 192.168.1.1 icmp_seq=1 Frag needed and DF set (mtu = 1400)
		- causes
			- Path MTU Discovery failing
			- Encapsulation overhead (VPN, GRE, IPSec)
			- Packets too large for network path; MTU mismatch.	
		- tools
			- ping -M do -s <size> <host>, tracepath <host>	
		- solutions
			- Lower MTU (common for VPNs: 1400–1420) or correct tunnel configuration
				- Typical fix: set MTU to 1400 on VPN interfaces.
					sudo ip link set dev eth0 mtu 1400
			- Adjust router MTU or disable DF flag
			- check tunnel/VPN MTU settings

	- DHCP issues	
		- symptoms
			- No IP assigned, network unreachable	
		- causes
			- DHCP server down
			- DHCP scope exhausted	
		- tools
			- journalctl -u NetworkManager, tcpdump -i eth0 port 67 or 68	
		- solutions
			- Restart DHCP service
			- Increase DHCP range
			- Verify client can reach DHCP server

	- SSL/TLS/HTTPS problems
		- symptoms
			- HTTPS site fails to load/connection fails
			- “SSL handshake failed” or “certificate not trusted” errors
			- Insecure connection warnings
		- causes
			- Incorrect chain
			- Cipher mismatch	
			- Expired/mismatched/missing/self-signed certificates
			- Protocol mismatch (TLS1.0 vs TLS1.2)
			- Wrong hostname (CN mismatch)
		- tools
			- openssl s_client -connect host:443 -showcerts
			- Browser DevTools network tab
			- curl -v https://...
			- SSL Labs test
		- solutions
			- Renew/reissue certificates (e.g., Let’s Encrypt)
			- Include full chain including root/intermediate certs in chain, add the CA certificate into client trusted root store
			- Enforce modern TLS versions (≥1.2)
			- Match CN/SAN to domain

		- SSL/TLS handshake or certificate chain issues: 
			- symptoms
				- HTTPS or SMTP connection failures
				- openssl s_client -connect host:443 shows cert verify error or unsupported cipher
			- causes
				- Misconfiguration in intermediate certs, SNI mismatch, or cipher suite incompatibility.		
			- tools: openssl, curl -v
			- solutions
				- Use openssl s_client, test with SSL Labs, renew certs, configure proper chains
				- Wrong cert chain or cipher mismatch. Reinstall intermediate certs, renew cert, or update cipher list.

		- SSL Certificate Expired
			- symptom:
				echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
					notBefore=Oct  1 00:00:00 2024 GMT
					notAfter=Oct  1 00:00:00 2025 GMT
			- causes: If current date > notAfter, the cert is expired.
			- solution: Renew certificate (certbot renew, reissue from CA).
		
	- Load Balancer / Proxy Issues
		- symptoms
			- Some users see errors while others don’t or some users can’t connect, or some requests fail or time out
			- Uneven traffic distribution
			- High latency or 502/504 errors
			- Backend servers idle or overloaded
		- causes
			- Incorrect health checks
			- Sticky session misconfiguration
			- Wrong/unhealthy backend targets, backend unreachable
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
			- Fix backend pool configuration
			- Enable session persistence if required

		- Load balancer sticky session errors: Sessions pinned inconsistently to backend servers.	
			- symptoms
				- Authentication/session failures under load.	
			- solutions
				- Enable consistent hashing or session replication

	- VPN or tunnel issues	
		- symptoms
			- Remote access fails, unstable connection	
		- causes
			- MTU mismatch
			- Misconfigured routing
			- Key/cert expiry	
		- tools
			- ip route, ping, journalctl -u openvpn	
		- solutions
			- Reissue VPN keys
			- Fix routing entries
			- Adjust MTU or compression settings

	- Proxy or NAT issues
		- symptoms	
			- Can’t access external resources	
		- causes
			- Wrong proxy configuration
			- NAT rule misconfigured	
		- tools
			- env | grep -i proxy, iptables -t nat -L -n -v
		- solutions

	- ARP cache issues	
		- symptoms
			- Intermittent connectivity	
		- causes
			- Stale ARP cache or spoofing	
		- tools
			- arp -n, ip neigh show	
		- solutions
			- Flush ARP cache: sudo ip -s -s neigh flush all
			- Use static ARP entries for critical hosts

	- Network driver or firmware bugs	
		- symptoms
			- NIC stops working randomly	
		- causes
			- Outdated driver
			- Kernel bug	
		- tools
			- dmesg	| grep eth, ethtool -i eth0
		- solutions

	- DoS / excessive connections	
		- symptoms
			- Server unresponsive, high network usage	
		- causes
			- Flood of inbound connections	
		- tools
			- netstat -an | grep ESTABLISHED
		- solutions

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

- Application/Server problems

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
		- Corrupted files or databases.
		- Insufficient system resources (e.g., RAM or CPU).
		- Permission issues on files or directories.
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
		- Ensure enough system resources are available (CPU, memory, disk space).
		- Test service startup with debugging: systemctl start <service_name> --debug

	- Heisenbugs (timing-dependent bugs): Vanish or change behavior when observed (e.g., with breakpoints or logging).	
		- symptoms
			- Works when debugging, fails in production.	
		- solutions
			- Use logging with timestamps, deterministic record/replay debuggers, increase log granularity instead of using breakpoints
	
	- Floating-point precision errors: Small rounding differences cascade into major output errors.	
		- symptoms
			- Non-deterministic results, NaNs, or diverging numerical algorithms.	
		- solutions
			- Use high-precision math libraries, test with tolerances (assertAlmostEqual), or symbolic computation tools
	
	- Undefined behavior (UB) in C/C++): Compiler optimizations make incorrect assumptions.	
		- symptoms
			- Crashes, wrong results, or silent data corruption.	
		- solutions
			- Use UBSan (UndefinedBehaviorSanitizer), Clang sanitizers, or static analyzers like Coverity or cppcheck
	
	- Non-reproducible builds: Builds differ across environments, causing “it works on my machine” issues.	
		- symptoms
			- Failures only on certain machines or CI/CD.	
		- solutions
			- Use Docker, Bazel, Nix, or reproducible build systems. Record compiler and dependency versions
	
	- Thread starvation or priority inversion: Threads waiting for CPU or low-priority threads blocking high-priority ones.	
		- symptoms 
			- Poor performance, random stalls.	
		- solutions
			- Use thread analyzers, change scheduling policy, or limit lock contention

	- Memory Leak
		- symptoms:
			- Gradual performance degradation
			- OOM (out of memory) errors
			- Increasing memory footprint
			- swapping occurring on the disk
			- RSS steadily increasing in top, ps, or smem; valgrind --leak-check=full output: definitely lost: 128 bytes in 1 blocks
			valgrind --leak-check=full ./myapp
				==1234== 256 bytes in 1 blocks are definitely lost in loss record 1 of 1
				==1234==    at 0x4C2FB55: malloc (vg_replace_malloc.c:299)
				==1234==    by 0x4005ED: main (leak.c:5)
		- causes: 
			- Memory allocated but never freed
			- Unreleased objects/resources
			- Cyclic references
			- Poor GC tuning
			- Insufficient RAM for the workload
			- Cache mismanagement (unused cache blocks not freed)
		- tools: 
			- top, ps, valgrind, pmap
			- Memory profilers (Valgrind)
			- Runtime metrics (Prometheus/Grafana)
			- Heap dumps
		- solution: 
			- identify with Valgrind, use smart pointers or delete references.
			- Free unused objects
			- Close resources
			- Fix cyclic references
			- Tune GC / increase memory
			- Limit cache size
			- Increase server RAM or optimize virtual memory settings (vm.overcommit_memory on Linux)

		- Memory leaks across languages (e.g., C in Python extension): Memory management crosses GC and manual boundary
			- symptoms
				- Gradual RAM growth, untracked allocations
			- solutions
				- Use profilers that support native + managed layers, Valgrind, LeakSanitizer

	- Thread Leak
		- symptom: ps -L PID or top -H shows thread count increasing
			ps -L <PID> | wc -l
				3001
		- causes: Process has thousands of threads → thread creation without termination.
		- tools: top, pstree, gdb
		- solution: Threads created without join/exit; fix thread lifecycle management, join finished threads or use a thread pool.

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

	- File descriptor leaks / handle exhaustion: Process opens files/sockets without closing
		- symptoms
			- “Too many open files” errors, hangs on I/O
		- solutions
			- Use lsof, monitor /proc/<pid>/fd/, enforce limits via ulimit

	- Too Many Open Files or Child Processes
		- symptoms
			- “Too many open files” (EMFILE) error
			- Resource exhaustion
			- Slow system or failing new connections
			- Zombie processes
			- lsof | wc -l > limit
				lsof | wc -l
					10240
		- causes
			- File descriptors not closed or file descriptor limit too low
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

	- Out of Memory (OOM Killer)
		- symptoms:
			- Out of memory: Kill process 2345 (java) score 912 or sacrifice child
		- solutions: 
			- Check memory:
				free -h
				vmstat 1
			- Increase swap:
				sudo fallocate -l 4G /swapfile
				sudo chmod 600 /swapfile
				sudo mkswap /swapfile
				sudo swapon /swapfile
			- Optimize app memory usage

	- Swap overuse / memory pressure
		- symptom: vmstat shows high swap in/out; free -m shows low available memory
		- tools: vmstat, free, sar
		- solution: Add RAM, tune swappiness (/proc/sys/vm/swappiness), or fix memory leaks.

	- Zombie Process

		- symptoms
			- ps aux | grep 'Z' shows <defunct>
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
			- Restart parent process, if persistent:
				kill -HUP <parent_pid>

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

	- Deadlock (Threads) / Race Conditions

		- symptoms
			- Random inconsistent results
			- Intermittent crashes, corrupted data, missing or duplicated output
			- Hard-to-reproduce bugs
			- Inconsistent results between runs
			- thread sanitizer reports: Race on variable 'x' at address 0x7ff...
			- Incorrect counters or data corruption
			- Occasional crashes under concurrency
			- System/app freezes but no crash
			- CPU idle
			- Program hangs with no CPU activity, no errors.
			- jstack <PID>
				Found one Java-level deadlock:
					"Thread-1": waiting to lock monitor 0x00007f8c1400f000 (object 0x00000000d0a...)
					"Thread-2": waiting to lock monitor 0x00007f8c1400f100 (object 0x00000000d0b...)
		- causes
			- Shared mutable state accessed unsafely
			- Missing synchronization primitives
			- Improper use of threads/futures
			- Circular lock dependencies: two or more processes/threads each holding resources the other needs
			- Deadlocks: Multiple threads/processes wait indefinitely for each other’s locks
		- tools
			- Thread analyzers (ThreadSanitizer, Helgrind, Go race detector)
			- Logging with timestamps and thread IDs
			- Deterministic test frameworks
			- Thread dump (jstack, pstack)
			- lsof, strace for blocked syscalls
		- solutions
			- Use mutexes, locks, or atomic variables to synchronize
			- Avoid shared mutable data
			- Design for immutability or message passing
			- Use timeout-based locking or lock hierarchy
			- Reduce resource coupling
			- Avoid nested locks
			- Use consistent lock order
			- Add synchronization
			- Use lock order analysis, thread dumps (jstack), or deadlock detectors
			- Reorder lock acquisition to fix lock hierarchy, or use try-locks with timeouts
			- Use thread sanitizers, add locks, use deterministic replay (rr, gdb, valgrind), log timestamps, stress-test concurrency

		- Race conditions in hardware timing: Timing mismatch between components, especially in embedded systems or FPGAs.	
			- symptoms
				- Works at room temperature, fails under stress or cold.	
			- solutions
				- Hardware logic analyzers, temperature variation testing, formal timing verification		

	- Segmentation Fault (Segfault)

		- symptoms
			- Program crashes with “Segmentation fault (core dumped)”
			- Memory corruption
			- Inconsistent behavior depending on input
			- dmesg logs: segfault at 0x00000000 ip ... error 4 in <binary>
				gdb ./myapp core
					(gdb) bt
						#0  0x00007f2a12345678 in strcpy () from /lib/x86_64-linux-gnu/libc.so.6
						#1  0x00000000004005b1 in main () at main.c:10
		- causes
			- Dereferencing null or freed pointers
			- Buffer overflow
			- Stack corruption
			- Invalid memory access
			- Invalid memory write in strcpy()
		- tools
			- dmesg
			- gdb or lldb to inspect stack traces
			- Core dumps (ulimit -c unlimited)
			- AddressSanitizer / Valgrind Memcheck
		- solutions
			- Fix pointer handling
			- Validate array bounds
			- Use smart pointers (C++) or managed memory
			- Enable compiler warnings and sanitizers
			- Ensure destination buffer is large enough
			- Use strncpy(), null pointer dereference or invalid access
			- run under gdb, inspect backtrace.	

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

	- Memory corruption (use-after-free, buffer overflow): May not cause immediate crash; can corrupt unrelated data.	
		- symptoms
			- Random crashes, segfaults in unrelated modules.	
		- solutions
			- Use AddressSanitizer (ASan), Valgrind, or hardware watchpoints
	
	- Heap corruption
		- symptom: Valgrind output: Invalid free() / delete / delete[]
		- tools: valgrind, ASan
		- solution: Fix double free or buffer overrun.
	
	- Filesystem Corruption
		- symptoms: 
			- Boot shows “fsck failed” or dmesg logs “EXT4-fs error”
			sudo dmesg | grep -i "I/O error"
			sudo fsck /dev/sda1
		- tools: fsck, dmesg, smartctl
		- solutions: 
			- Run fsck, check disk health, restore from backup.
			- Boot into single-user or rescue mode.
				sudo fsck -f -y /dev/sda1
			- If recurring, suspect disk hardware failure (smartctl -a /dev/sda).

- Fragmentation

	- Memory fragmentation	
		- Memory becomes split into small unusable blocks (heap fragmentation) or scattered pages (virtual memory fragmentation).	
		- symptoms
			- Increases memory usage, allocation failures, or OOM errors.
			- High resident memory (RSS) despite low heap usage.
			- malloc() or new failures under high memory pressure.
			- Frequent page faults or swap usage.
			- Application memory footprint grows steadily without leaks.
		- tools
			- pmap <pid>: Shows memory map and fragmentation of virtual memory.
			- smem / ps_mem: Check proportional set size (PSS) and shared memory/swap space usage
			- /proc/<pid>/smaps: Shows per-region fragmentation and page usage.
				- If total allocated memory is large but RSS much larger → memory fragmentation.
			- malloc_info() / mallinfo(): Inspect heap usage in glibc apps.
			- Valgrind Massif: Visualizes heap usage over time (valgrind --tool=massif ./app).
			- perf / eBPF: Track memory allocation/free patterns.
		- causes/solutions
			- Frequent alloc/free of different sizes: Use memory pools, slabs, or custom allocators.
			- Long-lived small allocations: Compact or batch allocations.
			- Fragmented heap: Restart process or use jemalloc / tcmalloc.
			- Overcommit issues: Adjust /proc/sys/vm/overcommit_memory.

	- Database fragmentation	
		- Data and indexes are stored non-contiguously on disk.	
		- symptoms
			- Queries slow down over time.
			- Disk usage grows despite data deletions.
			- Index scans and I/O stats show excessive reads.
			- Query plans use more buffers or pages than expected.
			- Slower reads, larger indexes, higher I/O latency.
		- tools
			- PostgreSQL	
				- VACUUM VERBOSE: Shows dead tuples and bloat.
				- SELECT * FROM pgstattuple('table'): Shows live/dead tuples, bloat %.
				- pg_stat_all_tables: Track dead tuples.
			- MySQL / InnoDB	
				- SHOW TABLE STATUS: Compare Data_free vs Data_length.
				- OPTIMIZE TABLE tablename: Defragment table storage.
			- SQL Server	
				- sys.dm_db_index_physical_stats: Reports fragmentation percent.
				- ALTER INDEX … REORGANIZE: Defrag index without rebuild.
			- Oracle	
				- ANALYZE TABLE … COMPUTE STATISTICS: Detects fragmentation
		- solutions
			- rebuild/vacuum/optimize fragmented indexes/tables, monitor bloat

	- File system fragmentation	
		- Files are stored in many scattered disk blocks.	
		- symptoms
			- Slow I/O performance, longer file access times.
			- File reads/writes slow down over time.
			- High disk I/O latency (iostat, sar).
			- fsck shows fragmented inodes or blocks.
			- filefrag -v file shows high extent count
		- causes
			- Poor layout on disk	
		- tools
			- ext4 (e4defrag -c /path): Show fragmentation score.
			- xfs (xfs_db -c frag -r /dev/sdX): Report file system fragmentation.
			- NTFS (Windows) (defrag C: /A): Analyze disk fragmentation.
			- btrfs (filefrag -v filename): Shows number of file extents.
		- solutions
			- Defragment filesystem or migrate data; Run e4defrag /mountpoint or xfs_fsr.
			- Move large files to a separate disk.
			- Maintain 20–30% free space on disk to avoid fragmentation.
			- use modern FS like ext4/XFS/ZFS

	- Network fragmentation	
		- IP packets are split into multiple fragments due to MTU limits.	
		- symptoms
			- Packet loss, reassembly errors, latency, and sometimes crashes.
			- High latency or packet loss for large payloads.
			- “Fragmented packet” or “reassembly failed” errors in logs.
			- MTU mismatch between devices (e.g., VPN or tunnel).
			- Some services unreachable via specific routes.
		- tools
			- ping -M do -s <size> <host>: Check maximum MTU before fragmentation.
			- tracepath <host>: Shows path MTU discovery (PMTU).
			- tcpdump -vv: Inspect IP fragmentation flags (MF or frag offset).
			- wireshark: Detect fragmented and reassembled packets.
			- ethtool -i eth0: Check NIC offload settings (can affect fragmentation)
		- solutions
			- adjust MTUs to be consistent, fix routing, disable tunnel mismatch, avoid double encapsulation

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

	- Cache misconfiguration
		- symptom: Cache hit ratio in metrics < 10%; stale data served
		- tools: Application metrics, redis-cli INFO
		- solution: Adjust eviction policy, key TTLs, or backend invalidation logic.

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
	
	- Distributed state or cache incoherency: State replicated across nodes drifts out of sync.	
		- symptoms
			- Conflicting data, inconsistent reads
		- solutions
			- Use consensus protocols (Raft, Paxos), version vectors, or CRDTs. Log vector clocks and timestamps

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


- sources
	- linux commands: https://www.cyberciti.biz/tips/top-linux-monitoring-tools.html
	- perf commands: https://www.brendangregg.com/perf.html
	- performance tuning: https://www.linuxjournal.com/content/linux-system-performance-tuning-optimizing-cpu-memory-and-disk