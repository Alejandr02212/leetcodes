# Explained reference solution — 025. Range Sum Queries
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

SOLUTION EXPLANATION
Define prefix[i] as the sum of the first i values, so prefix[0]=0. The prefix through right contains the desired range plus the prefix through left. Subtracting prefix[left] cancels the unwanted beginning and leaves exactly nums[left:right]. The extra leading zero makes empty ranges and ranges starting at zero use the same formula.

COMPLEXITY
For n values and q queries: time O(n+q), auxiliary space O(n) for prefix sums plus O(q) output.

COMMON MISTAKES
right is exclusive here; many other statements use inclusive bounds. A prefix array has n+1 entries, including the initial zero.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)
    return [prefix[right] - prefix[left] for left, right in queries]


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
