# Explained reference solution — 096. Minimum Window Substring
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

SOLUTION EXPLANATION
missing counts required occurrences not yet supplied by the current
window, including duplicates. Adding a character reduces missing only if that
occurrence fills a deficit. Once missing reaches zero, the window is valid.
Record it, then remove left characters until the first required occurrence is
lost. For a fixed right endpoint this examines progressively shorter valid
windows, including its shortest one. A discarded earlier left endpoint cannot
produce a better future answer because extending right only lengthens that
already-recorded valid window. Thus moving both boundaries only forward still
finds a global shortest window. Updating the best only for a strictly smaller
length preserves the earliest starting position on ties. Return the substring
once, after scanning, to avoid repeatedly copying candidate windows.

COMPLEXITY
For n=len(s), m=len(t), expected O(n+m) time including the final slice, and O(U) auxiliary frequency storage for U distinct characters across the inputs, plus the returned substring.

COMMON MISTAKES
A set loses duplicate requirements. Do not decrease missing for surplus occurrences. Update outgoing counts before checking the deficit. Empty t needs a guard to avoid endless shrinking.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(s: str, t: str) -> str:
    from collections import Counter
    if not t:
        return ''
    need = Counter(t)
    window = Counter()
    missing = len(t)
    left = 0
    best_start, best_length = 0, len(s) + 1
    for right, char in enumerate(s):
        window[char] += 1
        if window[char] <= need[char]:
            missing -= 1
        while missing == 0:
            length = right - left + 1
            if length < best_length:
                best_start, best_length = left, length
            outgoing = s[left]
            window[outgoing] -= 1
            if window[outgoing] < need[outgoing]:
                missing += 1
            left += 1
    return '' if best_length == len(s) + 1 else s[best_start:best_start + best_length]


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
