# Explained reference solution — 020. Contains a Duplicate
"""
020. Contains a Duplicate
Difficulty: Easy | Pattern: Seen set and early exit
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return True if any integer occurs at least twice in nums, otherwise False.

EXAMPLES
solve([1,2,1]) -> True
solve([1,2,3]) -> False

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; integers. Do not mutate nums.

SOLUTION EXPLANATION
Before processing a value, seen contains exactly the earlier values. Membership therefore proves a repeated occurrence; otherwise inserting preserves the invariant. If the full scan finds no match, every value is distinct.

COMPLEXITY
For n values: expected time O(n), auxiliary space O(n).

COMMON MISTAKES
Use set(), because {} creates a dictionary. Check membership before adding the current value.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> bool:
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False


def run_tests() -> None:
    assert solve([1, 2, 1]) is True
    assert solve([1, 2, 3]) is False
    assert solve([]) is False
    assert solve([0]) is False
    assert solve([0, 0]) is True
    assert solve([-1, 2, -1]) is True
    assert solve([4, 5, 6, 4]) is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 020 — Contains a Duplicate")
