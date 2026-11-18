# Explained reference solution — 094. Edit Distance
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

SOLUTION EXPLANATION
Think of aligning two prefixes. If their final characters match, align
them at zero cost and solve the smaller pair. Otherwise a final alignment step
must delete word1's last character, insert word2's last character, or replace
one with the other. Their remaining prefix states are respectively above, left,
and diagonal; each operation adds one. Taking the cheapest covers all possible
last alignment steps. Empty-prefix boundaries require deleting or inserting
every remaining character. Filling in dependency order proves correctness
inductively over prefix lengths. This DP contrasts with LCS: the state geometry
is similar, but the objective and allowed transition costs differ. Two rows
can reduce memory once the full-table recurrence is understood.

COMPLEXITY
For m=len(word1) and n=len(word2), O((m+1)*(n+1)) time and auxiliary space, usually written O(m*n) for nonempty strings. A rolling-row variant uses O(min(m,n)+1) space.

COMMON MISTAKES
Initialize the entire boundary row and column. Insertion and deletion use different neighbors. LCS length alone does not give this distance when replacement costs one.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


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
