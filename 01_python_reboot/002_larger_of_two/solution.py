# Explained reference solution — 002. Larger of Two Numbers
"""
002. Larger of Two Numbers
Difficulty: Easy | Pattern: Conditionals
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the larger of integers a and b. If they are equal, return that value. Practice an if statement before using the built-in max.

EXAMPLES
solve(3, 8) -> 8
solve(4, 4) -> 4

CONSTRAINTS AND CONTRACT
-10**9 <= a, b <= 10**9.

SOLUTION EXPLANATION
There are two exhaustive possibilities: a is at least b, or b is greater than a. In the first branch a is a maximum; otherwise b must be. Returning in both paths also handles equality.

COMPLEXITY
Time O(1), auxiliary space O(1).

COMMON MISTAKES
Use >= or account for equality in your other branch. Indentation defines the branch body.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    if a >= b:
        return a
    return b


def run_tests() -> None:
    assert solve(3, 8) == 8
    assert solve(8, 3) == 8
    assert solve(4, 4) == 4
    assert solve(-8, -3) == -3
    assert solve(0, -1) == 0
    assert solve(-1, 0) == 0


if __name__ == "__main__":
    run_tests()
    print("PASS: 002 — Larger of Two Numbers")
