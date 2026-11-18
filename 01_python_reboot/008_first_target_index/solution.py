# Explained reference solution — 008. First Target Index
"""
008. First Target Index
Difficulty: Easy | Pattern: Linear search with early return
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the zero-based index of the first occurrence of target in nums. Return -1 when target is absent.

EXAMPLES
solve([5, 8, 5], 5) -> 0
solve([1, 2], 9) -> -1

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; all values and target are integers. Do not mutate nums.

SOLUTION EXPLANATION
enumerate provides each zero-based index together with its value. Scan from left to right, so the first equality encountered is necessarily the earliest match. If the loop finishes, every value differed from target, which justifies returning -1.

COMPLEXITY
For n values: worst-case time O(n), auxiliary space O(1).

COMMON MISTAKES
Returning -1 inside the loop rejects the input after only one mismatch. Return the index rather than the matching value.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1


def run_tests() -> None:
    assert solve([5, 8, 5], 5) == 0
    assert solve([1, 2], 9) == -1
    assert solve([], 1) == -1
    assert solve([9], 9) == 0
    assert solve([3, 4, 9], 9) == 2
    assert solve([-1, 0, -1], 0) == 1


if __name__ == "__main__":
    run_tests()
    print("PASS: 008 — First Target Index")
