# Explained reference solution — 013. Move Zeroes to the End
"""
013. Move Zeroes to the End
Difficulty: Easy | Pattern: In-place write pointer
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Move all zero values to the end of nums in place, preserving the relative order of nonzero values. Return the same list object as a convenience for testing.

EXAMPLES
solve([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
solve([]) -> []

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; integer values. Mutate nums using O(1) auxiliary space.

SOLUTION EXPLANATION
The write index marks the next free slot in a compact nonzero prefix. It never exceeds read, so writing cannot destroy an unread value. Scanning left to right preserves nonzero order. Once all nonzeros are packed, every remaining slot must be zero to preserve the original length and multiset.

COMPLEXITY
For n values: time O(n), auxiliary space O(1); the returned object is the existing input.

COMMON MISTAKES
Do not remove items while iterating over indices. Filling the zero suffix belongs after compaction. Preserve the same list object.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for index in range(write, len(nums)):
        nums[index] = 0
    return nums


def run_tests() -> None:
    assert solve([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solve([]) == []
    assert solve([0, 0]) == [0, 0]
    assert solve([1, 2]) == [1, 2]
    assert solve([-1, 0, -2]) == [-1, -2, 0]
    values = [0, 4, 0]
    assert solve(values) is values
    assert values == [4, 0, 0]


if __name__ == "__main__":
    run_tests()
    print("PASS: 013 — Move Zeroes to the End")
