---
name: compliance
description: Regulatory compliance validation and documentation for GDPR, HIPAA, SOC 2, PCI-DSS, and ISO 27001. Use when implementing compliance controls, conducting compliance audits, or preparing for certification. Provides automated compliance checks and evidence collection.
---

## When to Use This Skill

Use this skill when conducting compliance audits, implementing regulatory controls, preparing for certification audits, validating GDPR/HIPAA/SOC2/PCI-DSS/ISO27001 adherence, or documenting security and privacy practices for regulated industries.

## When NOT to Use This Skill

Do NOT use for non-regulated applications, internal tools without compliance requirements, proof-of-concept projects, or general security audits (use security-analyzer instead). Avoid using for unauthorized compliance testing of third-party systems.

## Success Criteria

- All applicable regulatory requirements identified with evidence mapping
- Compliance gaps documented with severity ratings (critical/high/medium/low)
- Controls implemented with validation tests (automated where possible)
- Evidence collection automated with audit trail timestamps
- Remediation plans created for all gaps with assigned owners
- Compliance score >90% for target framework
- Zero critical violations remaining before certification

## Edge Cases & Challenges

- Multi-jurisdiction compliance (GDPR + CCPA + local regulations)
- Legacy systems without compliance documentation
- Third-party services requiring BAA/DPA agreements
- Encrypted data requiring key escrow for compliance
- Real-time compliance monitoring vs periodic audits
- Conflicting requirements between frameworks
- Continuous compliance vs point-in-time certification

## Guardrails (CRITICAL SECURITY RULES)

- NEVER implement compliance controls on unauthorized systems
- NEVER collect or store PII/PHI without proper encryption and access controls
- NEVER bypass security controls to achieve compliance scores
- NEVER generate false compliance evidence or documentation
- ALWAYS document evidence collection methods with timestamps
- ALWAYS validate controls through independent testing
- ALWAYS obtain legal review for compliance interpretations
- ALWAYS maintain audit trails for all compliance activities
- ALWAYS use encryption at rest and in transit for sensitive data
- ALWAYS implement least-privilege access for compliance tools

## Evidence-Based Validation

All compliance findings MUST be validated through:
1. **Automated scanning** - Use compliance scanning tools with documented results
2. **Manual verification** - Independent review of at least 20% of automated findings
3. **Evidence collection** - Screenshots, logs, configurations with timestamps
4. **Cross-validation** - Multiple methods confirm same finding (tool + manual + audit)
5. **Expert review** - Compliance specialist validates critical findings
6. **Remediation testing** - Verify fixes resolve violations without introducing new gaps

# Compliance - Regulatory Standards Validation

Comprehensive compliance validation and documentation for major regulatory frameworks.

## When to Use This Skill

Use when implementing compliance controls for regulated industries, preparing for compliance audits or certifications, documenting security and privacy practices, or validating adherence to regulatory standards.

## Supported Compliance Frameworks

### GDPR (General Data Protection Regulation)
- Data privacy and protection
- Right to erasure and portability
- Consent management
- Data breach notification
- Privacy by design

### HIPAA (Health Insurance Portability and Accountability Act)
- Protected Health Information (PHI) safeguards
- Administrative, physical, technical safeguards
- Business Associate Agreements (BAA)
- Audit controls and logging
- Breach notification

### SOC 2 (Service Organization Control 2)
- Trust Services Criteria (Security, Availability, Confidentiality)
- Control documentation
- Evidence collection
- Continuous monitoring
- Independent auditor reports

### PCI-DSS (Payment Card Industry Data Security Standard)
- Cardholder data protection
- Network security controls
- Access control mechanisms
- Regular security testing
- Security policy maintenance

### ISO 27001 (Information Security Management)
- Information Security Management System (ISMS)
- Risk assessment and treatment
- 114 security controls across 14 domains
- Continuous improvement process
- Certification preparation

## Process

1. **Identify compliance requirements**
   - Determine applicable regulations
   - Map business processes to controls
   - Identify data flows and storage
   - Assess current compliance gaps

2. **Implement controls**
   - Technical controls (encryption, access management)
   - Administrative controls (policies, procedures)
   - Physical controls (facility security)
   - Documentation and evidence

3. **Validate compliance**
   - Automated compliance scanning
   - Manual control testing
   - Evidence collection and review
   - Gap analysis and remediation

4. **Maintain compliance**
   - Continuous monitoring
   - Regular audits and assessments
   - Update controls for regulatory changes
   - Train personnel

5. **Prepare for audits**
   - Organize compliance documentation
   - Conduct pre-audit assessments
   - Engage external auditors
   - Implement findings

## Automated Compliance Checks

- **Access Control**: IAM policies, least privilege
- **Encryption**: Data at rest and in transit
- **Logging**: Audit trails and monitoring
- **Network Security**: Firewalls, segmentation
- **Incident Response**: Breach notification procedures
## Core Principles

Compliance operates on 3 fundamental principles:

### Principle 1: Evidence-Based Validation
Every compliance claim must be backed by verifiable evidence collected through automated scanning, manual verification, and independent testing. This prevents false compliance and ensures audit readiness.

In practice:
- Automated compliance tools generate timestamped evidence logs
- Manual verification of 20% of automated findings catches tool blind spots
- Cross-validation using multiple methods confirms critical controls

### Principle 2: Continuous Compliance Monitoring
Compliance is an ongoing state maintained through continuous monitoring rather than a point-in-time certification. This detects drift and enables rapid remediation.

In practice:
- Real-time alerting on compliance violations (access control changes, encryption disabled)
- Automated evidence collection runs daily with audit trail retention
- Regular control testing identifies degradation before audits

### Principle 3: Risk-Prioritized Remediation
Compliance gaps are triaged by severity (critical/high/medium/low) with mandatory remediation timelines for critical violations before certification or production deployment.

In practice:
- Critical gaps (PII exposure, missing encryption) block deployment
- High-severity gaps require remediation plans with assigned owners
- Compliance score >90% required for certification readiness

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Checkbox Compliance** | Implementing controls to pass audits without ensuring actual security creates false sense of compliance | Validate controls through independent testing, collect evidence of effectiveness not just existence |
| **Point-in-Time Certification** | Achieving compliance for audit then allowing drift creates compliance gaps and violation risks | Implement continuous monitoring with automated alerting on control changes |
| **Manual Evidence Collection** | Gathering evidence manually is error-prone, time-consuming, and difficult to maintain consistently | Automate evidence collection with timestamped logs, use compliance-as-code tools |

## Conclusion

Compliance provides comprehensive regulatory validation and documentation for major frameworks (GDPR, HIPAA, SOC 2, PCI-DSS, ISO 27001) through evidence-based controls, continuous monitoring, and automated compliance checks. By treating compliance as an engineering discipline with measurable outcomes and automated validation, this skill transforms regulatory adherence from a periodic burden to a continuous process.

Use this skill when implementing controls for regulated industries, preparing for certification audits, or maintaining ongoing compliance for production systems. The framework supports multi-jurisdiction compliance (GDPR + CCPA), automated evidence collection with audit trails, and risk-prioritized remediation plans. Critical guardrails prevent false compliance claims, unauthorized system access, and security control bypasses. The result is verifiable compliance readiness with 90%+ framework coverage and zero critical violations.