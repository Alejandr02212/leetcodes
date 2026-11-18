# Your practice file — 003. Absolute Difference
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Start with a - b.
2. Is the result negative?
3. Negate only a negative result.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(a: int, b: int) -> int:
    # Write your solution here.
    return abs(a - b)
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
