# Your practice file — 054. Daily Temperatures
"""
054. Daily Temperatures
Difficulty: Medium | Pattern: Monotonic stack of unresolved indices
Prerequisites: Problem 051 stacks; arrays and indices

TASK
For each daily temperature, return how many days you must wait until a
strictly warmer temperature. Use 0 when no later day is warmer. Return a
list of the same length; do not modify temperatures.

EXAMPLES
solve([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0].
solve([30, 30, 31]) -> [2, 1, 0]: equal temperatures are not warmer.
solve([]) -> [].

CONSTRAINTS AND CONTRACT
0 <= len(temperatures) <= 100000. Each temperature is an integer; negative values are allowed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep the indices of days still waiting for a warmer future day.
2. A new temperature resolves every smaller temperature at the stack top.
3. The stack temperatures remain nonincreasing; each resolved answer is current_index - old_index.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(temperatures: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == []
    assert solve([4]) == [0]
    assert solve([30, 30, 31]) == [2, 1, 0]
    assert solve([5, 4, 3, 2]) == [0, 0, 0, 0]
    assert solve([-3, -2, -1]) == [1, 1, 0]
    assert solve([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    from itertools import product
    for values in product(range(3), repeat=5):
        expected = []
        for i in range(len(values)):
            expected.append(next((j-i for j in range(i+1, len(values)) if values[j] > values[i]), 0))
        assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 054 — Daily Temperatures")
