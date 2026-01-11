#!/usr/bin/env python3
"""
Unit tests for bug-detector.py fixes.

Tests verify that the 5 critical issues identified in the forensic analysis
have been properly fixed:

1. String Matching Fallacy (JS detector)
2. Scope Blindness (Python race condition)
3. Append Hallucination (Python memory leak)
4. XSS Regex Bypass (JS XSS detection)
5. Exception Swallowing (scan completeness)
"""

import ast
import unittest
import sys
from pathlib import Path

# Import the detector module (handle hyphenated filename)
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util
spec = importlib.util.spec_from_file_location(
    "bug_detector",
    Path(__file__).parent / "bug-detector.py"
)
bug_detector_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bug_detector_module)

PythonBugDetector = bug_detector_module.PythonBugDetector
JavaScriptBugDetector = bug_detector_module.JavaScriptBugDetector
BugDetectorEngine = bug_detector_module.BugDetectorEngine
ScanResult = bug_detector_module.ScanResult


class TestIssue1_StringMatchingFallacy(unittest.TestCase):
    """Test that JS detector uses proper keyword detection, not substring matching."""

    def test_should_not_skip_certificate_variable(self):
        """Lines with 'certificate' should NOT be skipped (contains 'if' substring)."""
        code = """
const certificate = await getCert();
const result = certificate.data.value;
"""
        detections = JavaScriptBugDetector.detect_null_undefined_issues(code, "test.js")
        # Should detect potential null reference on certificate.data.value
        # Previously would skip because 'certificate' contains 'if'
        self.assertTrue(
            any("certificate" in d.code_snippet or "result" in d.code_snippet for d in detections),
            "Should detect property access on 'certificate' variable"
        )

    def test_should_not_skip_manifest_variable(self):
        """Lines with 'manifest' should NOT be skipped (contains 'if' substring)."""
        code = "const config = manifest.settings.theme;"
        detections = JavaScriptBugDetector.detect_null_undefined_issues(code, "test.js")
        self.assertTrue(len(detections) > 0, "Should detect property access on 'manifest'")

    def test_should_skip_actual_if_statement(self):
        """Lines with actual 'if' keyword should be skipped."""
        code = "if (user && user.profile) { console.log(user.profile.name); }"
        detections = JavaScriptBugDetector.detect_null_undefined_issues(code, "test.js")
        self.assertEqual(len(detections), 0, "Should skip lines with proper null checks")

    def test_should_not_flag_safe_objects(self):
        """Should not flag console.log, Math.*, JSON.*, etc."""
        code = """
console.log("debug");
const x = Math.round(3.14);
"""
        detections = JavaScriptBugDetector.detect_null_undefined_issues(code, "test.js")
        self.assertEqual(len(detections), 0, "Should not flag built-in safe objects")


class TestIssue2_ScopeBlindness(unittest.TestCase):
    """Test that race condition detector properly tracks variable scope."""

    def test_should_flag_module_level_shared_var(self):
        """Should flag module-level variables modified in threaded code."""
        code = """
import threading

counter = 0

def worker():
    global counter
    counter += 1

t = threading.Thread(target=worker)
"""
        tree = ast.parse(code)
        detections = PythonBugDetector.detect_race_conditions(tree, "test.py", code)
        self.assertTrue(
            any("counter" in d.message for d in detections),
            "Should detect race condition on module-level 'counter'"
        )

    def test_should_not_flag_local_variables(self):
        """Should NOT flag local function variables (they're not shared)."""
        code = """
import threading

def process_a():
    count = 0
    for i in range(10):
        count += 1
    return count

def process_b():
    count = 0
    for i in range(10):
        count += 1
    return count
"""
        tree = ast.parse(code)
        detections = PythonBugDetector.detect_race_conditions(tree, "test.py", code)
        # Local 'count' in each function is NOT shared, should not flag
        self.assertEqual(len(detections), 0, "Should not flag local variables as shared")


class TestIssue3_AppendHallucination(unittest.TestCase):
    """Test that memory leak detector uses context-aware heuristics."""

    def test_should_not_flag_local_list_append(self):
        """Should NOT flag standard pattern of building result lists."""
        code = """
def process_items(items):
    results = []
    for item in items:
        results.append(process(item))
    return results
"""
        tree = ast.parse(code)
        detections = PythonBugDetector.detect_memory_leaks(tree, "test.py", code)
        self.assertEqual(len(detections), 0, "Should not flag local list appends")

    def test_should_flag_unbounded_loop_append(self):
        """Should flag appends in 'while True' without cleanup."""
        # Module-level list with while True - should flag
        code = """
data = []

while True:
    data.append(get_next())
"""
        tree = ast.parse(code)
        detections = PythonBugDetector.detect_memory_leaks(tree, "test.py", code)
        # Either unbounded or module-level detection is acceptable
        self.assertTrue(
            len(detections) > 0,
            "Should flag unbounded loop without cleanup"
        )

    def test_should_not_flag_list_with_cleanup(self):
        """Should NOT flag if list has visible cleanup."""
        code = """
data = []

def process():
    for item in items:
        data.append(item)
    data.clear()
"""
        tree = ast.parse(code)
        detections = PythonBugDetector.detect_memory_leaks(tree, "test.py", code)
        self.assertEqual(len(detections), 0, "Should not flag list with .clear()")


class TestIssue4_XSSRegexBypass(unittest.TestCase):
    """Test that XSS detection catches bracket notation bypasses."""

    def test_should_detect_bracket_notation_innerhtml(self):
        """Should detect innerHTML assignment via bracket notation."""
        code = "el['innerHTML'] = userInput;"
        detections = JavaScriptBugDetector.detect_xss_vulnerabilities(code, "test.js")
        self.assertTrue(
            any("bracket notation" in d.message.lower() for d in detections),
            "Should detect bracket notation innerHTML bypass"
        )

    def test_should_detect_document_write(self):
        """Should detect document.write with dynamic content."""
        code = "document.write(userContent);"
        detections = JavaScriptBugDetector.detect_xss_vulnerabilities(code, "test.js")
        self.assertTrue(len(detections) > 0, "Should detect document.write")

    def test_should_not_flag_sanitized_content(self):
        """Should not flag if DOMPurify.sanitize is used."""
        code = "el.innerHTML = DOMPurify.sanitize(userInput);"
        detections = JavaScriptBugDetector.detect_xss_vulnerabilities(code, "test.js")
        self.assertEqual(len(detections), 0, "Should not flag sanitized content")

    def test_should_not_flag_string_literal(self):
        """Should not flag pure string literals."""
        code = 'el.innerHTML = "<div>Hello</div>";'
        detections = JavaScriptBugDetector.detect_xss_vulnerabilities(code, "test.js")
        self.assertEqual(len(detections), 0, "Should not flag string literal")


class TestIssue5_ExceptionSwallowing(unittest.TestCase):
    """Test that scan results include completeness status."""

    def test_scan_result_has_completeness_status(self):
        """ScanResult should have scan_complete field."""
        detector = BugDetectorEngine(['python'])
        # Create a simple valid Python file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("x = 1\n")
            temp_path = f.name

        try:
            result = detector.scan_file(Path(temp_path))
            self.assertIsInstance(result, ScanResult)
            self.assertTrue(hasattr(result, 'scan_complete'))
            self.assertTrue(result.scan_complete, "Valid file should have scan_complete=True")
        finally:
            Path(temp_path).unlink()

    def test_scan_stats_tracked(self):
        """Detector should track scan statistics."""
        detector = BugDetectorEngine(['python'])
        self.assertIn('files_scanned', detector.scan_stats)
        self.assertIn('files_failed', detector.scan_stats)
        self.assertIn('errors', detector.scan_stats)


if __name__ == '__main__':
    # Run tests with verbosity
    unittest.main(verbosity=2)
