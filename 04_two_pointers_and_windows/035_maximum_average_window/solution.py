# Explained reference solution — 035. Maximum Average Fixed Window
"""
035. Maximum Average Fixed Window
Difficulty: Easy | Pattern: Fixed-size sliding window
Prerequisites: Running sums; list indexing.

TASK
Return the maximum average among all contiguous windows of exactly k values
in nums. Return a float. Raise ValueError if k < 1 or k > len(nums).
Do not change nums.

EXAMPLES
solve([1, 12, -5, -6, 50, 3], 4) -> 12.75: window [12, -5, -6, 50].
solve([-5, -2], 1) -> -2.0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; integer values with absolute value <= 10**9. k is an integer; invalid k must raise ValueError.

SOLUTION EXPLANATION
The initial sum covers indices 0 through k-1. For each later right endpoint,
adding nums[right] and removing nums[right-k] leaves exactly the k values
ending at right. Thus every fixed-size window is considered once. Because
k is positive and constant, the window with largest sum also has the largest
average. Dividing only once avoids unnecessary repeated floating-point work.
Starting best at the first actual sum handles all-negative arrays correctly.

COMPLEXITY
Time O(n), auxiliary space O(1), where n = len(nums); the generator does not allocate a k-item slice.

COMMON MISTAKES
Initializing best to 0 fails when every window is negative. The outgoing index is right-k, not right-k+1.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> float:
    if not 1 <= k <= len(nums):
        raise ValueError('k must be between 1 and len(nums)')
    window_sum = sum(nums[i] for i in range(k))
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)
    return best / k


def run_tests() -> None:
    assert solve([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert solve([-5, -2], 1) == -2.0
    assert solve([5], 1) == 5.0
    assert solve([1, 2, 3], 3) == 2.0
    assert solve([0, 0, 0], 2) == 0.0
    assert abs(solve([1, 2, 4], 3) - 7 / 3) < 1e-12
    for nums, k in [([], 1), ([1], 0), ([1], 2), ([1], -1)]:
        try:
            solve(nums, k)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid k must raise ValueError')


if __name__ == "__main__":
    run_tests()
    print("PASS: 035 — Maximum Average Fixed Window")
