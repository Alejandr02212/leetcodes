# Your practice file — 089. Unique Grid Paths
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A cell is reached from directly above or directly left.
2. Every first-row and first-column cell has exactly one route.
3. Update one row left to right: dp[c] still holds above, dp[c-1] already holds left.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(m: int, n: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
