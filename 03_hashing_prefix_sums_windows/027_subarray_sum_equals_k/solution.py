# Explained reference solution — 027. Subarray Sum Equals K
"""
027. Subarray Sum Equals K
Difficulty: Medium | Pattern: Prefix sums + frequency map
Prerequisites: Dictionary counts; prefix sums (025–026).

TASK
Count the nonempty contiguous subarrays whose sum equals k. Different index
ranges count separately even when they contain identical values. Do not change nums.

EXAMPLES
solve([1, 1, 1], 2) -> 2: ranges [0:2] and [1:3].
solve([1, -1, 0], 0) -> 3: [1, -1], [0], and [1, -1, 0].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; nums and k are integers, including negatives and zero.

SOLUTION EXPLANATION
Let P[j] be the sum before index j. A range [i, j) sums to k exactly
when P[i] = P[j] - k. While reading each new endpoint j, seen stores the
frequency of prefix sums at earlier endpoints only. Its count for P[j]-k
therefore counts all valid starts for this endpoint. Add that count before
inserting P[j], so an empty range is never counted. The initial {0: 1}
represents the endpoint before the array and allows ranges starting at 0.
Every nonempty range has one right endpoint and is counted exactly once.
Sliding windows cannot replace this argument when negative values occur.

COMPLEXITY
Expected time O(n), auxiliary space O(n), where n = len(nums), using hash-table operations.

COMMON MISTAKES
A set loses repeated prefix sums. Inserting the current prefix before counting incorrectly counts empty ranges when k = 0.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> int:
    seen = {0: 1}
    prefix = 0
    answer = 0
    for value in nums:
        prefix += value
        answer += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return answer


def run_tests() -> None:
    assert solve([1, 1, 1], 2) == 2
    assert solve([1, -1, 0], 0) == 3
    assert solve([], 0) == 0
    assert solve([0, 0, 0], 0) == 6
    assert solve([-1, -1, 1], -1) == 3
    assert solve([3], 3) == 1
    assert solve([2, 4], 3) == 0
    from itertools import product
    for size in range(5):
        for values in product((-1, 0, 1), repeat=size):
            for target in (-1, 0, 1):
                expected = sum(sum(values[i:j]) == target
                               for i in range(size) for j in range(i + 1, size + 1))
                assert solve(list(values), target) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 027 — Subarray Sum Equals K")
