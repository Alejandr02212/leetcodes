# Your practice file — 024. Product Except Self
"""
024. Product Except Self
Difficulty: Medium | Pattern: Prefix and suffix accumulators
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return a list whose ith value is the product of all nums values except nums[i]. Do not use division. For a singleton, the empty product is 1; for an empty input, return [].

EXAMPLES
solve([1,2,3,4]) -> [24,12,8,6]
solve([0,2,3]) -> [6,0,0]

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; -10 <= values <= 10. Assume fixed-width arithmetic for the usual interview complexity; Python supports larger integers. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Split the wanted product into values before and after i.
2. Store left products in the output on a forward pass.
3. Multiply by right products on a backward pass.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solve([]) == []
    assert solve([8]) == [1]
    assert solve([0, 2, 3]) == [6, 0, 0]
    assert solve([0, 2, 0]) == [0, 0, 0]
    assert solve([-1, 2, -3]) == [-6, 3, -2]
    assert solve([2, 5]) == [5, 2]


if __name__ == "__main__":
    run_tests()
    print("PASS: 024 — Product Except Self")
