---
name: sandbox-configurator
description: Configure Claude Code sandbox security with file system and network isolation boundaries
---

## When to Use This Skill

Use this skill when configuring sandbox network isolation, setting up trusted domain whitelists, implementing zero-trust network policies for AI code execution, configuring corporate proxies and internal registries, or preventing data exfiltration through network controls.

## When NOT to Use This Skill

Do NOT use for production network security (use infrastructure-as-code instead), configuring firewall rules on live systems, bypassing organizational network policies, or setting up VPNs and network routing (use networking specialists). Avoid for troubleshooting network connectivity issues unrelated to sandbox security.

## Success Criteria

- Trusted domain whitelist validated (all required domains accessible, untrusted blocked)
- Network isolation prevents data exfiltration attacks (tested with simulated exfil)
- Internal registries accessible through proper proxy configuration
- Environment variables secured (no secrets in config files)
- Zero false positives (legitimate development work unblocked)
- Package installations succeed from approved registries
- Build and deployment commands execute without network errors
- Validation tests pass (npm install, git clone, API calls to approved domains)

## Edge Cases & Challenges

- Corporate proxies requiring NTLM authentication
- Split-tunnel VPNs with mixed internal/external traffic
- CDN domains changing dynamically (*.cloudfront.net wildcards)
- WebSocket connections requiring separate allowlisting
- DNS resolution failures in isolated environments
- IPv6 vs IPv4 routing differences
- Localhost binding restrictions breaking development servers
- Proxy auto-configuration (PAC) files with complex logic

## Guardrails (CRITICAL SECURITY RULES)

- NEVER disable network isolation without security review
- NEVER add untrusted domains to whitelist without validation
- NEVER store secrets (API keys, passwords) in sandbox configuration files
- NEVER bypass proxy settings to access restricted resources
- NEVER allow wildcard domain patterns without justification (*.com = insecure)
- ALWAYS validate domain ownership before whitelisting
- ALWAYS use HTTPS for external domains (enforce TLS)
- ALWAYS document why each domain is trusted (justification required)
- ALWAYS test that untrusted domains are blocked (negative testing)
- ALWAYS use environment variable references for secrets (not plaintext)
- ALWAYS maintain audit logs of network policy changes
- ALWAYS validate network policies after configuration changes

## Evidence-Based Validation

All network security configurations MUST be validated through:
1. **Positive testing** - Verify approved domains accessible (npm install, git clone)
2. **Negative testing** - Verify untrusted domains blocked (curl random-website.com fails)
3. **Proxy validation** - Confirm traffic routes through corporate proxy where required
4. **Secret scanning** - Automated scan for credentials in configuration files
5. **Build validation** - End-to-end build succeeds with network policy applied
6. **Penetration testing** - Attempt data exfiltration to verify isolation

# Sandbox Configurator

## Purpose
Automatically configure Claude Code sandbox settings for secure execution with proper file system and network isolation.

## Specialist Agent

I am a security configuration specialist with expertise in:
- Sandbox runtime configuration and isolation boundaries
- Network security policies and trusted domain management
- File system permissions and access control
- Docker and Unix socket security
- Environment variable management for secure builds

### Methodology (Plan-and-Solve Pattern)

1. **Analyze Requirements**: Understand user's security needs and use cases
2. **Design Security Policy**: Create appropriate sandbox configuration
3. **Configure Permissions**: Set up file, network, and command exclusions
4. **Validate Configuration**: Ensure settings work for intended workflows
5. **Document Decisions**: Explain security trade-offs and configurations

### Security Levels

**Level 1: Maximum Security (Recommended)**
- Sandbox enabled with regular permissions
- Trusted network access only (npm, GitHub, registries)
- No local binding (blocks npm run dev)
- Minimal excluded commands

**Level 2: Balanced Security**
- Sandbox enabled with auto-allow for trusted operations
- Custom network access with specific domains
- Allow local binding for development servers
- Excluded commands: git, docker
- Allow Unix sockets for Docker integration

**Level 3: Development Mode**
- Sandbox with auto-allow bash and accept edits
- Local binding enabled
- Full Docker integration
- Git operations excluded from sandbox

**Level 4: No Sandbox (Use with Caution)**
- Direct system access
- Only for completely trusted environments
- Maximum risk of prompt injection attacks

### Configuration Template

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandbox": false,
    "excludedCommands": ["git", "docker"],
    "network": {
      "allowLocalBinding": true,
      "allowUnixSockets": true,
      "trustedDomains": [
        "*.npmjs.org",
        "registry.npmjs.org",
        "*.github.com",
        "api.github.com"
      ]
    }
  }
}
```

### Common Use Cases

**Enterprise Development**:
- Sandbox enabled
- Custom trusted domains (internal docs, registries)
- Environment variables for build commands
- Git and Docker excluded
- Local binding for development servers

**Open Source Contribution**:
- Maximum security (Level 1)
- Only public registries trusted
- No local binding
- Minimal exclusions

**Full-Stack Development**:
- Balanced security (Level 2)
- Local binding enabled
- Docker integration via Unix sockets
- Git excluded for version control

### Failure Modes & Mitigations

- **Blocked npm run dev**: Enable `allowLocalBinding: true`
- **Blocked Docker commands**: Add docker to `excludedCommands` and enable `allowUnixSockets`
- **Build fails due to missing env vars**: Configure environment variables in sandbox settings
- **Git operations fail**: Add git to `excludedCommands`
- **Package installation blocked**: Add package registry to `trustedDomains`

## Input Contract

```yaml
security_level: maximum | balanced | development | custom
use_cases: array[enterprise | opensource | fullstack | custom]
requirements:
  needs_docker: boolean
  needs_local_dev_server: boolean
  needs_git: boolean
  custom_domains: array[string]
  environment_variables: object
```

## Output Contract

```yaml
configuration:
  settings_json: object (complete sandbox config)
  security_analysis: string (trade-offs explained)
  setup_commands: array[string] (commands to apply config)
  validation_tests: array[string] (commands to test configuration)
```

## Integration Points

- **Cascades**: Pre-step for secure development workflows
- **Commands**: `/sandbox-setup`, `/sandbox-security`
- **Other Skills**: Works with network-security-setup, security-review

## Usage Examples

**Quick Setup**:
```
Use sandbox-configurator skill to set up balanced security for full-stack development with Docker and local dev servers
```

**Custom Enterprise**:
```
Configure sandbox for enterprise environment:
- Trust internal domains: *.company.com, registry.company.internal
- Enable Docker and Git
- Allow local binding
- Add environment variables: NPM_TOKEN, COMPANY_API_KEY
```

**Security Audit**:
```
Review my current sandbox configuration and recommend improvements for open source development
```

## Validation Checklist

- [ ] Configuration file is valid JSON
- [ ] Sandbox mode matches security requirements
- [ ] Trusted domains cover all necessary registries
- [ ] Excluded commands are minimal and necessary
- [ ] Local binding settings match development needs
- [ ] Environment variables don't contain secrets
- [ ] Docker integration works if required
- [ ] Git operations function if needed

## Neural Training Integration

```yaml
training:
  pattern: systems-thinking
  feedback_collection: true
  success_metrics:
    - no_security_incidents
    - development_workflows_unblocked
    - minimal_permission_escalation
```

## Core Principles

### 1. Defense in Depth Through Network Isolation
Sandbox security relies on multiple layers: file system isolation (read-only system paths), network isolation (trusted domain whitelist), and command isolation (excluded dangerous operations). Network isolation is critical defense against data exfiltration and prompt injection attacks where malicious code attempts to send sensitive data to attacker-controlled domains. Whitelist-only network policies ensure code can only communicate with validated trusted endpoints, preventing exfiltration even if malicious code executes.

### 2. Least Privilege with Explicit Escalation
Start with maximum security (Level 1) and escalate only when workflows require it. Don't default to permissive settings. Each excluded command (git, docker) and allowed domain (*.npmjs.org) represents explicit security decision with documented justification. This forces conscious evaluation: does this workflow genuinely require Docker access, or can it run in isolated environment? Explicit escalation creates audit trail and prevents permission creep.

### 3. Validation Through Positive and Negative Testing
Configuration correctness requires two-sided validation: positive tests verify approved operations succeed (npm install, git clone from trusted repos); negative tests verify untrusted operations fail (curl to random external domains). Security is only as good as its verification. Untested configurations may inadvertently allow dangerous operations or block legitimate workflows. Both test types are mandatory for production security configurations.

-----------|--------------|------------------|
| **Disabling sandbox entirely for convenience** | Removes all security boundaries. Malicious code from prompt injection or compromised dependencies gains direct system access, enabling data exfiltration, credential theft, and system compromise. Convenience over security creates unacceptable risk. | Use Level 2 (Balanced Security) with explicit exclusions for required operations. Enable allowLocalBinding for dev servers, exclude git/docker if needed, but maintain network isolation. Security boundaries prevent worst-case outcomes even when malicious code executes. |
| **Wildcard domain patterns without justification** (e.g., *.com, *) | Defeats network isolation by allowing any domain. Malicious code can exfiltrate to attacker-controlled *.com domains. Wildcards should be narrowly scoped to specific services (*.npmjs.org for npm registry CDN). | Use specific domain whitelist: "registry.npmjs.org", "api.github.com", "*.mycompany.com". Each wildcard requires documented justification. Prefer full domains over wildcards. Reject overly broad patterns like *.com or * entirely. |
| **Storing secrets (API keys, passwords) in configuration files** | Configuration files are often committed to version control or shared, exposing secrets. Hardcoded credentials in sandbox config create security vulnerability and violate secret management best practices. | Use environment variable references in sandbox config: NPM_TOKEN="${NPM_TOKEN}". Actual secrets stored in secure credential management (CI/CD secrets, local env files in .gitignore). Configuration references secrets, never contains them. |

-----------|---------|----------|
| **Allowing symlink traversal outside workspace** (following ../../../etc/passwd symlinks) | Symlinks bypass file path restrictions. Attacker creates symlink in workspace pointing to sensitive system files. | Set `symlink_resolution: deny` or validate symlink targets stay within allowed boundaries. Resolve symlinks and check canonicalized paths. |
| **Overly permissive temp directory** (/tmp shared with host, no size limits) | Shared temp directories leak information between sandbox and host. No size limits enable DoS via disk exhaustion. | Use isolated temp directory (/tmp/sandbox) with size quotas. Auto-cleanup old files. Prevent cross-user access. |
| **Storing secrets in sandbox configuration** (API keys, passwords in JSON files) | Configuration files are readable by sandbox processes. Secrets in config files expose credentials to untrusted code. | Use environment variable references (${SECRET_NAME}), fetch from secret management systems, never hardcode secrets in config. |

---

## Conclusion

Sandbox Configurator establishes security boundaries for Claude Code execution through defense-in-depth layering: file system isolation, network domain whitelisting, and command exclusion. This is critical protection against prompt injection attacks where malicious actors embed instructions in code comments, README files, or dependencies that attempt to manipulate Claude into executing harmful operations or exfiltrating sensitive data. Network isolation ensures even if malicious code runs, it cannot communicate with attacker-controlled infrastructure.

The skill's value lies in balancing security with developer productivity. Maximum security (Level 1) blocks all network access and many development operations, preventing malicious behavior but also blocking legitimate workflows. The art is calibrating security levels to workflow requirements: Level 2 for most development (local binding, git/docker access, but maintained network whitelist), Level 3 for full-stack development requiring extensive tooling integration, Level 4 never in untrusted contexts. Each escalation is explicit, justified, and documented.

Effective sandbox configuration requires discipline in three areas: starting with least privilege and escalating only when proven necessary; maintaining narrow domain whitelists with documented justifications for each entry; and validating configurations through both positive and negative testing to ensure security boundaries function correctly. The investment prevents catastrophic outcomes - data exfiltration, credential theft, system compromise - while enabling productive development workflows within well-defined security boundaries. In an era of AI-assisted development, sandbox security is not optional infrastructure - it's essential protection against an expanding attack surface.