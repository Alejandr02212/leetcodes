# Explained reference solution — 052. Simplify an Absolute Unix Path
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

SOLUTION EXPLANATION
Treat the path as a sequence of navigation commands. The stack contains
exactly the ordinary directory names in the normalized path after each
prefix of commands. Ignoring '.' or an empty component preserves that path.
'..' undoes one ordinary component, except at root where there is nothing to
undo. An ordinary name enters that directory, so append it. This invariant
justifies each update and gives the canonical answer after the last command.
Joining retained names with single slashes enforces the output format.

COMPLEXITY
Time O(n) and auxiliary space O(n), where n = len(path); the returned string also uses O(n) space.

COMMON MISTAKES
Only the exact component '..' means parent; '...' is a name. Root has no parent. Do not use replace('../', '') or consult actual directories.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(path: str) -> str:
    parts = []
    for component in path.split('/'):
        if component in ('', '.'):
            continue
        if component == '..':
            if parts:
                parts.pop()
        else:
            parts.append(component)
    return '/' + '/'.join(parts)


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
