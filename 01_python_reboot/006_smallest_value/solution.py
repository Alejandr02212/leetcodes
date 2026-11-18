# Explained reference solution — 006. Smallest Value
"""
006. Smallest Value
Difficulty: Easy | Pattern: Running best
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the smallest value in a nonempty list nums. Do not call min or sort the list.

EXAMPLES
solve([7, 2, 9]) -> 2
solve([-3]) -> -3

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 10000; integer values have absolute value <= 10**9. Do not mutate nums.

SOLUTION EXPLANATION
Initialize best to a real input value. At each step it is the minimum of the values seen so far. A smaller value replaces it; a larger value cannot change that minimum. The invariant gives the overall minimum at the end.

COMPLEXITY
For n values: time O(n), auxiliary space O(1).

COMMON MISTAKES
Starting best at zero breaks lists containing only positive values. Sorting does unnecessary work and may mutate the input.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    best = nums[0]
    for value in nums:
        if value < best:
            best = value
    return best


def run_tests() -> None:
    assert solve([7, 2, 9]) == 2
    assert solve([-3]) == -3
    assert solve([4, 5]) == 4
    assert solve([5, 4]) == 4
    assert solve([-2, -8, 0]) == -8
    assert solve([6, 6, 6]) == 6


if __name__ == "__main__":
    run_tests()
    print("PASS: 006 — Smallest Value")
