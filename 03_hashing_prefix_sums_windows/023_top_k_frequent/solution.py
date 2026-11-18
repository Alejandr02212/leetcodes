# Explained reference solution — 023. Top K Frequent Values
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

SOLUTION EXPLANATION
Frequencies lie between one and n, so use them as array indices. Count values in an insertion-ordered dictionary; traversing that dictionary places tied values into their frequency bucket in first-appearance order. Scan buckets from largest frequency downward. Every appended value ranks before all remaining buckets, so stopping after k produces the required result and tie order.

COMPLEXITY
For n input values: expected time O(n), auxiliary space O(n) for counts and buckets, plus O(k) output.

COMMON MISTAKES
Initialize separate bucket lists with a comprehension; [[]] * size aliases the same list. Handle k=0 before appending anything.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> list[int]:
    if k == 0:
        return []
    counts = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for value, frequency in counts.items():
        buckets[frequency].append(value)
    result = []
    for frequency in range(len(nums), 0, -1):
        for value in buckets[frequency]:
            result.append(value)
            if len(result) == k:
                return result
    return result


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
