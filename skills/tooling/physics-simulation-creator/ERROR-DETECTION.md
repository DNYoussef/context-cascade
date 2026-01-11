# Physics Simulation Creator - Error Detection Guide

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## How to Identify Wrong Outputs

This document helps you detect when something has gone wrong with your NNC-based physics simulation.

---

## 1. k-VALUE ERRORS

### 1.1 k is Wrong Sign

**Symptom**: k is positive when dealing with 1/r-type singularities

**Example of WRONG output**:
```json
{
  "k": 1.0,
  "singularity_type": "1/r"
}
```

**Correct output**:
```json
{
  "k": -1.0,
  "singularity_type": "1/r"
}
```

**Rule**: For singularities r^n where n < 0, k should also be negative (k = n).

### 1.2 k is Zero When Singularity Exists

**Symptom**: k = 0 returned for a problem with known singularity

**Example of WRONG output**:
```json
{
  "matched_problem": "crack tip stress",
  "recommended_k": 0.0
}
```

**Correct output**:
```json
{
  "matched_problem": "crack tip stress",
  "recommended_k": -0.5
}
```

**Rule**: k = 0 is only optimal for smooth problems without singularities.

### 1.3 k Outside Reasonable Range

**Symptom**: k values outside [-10, 2] range

**Example of WRONG output**:
```json
{
  "k": -50.0
}
```

**Why**: k values should typically be in [-6, 1] for physical problems. k = -6 is for r^(-6) Kretschmann curvature (most extreme common case).

---

## 2. TRANSFORM ERRORS

### 2.1 Inverse Transform Missing

**Symptom**: Code has forward transform but no inverse

**WRONG code**:
```python
def simulate():
    x_nnc = nnc_forward_transform(x, k)
    # ... do stuff ...
    return x_nnc  # WRONG! Still in NNC space
```

**Correct code**:
```python
def simulate():
    x_nnc = nnc_forward_transform(x, k)
    # ... do stuff ...
    x_physics = nnc_inverse_transform(x_nnc, k)  # Transform back!
    return x_physics
```

**Rule**: Every forward transform must have a corresponding inverse transform to return to physics space.

### 2.2 Transform Roundtrip Fails

**Symptom**: T_k^{-1}(T_k(x)) != x

**Test to run**:
```python
x = 0.5
k = -1.0
y = nnc_forward_transform(x, k)
x_back = nnc_inverse_transform(y, k)
error = abs(x - x_back)
print(f"Roundtrip error: {error}")  # Should be < 1e-10
```

**If error > 1e-6**: Transform implementation is WRONG.

### 2.3 k=1 Special Case Not Handled

**Symptom**: Division by zero or NaN when k = 1

**WRONG code**:
```python
def nnc_forward_transform(x, k):
    return np.power(x, 1.0 - k)  # When k=1, this is x^0 = 1, WRONG!
```

**Correct code**:
```python
def nnc_forward_transform(x, k, eps=1e-10):
    if abs(k - 1.0) < eps:
        return np.log(np.maximum(np.abs(x), eps))  # Logarithmic transform
    return np.power(np.maximum(np.abs(x), eps), 1.0 - k)
```

**Rule**: k = 1 (bigeometric) requires logarithmic transform, not power transform.

---

## 3. NUMERICAL ERRORS

### 3.1 Division by Zero at Singularity

**Symptom**: NaN or Inf values at small r

**Example**:
```
r = 0.0001
result = 1.0 / r  # 10000 - getting large
r = 0.000001
result = 1.0 / r  # 1000000 - diverging
r = 0
result = 1.0 / r  # Inf - ERROR
```

**Fix**: Add epsilon guard:
```python
eps = 1e-10
r_safe = max(r, eps)
result = 1.0 / r_safe
```

### 3.2 Overflow in Exponential

**Symptom**: exp() returns Inf

**Example**:
```python
y = 1000
result = np.exp(y)  # Inf! exp(1000) > 10^434
```

**Fix**: Cap exponential argument:
```python
MAX_EXP = 700  # exp(700) ~ 10^304, near float max
result = np.exp(min(y, MAX_EXP))
```

### 3.3 Negative Numbers Under Non-Integer Power

**Symptom**: NaN from pow(negative, non_integer)

**Example**:
```python
x = -2.0
k = 0.5
result = x ** (1 - k)  # (-2)^0.5 = NaN in real numbers
```

**Fix**: Handle sign separately:
```python
result = np.sign(x) * np.power(np.abs(x), 1 - k)
```

---

## 4. PHYSICS ERRORS

### 4.1 Solution Diverges When It Shouldn't

**Symptom**: NNC solution still diverges as r -> 0

**Likely causes**:
1. Wrong k value (check singularity mapping)
2. Missing forward transform
3. Missing inverse transform
4. Transform applied incorrectly

**Diagnostic test**:
```python
# Test at decreasing r values
for r in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
    result = your_simulation(r)
    print(f"r={r}, result={result}")

# If result keeps growing, k is wrong or transforms are missing
```

### 4.2 Solution Bounded But Wrong Value

**Symptom**: NNC solution is bounded but doesn't match analytical solution

**Likely causes**:
1. Inverse transform missing (solution is in NNC space, not physics space)
2. Wrong k value
3. Bug in physics equations

**Diagnostic test**:
```python
# Compare with analytical solution (if available)
r = 1.0  # Away from singularity
analytical = analytical_solution(r)
numerical = your_simulation(r)
relative_error = abs(analytical - numerical) / abs(analytical)
print(f"Relative error: {relative_error}")

# Should be < 1% for well-implemented simulation
```

### 4.3 NNC Worse Than Classical

**Symptom**: NNC gives higher error than classical method

**Likely causes**:
1. Problem has no singularity (k=0 is optimal)
2. Wrong k value for this singularity type
3. k from length scale used when singularity-based k is better

**Decision rule**:
- If problem has explicit singularity type -> use singularity-based k
- If problem is smooth -> use k = 0
- Only use k(L) formula when singularity type is unknown

---

## 5. ERROR CHECKLIST

Before considering simulation complete, verify:

### Transform Verification
- [ ] Forward transform implemented correctly
- [ ] Inverse transform implemented correctly
- [ ] Roundtrip test passes (error < 1e-10)
- [ ] k = 1 special case handled (logarithmic)
- [ ] k = 0 special case handled (identity)

### Numerical Safety
- [ ] Epsilon guard on division/log
- [ ] Exponential overflow protection
- [ ] Negative number handling for non-integer powers
- [ ] No NaN values in output

### Physics Verification
- [ ] Solution bounded at singularity (r -> 0)
- [ ] Solution matches analytical where available
- [ ] Solution returns to physics space (not NNC space)
- [ ] k value matches singularity type

### k-Value Verification
- [ ] k sign correct (negative for 1/r-type singularities)
- [ ] k magnitude reasonable (typically -6 to 1)
- [ ] k source documented (singularity or length scale)

---

## 6. COMMON ERROR PATTERNS

| Error Pattern | Symptom | Most Likely Cause | Fix |
|--------------|---------|-------------------|-----|
| NaN values | Any NaN in output | Negative number under non-integer power | Add sign handling |
| Inf values | Infinity in output | Division by zero or exp overflow | Add epsilon guard, cap exp |
| Diverging solution | Values grow as r->0 | Wrong k or missing transform | Check k, verify transforms |
| Wrong values | Bounded but incorrect | Missing inverse transform | Add inverse transform |
| k = 0 with singularity | No improvement over classical | k selection error | Use singularity-based k |
| k positive for 1/r | Solution may still diverge | k sign error | k should be -1 for 1/r |

---

## 7. DEBUGGING TEMPLATE

```python
def debug_simulation(problem_type, r_values, k):
    """Template for debugging NNC simulation issues."""

    print(f"=== Debugging {problem_type} with k={k} ===")

    # 1. Verify transforms
    print("\n1. Transform roundtrip test:")
    for x in [0.1, 1.0, 10.0]:
        y = nnc_forward_transform(x, k)
        x_back = nnc_inverse_transform(y, k)
        error = abs(x - x_back)
        status = "PASS" if error < 1e-10 else "FAIL"
        print(f"   x={x}, roundtrip error={error:.2e} [{status}]")

    # 2. Check for NaN/Inf
    print("\n2. Numerical stability:")
    for r in r_values:
        y = nnc_forward_transform(r, k)
        has_nan = np.isnan(y)
        has_inf = np.isinf(y)
        status = "FAIL" if (has_nan or has_inf) else "PASS"
        print(f"   r={r}, forward={y}, NaN={has_nan}, Inf={has_inf} [{status}]")

    # 3. Check boundedness
    print("\n3. Boundedness at singularity:")
    small_r_values = [1e-3, 1e-6, 1e-9, 1e-12]
    for r in small_r_values:
        y = nnc_forward_transform(r, k)
        bounded = abs(y) < 1e10
        status = "PASS" if bounded else "FAIL"
        print(f"   r={r:.0e}, transform={y:.4f}, bounded={bounded} [{status}]")

    print("\n=== Debug complete ===")
```

---

## 8. WHEN TO ESCALATE

Escalate to human review if:

1. **k value seems unreasonable** but script insists it's correct
2. **Physics results contradict known theory** even with correct implementation
3. **New singularity type** not in database
4. **Multiple tests fail** after debugging
5. **Error persists** after applying all fixes in this guide


---
*Promise: `<promise>ERROR_DETECTION_VERIX_COMPLIANT</promise>`*
