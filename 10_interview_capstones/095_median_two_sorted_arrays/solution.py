# Explained reference solution — 095. Median of Two Sorted Arrays
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

SOLUTION EXPLANATION
We need the boundary between the lower and upper halves, rather than all
merged elements. Pick i elements from the shorter array a and j=left_size-i
from b. Because m<=n, every i in 0..m gives a valid j. Each array is internally
sorted, so the split is valid exactly when a_left<=b_right and b_left<=a_right.
If a_left>b_right, too many large a values lie on the left; decreasing i is the
only useful direction. Otherwise b_left>a_right, requiring a larger i. These
monotone conditions justify binary search. Negative/positive infinity handles
empty pieces uniformly. A valid split puts the extra element on the left for
odd totals. Its maximum left value is the odd median; for even totals, average
that value and the minimum right value.

COMPLEXITY
Let m and n be the input lengths. O(log(min(m,n)+1)) time, with constant work when the shorter array is empty; O(1) auxiliary space.

COMMON MISTAKES
Search the shorter array so j stays valid. Use <= to allow duplicates. Include one extra left element for odd totals. Do not index past an empty partition.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums1: list[int], nums2: list[int]) -> float:
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    left_size = (m + n + 1) // 2
    low, high = 0, m
    while low <= high:
        i = (low + high) // 2
        j = left_size - i
        a_left = a[i - 1] if i else float('-inf')
        a_right = a[i] if i < m else float('inf')
        b_left = b[j - 1] if j else float('-inf')
        b_right = b[j] if j < n else float('inf')
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            high = i - 1
        else:
            low = i + 1
    raise ValueError('Inputs must be sorted and not both empty')


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
