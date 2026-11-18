# Explained reference solution — 043. First and Last Position
"""
043. First and Last Position
Difficulty: Medium | Pattern: Lower bound + upper bound
Prerequisites: Search Insert Position (042).

TASK
Return [first_index, last_index] of target in nondecreasing nums. If target
is absent return [-1, -1]. Use O(log n) time; do not scan all duplicates or change nums.

EXAMPLES
solve([5, 7, 7, 8, 8, 10], 8) -> [3, 4].
solve([5, 7, 7, 8, 8, 10], 6) -> [-1, -1].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; sorted integers with duplicates allowed.

SOLUTION EXPLANATION
A sorted array groups every occurrence of target into one contiguous block.
Its left boundary is the first >= target index; its exclusive right boundary
is the first > target index. Both predicates are monotone, so each boundary
can be located by the half-open search from 042. The helper changes whether
equality belongs on the left side of the boundary. Check that the lower
bound really contains target before subtracting one from the upper bound.
Two logarithmic searches retain logarithmic total time, even if the entire
array consists of one repeated value.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
A lower bound can point at another value or one past the array. Searching for one match then scanning duplicates becomes O(n).

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> list[int]:
    def boundary(strict: bool) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target or (strict and nums[mid] == target):
                left = mid + 1
            else:
                right = mid
        return left

    first = boundary(False)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, boundary(True) - 1]


def run_tests() -> None:
    assert solve([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solve([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solve([], 1) == [-1, -1]
    assert solve([2], 2) == [0, 0]
    assert solve([2, 2, 2], 2) == [0, 2]
    assert solve([1, 2, 3], 1) == [0, 0]
    assert solve([1, 2, 3], 3) == [2, 2]
    assert solve([1, 2, 3], 5) == [-1, -1]
    for target in range(-1, 6):
        nums = [0, 0, 1, 3, 3, 3, 4]
        positions = [i for i, value in enumerate(nums) if value == target]
        expected = [positions[0], positions[-1]] if positions else [-1, -1]
        assert solve(nums, target) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 043 — First and Last Position")
