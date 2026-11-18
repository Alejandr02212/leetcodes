# Explained reference solution — 054. Daily Temperatures
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

SOLUTION EXPLANATION
A naive scan repeats the same search for many days. Instead, keep only
unresolved days. Their temperatures are nonincreasing from stack bottom to
top: a new warmer day removes every smaller top before it is added. When
index i removes index j, temperature[i] is warmer and no earlier day after j
could have been warmer; otherwise j would already have been removed. Thus
i-j is the first valid wait. Days left in the stack have no warmer successor,
so their initial 0 is correct.

The nested while loop is linear in total because every index is pushed once
and popped at most once. This is the amortized-analysis template.

COMPLEXITY
Time O(n), auxiliary stack O(n), and output O(n), where n is the number of days.

COMMON MISTAKES
Store indices, not just temperatures, because answers are distances. Use < rather than <= for strictly warmer. A nested loop can still be O(n) when each item is removed once.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    waiting = []
    for index, temperature in enumerate(temperatures):
        while waiting and temperatures[waiting[-1]] < temperature:
            previous = waiting.pop()
            answer[previous] = index - previous
        waiting.append(index)
    return answer


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
