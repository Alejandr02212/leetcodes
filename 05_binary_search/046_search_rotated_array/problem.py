# Your practice file — 046. Search a Rotated Sorted Array
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. At least one half around mid is sorted.
2. If nums[left] <= nums[mid], the left half is sorted.
3. Check whether target lies within that half before deciding which side to keep.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
