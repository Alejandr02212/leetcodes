# Explained reference solution — 048. Find a Peak Element
"""
048. Find a Peak Element
Difficulty: Medium | Pattern: Binary search on a slope
Prerequisites: Boundary-preserving binary search (047).

TASK
Return an index i whose value is strictly greater than its immediate
neighbors. Treat values beyond either end as negative infinity. Adjacent
input values are never equal. Any peak index is accepted; use O(log n) time.

EXAMPLES
solve([1, 2, 3, 1]) -> 2.
solve([1, 2, 1, 3, 5, 6, 4]) -> 1 or 5.

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 1000000; integers; nums[i] != nums[i+1]. Nonadjacent values may repeat.

SOLUTION EXPLANATION
Keep an interval [left, right] whose left endpoint is higher than the
value just outside on its left, and whose right endpoint is higher than the
value just outside on its right. The initial interval satisfies this with
virtual -infinity neighbors. On an uphill middle edge, discarding through
mid makes mid+1 a valid new left endpoint. On a downhill edge, keeping through
mid makes mid a valid new right endpoint. Thus the interval always contains
a peak: a maximum inside it exceeds both outside neighbors, and adjacent
inequality makes an appropriate local maximum strict. At one index the
invariant says that index exceeds both neighbors. mid+1 is safe because
left < right ensures mid < right.

COMPLEXITY
Time O(log(n+1)), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
This finds a local peak, which need not be the global maximum. Do not assume the whole array is sorted or unimodal.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def run_tests() -> None:
    def check(nums):
        index = solve(nums)
        assert 0 <= index < len(nums)
        assert index == 0 or nums[index] > nums[index - 1]
        assert index == len(nums) - 1 or nums[index] > nums[index + 1]
    check([1, 2, 3, 1])
    check([1, 2, 1, 3, 5, 6, 4])
    check([8])
    check([1, 2])
    check([2, 1])
    check([1, 3, 2, 4, 1])
    check([-4, -3, -2])
    from itertools import product
    for size in range(1, 7):
        for values in product((0, 1, 2), repeat=size):
            if all(values[i] != values[i + 1] for i in range(size - 1)):
                check(list(values))


if __name__ == "__main__":
    run_tests()
    print("PASS: 048 — Find a Peak Element")
