# Your practice file — 015. Merge Two Sorted Arrays
"""
015. Merge Two Sorted Arrays
Difficulty: Easy | Pattern: Two sorted streams
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return a new sorted list containing every value from sorted lists left and right, including duplicates. Leave both inputs unchanged. Use a two-pointer merge rather than sorting the concatenation.

EXAMPLES
solve([1,3], [2,3]) -> [1,2,3,3]
solve([], [4]) -> [4]

CONSTRAINTS AND CONTRACT
0 <= len(left), len(right) <= 10000; both lists sorted nondecreasing, integer values.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare the smallest unused value in each list.
2. Append the smaller and advance its pointer.
3. Once one list ends, append the other remainder.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(left: list[int], right: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 3], [2, 3]) == [1, 2, 3, 3]
    assert solve([], []) == []
    assert solve([], [4]) == [4]
    assert solve([4], []) == [4]
    assert solve([-3, 0], [-2, 0, 8]) == [-3, -2, 0, 0, 8]
    a, b = [1, 5], [2, 6]
    assert solve(a, b) == [1, 2, 5, 6]
    assert a == [1, 5] and b == [2, 6]


if __name__ == "__main__":
    run_tests()
    print("PASS: 015 — Merge Two Sorted Arrays")
