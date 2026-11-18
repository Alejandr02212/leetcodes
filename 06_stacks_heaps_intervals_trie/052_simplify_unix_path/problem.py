# Your practice file — 052. Simplify an Absolute Unix Path
"""
052. Simplify an Absolute Unix Path
Difficulty: Medium | Pattern: Stack: normalize components
Prerequisites: Problem 051 stack operations; str.split and str.join

TASK
Return the canonical lexical form of an absolute Unix-style path. Ignore
repeated '/', ignore '.' components, and interpret '..' by removing the
most recent ordinary component if one exists. '..' at root stays at root.
All other nonempty components, including '...', are ordinary names. Return
one leading slash and no trailing slash unless the result is '/'. This is
string processing; do not access the filesystem or resolve symbolic links.

EXAMPLES
solve("/a//b/.././c/") -> "/a/c".
solve("/../../") -> "/".
solve("/.../x/..") -> "/...".

CONSTRAINTS AND CONTRACT
1 <= len(path) <= 10000; path starts with '/'. Components contain no slash; no real filesystem semantics are required.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Split the path on '/'; consecutive slashes produce empty components.
2. A stack can represent the directory names kept so far.
3. Skip '' and '.', pop for '..' when possible, and append every other component.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(path: str) -> str:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve("/") == "/"
    assert solve("/a//b/.././c/") == "/a/c"
    assert solve("/../../") == "/"
    assert solve("/.../x/..") == "/..."
    assert solve("///alpha////beta//") == "/alpha/beta"
    assert solve("/a/../../b") == "/b"
    assert solve("/./a/./b/.") == "/a/b"
    assert solve("/a/.hidden/../file") == "/a/file"


if __name__ == "__main__":
    run_tests()
    print("PASS: 052 — Simplify an Absolute Unix Path")
