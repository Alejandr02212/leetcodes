# Explained reference solution — 032. Valid Palindrome Ignoring Punctuation
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

SOLUTION EXPLANATION
After each successful comparison, all retained characters outside the
pointers have matching partners. Punctuation contributes no retained character,
so skipping it preserves that invariant. The next retained endpoints must
match in any palindrome; a mismatch proves failure. Matching endpoints can
be discarded, leaving the same question for the inner range. Crossing the
pointers means every required pair has matched. The ASCII restriction makes
per-character lowercasing sufficient for this specified case rule.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(text).

COMMON MISTAKES
Digits count as alphanumeric. Guard pointer bounds while skipping punctuation. Unicode case folding has additional rules outside this exercise contract.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


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
