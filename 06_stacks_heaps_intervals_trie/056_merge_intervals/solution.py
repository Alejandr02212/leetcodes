# Explained reference solution — 056. Merge Overlapping Intervals
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

SOLUTION EXPLANATION
Sorting makes overlap local. After each interval, merged describes exactly
the union of the processed intervals as sorted, separated blocks. Only its
last block can overlap the next interval: all earlier blocks already end
before the last block begins. If the next start is no greater than the last
end, the union is one block with the larger end. Otherwise append a new
block. This preserves the union and the separation invariant, proving the
final representation is correct. Construct new [start, end] lists so extending
an output interval never changes a caller's interval.

COMPLEXITY
Time O(n log n) for sorting; auxiliary space O(n) for the sorted copy and sorting, plus O(n) output in the worst case.

COMMON MISTAKES
Touching endpoints merge because these intervals are closed. Use max for nested intervals. Assigning input interval lists directly to output can accidentally mutate the input.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(intervals: list[list[int]]) -> list[list[int]]:
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


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
