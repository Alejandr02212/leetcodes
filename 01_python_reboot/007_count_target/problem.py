# Your practice file — 007. Count a Target
"""
007. Count a Target
Difficulty: Easy | Pattern: Predicate counting
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the number of positions in nums whose value equals target. Count repeated occurrences separately.

EXAMPLES
solve([2, 1, 2], 2) -> 2
solve([], 5) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; nums and target contain integers. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. This is problem 004 with a different condition.
2. Compare each value to target.
3. Add one on every equality.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([2, 1, 2], 2) == 2
    assert solve([], 5) == 0
    assert solve([1, 2, 3], 4) == 0
    assert solve([7], 7) == 1
    assert solve([0, 0, 0], 0) == 3
    assert solve([-1, 1, -1], -1) == 2


if __name__ == "__main__":
    run_tests()
    print("PASS: 007 — Count a Target")
