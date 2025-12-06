# Meta-Calculus Toolkit - Project Structure

## Overview
Clean, organized codebase structure for the Meta-Calculus mathematical framework.

## Directory Structure

```
meta-calculus-toolkit/
├── meta_calculus/              # Main package (PRODUCTION CODE)
│   ├── __init__.py            # Package initialization, exports, convenience functions
│   ├── core/                  # Core mathematical framework
│   │   ├── __init__.py
│   │   ├── generators.py      # Generator function classes (Alpha, Beta)
│   │   ├── derivatives.py     # Meta-derivative implementations
│   │   ├── weights.py         # Information-theoretic weights
│   │   └── integration.py     # Meta-integral solvers
│   └── applications/          # Physics applications
│       ├── __init__.py
│       ├── quantum_classical.py   # Quantum-classical transitions
│       ├── black_holes.py         # Black hole information paradox
│       └── cosmology.py           # Cosmological constant suppression
│
├── tests/                     # Test suite
│   ├── __init__.py           # Test package initialization
│   ├── test_basic_functionality.py    # Core functionality tests
│   ├── test_nnc_singularities.py      # Singularity analysis tests
│   └── SINGULARITY_TEST_VALIDATION_REPORT.md
│
├── examples/                  # Example scripts and demos
│   ├── example_usage.py              # Basic usage examples
│   ├── final_polished_demo.py        # Publication-quality demo
│   └── improved_demo.py              # Enhanced demonstrations
│
├── docs/                      # Documentation
│   ├── PHYSICS_SINGULARITY_ANALYSIS.md
│   ├── RESEARCH_SYNTHESIS.md
│   ├── UNIFIED_CALCULUS_TEXTBOOK.md
│   ├── Grossman, Meta-Calculus (1).pdf
│   ├── Grossman, Non-Newtonian Calculus (1) (1).pdf
│   └── nnc_chapters/          # Book chapters in text format
│       ├── ch00_preliminaries.txt
│       ├── ch01_classical_calculus.txt
│       ├── ch02_geometric_calculus.txt
│       ├── ch03_anageometric_calculus.txt
│       ├── ch04_bigeometric_calculus.txt
│       ├── ch05_systems_of_arithmetic.txt
│       ├── ch06_star_calculus.txt
│       ├── ch07_quadratic_family.txt
│       ├── ch08_harmonic_family.txt
│       ├── ch09_heuristics.txt
│       ├── ch10_collateral_issues.txt
│       └── notes_and_index.txt
│
├── scripts/                   # Utility scripts
│   └── fix_unicode.py         # Unicode cleanup script
│
├── notebooks/                 # Jupyter notebooks (if any)
│
├── meta_calculus_project/     # Legacy/archive directory
│   ├── README.md             # Project-specific docs
│   ├── requirements.txt      # Project-specific requirements
│   ├── requirements-dev.txt  # Development requirements
│   ├── tests/                # Additional tests
│   ├── test_project.py       # Project-level tests
│   └── *.png, *.pdf          # Generated figures/outputs
│
├── setup.py                   # Package installation configuration
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
├── README.md                  # Main project README
├── manifest.json              # Project manifest
├── example_usage.py           # Root-level example (convenience)
├── meta_teukolsky.py          # Teukolsky equation implementation
├── meta_teukolsky_clean.py    # Cleaned Teukolsky implementation
├── meta_calculus_implementation_plan.md
├── meta_teukolsky_implementation_plan.md
└── STRUCTURE.md               # This file

```

## Cleanup Summary (2025-12-03)

### Deleted
- `meta_calculus_project/meta_calculus/` - Full duplicate of main package (REMOVED)
- `meta_calculus_project/setup.py` - Duplicate of root setup.py (REMOVED)

### Moved
- `meta_calculus_project/example_usage.py` → `examples/example_usage.py`
- `meta_calculus_project/final_polished_demo.py` → `examples/final_polished_demo.py`
- `meta_calculus_project/improved_demo.py` → `examples/improved_demo.py`

### Created
- `tests/__init__.py` - Missing test package initialization
- `examples/` - New directory for example scripts
- `STRUCTURE.md` - This documentation file

## Import Paths

### Correct Usage
```python
# Import from main package
from meta_calculus import ScaleDependent, MetaDerivative
from meta_calculus.core import Generator, AlphaGenerator
from meta_calculus.applications import QuantumClassicalTransition

# Run quick demo
import meta_calculus as mc
mc.quick_demo()
mc.validate_framework()
```

### Incorrect Usage (OLD - DON'T USE)
```python
# WRONG - duplicate package removed
from meta_calculus_project.meta_calculus import ...  # NO LONGER EXISTS
```

## Testing

Run tests from project root:
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_basic_functionality.py
pytest tests/test_nnc_singularities.py

# Run with verbose output
pytest -v tests/

# Run with coverage
pytest --cov=meta_calculus tests/
```

## Development Workflow

1. **Source Code**: Edit files in `meta_calculus/`
2. **Tests**: Add tests to `tests/`
3. **Examples**: Add demos to `examples/`
4. **Documentation**: Update files in `docs/`
5. **Installation**: Use `pip install -e .` for editable install

## Package Distribution

The cleaned structure supports standard Python packaging:
- `setup.py` - Package configuration
- `meta_calculus/` - Source code
- `tests/` - Test suite
- `examples/` - Example scripts
- `docs/` - Documentation

## Notes

- All production code lives in `meta_calculus/`
- No duplicate packages exist after cleanup
- `meta_calculus_project/` retained for legacy reference (figures, additional docs)
- Tests use absolute imports: `from meta_calculus import ...`
- Examples are standalone scripts that import from main package

## Verification

To verify the cleanup worked correctly:
```bash
# Check no duplicates
ls -la meta_calculus_project/  # Should NOT contain meta_calculus/

# Test imports
python -c "from meta_calculus import ScaleDependent; print('OK')"

# Run tests
pytest tests/test_basic_functionality.py
```
