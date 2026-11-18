# Explained reference solution — 038. Max Consecutive Ones After K Flips
"""
038. Max Consecutive Ones After K Flips
Difficulty: Medium | Pattern: Variable window with a budget
Prerequisites: Sliding-window shrinking (030, 037).

TASK
Return the longest contiguous run of ones obtainable after changing at
most k zeroes to ones. nums contains only 0 and 1. Do not change nums.

EXAMPLES
solve([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) -> 6.
solve([0, 0, 1, 1], 1) -> 3.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; values are 0 or 1; k >= 0.

SOLUTION EXPLANATION
Each zero inside the chosen window requires one flip, so a window is
feasible exactly when its zero count is at most k. After adding a right
endpoint, discard left values until feasibility returns. A discarded start
was already over budget; adding more values cannot reduce its zero count,
so it can never become useful later. Consequently the remaining window is
the longest feasible one ending at right. Tracking its maximum over all
endpoints yields the answer without actually changing any bits.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(nums).

COMMON MISTAKES
At most k allows fewer flips. Do not reset the whole window at a zero; shrinking preserves useful overlap.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> int:
    left = 0
    zeros = 0
    best = 0
    for right, value in enumerate(nums):
        if value == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def run_tests() -> None:
    assert solve([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert solve([0, 0, 1, 1], 1) == 3
    assert solve([], 0) == 0
    assert solve([0, 0], 0) == 0
    assert solve([1, 1, 1], 0) == 3
    assert solve([0, 0, 0], 5) == 3
    assert solve([1, 0, 1, 0, 1], 1) == 3
    assert solve([0], 1) == 1


if __name__ == "__main__":
    run_tests()
    print("PASS: 038 — Max Consecutive Ones After K Flips")
