# Explained reference solution — 009. Reverse Into a New List
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

SOLUTION EXPLANATION
The last index is len(nums)-1. A step of -1 visits each index down to zero; the exclusive stop -1 lets zero be visited. Appending in that order constructs the reversed sequence, while reading only leaves the original unchanged.

COMPLEXITY
For n values: time O(n), auxiliary working space O(1) beyond the O(n) returned list.

COMMON MISTAKES
range excludes its stop. nums.reverse() mutates and returns None. Assigning result = nums aliases the input.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    result = []
    for index in range(len(nums) - 1, -1, -1):
        result.append(nums[index])
    return result


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
