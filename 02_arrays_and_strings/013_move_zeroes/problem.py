# Your practice file — 013. Move Zeroes to the End
"""
013. Move Zeroes to the End
Difficulty: Easy | Pattern: In-place write pointer
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Move all zero values to the end of nums in place, preserving the relative order of nonzero values. Return the same list object as a convenience for testing.

EXAMPLES
solve([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
solve([]) -> []

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; integer values. Mutate nums using O(1) auxiliary space.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep a pointer to the next nonzero destination.
2. Copy each encountered nonzero there and advance it.
3. Fill the unused suffix with zeroes.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solve([]) == []
    assert solve([0, 0]) == [0, 0]
    assert solve([1, 2]) == [1, 2]
    assert solve([-1, 0, -2]) == [-1, -2, 0]
    values = [0, 4, 0]
    assert solve(values) is values
    assert values == [4, 0, 0]


if __name__ == "__main__":
    run_tests()
    print("PASS: 013 — Move Zeroes to the End")
