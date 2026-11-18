# Your practice file — 044. Integer Square Root
"""
044. Integer Square Root
Difficulty: Easy | Pattern: Binary search on an answer
Prerequisites: Boundary search (042).

TASK
Given a nonnegative integer x, return floor(sqrt(x)): the largest integer r
with r*r <= x. Do not use square-root functions or fractional exponentiation.

EXAMPLES
solve(8) -> 2, because 2*2 <= 8 < 3*3.
solve(16) -> 4.

CONSTRAINTS AND CONTRACT
0 <= x <= 10**18; Python integer arithmetic is available.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Candidate answers lie between 0 and x.
2. The predicate r*r <= x changes from True to False exactly once.
3. Find the first r whose square is too large, then subtract one.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(x: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(8) == 2
    assert solve(16) == 4
    assert solve(0) == 0
    assert solve(1) == 1
    assert solve(2) == 1
    assert solve(10**18) == 10**9
    assert solve(10**18 - 1) == 10**9 - 1
    for x in range(1000):
        root = solve(x)
        assert root * root <= x < (root + 1) * (root + 1)


if __name__ == "__main__":
    run_tests()
    print("PASS: 044 — Integer Square Root")
