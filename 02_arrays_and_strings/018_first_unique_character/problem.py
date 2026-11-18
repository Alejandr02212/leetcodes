# Your practice file — 018. First Unique Character
"""
018. First Unique Character
Difficulty: Easy | Pattern: Count first, scan second
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the zero-based index of the first character in text that occurs exactly once. Return -1 if none exists.

EXAMPLES
solve('leetcode') -> 0
solve('aabbc') -> 4

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 10000. Characters are compared exactly.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. You need final frequencies before deciding uniqueness.
2. Build counts in one pass.
3. Scan the string again and stop at the first count of one.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('leetcode') == 0
    assert solve('aabbc') == 4
    assert solve('') == -1
    assert solve('aabb') == -1
    assert solve('z') == 0
    assert solve('loveleetcode') == 2
    assert solve('aAbA') == 0


if __name__ == "__main__":
    run_tests()
    print("PASS: 018 — First Unique Character")
