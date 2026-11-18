# Your practice file — 056. Merge Overlapping Intervals
"""
056. Merge Overlapping Intervals
Difficulty: Medium | Pattern: Sort then merge an active interval
Prerequisites: Sorting by a key; list construction

TASK
Given closed intervals [start, end] in any order, merge all overlapping
intervals and return the merged intervals sorted by start. Touching endpoints
overlap: [1, 2] and [2, 3] merge. Return fresh interval lists and do not modify
the input.

EXAMPLES
solve([[1, 3], [2, 6], [8, 10], [9, 12]]) -> [[1, 6], [8, 12]].
solve([[5, 5], [1, 5]]) -> [[1, 5]].
solve([]) -> [].

CONSTRAINTS AND CONTRACT
0 <= number of intervals <= 100000. Endpoints are integers with start <= end. The input need not be sorted.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Sort by start, so future intervals cannot begin before the active interval.
2. Compare each start with the end of the most recent output interval.
3. If it overlaps, extend the end with max; otherwise start a new output interval.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(intervals: list[list[int]]) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == []
    assert solve([[1, 1]]) == [[1, 1]]
    assert solve([[2, 3], [1, 2]]) == [[1, 3]]
    assert solve([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
    assert solve([[1, 3], [2, 6], [8, 10], [9, 12]]) == [[1, 6], [8, 12]]
    assert solve([[-5, -3], [-2, 0]]) == [[-5, -3], [-2, 0]]
    original = [[3, 4], [1, 3]]
    result = solve(original)
    assert original == [[3, 4], [1, 3]]
    result[0][0] = 99
    assert original == [[3, 4], [1, 3]]


if __name__ == "__main__":
    run_tests()
    print("PASS: 056 — Merge Overlapping Intervals")
