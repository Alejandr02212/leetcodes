# Your practice file — 006. Smallest Value
"""
006. Smallest Value
Difficulty: Easy | Pattern: Running best
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the smallest value in a nonempty list nums. Do not call min or sort the list.

EXAMPLES
solve([7, 2, 9]) -> 2
solve([-3]) -> -3

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 10000; integer values have absolute value <= 10**9. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Remember the best value seen so far.
2. Start with the first element.
3. Replace it only when you see a smaller element.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    smallest = nums[0]
    # Write your solution here.
    for i in range(len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest 
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([7, 2, 9]) == 2
    assert solve([-3]) == -3
    assert solve([4, 5]) == 4
    assert solve([5, 4]) == 4
    assert solve([-2, -8, 0]) == -8
    assert solve([6, 6, 6]) == 6


if __name__ == "__main__":
    run_tests()
    print("PASS: 006 — Smallest Value")
