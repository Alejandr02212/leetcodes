# Your practice file — 032. Valid Palindrome Ignoring Punctuation
"""
032. Valid Palindrome Ignoring Punctuation
Difficulty: Easy | Pattern: Two pointers + skipping irrelevant characters
Prerequisites: Palindrome basics (010); string methods.

TASK
Return whether text reads the same forward and backward after discarding
non-alphanumeric characters and ignoring ASCII letter case. Avoid constructing
a filtered copy. An empty filtered string is a palindrome.

EXAMPLES
solve('A man, a plan, a canal: Panama!') -> True.
solve('race a car') -> False.

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 100000; text contains ASCII characters only. Digits are retained.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Put pointers at both ends.
2. Skip punctuation independently at either end.
3. Compare lowercase characters, then move both pointers inward.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('A man, a plan, a canal: Panama!') is True
    assert solve('race a car') is False
    assert solve('') is True
    assert solve('!!!') is True
    assert solve('0P') is False
    assert solve('1aA1') is True
    assert solve('a.') is True
    assert solve('ab') is False


if __name__ == "__main__":
    run_tests()
    print("PASS: 032 — Valid Palindrome Ignoring Punctuation")
