# Your practice file — 002. Larger of Two Numbers
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare the values.
2. Which one should you return when a >= b?
3. Use one if branch and a final return.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    # Write your solution here.
    if a < b:
        return b
    else:
        return a
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
