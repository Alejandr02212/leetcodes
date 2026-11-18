# Your practice file — 058. Minimum Arrows to Burst Balloons
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Consider the balloon that ends first: some arrow must hit it.
2. Moving that arrow right to this end cannot hurt any balloon it previously hit that ends no earlier.
3. Sort by end; fire only when the last shot lies before the next balloon's start.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(balloons: list[list[int]]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
