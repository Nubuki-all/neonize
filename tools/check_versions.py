"""Fail if the neonize and goneonize versions disagree.

The goneonize version (goneonize/version.go and __GONEONIZE_VERSION__ in
neonize/download.py) is the release tag the shared library is downloaded
from, so it must equal __version__ (digits only: 0.3.13.post1 -> 0.3.13.1).
Fix a mismatch with `uv run task version sync`.
"""

import re
import sys
from pathlib import Path

root = Path(__file__).parent.parent


def find(path: str, pattern: str) -> str:
    match = re.search(pattern, (root / path).read_text())
    if not match:
        sys.exit(f"version not found in {path}")
    return match.group(1)


neonize = ".".join(re.findall(r"\d+", find("neonize/__init__.py", r'__version__ = "([\w.]+)"')))
versions = {
    "neonize/__init__.py (__version__)": neonize,
    "neonize/download.py (__GONEONIZE_VERSION__)": find(
        "neonize/download.py", r'__GONEONIZE_VERSION__ = "([\w.]+)"'
    ),
    "goneonize/version.go": find("goneonize/version.go", r'version := "([\w.]+)"'),
}
if len(set(versions.values())) > 1:
    for path, version in versions.items():
        print(f"{version:<12} {path}")
    sys.exit("versions differ; run `uv run task version sync`")
print(f"versions in sync: {neonize}")
