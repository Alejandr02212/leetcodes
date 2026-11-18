# Your practice file — 047. Minimum in a Rotated Array
"""
047. Minimum in a Rotated Array
Difficulty: Medium | Pattern: Binary search retaining a candidate
Prerequisites: Rotated-array search (046).

TASK
Return the minimum value in nums, a nonempty rotation of a strictly
increasing array. A rotation by zero places is allowed. Use O(log n) time
without changing nums.

EXAMPLES
solve([3, 4, 5, 1, 2]) -> 1.
solve([1, 2, 3]) -> 1.

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 1000000; distinct integer values.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare nums[mid] with the right endpoint.
2. If nums[mid] > nums[right], the minimum must lie strictly to the right.
3. Otherwise the minimum lies at mid or to its left, so keep mid.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([3, 4, 5, 1, 2]) == 1
    assert solve([1, 2, 3]) == 1
    assert solve([7]) == 7
    assert solve([2, 1]) == 1
    assert solve([2, 3, 4, 1]) == 1
    assert solve([-1, 0, -5, -3]) == -5
    for size in range(1, 30):
        nums = list(range(-size, size, 2))
        for shift in range(size):
            rotated = nums[shift:] + nums[:shift]
            assert solve(rotated) == min(rotated)


if __name__ == "__main__":
    run_tests()
    print("PASS: 047 — Minimum in a Rotated Array")
