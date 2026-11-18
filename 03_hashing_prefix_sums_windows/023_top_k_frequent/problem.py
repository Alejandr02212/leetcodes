# Your practice file — 023. Top K Frequent Values
"""
023. Top K Frequent Values
Difficulty: Medium | Pattern: Frequency buckets
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the k most frequent distinct values in nums, ordered by decreasing frequency. Break frequency ties by the value's first appearance in nums. k=0 returns []. Use frequency buckets rather than sorting the whole input.

EXAMPLES
solve([1,1,1,2,2,3], 2) -> [1,2]
solve([8,7,8,7,9], 2) -> [8,7]

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; 0 <= k <= number of distinct values. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Count occurrences.
2. Frequency cannot exceed the length of the list.
3. Bucket values by frequency, then walk buckets backward.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert solve([8, 7, 8, 7, 9], 2) == [8, 7]
    assert solve([], 0) == []
    assert solve([1], 0) == []
    assert solve([5, 5], 1) == [5]
    assert solve([3, 1, 2], 3) == [3, 1, 2]
    assert solve([-1, 0, 0, -1, 2, 0], 2) == [0, -1]


if __name__ == "__main__":
    run_tests()
    print("PASS: 023 — Top K Frequent Values")
