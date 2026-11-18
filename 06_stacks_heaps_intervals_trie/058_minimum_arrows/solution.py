# Explained reference solution — 058. Minimum Arrows to Burst Balloons
"""
058. Minimum Arrows to Burst Balloons
Difficulty: Medium | Pattern: Greedy interval stabbing: choose the earliest end
Prerequisites: Problem 056 intervals; greedy exchange arguments

TASK
Each closed interval [start, end] represents the horizontal extent of a
balloon. An arrow fired at coordinate x bursts every balloon with start <= x
<= end. Return the minimum arrows needed to burst all balloons. You may
choose any real coordinate; integer endpoints suffice for an optimal answer.
Do not change the input.

EXAMPLES
solve([[10, 16], [2, 8], [1, 6], [7, 12]]) -> 2: shoot at 6 and 12.
solve([[1, 2], [2, 3]]) -> 1: a shot at 2 hits both.
solve([]) -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(balloons) <= 100000. Each start and end is an integer with start <= end; negative endpoints are allowed.

SOLUTION EXPLANATION
Let e be the earliest end among remaining balloons. Any valid solution
needs an arrow somewhere inside that balloon. Move such an arrow to e.
Every other remaining balloon ends at or after e; if it contained the old
coordinate and started before it, its start is also at most e, so it still
contains the moved shot. Therefore an optimum exists with a shot at e.
Remove the balloons hit and repeat the same argument. Sorting by end lets a
single scan implement these repeated choices. If a later start exceeds the
previous shot, that balloon needs another arrow; otherwise it is already hit.

COMPLEXITY
Time O(n log n), auxiliary space O(n) for the sorted copy/sort, and O(1) returned output.

COMMON MISTAKES
Sort by end, not start, to justify the greedy choice. A balloon beginning exactly at the previous shot is already burst. Avoid an arbitrary finite sentinel for the first shot.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(balloons: list[list[int]]) -> int:
    arrows = 0
    shot = None
    for start, end in sorted(balloons, key=lambda interval: interval[1]):
        if shot is None or start > shot:
            arrows += 1
            shot = end
    return arrows


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([[3, 3]]) == 1
    assert solve([[1, 2], [2, 3]]) == 1
    assert solve([[1, 2], [3, 4], [5, 6]]) == 3
    assert solve([[1, 10], [2, 9], [3, 8]]) == 1
    assert solve([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert solve([[-10, -8], [-8, -5], [0, 0]]) == 2
    data = [[4, 8], [1, 2]]
    assert solve(data) == 2 and data == [[4, 8], [1, 2]]


if __name__ == "__main__":
    run_tests()
    print("PASS: 058 — Minimum Arrows to Burst Balloons")
