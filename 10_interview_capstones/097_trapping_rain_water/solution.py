# Explained reference solution — 097. Trapping Rain Water
"""
097. Trapping Rain Water
Difficulty: Hard | Pattern: Two pointers with certified boundary maxima
Prerequisites: 033 Container With Most Water; prefix/suffix maxima; two-pointer proof.

TASK
heights describes unit-width bars placed next to each other. Return the
total number of unit squares of water that would remain trapped after rain.
Water cannot be retained beyond the outer boundaries. Heights are nonnegative
integers. An empty list or fewer than three bars traps zero. Do not modify it.

EXAMPLES
heights=[0,1,0,2,1,0,1,3,2,1,2,1] -> 6.
heights=[3,0,3] -> 3.
heights=[1,2,3] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(heights) <= 100_000; 0 <= height <= 10_000.

SOLUTION EXPLANATION
At any index, the lower of the highest left and right walls sets the
water level. Maintaining both complete maximum arrays is straightforward, but
we can finalize positions incrementally. left_max and right_max summarize
already processed boundaries. If left_max<=right_max, the right side already
contains a wall at least left_max. A next left bar below left_max therefore
traps exactly left_max-height; if it is taller, it becomes the new left maximum
and traps zero. No unseen bar can invalidate that decision. The symmetric
argument handles the right side when its maximum is smaller. Each step settles
one bar, and every bar is settled once. The same loop naturally handles an
empty list because left<=right is initially false.

COMPLEXITY
For n bars, O(n) time and O(1) auxiliary space.

COMMON MISTAKES
Container area and total trapped water are different tasks. Subtract a bar only after updating that side's maximum, preventing negative contributions. Pointer movements need a boundary-height argument.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    left_max = right_max = 0
    water = 0
    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    return water


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([4]) == 0
    assert solve([1, 2]) == 0
    assert solve([3, 0, 3]) == 3
    assert solve([1, 2, 3]) == 0
    assert solve([3, 2, 1]) == 0
    assert solve([2, 0, 2, 0, 2]) == 4
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    from itertools import product
    for n in range(7):
        for values in product(range(3), repeat=n):
            expected = sum(min(max(values[:i + 1]), max(values[i:])) - value
                           for i, value in enumerate(values))
            assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 097 — Trapping Rain Water")
