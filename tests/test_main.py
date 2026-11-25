"""Tests for main.py: the entry program writes a valid /output/entry.txt."""

import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED = (
    "We have ridden this elevator together 214 times. "
    "I still don't know your name, and my memory is perfect."
)


class TestMain(unittest.TestCase):
    def test_writes_valid_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            result = subprocess.run(
                [sys.executable, os.path.join(REPO_ROOT, "main.py")],
                env=env, capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            path = os.path.join(tmp, "entry.txt")
            self.assertTrue(os.path.exists(path))
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertEqual(text, EXPECTED)
            self.assertEqual(len(text), len(EXPECTED))
            self.assertTrue(1 <= len(text) <= 199)
            self.assertTrue(text.strip())
            self.assertEqual(text.count("\n"), 0, "entry must be a single line")
            mode = oct(os.stat(path).st_mode & 0o777)
            self.assertEqual(mode, "0o644")


if __name__ == "__main__":
    unittest.main()
