# Explained reference solution — 018. First Unique Character
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

SOLUTION EXPLANATION
Uniqueness depends on the entire string, so determine all frequencies first. Then scan original positions in order. The first position with frequency one is the earliest unique character; if no such position exists, returning -1 follows directly from the full scan.

COMPLEXITY
For n characters and u distinct characters: expected time O(n), auxiliary space O(u).

COMMON MISTAKES
A character seen once so far may repeat later. Return an index, not the character itself.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str) -> int:
    counts = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    for index, character in enumerate(text):
        if counts[character] == 1:
            return index
    return -1


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
