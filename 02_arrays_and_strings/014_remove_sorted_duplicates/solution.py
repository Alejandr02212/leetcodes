# Explained reference solution — 014. Remove Duplicates From a Sorted Array
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

SOLUTION EXPLANATION
Sorting places equal values together. The prefix nums[:write] contains exactly one copy of each distinct value already processed. Compare the next value with the last kept value; only a different value needs a new slot. write <= read keeps writes safe, and the prefix invariant proves the returned count and contents.

COMPLEXITY
For n values: time O(n), auxiliary space O(1).

COMMON MISTAKES
Return the count, not the modified list. Tests should inspect only the first k positions. Never read nums[write-1] when write is zero.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    write = 0
    for read in range(len(nums)):
        if write == 0 or nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


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
