# Explained reference solution — 090. Longest Common Subsequence
"""
090. Longest Common Subsequence
Difficulty: Medium | Pattern: Two-sequence dynamic programming
Prerequisites: Subsequences; grid DP; state meanings and boundary rows.

TASK
Return the length of the longest sequence of characters that is a
subsequence of both text1 and text2. Characters retain their original relative
order but need not be adjacent. Matching is case-sensitive. Return zero if
there is no shared character or either string is empty.

EXAMPLES
text1='abcde', text2='ace' -> 3 ('ace').
text1='abc', text2='def' -> 0.
text1='abc', text2='bac' -> 2 ('ac' or 'bc').

CONSTRAINTS AND CONTRACT
0 <= len(text1),len(text2) <= 500.

SOLUTION EXPLANATION
dp[i][j] measures an optimum over prefixes, so the zero row and column
represent comparisons with an empty string. When final characters match, there
exists an optimal subsequence ending with that character: append it to an LCS
of the shorter prefixes. When they differ, a shared subsequence cannot use both
final characters as its last match; it must omit at least one. Trying both
omissions gives max(dp[i-1][j], dp[i][j-1]). Filling rows from top to bottom and
columns left to right evaluates all dependencies before their consumers. This
is a subsequence problem, so gaps are allowed. A longest common substring uses
a different transition that resets on mismatches. Space can later be reduced
to two rows, but the full table makes the state and recurrence visible.

COMPLEXITY
For m=len(text1), n=len(text2), O((m+1)*(n+1)) time and auxiliary space (usually written O(m*n) for nonempty strings); rolling rows reduce space to O(n+1).

COMMON MISTAKES
Do not reset to zero on mismatch; that solves substring. Table indices refer to prefix lengths, so characters are accessed at i-1 and j-1.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text1: str, text2: str) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def run_tests() -> None:
    assert solve('', '') == 0
    assert solve('', 'abc') == 0
    assert solve('abc', 'def') == 0
    assert solve('abcde', 'ace') == 3
    assert solve('abc', 'bac') == 2
    assert solve('aaaa', 'aa') == 2
    assert solve('a', 'A') == 0
    assert solve('AGGTAB', 'GXTXAYB') == 4
    assert solve('same', 'same') == 4


if __name__ == "__main__":
    run_tests()
    print("PASS: 090 — Longest Common Subsequence")
