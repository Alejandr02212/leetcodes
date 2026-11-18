# Explained reference solution — 047. Minimum in a Rotated Array
"""
047. Minimum in a Rotated Array
Difficulty: Medium | Pattern: Binary search retaining a candidate
Prerequisites: Rotated-array search (046).

TASK
Return the minimum value in nums, a nonempty rotation of a strictly
increasing array. A rotation by zero places is allowed. Use O(log n) time
without changing nums.

EXAMPLES
solve([3, 4, 5, 1, 2]) -> 1.
solve([1, 2, 3]) -> 1.

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 1000000; distinct integer values.

SOLUTION EXPLANATION
Maintain that the minimum's index lies in [left, right]. If the middle
value exceeds the right value, the rotation break must occur after mid, so
none of the indices through mid can hold the minimum. Otherwise the suffix
from mid to right has no rotation break and its smallest value is at mid;
the global minimum is therefore either mid or farther left. The update
right = mid deliberately retains that candidate. Each step shrinks the
interval until one possible index remains.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
right = mid-1 may discard the minimum itself. The distinctness and nonempty contracts are required.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def run_tests() -> None:
    assert solve([3, 4, 5, 1, 2]) == 1
    assert solve([1, 2, 3]) == 1
    assert solve([7]) == 7
    assert solve([2, 1]) == 1
    assert solve([2, 3, 4, 1]) == 1
    assert solve([-1, 0, -5, -3]) == -5
    for size in range(1, 30):
        nums = list(range(-size, size, 2))
        for shift in range(size):
            rotated = nums[shift:] + nums[:shift]
            assert solve(rotated) == min(rotated)


if __name__ == "__main__":
    run_tests()
    print("PASS: 047 — Minimum in a Rotated Array")
