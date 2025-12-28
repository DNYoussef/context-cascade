---
name: reverse-engineering-deep-analysis
description: Advanced binary analysis with runtime execution and symbolic path exploration (RE Levels 3-4). Use when need runtime behavior, memory dumps, secret extraction, or input synthesis to reach specific program states. Completes in 3-7 hours with GDB+Angr.
---

## When to Use This Skill

Use this skill when analyzing malware samples, reverse engineering binaries for security research, conducting vulnerability assessments, extracting IOCs from suspicious files, validating software for supply chain security, or performing CTF challenges and binary exploitation research.

## When NOT to Use This Skill

Do NOT use for unauthorized reverse engineering of commercial software, analyzing binaries on production systems, reversing software without legal authorization, violating terms of service or EULAs, or analyzing malware outside isolated environments. Avoid for simple string extraction (use basic tools instead).

## Success Criteria

- All security-relevant behaviors identified (network, file, registry, process activity)
- Malicious indicators extracted with confidence scores (IOCs, C2 domains, encryption keys)
- Vulnerabilities documented with CVE mapping where applicable
- Analysis completed within sandbox environment (VM/container with snapshots)
- Findings validated through multiple analysis methods (static + dynamic + symbolic)
- Complete IOC report generated (STIX/MISP format for threat intelligence sharing)
- Zero false positives in vulnerability assessments
- Exploitation proof-of-concept created (if vulnerability research)

## Edge Cases & Challenges

- Anti-analysis techniques (debugger detection, VM detection, timing checks)
- Obfuscated or packed binaries requiring unpacking
- Multi-stage malware with encrypted payloads
- Kernel-mode rootkits requiring specialized analysis
- Symbolic execution state explosion (>10,000 paths)
- Binary analysis timeout on complex programs (>24 hours)
- False positives from legitimate software behavior
- Encrypted network traffic requiring SSL interception

## Guardrails (CRITICAL SECURITY RULES)

- NEVER execute unknown binaries on host systems (ONLY in isolated VM/sandbox)
- NEVER analyze malware without proper containment (air-gapped lab preferred)
- NEVER reverse engineer software without legal authorization
- NEVER share extracted credentials or encryption keys publicly
- NEVER bypass licensing mechanisms for unauthorized use
- ALWAYS use sandboxed environments with network monitoring
- ALWAYS take VM snapshots before executing suspicious binaries
- ALWAYS validate findings through multiple analysis methods
- ALWAYS document analysis methodology with timestamps
- ALWAYS assume binaries are malicious until proven safe
- ALWAYS use network isolation to prevent malware communication
- ALWAYS sanitize IOCs before sharing (redact internal IP addresses)

## Evidence-Based Validation

All reverse engineering findings MUST be validated through:
1. **Multi-method analysis** - Static + dynamic + symbolic execution confirm same behavior
2. **Sandbox validation** - Execute in isolated environment, capture all activity
3. **Network monitoring** - Packet capture validates network-based findings
4. **Memory forensics** - Validate runtime secrets through memory dumps
5. **Behavioral correlation** - Cross-reference with known malware signatures (YARA, ClamAV)
6. **Reproducibility** - Second analyst can replicate findings from analysis artifacts

# Reverse Engineering: Deep Analysis

## What This Skill Does

Performs deep reverse engineering through runtime execution and symbolic exploration:
- **Level 3 (≤1 hr)**: Dynamic analysis - Execute in sandbox with GDB, capture memory/secrets, trace syscalls
- **Level 4 (2-6 hrs)**: Symbolic execution - Use Angr/Z3 to synthesize inputs that reach target states

**Decision Gate**: After Level 3, evaluates if symbolic execution needed to reach unexplored paths.

**Timebox**: 3-7 hours total

## ⚠️ CRITICAL SECURITY WARNING

**NEVER execute unknown binaries on your host system!**

All dynamic analysis, debugging, and symbolic execution MUST be performed in:
- **Isolated VM** (VMware/VirtualBox with snapshots for rollback)
- **Docker container** with security policies (`--security-opt`, `--cap-drop=ALL`)
- **E2B sandbox** via sandbox-configurator skill with network monitoring
- **Dedicated malware analysis lab** (air-gapped if handling APTs)

**Consequences of unsafe execution:**
- Malware infection with kernel-level rootkits
- Memory corruption and system instability
- Data exfiltration via covert channels
- Supply chain attacks via trojanized builds
- Complete system compromise

**Safe Practices:**
- Always use sandboxed environments with snapshots
- Monitor syscalls and network activity during execution
- Use GDB/Angr in isolated containers only
- Never attach debuggers to binaries on production systems
- Validate all inputs before symbolic execution
- Assume all binaries are malicious until proven safe through static analysis

## Level 3: Dynamic Analysis (≤1 hour)

### Step 1: Safe Execution in Sandbox

```bash
/re:dynamic binary.exe --args "test input" --sandbox true
```

**Sandboxing**:
- Filesystem isolation (read-only /usr, /bin)
- Network disabled or monitored
- Process limits (CPU, memory, time)
- Prevents malware escape

### Step 2: Retrieve Static Analysis Context

Before executing, the skill automatically retrieves Level 2 findings:

```javascript
// Check memory-mcp for static analysis results
const staticFindings = await mcp__memory-mcp__vector_search({
  query: binary_hash,
  filter: {category: "reverse-engineering", re_level: 2}
})

// Extract critical functions and suggested breakpoints
const breakpoints = staticFindings.critical_functions.map(f => f.address)
// Example: ["0x401234", "0x401567", "0x4018ab"]
```

### Step 3: GDB Session with Auto-Loaded Breakpoints

Automatically loads breakpoints from Level 2 static analysis:

```gdb
# Auto-generated from static analysis
break *0x401234  # check_password function
break *0x401567  # validate_license function
break *0x4018ab  # decrypt_config function

# Run with test input
run --flag "test_input_from_user"
```

**GDB Session Commands** (executed automatically):

```gdb
# At each breakpoint:

# 1. Dump all registers
info registers

# 2. Dump stack (100 bytes)
x/100x $rsp

# 3. Dump heap allocations (if applicable)
info proc mappings
x/100x [heap_address]

# 4. Search for secrets in memory
find 0x600000, 0x700000, "password"
find 0x600000, 0x700000, "admin"

# 5. Dump interesting strings from registers
x/s $rdi  # First argument (often string pointer)
x/s $rsi  # Second argument
```

### Step 4: Capture Runtime State

At each breakpoint, the skill captures:

**Register State**:
```
RAX: 0x0000000000401337
RBX: 0x0000000000000000
RCX: 0x00007fffffffe010  → "user_input_here"
RDX: 0x0000000000000010
RSI: 0x00007fffffffe020  → "expected_password"
RDI: 0x00007fffffffe030  → buffer
RBP: 0x00007fffffffe100
RSP: 0x00007fffffffe0e0
RIP: 0x0000000000401234  → check_password
```

**Stack Dump** (saved to `re-project/dbg/0x401234-stack.bin`):
```
0x7fffffffe0e0: 0x0000000000401337  0x0000000000000000
0x7fffffffe0f0: 0x00007fffffffe200  0x0000000000000001
```

**Memory Secrets** (extracted automatically):
```
Found at 0x601000: "admin:SecretP@ss123"
Found at 0x601020: "license_key=ABC-DEF-GHI-JKL"
Found at 0x601040: "api_token=eyJhbGciOiJIUzI1NiIs..."
```

**Syscall Trace** (via strace):
```bash
# Automatically executed in parallel
strace -o re-project/dbg/syscalls.log ./binary.exe --flag test
```

**Output**:
```
open("/etc/config.ini", O_RDONLY) = 3
read(3, "password=admin123\n", 1024) = 18
socket(AF_INET, SOCK_STREAM, 0) = 4
connect(4, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("192.168.1.100")}, 16) = 0
send(4, "POST /api/login HTTP/1.1\r\n...", 256, 0) = 256
```

### Step 5: Output Structure

```
re-project/dbg/
├── gdb-session.log          # Full GDB transcript
├── breakpoints.txt          # List of breakpoints set
├── memory-dumps/
│   ├── 0x401234-registers.txt
│   ├── 0x401234-stack.bin
│   ├── 0x401567-registers.txt
│   ├── 0x401567-stack.bin
│   └── 0x4018ab-heap.bin
├── syscalls.log             # strace output
├── libcalls.log             # ltrace output
└── runtime-secrets.txt      # Extracted passwords, keys, tokens
```

### Step 6: Decision Gate - Escalate to Level 4?

```javascript
// Automatically evaluated via sequential-thinking MCP
const decision = await mcp__sequential-thinking__evaluate({
  question: "Should we proceed to symbolic execution (Level 4)?",
  factors: [
    `Branches explored: ${explored_branches}/${total_branches}`,
    `Unreachable code found: ${unreachable_functions.length > 0}`,
    `User's question answered: ${findings_sufficient}`,
    `Input-dependent paths: ${symbolic_paths_needed}`
  ]
})

// Example evaluation:
// - Explored 12/20 branches (60% coverage)
// - Found 3 unreachable functions (possible anti-debug)
// - User wants to reach "win" function at 0x401337 (NOT YET REACHED)
// - Input-dependent path detected (password check with strcmp)
// DECISION: ESCALATE TO LEVEL 4
```

## Advanced Options

### Custom Breakpoints (Dynamic Analysis)

```bash
# Set breakpoints at crypto functions
/re:dynamic binary.exe --breakpoints AES_encrypt,RSA_sign,MD5_update

# Set breakpoints at specific addresses
/re:dynamic binary.exe --breakpoints 0x401000,0x402000,0x403000

# Conditional breakpoints (GDB syntax)
/re:dynamic binary.exe --breakpoints "0x401234 if $rdi == 0x601000"
```

**Advanced GDB Scripting**:

```python
# Custom GDB Python script (auto-loaded if found)
# re-project/gdb-script.py

import gdb

class PasswordBreakpoint(gdb.Breakpoint):
    def __init__(self, location):
        super().__init__(location)

    def stop(self):
        # Extract password from RDI register
        rdi = gdb.parse_and_eval('$rdi')
        password = gdb.execute(f'x/s {rdi}', to_string=True)

        # Log to file
        with open('passwords.log', 'a') as f:
            f.write(f"{password}\n")

        # Continue execution
        return False

# Set custom breakpoint
PasswordBreakpoint("check_password")
```

### Symbolic Exploration Strategies

#### Strategy 1: Find ALL Solutions

```bash
# Exhaustive search (may take hours)
/re:symbolic binary.exe \
  --target-addr 0x401337 \
  --find-all true \
  --max-solutions 10 \
  --timeout 14400
```

```python
# In Angr script
simgr.explore(
    find=0x401337,
    avoid=avoid_addrs,
    num_find=10  # Find up to 10 solutions
)

# Process all found solutions
for idx, state in enumerate(simgr.found):
    solution = state.solver.eval(flag, cast_to=bytes)
    with open(f'solution-{idx+1}.txt', 'wb') as f:
        f.write(solution)
```

#### Strategy 2: Limit State Explosion

```bash
# Aggressive pruning
/re:symbolic binary.exe \
  --max-states 100 \
  --avoid-addrs 0x401400,0x401500,0x401600 \
  --strategy dfs  # Depth-first search (memory efficient)
```

```python
# Use Veritesting to merge paths
simgr.use_technique(angr.exploration_techniques.Veritesting())

# Drop states if too many active
simgr.use_technique(angr.exploration_techniques.LengthLimiter(max_length=100))

# Prioritize states closer to target
simgr.use_technique(angr.exploration_techniques.Explorer(
    find=0x401337,
    avoid=avoid_addrs,
    num_find=1
))
```

#### Strategy 3: Under-Constrained Symbolic Execution

```python
# Start from target address and work backwards
project = angr.Project('./binary.exe')

# Create state at target address (not entry point)
state = project.factory.blank_state(addr=0x401337)

# Make all memory symbolic
state.options.add(angr.options.SYMBION_SYNC_CLE)

# Explore backwards to find required input
simgr = project.factory.simulation_manager(state)
simgr.explore(find=project.entry)

# This finds inputs that MUST lead to target
```

### Memory Dump Analysis

```bash
# Dump specific memory regions
/re:dynamic binary.exe \
  --dump-regions heap,stack,data \
  --dump-at-breakpoints 0x401234,0x401567
```

**Custom Memory Analysis**:

```python
# GDB Python script for heap analysis
import gdb

def analyze_heap():
    # Get heap boundaries
    mappings = gdb.execute('info proc mappings', to_string=True)
    heap_start = extract_heap_start(mappings)
    heap_end = extract_heap_end(mappings)

    # Scan for interesting patterns
    for addr in range(heap_start, heap_end, 8):
        value = gdb.execute(f'x/g {addr}', to_string=True)

        # Check if value looks like a pointer
        if is_valid_pointer(value):
            gdb.execute(f'x/s {value}')  # Dereference as string

analyze_heap()
```

### Workflow 2: CTF Challenge - Reversing License Check

**Scenario**: Find valid license key to unlock "premium features" in binary

**Phase 1: Dynamic Analysis (Level 3)**

```bash
# Step 1: Test with invalid key
/re:dynamic challenge.exe --args "--license AAAA-BBBB-CCCC-DDDD"

# Output: "Invalid license key"

# Step 2: GDB reveals license check at 0x401234
(gdb) break *0x401234
(gdb) run --license AAAA-BBBB-CCCC-DDDD

# Step 3: Examine comparison
(gdb) x/s $rdi
0x7fffffffe010: "AAAA-BBBB-CCCC-DDDD"  # User input

(gdb) x/s $rsi
0x601000: [encrypted data, not readable]

# Observation: License key is compared against encrypted/hashed value
# Cannot extract valid key directly from memory
```

**Phase 2: Decision Gate**

```javascript
QUESTION: "Proceed to symbolic execution?"
FACTORS:
- License check function found ✅
- Valid key NOT extractable from memory ✅
- Comparison is complex (encryption/hashing) ✅
- User wants valid license key ✅
DECISION: ESCALATE TO LEVEL 4 (symbolic execution required)
```

**Phase 3: Symbolic Execution (Level 4)**

```bash
# Launch Angr symbolic execution
/re:symbolic challenge.exe \
  --target-addr 0x401337 \  # "Premium features unlocked" message
  --avoid-addrs 0x401400 \  # "Invalid license" path
  --input-format "FLAG-XXXX-XXXX-XXXX" \
  --max-states 500
```

**Angr Script** (auto-generated):

```python
import angr
import claripy

project = angr.Project('./challenge.exe', auto_load_libs=False)

# License key format: FLAG-XXXX-XXXX-XXXX (19 chars)
license_key = claripy.BVS('license', 19 * 8)

# Create entry state with symbolic license as argv[2]
state = project.factory.entry_state(args=['./challenge.exe', '--license', license_key])

# Constrain to valid format: FLAG-XXXX-XXXX-XXXX
for i in range(19):
    if i in [0, 1, 2, 3]:  # "FLAG"
        state.add_constraints(license_key.get_byte(i) == ord("FLAG"[i]))
    elif i in [4, 9, 14]:  # Dashes
        state.add_constraints(license_key.get_byte(i) == ord('-'))
    else:  # X = uppercase letters or digits
        byte = license_key.get_byte(i)
        state.add_constraints(
            claripy.Or(
                claripy.And(byte >= ord('A'), byte <= ord('Z')),
                claripy.And(byte >= ord('0'), byte <= ord('9'))
            )
        )

# Explore
simgr = project.factory.simulation_manager(state)
simgr.explore(find=0x401337, avoid=0x401400)

if simgr.found:
    solution = simgr.found[0].solver.eval(license_key, cast_to=bytes)
    print(f"Valid License: {solution.decode()}")
    # Output: "FLAG-A7B2-C9D4-E1F6"
```

**Validation**:

```bash
$ ./challenge.exe --license FLAG-A7B2-C9D4-E1F6
Premium features unlocked!
Congratulations! Here is your flag: CTF{symbolic_execution_wins}
```

**Output**: Challenge solved in 3.5 hours total (45min dynamic + 3hr symbolic).

## Troubleshooting

### Issue 1: Sandbox Blocks Execution

**Symptoms**: Binary fails to run with "Permission denied" or syscall blocked errors

**Cause**: Sandbox too restrictive, blocking necessary syscalls

**Solution 1**: Whitelist necessary syscalls

```bash
# Check which syscalls are blocked
strace ./binary.exe 2>&1 | grep "Operation not permitted"

# Create custom seccomp profile
cat > sandbox-profile.json <<EOF
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "syscalls": [
    {"names": ["read", "write", "open", "close"], "action": "SCMP_ACT_ALLOW"},
    {"names": ["socket", "connect"], "action": "SCMP_ACT_ALLOW"}
  ]
}
EOF

# Use custom profile
/re:dynamic binary.exe --sandbox-profile sandbox-profile.json
```

**Solution 2**: Use less restrictive sandbox

```bash
# Disable network isolation only (allow file access)
/re:dynamic server.bin --sandbox true --allow-network true

# Or use Docker instead of seccomp
docker run --rm -v $(pwd):/work -it ubuntu:20.04 /work/binary.exe
```

### Issue 3: Angr State Explosion

**Symptoms**: Symbolic execution runs out of memory or times out with thousands of active states

**Cause**: Binary has too many branches, creating exponential state explosion

**Solution 1**: Add more avoid states

```bash
# Find all "failure" functions from static analysis
/re:static binary.exe --list-functions | grep -i "fail\|error\|exit"

# Add all failure addresses to avoid list
/re:symbolic binary.exe \
  --target-addr 0x401337 \
  --avoid-addrs 0x401400,0x401500,0x401600,0x401700,0x401800 \
  --max-states 100
```

**Solution 2**: Use Veritesting (merge states automatically)

```python
# In custom Angr script
simgr.use_technique(angr.exploration_techniques.Veritesting())

# This merges similar states, reducing explosion by 10-100x
```

**Solution 3**: Start from intermediate address (skip unimportant code)

```python
# Skip initialization code, start at license check function
state = project.factory.blank_state(addr=0x401234)

# Set up expected register/memory state (from Level 3 analysis)
state.regs.rdi = state.solver.BVS('input', 32*8)

# Explore from this point only
simgr = project.factory.simulation_manager(state)
simgr.explore(find=0x401337)
```

### Issue 5: Symbolic Execution Timeout

**Symptoms**: Angr runs for hours without finding solution

**Cause**: Constraint solver (Z3) stuck on complex constraints

**Solution 1**: Increase timeout and simplify constraints

```bash
/re:symbolic binary.exe \
  --timeout 14400 \  # 4 hours
  --max-states 200 \
  --simplify-constraints true
```

**Solution 2**: Use incremental solving

```python
# Add constraints incrementally instead of all at once
state.solver.add(constraint1)
if state.satisfiable():
    state.solver.add(constraint2)
    if state.satisfiable():
        state.solver.add(constraint3)
```

**Solution 3**: Use faster solver (CVC4 or Boolector)

```python
import angr
import claripy

# Use faster solver backend
claripy.backends.backend_manager.backends._eager_backends = [
    claripy.backends.BackendConcrete,
    claripy.backends.BackendZ3  # Replace with BackendCVC4
]
```

### Speed Up Symbolic Execution (Level 4)

#### Optimization 1: Use Faster Exploration Strategy

```python
# DFS is memory-efficient but may explore wrong paths
simgr.use_technique(angr.exploration_techniques.DFS())

# BFS finds shortest path but uses more memory
simgr.use_technique(angr.exploration_techniques.BFS())

# Hybrid: BFS until 100 states, then switch to DFS
simgr.use_technique(angr.exploration_techniques.Explorer(
    find=0x401337,
    num_find=1
))
```

#### Optimization 2: Pre-Constrain Input Space

```python
# If you know input must start with "FLAG"
for i, char in enumerate("FLAG"):
    state.add_constraints(flag.get_byte(i) == ord(char))

# This reduces search space from 256^32 to 256^28
```

#### Optimization 3: Hook Complex Functions

```python
# Replace slow library functions with fast symbolic summaries
project.hook_symbol('strlen', angr.SIM_PROCEDURES['libc']['strlen']())
project.hook_symbol('strcmp', angr.SIM_PROCEDURES['libc']['strcmp']())
project.hook_symbol('memcpy', angr.SIM_PROCEDURES['libc']['memcpy']())

# These are much faster than symbolically executing the actual implementations
```

#### Optimization 4: Parallelize Exploration

```python
# Split state space across multiple cores
from multiprocessing import Pool

def explore_from_state(state):
    simgr = project.factory.simulation_manager(state)
    simgr.explore(find=0x401337, avoid=avoid_addrs)
    return simgr.found

# Split initial state into 4 copies with different constraints
states = [state.copy() for _ in range(4)]
states[0].add_constraints(flag[0] < 0x40)
states[1].add_constraints(claripy.And(flag[0] >= 0x40, flag[0] < 0x60))
states[2].add_constraints(claripy.And(flag[0] >= 0x60, flag[0] < 0x80))
states[3].add_constraints(flag[0] >= 0x80)

# Explore in parallel
with Pool(4) as p:
    results = p.map(explore_from_state, states)

# Collect solutions
for found_states in results:
    if found_states:
        print(found_states[0].solver.eval(flag, cast_to=bytes))
```

## Agents & Commands

### Agents Invoked

1. **RE-Runtime-Tracer** (Level 3)
   - Specialist: Dynamic analysis with GDB/strace/ltrace
   - Tools: GDB+GEF/Pwndbg, strace, ltrace, sandbox environments
   - Output: Memory dumps, syscall traces, runtime secrets

2. **RE-Symbolic-Solver** (Level 4)
   - Specialist: Symbolic execution with Angr/Z3
   - Tools: Angr, Z3, Python symbolic execution frameworks
   - Output: Synthesized inputs, constraint files, validated solutions

3. **sandbox-validator** (Level 3, automatic)
   - Provides safe binary execution environment
   - Prevents malware escape and system damage

4. **graph-analyst** (Level 4, automatic)
   - Generates execution path visualizations
   - Creates constraint dependency graphs

### Slash Commands

- `/re:deep <binary>` - Full Level 3+4 analysis (this skill's primary command)
- `/re:dynamic <binary>` - Level 3 only (dynamic analysis)
- `/re:symbolic <binary>` - Level 4 only (symbolic execution)

### MCP Servers

- **sandbox-validator**: Safe binary execution with isolation
- **memory-mcp**: Cross-session persistence, handoff coordination
- **sequential-thinking**: Decision gate logic for escalation
- **graph-analyst**: Visualization of execution paths and constraints

## Resources

### External Tools

- [GDB](https://www.gnu.org/software/gdb/) - GNU Debugger
- [GEF](https://github.com/hugsy/gef) - GDB Enhanced Features
- [Pwndbg](https://github.com/pwndbg/pwndbg) - GDB plugin for exploit development
- [Angr](https://angr.io/) - Binary analysis platform
- [Z3](https://github.com/Z3Prover/z3) - Microsoft SMT solver

### Learning Resources

- [Angr Documentation](https://docs.angr.io/) - Complete Angr guide
- [Z3 Tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm) - Z3 Python bindings
- [GDB to LLDB Command Map](https://lldb.llvm.org/use/map.html) - For macOS users
- [Practical Binary Analysis](https://nostarch.com/binaryanalysis) - Book

### Community

- [Angr Slack](https://angr.io/community/) - Official Angr community
- [r/ReverseEngineering](https://reddit.com/r/ReverseEngineering) - Subreddit
- [Binary Ninja Discord](https://binary.ninja/discord/) - Reverse engineering community

## Core Principles

Reverse Engineering: Deep Analysis operates on 3 fundamental principles:

### Principle 1: Isolation-First Execution
Runtime analysis MUST occur in isolated environments to prevent malware escape and system compromise.

In practice:
- Execute all binaries in snapshots VMs/containers with network monitoring
- Use sandboxed debuggers (GDB in Docker, QEMU with snapshot mode)
- Monitor syscalls, network traffic, and file operations during execution
- Maintain air-gapped lab infrastructure for APT analysis

### Principle 2: Multi-Method Validation
No single analysis technique provides complete truth - cross-validation prevents false positives.

In practice:
- Static analysis findings must be confirmed by dynamic execution
- Dynamic behavior must be reproducible across multiple runs
- Symbolic execution results must validate against real execution paths
- Memory dumps must correlate with network captures and syscall traces

### Principle 3: Progressive Escalation
Start with lightweight methods, escalate only when necessary to minimize analysis time.

In practice:
- Level 3 (dynamic) reveals 80% of malware behavior in under 1 hour
- Escalate to Level 4 (symbolic) only when paths are unreachable manually
- Use decision gates to avoid over-engineering simple analysis tasks
- Cache findings in memory-mcp to prevent duplicate work

-----------|---------|----------|
| **Executing malware on host system** | Complete system compromise, data exfiltration, ransomware deployment | ALWAYS use isolated VM with snapshots, network monitoring, and rollback capability |
| **Skipping static analysis before dynamic** | Waste time executing without understanding, miss packed binaries | Run Level 1-2 (strings + static) first to identify entry points and breakpoints |
| **Over-relying on symbolic execution** | State explosion, analysis timeout, resource exhaustion | Use symbolic execution only for input-dependent paths unreachable by manual fuzzing |
| **Ignoring anti-analysis techniques** | Debugger detection terminates analysis, VM detection changes behavior | Patch anti-debug checks, use stealthy debugging environments, monitor timing attacks |
| **Not documenting methodology** | Results not reproducible, findings challenged, legal issues | Timestamp all actions, save GDB transcripts, document tool versions and commands used |

---

## Conclusion

Reverse Engineering: Deep Analysis represents the critical bridge between static code inspection and complete program comprehension. By combining runtime execution (Level 3) with symbolic path exploration (Level 4), this skill enables security researchers to extract secrets, validate vulnerabilities, and synthesize inputs that reach specific program states - capabilities essential for malware analysis, CTF challenges, and vulnerability research.

The skill's power lies in its automated decision gates and progressive escalation strategy. Rather than immediately jumping to resource-intensive symbolic execution, the skill starts with lightweight dynamic analysis using GDB and system call tracing. Only when manual execution fails to reach target states does it escalate to Angr-based symbolic execution, minimizing analysis time while maximizing findings.

Use this skill when you need to understand runtime behavior that static analysis cannot reveal: memory secrets, network communication patterns, or valid inputs for complex authentication schemes. The skill excels at extracting indicators of compromise from malware, finding valid license keys in crackmes, and generating proof-of-concept exploits for vulnerabilities. Combined with memory-mcp integration for cross-session persistence and handoff coordination with firmware analysis (Level 5), it forms a comprehensive reverse engineering workflow suitable for both academic research and production security operations.