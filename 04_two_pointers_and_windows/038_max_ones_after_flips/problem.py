# Your practice file — 038. Max Consecutive Ones After K Flips
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A valid window has at most k zeroes.
2. Count zeroes when the right pointer advances.
3. While over budget, remove values from the left.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
