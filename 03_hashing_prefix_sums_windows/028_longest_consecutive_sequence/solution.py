# Explained reference solution — 028. Longest Consecutive Sequence
"""
028. Longest Consecutive Sequence
Difficulty: Medium | Pattern: Hash set + sequence starts
Prerequisites: Sets; linear scans.

TASK
Return the length of the longest run of consecutive integer values present
in nums. Input order does not matter, and duplicates do not extend a run.
Aim for expected O(n) time without sorting; do not change nums.

EXAMPLES
solve([100, 4, 200, 1, 3, 2]) -> 4: values 1, 2, 3, 4.
solve([0, 3, 1, 2, 2]) -> 4: the repeated 2 contributes once.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000; values are arbitrary integers.

SOLUTION EXPLANATION
A maximal consecutive run has exactly one smallest value: its predecessor
is absent. Only that value starts a walk, which counts the complete run until
the next integer is missing. Other values in the same run fail the start
test, so they do not repeat the walk. Every run is visited and best records
the longest. Although there is a nested loop, the total number of successful
inner steps is bounded by the number of distinct input values.

COMPLEXITY
Expected time O(n), auxiliary space O(n), where n = len(nums).

COMMON MISTAKES
Walking from every input element can become quadratic. Iterating the original list can also repeat walks for duplicate starts.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    values = set(nums)
    best = 0
    for value in values:
        if value - 1 not in values:
            length = 1
            while value + length in values:
                length += 1
            best = max(best, length)
    return best


def run_tests() -> None:
    assert solve([100, 4, 200, 1, 3, 2]) == 4
    assert solve([0, 3, 1, 2, 2]) == 4
    assert solve([]) == 0
    assert solve([7]) == 1
    assert solve([2, 2, 2]) == 1
    assert solve([-3, -2, -1, 1, 2]) == 3
    assert solve([10, 30, 50]) == 1
    assert solve(list(range(1000))) == 1000


if __name__ == "__main__":
    run_tests()
    print("PASS: 028 — Longest Consecutive Sequence")
