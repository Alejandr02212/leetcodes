# Explained reference solution — 030. Minimum Size Subarray Sum
"""
030. Minimum Size Subarray Sum
Difficulty: Medium | Pattern: Variable sliding window with positive numbers
Prerequisites: Running sums; longest unique window (029).

TASK
Given positive integers nums and a positive target, return the shortest
length of a nonempty contiguous subarray with sum at least target. Return 0
if none exists. Do not change nums.

EXAMPLES
solve([2, 3, 1, 2, 4, 3], 7) -> 2: [4, 3].
solve([1, 1, 1], 5) -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; each number > 0; target > 0.

SOLUTION EXPLANATION
Extending right can only increase the sum because every value is positive.
Whenever a window qualifies, record it and remove its first value to seek a
shorter qualifying window with the same right endpoint. Stop only when the
sum becomes too small. A removed left endpoint never needs revisiting:
its earlier qualifying window was already recorded, and a later right
endpoint would make its range longer. Thus all candidates that could improve
the minimum are considered. Each pointer moves forward at most n times.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
Use while, not if: several left removals may be needed. This template is invalid with negative numbers because the sum loses monotonicity.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    left = 0
    total = 0
    best = len(nums) + 1
    for right, value in enumerate(nums):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == len(nums) + 1 else best


def run_tests() -> None:
    assert solve([2, 3, 1, 2, 4, 3], 7) == 2
    assert solve([1, 1, 1], 5) == 0
    assert solve([], 1) == 0
    assert solve([8], 7) == 1
    assert solve([2, 2, 2], 6) == 3
    assert solve([1, 1, 1, 10], 10) == 1
    assert solve([1, 2, 3, 4], 6) == 2
    from itertools import product
    for size in range(5):
        for values in product((1, 3), repeat=size):
            for target in (1, 4, 8):
                lengths = [j - i for i in range(size) for j in range(i + 1, size + 1)
                           if sum(values[i:j]) >= target]
                assert solve(list(values), target) == min(lengths, default=0)


if __name__ == "__main__":
    run_tests()
    print("PASS: 030 — Minimum Size Subarray Sum")
