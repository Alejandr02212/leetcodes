# Explained reference solution — 033. Container With Most Water
"""
033. Container With Most Water
Difficulty: Medium | Pattern: Two pointers + safe greedy elimination
Prerequisites: Opposing pointers (031).

TASK
Each height[i] is the height of a vertical line at x = i. Pick two distinct
lines to maximize (right - left) * min(height[left], height[right]). Return
that maximum area; return 0 with fewer than two lines. Do not change height.

EXAMPLES
solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49: indices 1 and 8.
solve([1, 1]) -> 1.

CONSTRAINTS AND CONTRACT
0 <= len(height) <= 100000; all heights are nonnegative integers.

SOLUTION EXPLANATION
Suppose the left height is no taller than the right. Any other container
keeping this left endpoint and moving the right endpoint inward has smaller
width and limiting height at most height[left]. It cannot beat the current
container, whose area was recorded. Therefore the left endpoint can be
discarded safely. The symmetric argument handles a shorter right endpoint.
Each elimination removes only pairs that cannot improve best, so a globally
optimal area is recorded before its endpoints could both be discarded.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(height).

COMMON MISTAKES
Width is the index difference. Moving the taller side discards possibilities without the required proof.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return best


def run_tests() -> None:
    assert solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solve([1, 1]) == 1
    assert solve([]) == 0
    assert solve([5]) == 0
    assert solve([0, 0, 0]) == 0
    assert solve([5, 1, 1, 5]) == 15
    assert solve([4, 3, 2, 1]) == 4
    from itertools import product
    for size in range(6):
        for heights in product((0, 1, 3), repeat=size):
            expected = max(((j - i) * min(heights[i], heights[j])
                            for i in range(size) for j in range(i + 1, size)), default=0)
            assert solve(list(heights)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 033 — Container With Most Water")
