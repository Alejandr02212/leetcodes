# Explained reference solution — 021. Unique Intersection
"""
021. Unique Intersection
Difficulty: Easy | Pattern: Set operations and deterministic output
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the distinct integers appearing in both first and second, sorted in increasing order. Leave inputs unchanged.

EXAMPLES
solve([1,2,2,1], [2,2]) -> [2]
solve([4,9,5], [9,4,9,8,4]) -> [4,9]

CONSTRAINTS AND CONTRACT
0 <= input lengths <= 10000; integers.

SOLUTION EXPLANATION
A set removes repeated occurrences. Set intersection keeps exactly the values present in both sets, which is the requested membership rule. Sorting those distinct common values supplies the required deterministic order.

COMPLEXITY
For lengths n and m and k common distinct values: expected time O(n+m+k log k), auxiliary space O(n+m) for sets plus O(k) output/sort storage.

COMMON MISTAKES
Intersection ignores multiplicity. Sets have no sorted output guarantee; explicitly sort when the contract requires order.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(first: list[int], second: list[int]) -> list[int]:
    return sorted(set(first) & set(second))


def run_tests() -> None:
    assert solve([1, 2, 2, 1], [2, 2]) == [2]
    assert solve([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert solve([], [1]) == []
    assert solve([1], []) == []
    assert solve([1, 2], [3, 4]) == []
    assert solve([-1, 0, -1], [0, -1]) == [-1, 0]
    assert solve([3, 3], [3]) == [3]


if __name__ == "__main__":
    run_tests()
    print("PASS: 021 — Unique Intersection")
