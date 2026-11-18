# Explained reference solution — 026. Pivot Index
"""
026. Pivot Index
Difficulty: Easy | Pattern: Running prefix sum
Prerequisites: Sum a list; prefix sums (025).

TASK
Return the smallest index i such that the sum strictly before nums[i] equals
the sum strictly after it. Return -1 when no such index exists. Do not change nums.

EXAMPLES
solve([1, 7, 3, 6, 5, 6]) -> 3: both sides sum to 11.
solve([2, 1, -1]) -> 0: the empty left side and the right side both sum to 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; integers may be negative. The sum of an empty side is 0.

SOLUTION EXPLANATION
Before index i is checked, left is exactly the sum of indices 0 through i-1.
Subtract that sum and the current value from total to obtain the right sum.
Equal sums make i a valid pivot. Scanning from left to right means the first
valid pivot is the smallest. If no comparison succeeds, no index qualifies.
This is a useful prefix-sum reduction: derive one region from a total and the
other region instead of repeatedly summing slices.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
Do not add the current value to left until after checking it. The current value belongs to neither side.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    for i, value in enumerate(nums):
        if left == total - left - value:
            return i
        left += value
    return -1


def run_tests() -> None:
    assert solve([1, 7, 3, 6, 5, 6]) == 3
    assert solve([2, 1, -1]) == 0
    assert solve([]) == -1
    assert solve([8]) == 0
    assert solve([0, 0, 0]) == 0
    assert solve([1, 2, 3]) == -1
    assert solve([-1, -1, -1, -1, -1, 0]) == 2


if __name__ == "__main__":
    run_tests()
    print("PASS: 026 — Pivot Index")
