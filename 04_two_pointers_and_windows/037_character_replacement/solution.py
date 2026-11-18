# Explained reference solution — 037. Longest Repeating Character Replacement
"""
037. Longest Repeating Character Replacement
Difficulty: Medium | Pattern: Variable window + frequency constraint
Prerequisites: Variable windows (029–030); character counts.

TASK
Return the longest substring that can become one repeated letter by
replacing at most k of its characters. You may choose the repeated letter.
Replacements affect only the chosen substring; return its length.

EXAMPLES
solve('AABABBA', 1) -> 4: 'AABA' can become 'AAAA'.
solve('ABAB', 2) -> 4.

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 100000; uppercase English letters only; k >= 0.

SOLUTION EXPLANATION
Within a window, keeping its most frequent letter minimizes replacements:
all other positions must change, giving cost length - max(counts). Extend
right, then remove left characters until this cost is at most k. For any
fixed left endpoint, extending right never reduces the minimum replacement
cost: length rises by one while the maximum count rises by at most one.
A discarded start therefore cannot become valid at a later endpoint. The
remaining window is the longest valid one ending at right, and best covers
all endpoints. Recomputing the true maximum avoids a subtler stale-maximum
optimization until the basic window invariant is comfortable.

COMPLEXITY
Time O(26*n) = O(n), auxiliary space O(26) = O(1), where n = len(text). Each pointer moves at most n times.

COMMON MISTAKES
The most frequent letter may change after shrinking. A stale maximum uses a different proof; this version deliberately recomputes it.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str, k: int) -> int:
    counts = [0] * 26
    left = 0
    best = 0
    for right, char in enumerate(text):
        counts[ord(char) - ord('A')] += 1
        while right - left + 1 - max(counts) > k:
            counts[ord(text[left]) - ord('A')] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def run_tests() -> None:
    assert solve('AABABBA', 1) == 4
    assert solve('ABAB', 2) == 4
    assert solve('', 0) == 0
    assert solve('AAAA', 0) == 4
    assert solve('ABCDE', 0) == 1
    assert solve('ABCDE', 10) == 5
    assert solve('ABBB', 1) == 4
    from itertools import product
    for size in range(6):
        for letters in product('AB', repeat=size):
            text = ''.join(letters)
            for k in range(3):
                expected = 0
                for i in range(size):
                    for j in range(i + 1, size + 1):
                        segment = text[i:j]
                        if len(segment) - max(segment.count(c) for c in set(segment)) <= k:
                            expected = max(expected, len(segment))
                assert solve(text, k) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 037 — Longest Repeating Character Replacement")
