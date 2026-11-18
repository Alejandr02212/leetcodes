# Your practice file — 096. Minimum Window Substring
"""
096. Minimum Window Substring
Difficulty: Hard | Pattern: Variable sliding window with frequency deficits
Prerequisites: 029 Longest Unique Substring; 040 Anagram Windows; frequency counts; window invariants.

TASK
Return the shortest contiguous substring of s that contains every
character in t with at least its multiplicity. Extra characters are allowed.
If no window exists, return ''. When equally short answers exist, return the
one with the earliest starting index. An empty t returns ''. Matching is
case-sensitive; characters may be any Python string characters.

EXAMPLES
s='ADOBECODEBANC', t='ABC' -> 'BANC'.
s='a', t='aa' -> ''.
s='abxba', t='ab' -> 'ab' (earliest of two length-two answers).

CONSTRAINTS AND CONTRACT
0 <= len(s),len(t) <= 100_000.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Track how many required character occurrences are still missing.
2. Expand right until the window is valid, then shrink left while it remains valid.
3. Removing a character makes the window invalid only if its remaining count falls below its requirement.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(s: str, t: str) -> str:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('ADOBECODEBANC', 'ABC') == 'BANC'
    assert solve('a', 'aa') == ''
    assert solve('', 'a') == ''
    assert solve('abc', '') == ''
    assert solve('abxba', 'ab') == 'ab'
    assert solve('aaab', 'aab') == 'aab'
    assert solve('aA', 'A') == 'A'
    from collections import Counter
    from itertools import product
    def brute(source, target):
        if not target:
            return ''
        need = Counter(target)
        best = None
        for left in range(len(source)):
            for right in range(left + 1, len(source) + 1):
                candidate = source[left:right]
                counts = Counter(candidate)
                if all(counts[char] >= count for char, count in need.items()):
                    if best is None or len(candidate) < len(best):
                        best = candidate
        return best or ''
    for n in range(5):
        for chars in product('ab', repeat=n):
            source = ''.join(chars)
            for target in ('a', 'b', 'ab', 'aa', 'bb', ''):
                assert solve(source, target) == brute(source, target)


if __name__ == "__main__":
    run_tests()
    print("PASS: 096 — Minimum Window Substring")
