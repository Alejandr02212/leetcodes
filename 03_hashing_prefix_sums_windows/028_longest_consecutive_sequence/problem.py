# Your practice file — 028. Longest Consecutive Sequence
"""
028. Longest Consecutive Sequence
Difficulty: Medium | Pattern: Hash set + sequence starts
Prerequisites: Sets; linear scans.

TASK
Return the length of the longest run of consecutive integer values present
in nums. Input order does not matter, and duplicates do not extend a run.
Aim for expected O(n) time without sorting; do not change nums.

EXAMPLES
solve([100, 4, 200, 1, 3, 2]) -> 4: values 1, 2, 3, 4.
solve([0, 3, 1, 2, 2]) -> 4: the repeated 2 contributes once.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; values are arbitrary integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Membership checks in a set are expected O(1).
2. Only start walking at a value whose predecessor is absent.
3. Walk upward from each true start; each distinct value belongs to one walk.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([100, 4, 200, 1, 3, 2]) == 4
    assert solve([0, 3, 1, 2, 2]) == 4
    assert solve([]) == 0
    assert solve([7]) == 1
    assert solve([2, 2, 2]) == 1
    assert solve([-3, -2, -1, 1, 2]) == 3
    assert solve([10, 30, 50]) == 1
    assert solve(list(range(1000))) == 1000


if __name__ == "__main__":
    run_tests()
    print("PASS: 028 — Longest Consecutive Sequence")
