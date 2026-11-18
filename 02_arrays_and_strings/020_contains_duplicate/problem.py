# Your practice file — 020. Contains a Duplicate
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. You only need to remember which values appeared.
2. A set supports membership checks.
3. Return True at the first value already in the set.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
