# Your practice file — 005. Sum a List
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Choose a starting total that works for an empty list.
2. Add each value to it.
3. Return after every value is processed.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    suma = 0
    for i in range(len(nums)):
        suma = suma + nums[i]
    return suma
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
