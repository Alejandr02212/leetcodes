# Your practice file — 008. First Target Index
"""
008. First Target Index
Difficulty: Easy | Pattern: Linear search with early return
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the zero-based index of the first occurrence of target in nums. Return -1 when target is absent.

EXAMPLES
solve([5, 8, 5], 5) -> 0
solve([1, 2], 9) -> -1

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; all values and target are integers. Do not mutate nums.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Walk left to right.
2. enumerate gives both index and value.
3. Return immediately on a match; put -1 after the loop.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([5, 8, 5], 5) == 0
    assert solve([1, 2], 9) == -1
    assert solve([], 1) == -1
    assert solve([9], 9) == 0
    assert solve([3, 4, 9], 9) == 2
    assert solve([-1, 0, -1], 0) == 1


if __name__ == "__main__":
    run_tests()
    print("PASS: 008 — First Target Index")
