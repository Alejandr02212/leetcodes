# Your practice file — 057. Insert an Interval
"""
057. Insert an Interval
Difficulty: Medium | Pattern: Three phases: before, overlapping, after
Prerequisites: Problem 056 interval merging

TASK
The existing closed intervals are sorted by start and are pairwise
disjoint, with each end strictly less than the next start. Insert a new
interval and merge every overlap, including touching endpoints. Return fresh
intervals in sorted order without changing either input.

EXAMPLES
solve([[1, 3], [6, 9]], [2, 5]) -> [[1, 5], [6, 9]].
solve([[1, 2], [3, 4]], [2, 3]) -> [[1, 4]].
solve([], [4, 8]) -> [[4, 8]].

CONSTRAINTS AND CONTRACT
0 <= len(intervals) <= 100000. Every interval and new_interval has two integer endpoints start <= end. Existing intervals satisfy the sorted disjoint precondition.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Copy intervals strictly before the new interval.
2. While an interval starts before or at the merged end, expand the new interval.
3. Append the merged interval and then the untouched suffix.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([], [4, 8]) == [[4, 8]]
    assert solve([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solve([[1, 2], [3, 4]], [2, 3]) == [[1, 4]]
    assert solve([[2, 3]], [-2, -1]) == [[-2, -1], [2, 3]]
    assert solve([[2, 3]], [6, 7]) == [[2, 3], [6, 7]]
    assert solve([[1, 2], [4, 5], [7, 8]], [0, 10]) == [[0, 10]]
    intervals, new = [[1, 2], [4, 8]], [5, 6]
    result = solve(intervals, new)
    assert result == [[1, 2], [4, 8]]
    result[0][0] = 99
    assert intervals == [[1, 2], [4, 8]] and new == [5, 6]


if __name__ == "__main__":
    run_tests()
    print("PASS: 057 — Insert an Interval")
