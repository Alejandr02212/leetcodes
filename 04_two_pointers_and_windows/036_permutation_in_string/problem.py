# Your practice file — 036. Permutation in a String
"""
036. Permutation in a String
Difficulty: Medium | Pattern: Fixed window + character counts
Prerequisites: Anagrams (017); fixed-size window (035).

TASK
Return whether text contains a contiguous substring that is a permutation
of pattern. Character counts must match exactly. An empty pattern occurs at
every boundary, so return True for it.

EXAMPLES
solve('ab', 'eidbaooo') -> True: 'ba' is a matching window.
solve('ab', 'eidboaoo') -> False.

CONSTRAINTS AND CONTRACT
0 <= len(pattern), len(text) <= 100000; lowercase English letters only.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. An anagram has the same length and the same character counts.
2. Slide a window of length len(pattern) over text.
3. Compare 26-slot count arrays after each update.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(pattern: str, text: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('ab', 'eidbaooo') is True
    assert solve('ab', 'eidboaoo') is False
    assert solve('', '') is True
    assert solve('', 'abc') is True
    assert solve('abc', 'ab') is False
    assert solve('aab', 'xxaba') is True
    assert solve('aab', 'abb') is False
    assert solve('z', 'z') is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 036 — Permutation in a String")
