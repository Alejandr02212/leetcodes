# Your practice file — 090. Longest Common Subsequence
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Let dp[i][j] mean the LCS length of text1[:i] and text2[:j].
2. Equal final characters can extend the diagonal state by one.
3. Otherwise skip one final character: take max(above, left).

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text1: str, text2: str) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
