# Your practice file — 031. Two Sum in a Sorted Array
"""
031. Two Sum in a Sorted Array
Difficulty: Easy | Pattern: Opposing two pointers
Prerequisites: Two Sum (019); sorted arrays.

TASK
Given a nondecreasing array nums, return [left, right] with 0-based indices
left < right whose values sum to target. Return [] if absent. Any valid pair
is accepted. Do not change nums; aim for O(1) auxiliary space.

EXAMPLES
solve([2, 7, 11, 15], 9) -> [0, 1].
solve([1, 2, 3], 9) -> [].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; integers and target may be negative; duplicates allowed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Start with the smallest and largest values.
2. If their sum is too small, can the smallest value pair with anything else?
3. Increase left for a small sum, decrease right for a large sum.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([2, 7, 11, 15], 9) == [0, 1]
    assert solve([1, 2, 3], 9) == []
    assert solve([], 0) == []
    assert solve([5], 10) == []
    assert solve([3, 3], 6) == [0, 1]
    assert solve([-4, -1, 2, 6], 2) == [0, 3]
    assert solve([0, 0], 0) == [0, 1]
    nums = [1, 2, 3, 4, 5]
    result = solve(nums, 6)
    assert len(result) == 2 and result[0] < result[1]
    assert nums[result[0]] + nums[result[1]] == 6


if __name__ == "__main__":
    run_tests()
    print("PASS: 031 — Two Sum in a Sorted Array")
