# Explained reference solution — 001. Add Two Numbers
"""
001. Add Two Numbers
Difficulty: Easy | Pattern: Inputs, return values, and arithmetic
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Given two integers a and b, return their sum. This first exercise is about writing a function by hand and returning a value.

EXAMPLES
solve(2, 3) -> 5
solve(-4, 1) -> -3

CONSTRAINTS AND CONTRACT
-10**9 <= a, b <= 10**9. Inputs are integers. Do not read from input() or print the answer inside solve.

SOLUTION EXPLANATION
A function receives named inputs and sends one result back with return. The + operator computes the requested sum directly. Because the returned expression is exactly a + b, it satisfies the contract for positive, negative, and zero values.

COMPLEXITY
Time O(1), auxiliary space O(1) for the bounded integers in this exercise.

COMMON MISTAKES
Printing is different from returning. Python functions without an explicit return produce None.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    return a + b


def run_tests() -> None:
    assert solve(2, 3) == 5
    assert solve(0, 0) == 0
    assert solve(-4, 1) == -3
    assert solve(-7, -2) == -9
    assert solve(9, -9) == 0
    assert solve(10**9, 10**9) == 2 * 10**9


if __name__ == "__main__":
    run_tests()
    print("PASS: 001 — Add Two Numbers")
