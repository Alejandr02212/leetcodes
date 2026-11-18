# Explained reference solution — 019. Two Sum
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

SOLUTION EXPLANATION
For a current value x, its only possible partner value is target-x. Keep the earliest index for each value in the already scanned prefix. Looking up the complement checks all earlier possible partners in expected constant time. Checking before inserting prevents reuse of the current index. The scan and earliest-index map enforce the specified tie rule.

COMPLEXITY
For n values: expected time O(n), auxiliary space O(n).

COMMON MISTAKES
Insert after lookup so a number cannot pair with itself. Keep the first occurrence if the tie rule requires the earliest index.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        if value not in seen:
            seen[value] = index
    return []


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
