# Your practice file — 041. Binary Search
"""
041. Binary Search
Difficulty: Easy | Pattern: Binary search on a closed interval
Prerequisites: Sorted arrays; while loops.

TASK
Given strictly increasing nums, return the 0-based index of target, or -1
if absent. Use O(log n) time and do not change nums.

EXAMPLES
solve([-1, 0, 3, 5, 9, 12], 9) -> 4.
solve([-1, 0, 3, 5, 9, 12], 2) -> -1.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 1000000; distinct integers sorted ascending; target is an integer.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep the range that could still contain the target.
2. Compare its middle value and discard the impossible half.
3. For inclusive boundaries use while left <= right, then mid +/- 1.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solve([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solve([], 4) == -1
    assert solve([7], 7) == 0
    assert solve([7], 6) == -1
    assert solve([1, 3, 5], 1) == 0
    assert solve([1, 3, 5], 5) == 2
    for size in range(20):
        nums = list(range(0, size * 2, 2))
        for target in range(-1, size * 2 + 1):
            expected = nums.index(target) if target in nums else -1
            assert solve(nums, target) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 041 — Binary Search")
