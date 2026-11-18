# Explained reference solution — 057. Insert an Interval
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

SOLUTION EXPLANATION
Use the existing sorted order instead of sorting again. Intervals whose
ends are smaller than the new start cannot overlap and belong in the answer
first. The following intervals overlap exactly while their starts are at most
the current merged end; merging one may extend that end, so keep checking the
updated boundary. Once an interval starts later, every remaining interval
starts later as well and cannot overlap the merged block. These three
phases cover every interval exactly once and preserve the represented union.

COMPLEXITY
Time O(n). Auxiliary space O(1) excluding the returned O(n) fresh interval lists.

COMMON MISTAKES
Check the expanding end in the overlap loop, not the original end. Equality means overlap. Copy suffix/prefix interval lists if the output must not alias the input.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    answer = []
    start, end = new_interval
    index = 0
    while index < len(intervals) and intervals[index][1] < start:
        answer.append(intervals[index][:])
        index += 1
    while index < len(intervals) and intervals[index][0] <= end:
        start = min(start, intervals[index][0])
        end = max(end, intervals[index][1])
        index += 1
    answer.append([start, end])
    while index < len(intervals):
        answer.append(intervals[index][:])
        index += 1
    return answer


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
