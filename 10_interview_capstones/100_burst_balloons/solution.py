# Explained reference solution — 100. Burst Balloons
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

SOLUTION EXPLANATION
Pad the row with permanent boundary values 1. Define dp[left][right]
as the best score from bursting every balloon strictly between those indices,
while their boundary balloons remain. If last is the final balloon burst in
that interval, its neighbors at that moment are exactly left and right, so its
final reward is fixed. All balloons to its left and right can be solved as
independent smaller intervals while last remains. Thus try every last and take
the maximum of dp[left][last]+dp[last][right]+value[left]*value[last]*value[right].
Every complete burst order has such a last balloon, and combining optimal
suborders realizes each candidate, proving the recurrence. Adjacent boundaries
contain nothing and score zero. Increasing interval width solves dependencies
first. Thinking about the LAST operation is the key interval-DP insight.

COMPLEXITY
For n balloons, O(n^3) time and O(n^2) auxiliary DP space, plus O(n) padding. More precisely the allocated table is (n+2)^2, including empty input.

COMMON MISTAKES
Intervals are open: do not burst their boundary indices. The relevant neighbors are surviving balloons, not original adjacent values. Greedy smallest-first or largest-first is not generally optimal.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    values = [1] + nums + [1]
    size = len(values)
    dp = [[0] * size for _ in range(size)]
    for width in range(2, size):
        for left in range(size - width):
            right = left + width
            for last in range(left + 1, right):
                coins = (dp[left][last] + dp[last][right]
                         + values[left] * values[last] * values[right])
                dp[left][right] = max(dp[left][right], coins)
    return dp[0][-1]


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
