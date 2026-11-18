# Explained reference solution — 044. Integer Square Root
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

SOLUTION EXPLANATION
Squared nonnegative integers increase with the integer. Therefore candidates
whose square is <= x form an initial prefix. Search for the first candidate
outside that prefix using the lower-bound pattern. The artificial boundary
x+1 is guaranteed too large (including x=0), so a boundary always exists.
When the pointers meet, one less than that boundary is exactly the largest
valid integer. Integer multiplication avoids floating-point rounding near
large perfect squares.

COMPLEXITY
Time O(log(x+2)) integer-arithmetic steps, auxiliary space O(1) integer variables. Python big-integer bit costs are ignored under the given bound.

COMMON MISTAKES
A floating-point square root can round near a perfect square. Return the last valid candidate, not the first invalid one.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(x: int) -> int:
    left, right = 0, x + 1
    while left < right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid
    return left - 1


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
