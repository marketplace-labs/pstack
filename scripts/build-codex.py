#!/usr/bin/env python3
"""Build or check the self-contained Codex skill from this repository's sources."""

import argparse
import shutil
from pathlib import Path


def sources(root):
    for directory in ("skills", "agents", "docs/guide"):
        for source in sorted((root / directory).rglob("*")):
            if source.is_symlink():
                raise ValueError(f"Symlinks are not supported: {source}")
            if source.is_file():
                yield source.relative_to(root), source
    for filename in ("LICENSE", "UPSTREAM.md"):
        yield Path(filename), root / filename


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the bundle differs from source")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = root / "codex/pstack/references/upstream"
    expected = dict(sources(root))
    if args.check:
        actual = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
        changed = sorted(str(p) for p in actual ^ expected.keys())
        changed += [str(p) for p in actual & expected.keys()
                    if (target / p).read_bytes() != expected[p].read_bytes()]
        if changed:
            parser.exit(1, "Codex bundle is stale:\n" + "\n".join(changed) + "\n")
        print(f"Codex bundle matches {len(expected)} source files.")
        return
    if target.is_symlink():
        parser.exit(1, "Refusing to replace a symlinked bundle directory.\n")
    if target.exists():
        shutil.rmtree(target)
    for relative, source in expected.items():
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    print(f"Bundled {len(expected)} source files in {target.relative_to(root)}.")


if __name__ == "__main__":
    main()
