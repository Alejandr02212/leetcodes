# Your practice file — 009. Reverse Into a New List
"""
009. Reverse Into a New List
Difficulty: Easy | Pattern: Reverse traversal and output building
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return a new list containing nums in reverse order. Leave nums unchanged. Practice an index loop rather than slicing or reversed.

EXAMPLES
solve([1, 2, 3]) -> [3, 2, 1]
solve([]) -> []

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; values are integers. The returned list must be a different object.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Start at the last index.
2. Move toward zero with a negative step.
3. Append into a new empty list.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 3]) == [3, 2, 1]
    assert solve([]) == []
    assert solve([4]) == [4]
    assert solve([1, 2]) == [2, 1]
    assert solve([2, 2, 3]) == [3, 2, 2]
    original = [1, 5, 9]
    result = solve(original)
    assert original == [1, 5, 9]
    assert result == [9, 5, 1] and result is not original


if __name__ == "__main__":
    run_tests()
    print("PASS: 009 — Reverse Into a New List")
