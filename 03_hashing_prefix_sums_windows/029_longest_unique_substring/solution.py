# Explained reference solution — 029. Longest Substring Without Repeating Characters
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

SOLUTION EXPLANATION
Before adding text[right], the previous window has unique characters.
Its only possible new repetition is the incoming character. If its previous
occurrence is inside the window, every valid window ending here must start
after that occurrence. Move left to precisely that boundary. A previous
occurrence outside the window imposes no new restriction, hence max keeps
left from moving backward. The resulting window is the longest unique one
ending at right. Taking the maximum over all endpoints finds the answer.

COMPLEXITY
Expected time O(n), auxiliary space O(min(n, u)), where n = len(text) and u is the number of possible distinct characters.

COMMON MISTAKES
The answer is contiguous, not a subsequence. On abba, moving left backward when seeing the last a gives an invalid window.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, char in enumerate(text):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


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
