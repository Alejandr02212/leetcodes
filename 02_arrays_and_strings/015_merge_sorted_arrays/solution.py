# Explained reference solution — 015. Merge Two Sorted Arrays
"""
015. Merge Two Sorted Arrays
Difficulty: Easy | Pattern: Two sorted streams
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return a new sorted list containing every value from sorted lists left and right, including duplicates. Leave both inputs unchanged. Use a two-pointer merge rather than sorting the concatenation.

EXAMPLES
solve([1,3], [2,3]) -> [1,2,3,3]
solve([], [4]) -> [4]

CONSTRAINTS AND CONTRACT
0 <= len(left), len(right) <= 10000; both lists sorted nondecreasing, integer values.

SOLUTION EXPLANATION
Each pointer identifies the smallest unused value in its own list. The smaller of those two heads is therefore the smallest unused value overall, so appending it preserves sorted order. When one list ends, the other remainder is already sorted and can be appended in order. Every value is consumed once.

COMPLEXITY
For lengths m and n: time O(m+n), auxiliary working space O(1) beyond O(m+n) output.

COMMON MISTAKES
Advance only the pointer whose value was consumed. Include both leftovers. Copying with slicing would allocate extra temporary lists.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def run_tests() -> None:
    assert solve([1, 3], [2, 3]) == [1, 2, 3, 3]
    assert solve([], []) == []
    assert solve([], [4]) == [4]
    assert solve([4], []) == [4]
    assert solve([-3, 0], [-2, 0, 8]) == [-3, -2, 0, 0, 8]
    a, b = [1, 5], [2, 6]
    assert solve(a, b) == [1, 2, 5, 6]
    assert a == [1, 5] and b == [2, 6]


if __name__ == "__main__":
    run_tests()
    print("PASS: 015 — Merge Two Sorted Arrays")
