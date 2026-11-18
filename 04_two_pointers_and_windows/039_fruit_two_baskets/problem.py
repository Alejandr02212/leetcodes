# Your practice file — 039. Fruit Into Two Baskets
"""
039. Fruit Into Two Baskets
Difficulty: Medium | Pattern: Variable window with at most K distinct values
Prerequisites: Frequency maps; variable windows (029, 038).

TASK
Each integer in fruits identifies a fruit type at that position. Choose
one contiguous segment containing at most two distinct types, and return
its maximum possible length. Do not change fruits.

EXAMPLES
solve([1, 2, 1]) -> 3.
solve([0, 1, 2, 2]) -> 3: choose [1, 2, 2].

CONSTRAINTS AND CONTRACT
0 <= len(fruits) <= 100000; type identifiers are arbitrary integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Maintain a frequency map for the current window.
2. Shrink while the map contains more than two types.
3. Delete a type from the map when its count becomes zero.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(fruits: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 1]) == 3
    assert solve([0, 1, 2, 2]) == 3
    assert solve([]) == 0
    assert solve([9]) == 1
    assert solve([3, 3, 3, 3]) == 4
    assert solve([1, 2, 3, 2, 2]) == 4
    assert solve([1, 2, 3, 4, 5]) == 2
    assert solve([-1, -2, -1, -3, -3]) == 3


if __name__ == "__main__":
    run_tests()
    print("PASS: 039 — Fruit Into Two Baskets")
