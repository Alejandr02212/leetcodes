# Your practice file — 035. Maximum Average Fixed Window
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. All windows use the same denominator, so maximize their sums.
2. When a window moves right, remove its outgoing value and add its incoming value.
3. Initialize the best from the first window, not zero.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> float:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
