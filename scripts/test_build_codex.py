"""Exercise package generation and drift detection in a disposable repository."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CodexBundleTest(unittest.TestCase):
    def test_build_detects_edits_missing_files_and_extra_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "scripts/build-codex.py"
            script.parent.mkdir()
            shutil.copy2(Path(__file__).with_name("build-codex.py"), script)
            files = {
                "skills/no-comments/SKILL.md": "Keep useful rationale.\n",
                "agents/comment-sicko.md": "Keep uncertain comments.\n",
                "docs/guide/example.md": "Local guide.\n",
                "LICENSE": "Original licence notice.\n",
                "UPSTREAM.md": "Original attribution.\n",
            }
            for relative, content in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)

            def run(*args):
                return subprocess.run([sys.executable, str(script), *args],
                                      capture_output=True, text=True)

            self.assertEqual(run().returncode, 0)
            bundle = root / "codex/pstack/references/upstream"
            for relative, content in files.items():
                self.assertEqual((bundle / relative).read_text(), content)
            self.assertEqual(run("--check").returncode, 0)
            (root / "agents/comment-sicko.md").write_text("Updated policy.\n")
            self.assertNotEqual(run("--check").returncode, 0)
            self.assertEqual(run().returncode, 0)
            (bundle / "LICENSE").unlink()
            self.assertNotEqual(run("--check").returncode, 0)
            self.assertEqual(run().returncode, 0)
            (bundle / "unexpected.md").write_text("Stale content.\n")
            self.assertNotEqual(run("--check").returncode, 0)
            self.assertEqual(run().returncode, 0)
            self.assertFalse((bundle / "unexpected.md").exists())


if __name__ == "__main__":
    unittest.main()
