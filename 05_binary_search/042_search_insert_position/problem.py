# Your practice file — 042. Search Insert Position
"""
042. Search Insert Position
Difficulty: Easy | Pattern: Lower bound: first value >= target
Prerequisites: Binary Search (041).

TASK
Return the first index where target could be inserted into nondecreasing
nums while keeping it sorted. If target exists, return the index of its first
occurrence. The answer may be len(nums). Do not change nums.

EXAMPLES
solve([1, 3, 5, 6], 2) -> 1.
solve([1, 3, 3, 6], 3) -> 1.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; sorted integers, duplicates allowed; target is an integer.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Find the boundary between values < target and values >= target.
2. Use a half-open interval [left, right) with right initially len(nums).
3. For a middle value >= target keep mid as a possible boundary: right = mid.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 3, 5, 6], 2) == 1
    assert solve([1, 3, 3, 6], 3) == 1
    assert solve([], 10) == 0
    assert solve([1, 3], 0) == 0
    assert solve([1, 3], 5) == 2
    assert solve([2, 2, 2], 2) == 0
    assert solve([2], 3) == 1
    from bisect import bisect_left
    for nums in ([], [1], [1, 1, 2, 3, 3], [-3, -1, 0, 4]):
        for target in range(-5, 7):
            assert solve(nums, target) == bisect_left(nums, target)


if __name__ == "__main__":
    run_tests()
    print("PASS: 042 — Search Insert Position")
