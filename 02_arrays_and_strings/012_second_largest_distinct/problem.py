# Your practice file — 012. Second Largest Distinct Value
"""
012. Second Largest Distinct Value
Difficulty: Easy | Pattern: Maintain two best candidates
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the second largest distinct integer in nums, or None if fewer than two distinct values exist. Do not sort.

EXAMPLES
solve([5, 1, 5, 3]) -> 3
solve([7, 7]) -> None

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; values are integers. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Store the two largest distinct values seen.
2. A new maximum moves the old maximum into second place.
3. Ignore values equal to the maximum.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int | None:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([5, 1, 5, 3]) == 3
    assert solve([7, 7]) is None
    assert solve([]) is None
    assert solve([8]) is None
    assert solve([-5, -2, -9]) == -5
    assert solve([1, 2, 3]) == 2
    assert solve([3, 2, 1]) == 2
    assert solve([0, -1, 0]) == -1


if __name__ == "__main__":
    run_tests()
    print("PASS: 012 — Second Largest Distinct Value")
