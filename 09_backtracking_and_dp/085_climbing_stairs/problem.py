# Your practice file — 085. Climbing Stairs
"""
085. Climbing Stairs
Difficulty: Easy | Pattern: One-dimensional dynamic programming with rolling state
Prerequisites: Loops; recurrence relations; identifying repeated subproblems.

TASK
A staircase has n steps. Each move climbs either one or two steps.
Return the number of distinct ordered sequences of moves that reach exactly
step n. For n=0, count the one empty sequence. Return an exact Python integer.

EXAMPLES
n=3 -> 3: (1,1,1), (1,2), (2,1).
n=0 -> 1.
n=4 -> 5.

CONSTRAINTS AND CONTRACT
0 <= n <= 500. No external libraries or modulus are needed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Classify a complete route by whether its last move has length one or two.
2. ways(n)=ways(n-1)+ways(n-2), with ways(0)=ways(1)=1.
3. Only the previous two results are needed, so a whole table is optional.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(n: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(0) == 1
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(4) == 5
    assert solve(5) == 8
    assert solve(10) == 89
    assert solve(20) == 10946
    assert solve(50) == 20365011074


if __name__ == "__main__":
    run_tests()
    print("PASS: 085 — Climbing Stairs")
