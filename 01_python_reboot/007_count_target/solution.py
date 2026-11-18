# Explained reference solution — 007. Count a Target
"""
007. Count a Target
Difficulty: Easy | Pattern: Predicate counting
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the number of positions in nums whose value equals target. Count repeated occurrences separately.

EXAMPLES
solve([2, 1, 2], 2) -> 2
solve([], 5) -> 0

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; nums and target contain integers. Do not mutate nums.

SOLUTION EXPLANATION
Reuse the counting-loop template with a new predicate: equality to target. The running count always equals the matches in the processed prefix. Each occurrence contributes exactly one, so duplicates are handled naturally.

COMPLEXITY
For n values: time O(n), auxiliary space O(1).

COMMON MISTAKES
Use == for equality; = assigns. Do not stop after the first match.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], target: int) -> int:
    count = 0
    for value in nums:
        if value == target:
            count += 1
    return count


def run_tests() -> None:
    assert solve([2, 1, 2], 2) == 2
    assert solve([], 5) == 0
    assert solve([1, 2, 3], 4) == 0
    assert solve([7], 7) == 1
    assert solve([0, 0, 0], 0) == 3
    assert solve([-1, 1, -1], -1) == 2


if __name__ == "__main__":
    run_tests()
    print("PASS: 007 — Count a Target")
