# Your practice file — 010. Exact String Palindrome
"""
010. Exact String Palindrome
Difficulty: Easy | Pattern: Two pointers: compare mirrored positions
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return whether text reads identically forward and backward. Compare characters exactly: case, spaces, and punctuation all matter. Do not reverse the string.

EXAMPLES
solve('level') -> True
solve('Level') -> False

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 10000. Empty and one-character strings are palindromes.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare the first and last characters.
2. Move both pointers inward after a match.
3. One mismatch means False; no mismatches means True.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('level') is True
    assert solve('Level') is False
    assert solve('') is True
    assert solve('x') is True
    assert solve('abba') is True
    assert solve('abca') is False
    assert solve('a a') is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 010 — Exact String Palindrome")
