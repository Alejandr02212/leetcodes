# Explained reference solution — 005. Sum a List
"""
005. Sum a List
Difficulty: Easy | Pattern: Accumulator loop
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the sum of nums using a loop, without calling sum. The sum of an empty list is zero.

EXAMPLES
solve([3, -1, 4]) -> 6
solve([]) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; integer values have absolute value <= 10**9. Do not mutate nums.

SOLUTION EXPLANATION
The accumulator starts at the identity for addition, zero. After processing any prefix, total is the sum of exactly that prefix. Adding the next value extends the invariant, so after the full scan total is the required sum.

COMPLEXITY
For n values: time O(n), auxiliary space O(1), under bounded-word integer arithmetic.

COMMON MISTAKES
Initialize once before the loop. Return after the loop, otherwise only the first element is processed.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    total = 0
    for value in nums:
        total += value
    return total


def run_tests() -> None:
    assert solve([3, -1, 4]) == 6
    assert solve([]) == 0
    assert solve([0]) == 0
    assert solve([-5, -2]) == -7
    assert solve([8]) == 8
    assert solve([10, -10, 7]) == 7


if __name__ == "__main__":
    run_tests()
    print("PASS: 005 — Sum a List")
