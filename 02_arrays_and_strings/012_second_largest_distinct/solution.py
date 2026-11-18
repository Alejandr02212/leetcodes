# Explained reference solution — 012. Second Largest Distinct Value
"""
012. Second Largest Distinct Value
Difficulty: Easy | Pattern: Maintain two best candidates
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the second largest distinct integer in nums, or None if fewer than two distinct values exist. Do not sort.

EXAMPLES
solve([5, 1, 5, 3]) -> 3
solve([7, 7]) -> None

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; values are integers. Do not mutate nums.

SOLUTION EXPLANATION
Track the largest two distinct values in the processed prefix. A new largest pushes the old largest into second place. A different value below the largest improves second only when second is absent or smaller. Repeated copies of the largest do not create a distinct runner-up. These updates preserve the two-candidate invariant.

COMPLEXITY
For n values: time O(n), auxiliary space O(1).

COMMON MISTAKES
Duplicates of the maximum do not count as second. A zero sentinel breaks negative lists; use None to represent an absent candidate.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int | None:
    largest = second = None
    for value in nums:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value
    return second


def run_tests() -> None:
    assert solve([5, 1, 5, 3]) == 3
    assert solve([7, 7]) is None
    assert solve([]) is None
    assert solve([8]) is None
    assert solve([-5, -2, -9]) == -5
    assert solve([1, 2, 3]) == 2
    assert solve([3, 2, 1]) == 2
    assert solve([0, -1, 0]) == -1


if __name__ == "__main__":
    run_tests()
    print("PASS: 012 — Second Largest Distinct Value")
