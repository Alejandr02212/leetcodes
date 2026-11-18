# Explained reference solution — 041. Binary Search
"""
041. Binary Search
Difficulty: Easy | Pattern: Binary search on a closed interval
Prerequisites: Sorted arrays; while loops.

TASK
Given strictly increasing nums, return the 0-based index of target, or -1
if absent. Use O(log n) time and do not change nums.

EXAMPLES
solve([-1, 0, 3, 5, 9, 12], 9) -> 4.
solve([-1, 0, 3, 5, 9, 12], 2) -> -1.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; distinct integers sorted ascending; target is an integer.

SOLUTION EXPLANATION
Invariant: if target exists and has not been returned, its index lies in
the inclusive range [left, right]. A middle value smaller than target rules
out every index through mid; a larger value rules out mid and all later
indices. Update the corresponding boundary past mid, preserving the invariant
and strictly reducing the range. An empty range proves absence. Each step
roughly halves the number of candidates, producing logarithmic time.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
Mixing inclusive and half-open boundary rules causes off-by-one bugs. Boundaries must move beyond mid when no equality was found.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def run_tests() -> None:
    assert solve([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solve([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solve([], 4) == -1
    assert solve([7], 7) == 0
    assert solve([7], 6) == -1
    assert solve([1, 3, 5], 1) == 0
    assert solve([1, 3, 5], 5) == 2
    for size in range(20):
        nums = list(range(0, size * 2, 2))
        for target in range(-1, size * 2 + 1):
            expected = nums.index(target) if target in nums else -1
            assert solve(nums, target) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 041 — Binary Search")
