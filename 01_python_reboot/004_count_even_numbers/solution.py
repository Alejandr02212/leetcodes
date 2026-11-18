# Explained reference solution — 004. Count Even Numbers
"""
004. Count Even Numbers
Difficulty: Easy | Pattern: Counting loop
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Given a list of integers nums, return how many values are even. Zero and negative multiples of two count as even. Write a loop.

EXAMPLES
solve([1, 2, 4, 7]) -> 2
solve([]) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; values are integers with absolute value <= 10**9. Do not mutate nums.

SOLUTION EXPLANATION
Keep one running count. Before each iteration it equals the number of even values already visited. The modulo test recognizes the next even value, and incrementing exactly then preserves the invariant. After the loop every value has been visited.

COMPLEXITY
For n values: time O(n), auxiliary space O(1).

COMMON MISTAKES
Zero is even. Test value % 2 == 0 rather than dividing and checking a float.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    count = 0
    for value in nums:
        if value % 2 == 0:
            count += 1
    return count


def run_tests() -> None:
    assert solve([1, 2, 4, 7]) == 2
    assert solve([]) == 0
    assert solve([0]) == 1
    assert solve([-4, -3, -2]) == 2
    assert solve([1, 3, 5]) == 0
    assert solve([2, 2, 2]) == 3


if __name__ == "__main__":
    run_tests()
    print("PASS: 004 — Count Even Numbers")
