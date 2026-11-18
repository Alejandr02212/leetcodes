# Explained reference solution — 042. Search Insert Position
"""
042. Search Insert Position
Difficulty: Easy | Pattern: Lower bound: first value >= target
Prerequisites: Binary Search (041).

TASK
Return the first index where target could be inserted into nondecreasing
nums while keeping it sorted. If target exists, return the index of its first
occurrence. The answer may be len(nums). Do not change nums.

EXAMPLES
solve([1, 3, 5, 6], 2) -> 1.
solve([1, 3, 3, 6], 3) -> 1.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; sorted integers, duplicates allowed; target is an integer.

SOLUTION EXPLANATION
Everything strictly before left is known to be smaller than target, and
everything at or after right is known to be at least target. Initially both
known regions are empty. If nums[mid] is too small, sorted order lets us add
all indices through mid to the first region. Otherwise all indices from mid
onward belong to the second region. When left equals right, the unknown
region is empty and that meeting point is exactly the first >= target index,
or n if no such value exists. This lower-bound template is widely reusable.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
Returning immediately on equality may return a later duplicate. right = mid preserves a possible first occurrence.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def run_tests() -> None:
    assert solve([1, 3, 5, 6], 2) == 1
    assert solve([1, 3, 3, 6], 3) == 1
    assert solve([], 10) == 0
    assert solve([1, 3], 0) == 0
    assert solve([1, 3], 5) == 2
    assert solve([2, 2, 2], 2) == 0
    assert solve([2], 3) == 1
    from bisect import bisect_left
    for nums in ([], [1], [1, 1, 2, 3, 3], [-3, -1, 0, 4]):
        for target in range(-5, 7):
            assert solve(nums, target) == bisect_left(nums, target)


if __name__ == "__main__":
    run_tests()
    print("PASS: 042 — Search Insert Position")
