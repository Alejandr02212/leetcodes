# Explained reference solution — 089. Unique Grid Paths
"""
089. Unique Grid Paths
Difficulty: Medium | Pattern: Grid DP with a rolling row
Prerequisites: 085 Climbing Stairs; two-dimensional dependencies; array initialization.

TASK
A robot starts at the upper-left of an m-row, n-column grid and wants to
reach the lower-right. Each move goes one cell right or one cell down. Return
the number of distinct paths. There are no obstacles. A 1-by-1 grid has the
single empty path. Return an exact integer.

EXAMPLES
m=2, n=3 -> 3: RRD, RDR, DRR.
m=1, n=5 -> 1.
m=1, n=1 -> 1.

CONSTRAINTS AND CONTRACT
1 <= m,n <= 100.

SOLUTION EXPLANATION
Classify paths by their final move. Every route to an interior cell
comes from its upper or left neighbor, and the two categories are disjoint,
so paths[r][c]=paths[r-1][c]+paths[r][c-1]. Boundary cells each have one route.
A full m-by-n table makes these dependencies clear, but only the previous row
is needed. Before updating column c, dp[c] is the value above; after processing
c-1, dp[c-1] is the value to the left. Their sum updates the current cell.
Keeping dp[0]=1 handles the first column. The last entry after the last row is
the requested count. Right-to-left updates would not use the current left value.

COMPLEXITY
O(m*n) additions and O(n) integer slots. Under exact big-integer arithmetic, counts have O(m+n) bits, so a conservative bit bound is O(m*n*(m+n)) time and O(n*(m+n)) storage bits.

COMMON MISTAKES
Initialize boundaries to one, not zero. Grid dimensions count cells, so a 1-by-1 grid requires no moves. Do not use shared mutable row aliases for a full table.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(m: int, n: int) -> int:
    dp = [1] * n
    for row in range(1, m):
        for col in range(1, n):
            dp[col] += dp[col - 1]
    return dp[-1]


def run_tests() -> None:
    assert solve(1, 1) == 1
    assert solve(1, 5) == 1
    assert solve(6, 1) == 1
    assert solve(2, 3) == 3
    assert solve(3, 3) == 6
    assert solve(3, 7) == 28
    from math import comb
    for rows in range(1, 9):
        for cols in range(1, 9):
            assert solve(rows, cols) == comb(rows + cols - 2, rows - 1)


if __name__ == "__main__":
    run_tests()
    print("PASS: 089 — Unique Grid Paths")
