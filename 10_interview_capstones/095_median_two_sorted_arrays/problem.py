# Your practice file — 095. Median of Two Sorted Arrays
"""
095. Median of Two Sorted Arrays
Difficulty: Hard | Pattern: Binary search on a valid partition
Prerequisites: Binary search invariants; sorted arrays; median definition.

TASK
Given two nondecreasing sorted integer arrays nums1 and nums2, return
the median of their combined multiset as a float. For an even total length,
average the two middle values; for an odd total, use the middle value. The
arrays are not both empty. Do not merge the arrays or modify either input.
Target O(log(min(m,n)+1)) time and O(1) auxiliary space.

EXAMPLES
nums1=[1,3], nums2=[2] -> 2.0.
nums1=[1,2], nums2=[3,4] -> 2.5.
nums1=[], nums2=[-2,8] -> 3.0.

CONSTRAINTS AND CONTRACT
0 <= m,n <= 100_000; m+n >=1. Values lie in -1_000_000..1_000_000. Inputs are already sorted.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Split both arrays so the combined left side has (m+n+1)//2 elements.
2. A correct split has every left value <= every right value; checking the two cross-boundaries suffices.
3. Binary-search the split in the shorter array. If its left boundary is too large, move its split left.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums1: list[int], nums2: list[int]) -> float:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 3], [2]) == 2.0
    assert solve([1, 2], [3, 4]) == 2.5
    assert solve([], [-2, 8]) == 3.0
    assert solve([9], []) == 9.0
    assert solve([0, 0], [0, 0]) == 0.0
    assert solve([-5, -3], [-2]) == -3.0
    assert solve([1], [2, 3, 4, 5, 6]) == 3.5
    from itertools import combinations_with_replacement
    arrays = [list(values) for length in range(5)
              for values in combinations_with_replacement((-2, 0, 3), length)]
    for a in arrays:
        for b in arrays:
            if not a and not b:
                continue
            merged = sorted(a + b)
            size = len(merged)
            expected = (merged[(size - 1) // 2] + merged[size // 2]) / 2
            assert solve(a, b) == expected
            assert a == sorted(a) and b == sorted(b)


if __name__ == "__main__":
    run_tests()
    print("PASS: 095 — Median of Two Sorted Arrays")
