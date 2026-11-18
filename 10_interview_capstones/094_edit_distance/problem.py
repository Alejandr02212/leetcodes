# Your practice file — 094. Edit Distance
"""
094. Edit Distance
Difficulty: Hard | Pattern: Two-sequence DP over insert, delete, and replace operations
Prerequisites: 090 Longest Common Subsequence; prefix DP; optimal substructure.

TASK
Return the minimum number of single-character insertions, deletions,
and replacements needed to transform word1 into word2. Every operation costs
one; matching characters cost zero. Operations may occur at any position.
Matching is case-sensitive. The input strings are unchanged.

EXAMPLES
word1='horse', word2='ros' -> 3: replace h with r, delete the extra r, delete e.
word1='', word2='abc' -> 3 insertions.
word1='same', word2='same' -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(word1),len(word2) <= 500.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. dp[i][j] transforms word1[:i] into word2[:j].
2. A final deletion comes from dp[i-1][j]; insertion from dp[i][j-1]; replacement from the diagonal.
3. Empty-prefix boundaries cost i deletions or j insertions.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(word1: str, word2: str) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('', '') == 0
    assert solve('', 'abc') == 3
    assert solve('abc', '') == 3
    assert solve('same', 'same') == 0
    assert solve('horse', 'ros') == 3
    assert solve('intention', 'execution') == 5
    assert solve('a', 'b') == 1
    assert solve('ab', 'ba') == 2
    assert solve('kitten', 'sitting') == 3
    from functools import lru_cache
    from itertools import product
    def brute(a, b):
        @lru_cache(None)
        def visit(i, j):
            if i == len(a):
                return len(b) - j
            if j == len(b):
                return len(a) - i
            if a[i] == b[j]:
                return visit(i + 1, j + 1)
            return 1 + min(visit(i + 1, j), visit(i, j + 1), visit(i + 1, j + 1))
        return visit(0, 0)
    words = [''.join(chars) for length in range(4) for chars in product('ab', repeat=length)]
    for a in words:
        for b in words:
            assert solve(a, b) == brute(a, b)


if __name__ == "__main__":
    run_tests()
    print("PASS: 094 — Edit Distance")
