# Your practice file — 030. Minimum Size Subarray Sum
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Positive numbers make extending a window increase its sum.
2. After extending right, shrink while the sum still reaches target.
3. Record a length before removing the leftmost value.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
