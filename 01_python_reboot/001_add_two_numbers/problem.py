# Your practice file — 001. Add Two Numbers
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Identify the two inputs.
2. Python adds numbers with +.
3. Return the expression a + b.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    # Write your solution here.
    return a + b
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
