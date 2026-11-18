# Explained reference solution — 085. Climbing Stairs
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

SOLUTION EXPLANATION
Any route to step i has a final move of one or two. Removing that move
leaves a route to i-1 or i-2 respectively; these categories are disjoint and cover
all routes. Thus ways(i)=ways(i-1)+ways(i-2). Set ways(0)=1 to represent doing
nothing, and ways(1)=1. At the start of each loop, previous and current represent
the two consecutive smaller states. Simultaneous assignment advances them without
losing the old value. This illustrates the DP workflow: define a state, derive
its transition, choose base cases, and evaluate in dependency order. A naive
recursive implementation recomputes these same states exponentially often.

COMPLEXITY
O(n) arithmetic operations and O(1) integer variables. With exact big integers, the result has O(n) bits; total bit work is O(n^2) and auxiliary integer storage O(n) bits.

COMMON MISTAKES
Returning zero for n=0 breaks the recurrence. Sequentially overwriting previous before computing current loses a needed value. Move order matters here.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(n: int) -> int:
    if n == 0:
        return 1
    previous, current = 1, 1
    for step in range(2, n + 1):
        previous, current = current, previous + current
    return current


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
