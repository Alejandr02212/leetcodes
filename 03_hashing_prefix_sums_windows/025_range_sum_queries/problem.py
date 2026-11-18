# Your practice file — 025. Range Sum Queries
"""
025. Range Sum Queries
Difficulty: Easy | Pattern: Prefix sums and half-open ranges
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Given nums and queries [left, right], return the sum of nums[left:right] for each query. right is exclusive. Precompute once, then answer each query in constant time.

EXAMPLES
solve([2,-1,4,3], [[0,2],[1,4],[2,2]]) -> [1,6,0]
solve([], [[0,0]]) -> [0]

CONSTRAINTS AND CONTRACT
0 <= len(nums), len(queries) <= 10000. Every query satisfies 0 <= left <= right <= len(nums). Do not mutate inputs.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Cache sums of the first i values.
2. Include an initial zero before any values.
3. A range sum is prefix[right] - prefix[left].

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([2, -1, 4, 3], [[0, 2], [1, 4], [2, 2]]) == [1, 6, 0]
    assert solve([], [[0, 0]]) == [0]
    assert solve([], []) == []
    assert solve([5], [[0, 1], [0, 0], [1, 1]]) == [5, 0, 0]
    assert solve([-2, -3], [[0, 2], [1, 2]]) == [-5, -3]
    assert solve([1, 2, 3], []) == []
    assert solve([1, 2, 3], [[0, 3], [2, 3]]) == [6, 3]


if __name__ == "__main__":
    run_tests()
    print("PASS: 025 — Range Sum Queries")
