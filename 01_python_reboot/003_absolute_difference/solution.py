# Explained reference solution — 003. Absolute Difference
"""
003. Absolute Difference
Difficulty: Easy | Pattern: Conditionals and sign
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the nonnegative distance between integers a and b. Try solving it with a conditional before using abs.

EXAMPLES
solve(3, 10) -> 7
solve(-4, 2) -> 6

CONSTRAINTS AND CONTRACT
-10**9 <= a, b <= 10**9.

SOLUTION EXPLANATION
Subtracting gives a signed difference. If it is negative, negating it produces the distance; otherwise it already is the distance. The result therefore equals |a-b| in both cases.

COMPLEXITY
Time O(1), auxiliary space O(1).

COMMON MISTAKES
Return a nonnegative answer. Negating both inputs before subtracting does not automatically produce the distance.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    difference = a - b
    if difference < 0:
        return -difference
    return difference


def run_tests() -> None:
    assert solve(3, 10) == 7
    assert solve(10, 3) == 7
    assert solve(4, 4) == 0
    assert solve(-4, 2) == 6
    assert solve(-9, -2) == 7
    assert solve(0, -5) == 5


if __name__ == "__main__":
    run_tests()
    print("PASS: 003 — Absolute Difference")
