# Your practice file — 027. Subarray Sum Equals K
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Write a subarray sum as the difference of two prefix sums.
2. For current prefix p, you need earlier prefixes equal to p - k.
3. Seed frequency 0 with 1, count matches, then record the current prefix.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
