# Your practice file — 033. Container With Most Water
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Start with maximum width.
2. Moving the taller endpoint cannot overcome the shorter limiting height.
3. Record the area, then discard the shorter endpoint.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(height: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
