# Your practice file — 100. Burst Balloons
"""
100. Burst Balloons
Difficulty: Hard | Pattern: Interval DP: choose the LAST action in a subproblem
Prerequisites: Edit-distance DP tables; interval boundaries; optimal substructure.

TASK
nums gives a row of balloons with nonnegative integer values. Bursting
one balloon earns left_value * balloon_value * right_value, using the nearest
UNBURST neighbors at that moment. Missing outer neighbors have fixed value 1.
Afterward that balloon disappears and its former neighbors become adjacent.
Return the maximum total coins obtainable by bursting every balloon. Do not
modify nums. An empty row earns zero.

EXAMPLES
nums=[3,1,5,8] -> 167 (burst original values 1, then 5, then 3, then 8).
nums=[1,5] -> 10.
nums=[] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 150; 0 <= each value <= 100.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Choosing the FIRST balloon changes boundaries for many remaining subproblems.
2. Instead choose which balloon is LAST between two still-present boundary balloons.
3. With padded 1s, dp[left][right] solves the OPEN interval. Try every last index k and combine the two smaller intervals.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([5]) == 5
    assert solve([0]) == 0
    assert solve([1, 5]) == 10
    assert solve([3, 1, 5, 8]) == 167
    assert solve([0, 2, 0]) == 2
    assert solve([1, 1, 1]) == 3
    from functools import lru_cache
    from itertools import product
    @lru_cache(None)
    def brute(values):
        if not values:
            return 0
        return max((values[i - 1] if i else 1) * value
                   * (values[i + 1] if i + 1 < len(values) else 1)
                   + brute(values[:i] + values[i + 1:])
                   for i, value in enumerate(values))
    for n in range(6):
        for values in product(range(3), repeat=n):
            assert solve(list(values)) == brute(values)
    values = [3, 1, 5, 8]
    solve(values)
    assert values == [3, 1, 5, 8]


if __name__ == "__main__":
    run_tests()
    print("PASS: 100 — Burst Balloons")
