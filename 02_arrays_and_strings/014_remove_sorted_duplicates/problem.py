# Your practice file — 014. Remove Duplicates From a Sorted Array
"""
014. Remove Duplicates From a Sorted Array
Difficulty: Easy | Pattern: In-place read/write pointers
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Given nums sorted in nondecreasing order, compact its distinct values into its first k positions and return k. Mutate nums in place without changing its length. Values after position k-1 do not matter.

EXAMPLES
nums=[1,1,2]; solve(nums) -> 2 and nums[:2] == [1,2]
nums=[]; solve(nums) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; sorted integer list. Use O(1) auxiliary space.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Sorted duplicates are adjacent.
2. Compare each value to the last value you kept.
3. A write pointer is both a destination and the final distinct count.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    for values, expected in [([], []), ([1], [1]), ([1, 1, 2], [1, 2]), ([2, 2, 2], [2]), ([-3, -3, 0, 2, 2], [-3, 0, 2]), ([1, 2, 3], [1, 2, 3])]:
        size = len(values)
        count = solve(values)
        assert count == len(expected)
        assert values[:count] == expected
        assert len(values) == size


if __name__ == "__main__":
    run_tests()
    print("PASS: 014 — Remove Duplicates From a Sorted Array")
