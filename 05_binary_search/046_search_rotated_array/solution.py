# Explained reference solution — 046. Search a Rotated Sorted Array
"""
046. Search a Rotated Sorted Array
Difficulty: Medium | Pattern: Binary search by identifying a sorted half
Prerequisites: Binary Search (041).

TASK
nums is a rotation of a strictly increasing array. Return the index of
target, or -1 if absent. A rotation by zero places is allowed. Use O(log n)
time and do not change nums.

EXAMPLES
solve([4, 5, 6, 7, 0, 1, 2], 0) -> 4.
solve([4, 5, 6, 7, 0, 1, 2], 3) -> -1.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; distinct integer values; target is an integer.

SOLUTION EXPLANATION
A rotated strictly increasing array has at most one descending break.
Hence the two halves split at mid cannot both contain a break internally;
at least one is sorted. Identify the sorted half from endpoint comparisons.
Its value interval tells us exactly whether target could be inside it. Keep
that half if so; otherwise discard it and keep the other half. Equality at
mid is checked first, so updates can safely move beyond mid. Distinct values
make these comparisons decisive and ensure each step removes about half
the remaining indices.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
Duplicate values remove the decisive sorted-half test and require another algorithm. Use inclusive outer endpoints but exclude the already-checked mid.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def run_tests() -> None:
    assert solve([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solve([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solve([], 1) == -1
    assert solve([1], 1) == 0
    assert solve([1], 0) == -1
    assert solve([3, 1], 1) == 1
    assert solve([1, 2, 3], 3) == 2
    for size in range(1, 20):
        original = list(range(0, 2 * size, 2))
        for shift in range(size):
            rotated = original[shift:] + original[:shift]
            for target in range(-1, 2 * size + 1):
                expected = rotated.index(target) if target in rotated else -1
                assert solve(rotated, target) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 046 — Search a Rotated Sorted Array")
