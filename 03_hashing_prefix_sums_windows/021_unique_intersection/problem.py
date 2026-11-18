# Your practice file — 021. Unique Intersection
"""
021. Unique Intersection
Difficulty: Easy | Pattern: Set operations and deterministic output
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the distinct integers appearing in both first and second, sorted in increasing order. Leave inputs unchanged.

EXAMPLES
solve([1,2,2,1], [2,2]) -> [2]
solve([4,9,5], [9,4,9,8,4]) -> [4,9]

CONSTRAINTS AND CONTRACT
0 <= input lengths <= 10000; integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Remove duplicates with sets.
2. Keep members common to both sets.
3. Sort the resulting set.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(first: list[int], second: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 2, 1], [2, 2]) == [2]
    assert solve([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert solve([], [1]) == []
    assert solve([1], []) == []
    assert solve([1, 2], [3, 4]) == []
    assert solve([-1, 0, -1], [0, -1]) == [-1, 0]
    assert solve([3, 3], [3]) == [3]


if __name__ == "__main__":
    run_tests()
    print("PASS: 021 — Unique Intersection")
