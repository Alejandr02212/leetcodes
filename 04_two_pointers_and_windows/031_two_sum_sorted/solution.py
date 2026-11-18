# Explained reference solution — 031. Two Sum in a Sorted Array
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

SOLUTION EXPLANATION
At each step, any not-yet-eliminated pair lies between the two pointers.
If the endpoint sum is too small, nums[left] paired with any remaining value
is also too small, so left can be discarded. If it is too large, nums[right]
paired with any remaining value is also too large, so right can be discarded.
These are safe eliminations because the array is sorted. A match uses two
distinct indices since the loop requires left < right.

COMPLEXITY
Time O(n), auxiliary space O(1), excluding the constant-size result; n = len(nums).

COMMON MISTAKES
The sorted-input assumption is essential. Do not use the same element twice or accidentally return 1-based indices.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


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
