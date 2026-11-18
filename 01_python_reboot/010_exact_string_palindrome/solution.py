# Explained reference solution — 010. Exact String Palindrome
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

SOLUTION EXPLANATION
A palindrome requires each mirrored pair to match. Keep pointers at the two ends; after each successful comparison, the already removed outside pairs are known to match. A mismatch disproves the property immediately. When the pointers meet or cross, every required pair has matched.

COMPLEXITY
For n characters: time O(n), auxiliary space O(1).

COMMON MISTAKES
This exercise does not lowercase or discard punctuation. Use left < right so the middle character needs no special case.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


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
