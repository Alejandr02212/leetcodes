# Explained reference solution — 036. Permutation in a String
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

SOLUTION EXPLANATION
The needed array counts pattern's letters. After processing each endpoint,
the window array counts the most recent width letters, or the shorter prefix
until a full window exists. Incoming letters are added; the letter falling
outside that width is removed. A full window is a permutation exactly when
every letter count equals needed. Testing all full windows is exhaustive.
The fixed lowercase alphabet makes comparing 26 counters constant time.

COMPLEXITY
Time O(m + 26*n) = O(m+n), auxiliary space O(26) = O(1), where m = len(pattern), n = len(text).

COMMON MISTAKES
Matching distinct letters is insufficient: aab differs from abb. Do not compare a partial window before it reaches the required length.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(pattern: str, text: str) -> bool:
    width = len(pattern)
    if width == 0:
        return True
    if width > len(text):
        return False
    needed = [0] * 26
    window = [0] * 26
    for char in pattern:
        needed[ord(char) - ord('a')] += 1
    for right, char in enumerate(text):
        window[ord(char) - ord('a')] += 1
        if right >= width:
            window[ord(text[right - width]) - ord('a')] -= 1
        if right >= width - 1 and window == needed:
            return True
    return False


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
