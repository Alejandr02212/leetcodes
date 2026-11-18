# Your practice file — 029. Longest Substring Without Repeating Characters
"""
029. Longest Substring Without Repeating Characters
Difficulty: Medium | Pattern: Variable sliding window + last seen index
Prerequisites: String indexing; dictionaries.

TASK
Return the length of the longest contiguous substring of text containing
no repeated character. Characters are case-sensitive. Return a length, not the substring.

EXAMPLES
solve('abcabcbb') -> 3: 'abc' is one longest choice.
solve('abba') -> 2: 'ab' or 'ba'.

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 100000; any Python string characters are allowed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep a window with all unique characters.
2. When a character repeats inside it, move left beyond its last occurrence.
3. Use max(left, last_seen[char] + 1) so left never moves backward.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('abcabcbb') == 3
    assert solve('abba') == 2
    assert solve('') == 0
    assert solve('aaaa') == 1
    assert solve('pwwkew') == 3
    assert solve('abcdef') == 6
    assert solve('aA🙂a') == 3
    assert solve('dvdf') == 3


if __name__ == "__main__":
    run_tests()
    print("PASS: 029 — Longest Substring Without Repeating Characters")
