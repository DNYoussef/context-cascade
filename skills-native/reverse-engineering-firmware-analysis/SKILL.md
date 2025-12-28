---
name: reverse-engineering-firmware-analysis
description: Firmware extraction and IoT security analysis (RE Level 5) for routers and embedded systems. Use when analyzing IoT firmware, extracting embedded filesystems (SquashFS/JFFS2/CramFS), finding hardcoded credentials, performing CVE scans, or auditing embedded system security. Handles encrypted firmware with known decryption schemes. Completes in 2-8 hours with binwalk+firmadyne+QEMU emulation.
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

# Reverse Engineering: Firmware Analysis

## What This Skill Does

Extracts and analyzes firmware from IoT devices, routers, and embedded systems:
- **Extraction (30min-2hrs)**: Use binwalk to extract SquashFS/JFFS2/CramFS filesystems
- **Service Analysis (1-3hrs)**: Map init scripts, daemons, network listeners
- **Vulnerability Assessment (1-3hrs)**: Find hardcoded credentials, CVEs, injection points
- **Binary Analysis (1-2hrs)**: Apply Levels 1-4 to extracted binaries

**Timebox**: 2-8 hours total

## ⚠️ CRITICAL SECURITY WARNING

**NEVER execute firmware binaries or extracted files on your host system!**

All firmware extraction, binary execution, and emulation MUST be performed in:
- **Isolated VM** (VMware/VirtualBox with network isolation and snapshots)
- **Docker container** with strict security policies and no host filesystem access
- **E2B sandbox** via sandbox-configurator skill with monitored execution
- **Firmware analysis environment** (QEMU with `-snapshot`, firmadyne sandbox)

**Consequences of unsafe execution:**
- Backdoor installation and persistent network access
- Extraction of hardcoded credentials compromising related devices
- Malware propagation to development infrastructure
- IoT botnet recruitment (Mirai, Hajime variants)
- Compromise of cloud API keys and services

**Safe Practices:**
- Extract firmware in isolated containers with no network access
- Use QEMU emulation with snapshot mode (`-snapshot` flag)
- Never connect emulated devices to production networks
- Validate extracted credentials in isolated environments only
- Monitor all network connections during firmware emulation
- Treat all IoT firmware as potentially compromised
- Use read-only mounts for extracted filesystems

## Phase 1: Firmware Identification (5-10 minutes)

### Step 1: Basic File Analysis

```bash
# Identify file type
file firmware.bin

# Expected output examples:
# - "firmware.bin: u-boot legacy uImage, MIPS OpenWrt Linux-4.14.63"
# - "firmware.bin: data" (encrypted or compressed)
# - "firmware.bin: Flattened device tree blob (DTB)"
```

### Step 2: Entropy Analysis

Check if firmware is encrypted or compressed:

```bash
# Entropy analysis
binwalk --entropy firmware.bin

# Output visualization:
# High entropy throughout (> 0.9): Likely encrypted
# Low entropy with peaks: Normal firmware with compressed sections
# Uniform low entropy (< 0.5): Uncompressed firmware
```

**Interpretation**:
- **Entropy 0.9-1.0**: Encrypted firmware (need decryption key)
- **Entropy 0.6-0.8**: Compressed sections (normal)
- **Entropy 0.3-0.5**: Uncompressed data

### Step 3: Component Identification

```bash
# Identify firmware components
binwalk --signature firmware.bin

# Expected output:
# DECIMAL       HEXADECIMAL     DESCRIPTION
# --------------------------------------------------------------------------------
# 0             0x0             uImage header, header size: 64 bytes
# 64            0x40            LZMA compressed data
# 1048576       0x100000        Squashfs filesystem, little endian
# 15728640      0xF00000        JFFS2 filesystem, little endian
```

**Components**:
- **Bootloader**: u-boot, Das U-Boot
- **Kernel**: Linux kernel (compressed with LZMA/gzip)
- **Root Filesystem**: SquashFS, JFFS2, CramFS, UBIFS
- **Configuration**: JFFS2 partition for persistent data

## Phase 3: Service Discovery (1-3 hours)

### Step 1: Identify Init System

```bash
# Check for init scripts
ls ./squashfs-root/etc/init.d/

# Common init systems:
# - init.d/ scripts (SysVinit)
# - rc.d/ scripts (BSD-style init)
# - systemd/ units (systemd)
# - procd/ configs (OpenWrt procd)
```

### Step 2: Analyze Startup Services

```bash
# OpenWrt/procd example
cat ./squashfs-root/etc/rc.d/*

# SysVinit example
cat ./squashfs-root/etc/init.d/rcS

# Example output:
# #!/bin/sh
# /usr/sbin/telnetd -l /bin/sh
# /usr/sbin/httpd -p 80 -h /www
# /usr/sbin/dropbear -p 22
```

**Key Services to Map**:
- **telnetd**: Telnet server (port 23)
- **httpd**: Web server (port 80/443)
- **dropbear/sshd**: SSH server (port 22)
- **ftpd**: FTP server (port 21)
- **upnpd**: UPnP daemon
- **dnsmasq**: DNS/DHCP server

### Step 3: Find Network Listeners

```bash
# Search for network binding code
grep -r "0.0.0.0" ./squashfs-root/etc/
grep -r "bind(" ./squashfs-root/usr/sbin/ 2>/dev/null
grep -r "listen(" ./squashfs-root/usr/sbin/ 2>/dev/null

# Search for port numbers
grep -rE ":[0-9]{2,5}" ./squashfs-root/etc/ | grep -E "(80|443|23|22|21)"

# Example findings:
# ./squashfs-root/etc/config/uhttpd:  option listen_http '0.0.0.0:80'
# ./squashfs-root/etc/config/dropbear: option Port '22'
# ./squashfs-root/etc/inetd.conf:telnet stream tcp nowait root /usr/sbin/telnetd
```

### Step 4: Map CGI Scripts and Web Interface

```bash
# Find web root
ls ./squashfs-root/www/
ls ./squashfs-root/usr/www/

# Find CGI scripts (potential injection points)
find ./squashfs-root/www/ -name "*.cgi" -o -name "*.sh"

# Example CGI scripts:
# ./squashfs-root/www/cgi-bin/login.cgi
# ./squashfs-root/www/cgi-bin/admin.cgi
# ./squashfs-root/www/cgi-bin/status.sh

# Analyze for command injection
grep -E "(system|popen|exec)" ./squashfs-root/www/cgi-bin/*.cgi
```

**Output Summary**:
```
Network Services Detected:
- telnetd on 0.0.0.0:23 (CRITICAL: Unauthenticated shell access)
- httpd on 0.0.0.0:80 (Web interface)
- dropbear on 0.0.0.0:22 (SSH with password auth)
- upnpd on 0.0.0.0:1900 (UPnP potential SSRF)

CGI Scripts Found:
- /cgi-bin/admin.cgi (Command injection vulnerable)
- /cgi-bin/login.cgi (Credential check)
- /cgi-bin/upgrade.cgi (Firmware upload)
```

## Phase 5: Vulnerability Scanning (1-3 hours)

### Step 1: Identify Library Versions

```bash
# Find shared libraries
ls ./squashfs-root/lib/
ls ./squashfs-root/usr/lib/

# Check library versions
strings ./squashfs-root/lib/libc.so.0 | grep -i version

# Example output:
# OpenSSL 1.0.1e (VULNERABLE: Heartbleed CVE-2014-0160)
# BusyBox v1.24.1 (CHECK: Known CVEs)
# Dropbear 2014.63 (CHECK: Known CVEs)
```

### Step 2: CVE Scanning with MCP

```bash
# Use security-manager MCP for automated CVE scanning
/re:firmware router.bin --cve-scan true
```

**Under the Hood**:

```javascript
// Automatically invoked by skill
const cveResults = await mcp__security-manager__scan_vulnerabilities({
  filesystem_root: "./squashfs-root/",
  library_scan: true,
  cve_database: "nvd",  // National Vulnerability Database
  check_versions: true
})

// Example output:
// {
//   "vulnerabilities": [
//     {
//       "cve": "CVE-2014-0160",
//       "severity": "CRITICAL",
//       "component": "OpenSSL 1.0.1e",
//       "description": "Heartbleed vulnerability allows memory disclosure",
//       "cvss": 7.5
//     },
//     {
//       "cve": "CVE-2019-12345",
//       "severity": "HIGH",
//       "component": "httpd CGI handler",
//       "description": "Command injection via admin.cgi parameter",
//       "cvss": 8.8
//     }
//   ]
// }
```

### Step 3: Manual Vulnerability Assessment

#### Check for Command Injection:

```bash
# Analyze CGI scripts for command injection
grep -E "(system|exec|popen|shell_exec)" ./squashfs-root/www/cgi-bin/*.cgi

# Example vulnerable code in admin.cgi:
# system("ping -c 1 " . $QUERY_STRING);  # CRITICAL: Command injection!
```

#### Check for SQL Injection:

```bash
# Find database queries
grep -rE "(SELECT|INSERT|UPDATE|DELETE)" ./squashfs-root/www/

# Example vulnerable query:
# $query = "SELECT * FROM users WHERE username='" . $_GET['user'] . "'";
```

#### Check for Path Traversal:

```bash
# Find file operations
grep -rE "(fopen|readfile|include)" ./squashfs-root/www/

# Example vulnerable code:
# readfile("/www/" . $_GET['file']);  # Path traversal: ?file=../etc/shadow
```

### Step 4: Check for Backdoors

```bash
# Search for suspicious listening ports
grep -rE "port.*[0-9]{4,5}" ./squashfs-root/etc/

# Search for reverse shell code
grep -rE "(nc.*-e|bash.*>&|/dev/tcp)" ./squashfs-root/

# Search for hidden services
find ./squashfs-root/ -name ".*" -type f

# Check for suspicious cron jobs
cat ./squashfs-root/etc/crontabs/*
```

**Vulnerability Report**:
```
CRITICAL Vulnerabilities:
1. CVE-2014-0160 (Heartbleed) - OpenSSL 1.0.1e
2. Command Injection - admin.cgi (unauthenticated)
3. Hardcoded credentials - root:5up

HIGH Vulnerabilities:
4. Path Traversal - download.cgi
5. Weak SSL certificate - 512-bit RSA key
6. Telnet enabled on 0.0.0.0:23 (no authentication)

MEDIUM Vulnerabilities:
7. Default credentials - admin:admin
8. UPnP enabled (SSRF potential)
9. SQL Injection - login.cgi
```

## Comprehensive Workflow Examples

### Workflow 1: Router Firmware Complete Analysis

**Scenario**: Analyze TP-Link router firmware for vulnerabilities

**Step 1: Extraction (30 min)**

```bash
# Download firmware
wget http://vendor.com/TL-WR841N-v14-firmware.bin

# Identify and extract
binwalk -E TL-WR841N-v14-firmware.bin  # Check entropy
binwalk -Me TL-WR841N-v14-firmware.bin # Extract

# Navigate to filesystem
cd _TL-WR841N-v14-firmware.bin.extracted/squashfs-root/
```

**Step 2: Service Discovery (1 hr)**

```bash
# Find init scripts
cat etc/rc.d/S*

# Services found:
# - telnetd on 0.0.0.0:23 (CRITICAL)
# - httpd on 0.0.0.0:80
# - dnsmasq on 0.0.0.0:53

# Map CGI scripts
find www/ -name "*.cgi"

# CGI scripts found:
# - www/cgi-bin/admin.cgi (admin interface)
# - www/cgi-bin/upgrade.cgi (firmware upload)
```

**Step 3: Credential Hunting (15 min)**

```bash
# Check shadow file
cat etc/shadow
# Output: admin:5up:0:0:admin:/root:/bin/sh

# Check config files
grep -ri "password" etc/config/
# Output: option admin_password 'admin'

# CRITICAL: Default credentials admin:5up
```

**Step 4: CVE Scanning (30 min)**

```bash
# Check library versions
strings lib/libc.so.0 | grep version
# OpenSSL 1.0.1e (CVE-2014-0160 Heartbleed)

# Automated CVE scan
/re:firmware TL-WR841N-v14-firmware.bin --cve-scan true

# Results:
# - CVE-2014-0160 (CRITICAL): Heartbleed
# - CVE-2019-12345 (HIGH): Command injection in admin.cgi
```

**Step 5: Binary Analysis (1 hr)**

```bash
# Analyze admin CGI
/re:strings www/cgi-bin/admin.cgi
# Found: "system(sh -c %s)" - command injection

# Static analysis
/re:static www/cgi-bin/admin.cgi --tool ghidra

# Decompiled code shows:
# char *cmd = getenv("QUERY_STRING");
# system(cmd);  # CRITICAL: No sanitization!
```

**Final Report**:

```
TP-Link TL-WR841N Firmware Analysis
====================================

CRITICAL Vulnerabilities:
1. Hardcoded credentials: admin:5up
2. Unauthenticated telnet on port 23
3. Command injection in admin.cgi
4. Heartbleed (CVE-2014-0160) in OpenSSL 1.0.1e

HIGH Vulnerabilities:
5. Weak default WiFi password
6. No CSRF protection on admin interface

Attack Scenario:
1. Telnet to router (no password required)
2. Or exploit command injection: http://router/cgi-bin/admin.cgi?cmd=reboot
3. Gain root shell access

Recommendation: Update to patched firmware version
```

**Time**: 3.25 hours total

### Workflow 3: Smart Thermostat Firmware - Finding Debug Interface

**Scenario**: Analyze Nest-like thermostat for hidden debug interfaces

**Step 1: Extraction (1 hr)**

```bash
# Encrypted firmware (high entropy)
binwalk --entropy thermostat-firmware.bin
# Entropy: 0.95 (encrypted)

# Search for decryption keys in vendor SDK
find ./vendor-sdk/ -name "*.key" -o -name "*aes*"

# Found: encryption_key.bin
# Decrypt firmware
openssl enc -d -aes-256-cbc -in thermostat-firmware.bin \
  -out decrypted.bin -K $(cat encryption_key.bin)

# Extract decrypted firmware
binwalk --extract --matryoshka decrypted.bin
```

**Step 2: Find Debug Interfaces (30 min)**

```bash
# Search for UART/serial references
grep -ri "uart\|serial\|console" ./squashfs-root/etc/

# Found:
# ./etc/inittab: ttyS0::respawn:/bin/sh  # UART console!

# Search for debug commands
grep -ri "debug\|test\|diag" ./squashfs-root/usr/bin/

# Found debug binary
ls ./squashfs-root/usr/bin/debug-shell
```

**Step 3: Analyze Debug Shell (1 hr)**

```bash
# String analysis of debug shell
/re:strings ./squashfs-root/usr/bin/debug-shell

# Found:
# - "Enter admin password:" (authentication required)
# - "Debug mode enabled"
# - "dump_nvram" (NVRAM dumping command)
# - "factory_reset"

# Static analysis
/re:static ./squashfs-root/usr/bin/debug-shell --tool ghidra

# Decompiled password check:
bool check_debug_password(char *input) {
  char *correct_password = "DebugMode2023";  // Hardcoded!
  return strcmp(input, correct_password) == 0;
}
```

**Step 4: Test Debug Interface (30 min)**

```bash
# Emulate debug shell
qemu-arm-static ./squashfs-root/usr/bin/debug-shell

# Connect to UART console
screen /dev/ttyUSB0 115200

# Enter debug password: DebugMode2023
# Access granted!

# Available debug commands:
# - dump_nvram (dumps all settings including WiFi password)
# - factory_reset (wipes device)
# - enable_telnet (enables telnet on port 23)
```

**Final Report**:

```
Smart Thermostat Debug Interface Analysis
==========================================

CRITICAL Findings:
1. UART console enabled with debug shell access
2. Hardcoded debug password: "DebugMode2023"
3. Debug commands allow full device control
4. NVRAM dump reveals WiFi credentials

Attack Scenario:
1. Open device and connect to UART pins
2. Boot device and access serial console
3. Launch debug-shell
4. Enter password "DebugMode2023"
5. Execute dump_nvram to extract WiFi password
6. Execute enable_telnet for remote access

Impact: Physical access to device = full compromise

Recommendation:
- Disable debug interfaces in production firmware
- Use unique per-device debug passwords
- Implement secure boot to prevent firmware modifications
```

**Time**: 3 hours total

## Troubleshooting

### Issue 1: Encrypted Firmware

**Symptoms**: High entropy (>0.9), binwalk finds no filesystems

**Cause**: Firmware is encrypted

**Solution 1**: Find decryption key

```bash
# Search vendor SDK for keys
find ./vendor-sdk/ -name "*.key" -o -name "*aes*" -o -name "*decrypt*"

# Common key locations:
# - vendor-sdk/tools/encryption_key.bin
# - vendor-docs/firmware-encryption.txt
# - GPL source code archives
```

**Solution 2**: Check for known encryption schemes

```bash
# TP-Link uses custom encryption
tplink-safeloader -d firmware.bin -o decrypted.bin

# D-Link uses AES-256-CBC with known IV
openssl enc -d -aes-256-cbc -in firmware.bin -out decrypted.bin \
  -K <known_key> -iv <known_iv>
```

**Solution 3**: Reverse engineer bootloader

```bash
# Extract bootloader (usually at offset 0)
dd if=firmware.bin bs=1 count=65536 of=bootloader.bin

# Analyze bootloader for decryption routine
/re:static bootloader.bin --tool ghidra

# Look for AES/DES crypto initialization
```

### Issue 3: Binaries Won't Execute (Architecture Mismatch)

**Symptoms**: "Exec format error" when running extracted binaries

**Cause**: Binary compiled for different architecture (MIPS, ARM, etc.)

**Solution 1**: Identify architecture and use correct QEMU

```bash
# Identify architecture
file ./squashfs-root/usr/sbin/httpd

# Example outputs:
# - "ELF 32-bit LSB executable, MIPS" → Use qemu-mipsel-static
# - "ELF 32-bit LSB executable, ARM" → Use qemu-arm-static
# - "ELF 64-bit LSB executable, ARM aarch64" → Use qemu-aarch64-static

# Run with appropriate QEMU
qemu-mipsel-static ./squashfs-root/usr/sbin/httpd

# Or with chroot
sudo chroot ./squashfs-root qemu-mipsel-static /usr/sbin/httpd
```

**Solution 2**: Full system emulation with QEMU

```bash
# Create QEMU disk image
qemu-img create -f qcow2 firmware.qcow2 1G

# Boot with QEMU
qemu-system-mips -M malta -kernel vmlinux -hda firmware.qcow2 \
  -append "root=/dev/sda1 console=ttyS0" -nographic

# Or use firmadyne (automated)
firmadyne.sh firmware.bin
```

**Solution 3**: Use Docker with QEMU user emulation

```bash
# Docker with multi-arch support
docker run --rm -it --platform linux/arm/v7 \
  -v $(pwd)/squashfs-root:/firmware \
  arm32v7/ubuntu:20.04 bash

# Inside container
cd /firmware
./usr/sbin/httpd
```

### Issue 5: Cannot Find Hardcoded Credentials

**Symptoms**: grep searches return no passwords despite expecting them

**Cause**: Credentials encoded/encrypted or stored in binary format

**Solution 1**: Search for encoded strings

```bash
# Base64 encoded credentials
find ./squashfs-root/ -type f -exec grep -l "YWRtaW46YWRtaW4=" {} \;
# (base64 decode: admin:admin)

# Hex encoded
grep -rE "61646d696e" ./squashfs-root/etc/
# (hex decode: admin)

# URL encoded
grep -rE "%61%64%6d%69%6e" ./squashfs-root/
```

**Solution 2**: Search in binaries and databases

```bash
# SQLite databases
find ./squashfs-root/ -name "*.db" -o -name "*.sqlite"
sqlite3 ./etc/config.db "SELECT * FROM users;"

# Binary config files
strings ./squashfs-root/etc/config.bin | grep -i "password\|admin"
```

**Solution 3**: Reverse engineer authentication binary

```bash
# Analyze login binary
/re:static ./squashfs-root/usr/bin/login --tool ghidra

# Decompiled code often reveals credential check:
# if (strcmp(input, "hardcoded_password") == 0) { ... }
```

## Memory-MCP Integration

### Storing Firmware Analysis

```javascript
// After firmware extraction completes
mcp__memory-mcp__memory_store({
  content: {
    firmware_hash: "sha256:abc123...",
    device_info: {
      vendor: "TP-Link",
      model: "TL-WR841N",
      version: "v14",
      arch: "MIPS"
    },
    filesystem: {
      type: "squashfs",
      extracted_files: 1247,
      total_size_mb: 8.5
    },
    services: [
      {name: "telnetd", port: 23, auth: false, severity: "CRITICAL"},
      {name: "httpd", port: 80, auth: true, severity: "MEDIUM"},
      {name: "dropbear", port: 22, auth: true, severity: "LOW"}
    ],
    credentials: [
      {type: "root", user: "root", pass: "5up", location: "/etc/shadow"},
      {type: "admin", user: "admin", pass: "admin", location: "/etc/config/system"}
    ],
    vulnerabilities: [
      {cve: "CVE-2014-0160", severity: "CRITICAL", component: "OpenSSL 1.0.1e"},
      {cve: "CVE-2019-12345", severity: "HIGH", component: "httpd command injection"}
    ],
    attack_surface: [
      "Unauthenticated telnet on 0.0.0.0:23",
      "Command injection in /cgi-bin/admin.cgi",
      "Path traversal in /cgi-bin/download.cgi"
    ],
    binary_analysis: {
      analyzed: ["/usr/sbin/httpd", "/www/cgi-bin/admin.cgi"],
      findings: "Command injection confirmed in admin.cgi"
    }
  },
  metadata: {
    agent: "RE-Firmware-Analyst",
    category: "reverse-engineering",
    intent: "firmware-analysis",
    layer: "long_term",
    project: `firmware-analysis-${date}`,
    keywords: ["firmware", "iot", "router", "embedded"],
    re_level: 5,
    firmware_hash: "sha256:abc123...",
    timestamp: new Date().toISOString()
  }
})
```

## Related Skills

- [Reverse Engineering: Quick Triage](../reverse-engineering-quick/) - Levels 1-2 (apply to extracted binaries)
- [Reverse Engineering: Deep Analysis](../reverse-engineering-deep/) - Levels 3-4 (apply to extracted binaries)
- [Code Review Assistant](../code-review-assistant/) - Review extracted source code
- [Security Manager](../security-manager/) - Comprehensive vulnerability scanning

**Created**: 2025-11-01
**RE Level**: 5 (Firmware Analysis)
**Timebox**: 2-8 hours
**Category**: IoT Security, Embedded Systems, Firmware Reverse Engineering
**Difficulty**: Advanced
## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Executing firmware binaries on host** | Architecture mismatch (MIPS/ARM), potential backdoors, system compromise | Use QEMU user-mode emulation or full system emulation with firmadyne |
| **Ignoring encrypted firmware** | Incomplete analysis, missed vulnerabilities, false sense of security | Search vendor SDKs for decryption keys, reverse bootloader crypto routines, check known device decryption schemes |
| **Skipping service discovery** | Miss network-exposed attack surfaces (unauthenticated telnet, vulnerable CGI) | Analyze init scripts, grep for bind/listen calls, map network listeners to binaries |
| **Not validating extraction** | Corrupted filesystems, missing files, incomplete analysis | Verify critical directories exist (/bin, /etc, /lib, /www), check file counts match expectations |
| **Sharing raw credentials publicly** | Legal liability, compromise of related devices, customer privacy violation | Redact internal IPs, sanitize credentials before publishing IOCs, use secure disclosure channels |

---

## Conclusion

Reverse Engineering: Firmware Analysis is the gateway to understanding the security posture of billions of IoT and embedded devices deployed worldwide. By systematically extracting filesystems, mapping network services, hunting for hardcoded credentials, and scanning for CVEs, this skill reveals the critical vulnerabilities that make IoT devices prime targets for botnet recruitment and supply chain attacks.

The skill's value extends beyond individual device analysis - findings apply to entire product lines sharing the same firmware base. A single extracted default password or command injection vulnerability can compromise thousands of devices. Combined with Level 1-4 binary analysis of extracted executables, this skill enables comprehensive security assessments from bootloader to application layer.

Use this skill when analyzing router firmware before deployment, auditing smart home devices for privacy concerns, or conducting vulnerability research on embedded systems. The 2-8 hour timebox makes it suitable for both targeted security audits and large-scale IoT security research programs. Integration with memory-mcp enables cross-firmware correlation to identify common vulnerabilities across vendors, accelerating IoT security research at scale.