# Your practice file — 004. Count Even Numbers
"""
004. Count Even Numbers
Difficulty: Easy | Pattern: Counting loop
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Given a list of integers nums, return how many values are even. Zero and negative multiples of two count as even. Write a loop.

EXAMPLES
solve([1, 2, 4, 7]) -> 2
solve([]) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; values are integers with absolute value <= 10**9. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Start a counter at zero.
2. Even means remainder zero after division by two.
3. Increment once for each matching value.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    count = 0 
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 4, 7]) == 2
    assert solve([]) == 0
    assert solve([0]) == 1
    assert solve([-4, -3, -2]) == 2
    assert solve([1, 3, 5]) == 0
    assert solve([2, 2, 2]) == 3


if __name__ == "__main__":
    run_tests()
    print("PASS: 004 — Count Even Numbers")
