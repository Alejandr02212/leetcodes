# Your practice file — 019. Two Sum
"""
019. Two Sum
Difficulty: Easy | Pattern: Hash lookup for a complement
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return [i, j] with i < j and nums[i] + nums[j] == target. Use distinct positions. If no pair exists, return []. If several pairs exist, return the pair encountered first by scanning j left to right, with the earliest possible i for that j.

EXAMPLES
solve([2,7,11,15], 9) -> [0,1]
solve([3,3], 6) -> [0,1]

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; integer values and target. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. For each value, compute target - value.
2. Ask whether that complement appeared earlier.
3. Store value -> earliest index, after checking.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([2, 7, 11, 15], 9) == [0, 1]
    assert solve([3, 3], 6) == [0, 1]
    assert solve([], 1) == []
    assert solve([3], 6) == []
    assert solve([1, 2, 3], 9) == []
    assert solve([-3, 4, 3, 90], 0) == [0, 2]
    assert solve([1, 1, 4], 5) == [0, 2]
    assert solve([1, 4, 2, 3], 5) == [0, 1]


if __name__ == "__main__":
    run_tests()
    print("PASS: 019 — Two Sum")
