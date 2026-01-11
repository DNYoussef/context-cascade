# Testing Quality - Quick Reference v2.1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Test suite quality assessment and improvement.

## Quality Dimensions

| Dimension | Target |
|-----------|--------|
| Coverage | >= 80% |
| Flaky Rate | < 1% |
| Speed | < 5 min |
| Assertions | >= 2/test |

## Quick Commands

```bash
# Audit test quality
Use testing-quality audit: [test path]

# Coverage analysis
Use testing-quality coverage: [project]

# Find flaky tests
Use testing-quality flaky: [test suite]
```

## Anti-Patterns

- Flaky tests
- Test interdependence
- Over-mocking
- Missing assertions
- Slow CI tests
- Commented tests

## Coverage Targets

```yaml
line: 80%
branch: 75%
function: 80%
critical: 100%
```

## Related Skills

- **testing**
- **code-review-assistant**
- **functionality-audit**


---
*Promise: `<promise>QUICK_REFERENCE_VERIX_COMPLIANT</promise>`*
