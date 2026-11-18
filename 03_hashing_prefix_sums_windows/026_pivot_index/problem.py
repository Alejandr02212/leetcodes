# Your practice file — 026. Pivot Index
"""
026. Pivot Index
Difficulty: Easy | Pattern: Running prefix sum
Prerequisites: Sum a list; prefix sums (025).

TASK
Return the smallest index i such that the sum strictly before nums[i] equals
the sum strictly after it. Return -1 when no such index exists. Do not change nums.

EXAMPLES
solve([1, 7, 3, 6, 5, 6]) -> 3: both sides sum to 11.
solve([2, 1, -1]) -> 0: the empty left side and the right side both sum to 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; integers may be negative. The sum of an empty side is 0.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. What can the total sum tell you about the right side?
2. Keep only the sum of values already visited.
3. At i, right = total - left - nums[i]; compare before updating left.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 7, 3, 6, 5, 6]) == 3
    assert solve([2, 1, -1]) == 0
    assert solve([]) == -1
    assert solve([8]) == 0
    assert solve([0, 0, 0]) == 0
    assert solve([1, 2, 3]) == -1
    assert solve([-1, -1, -1, -1, -1, 0]) == 2


if __name__ == "__main__":
    run_tests()
    print("PASS: 026 — Pivot Index")
