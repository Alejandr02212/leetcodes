# Explained reference solution — 086. House Robber
"""
086. House Robber
Difficulty: Medium | Pattern: DP: take or skip the current item
Prerequisites: 085 Climbing Stairs; state definitions; rolling DP values.

TASK
nums contains the nonnegative cash in a row of houses. Return the maximum
cash you can collect without choosing two adjacent houses. You may choose no
houses. The street is a LINE, so the first and last houses are not adjacent.
Do not modify nums.

EXAMPLES
nums=[2,7,9,3,1] -> 12 (2+9+1).
nums=[2,1,1,2] -> 4 (first and last).
nums=[] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10_000; 0 <= each amount <= 10_000.

SOLUTION EXPLANATION
Define best(i) as the maximum obtainable from the first i houses. An
optimal plan either skips house i, preserving best(i-1), or takes it, leaving
only the first i-2 houses available and yielding best(i-2)+amount. These are all
possibilities and their subproblems remain optimal, so their maximum is correct.
Initialize the empty-prefix totals to zero. During the scan, one_back is the
best total for all processed houses and two_back is the best total excluding
the latest one. Simultaneous assignment preserves both old values while forming
the next state. Choosing each locally largest house greedily fails because its
two neighbors together may be more valuable.

COMPLEXITY
For n houses, O(n) time and O(1) auxiliary space under the usual bounded-integer model.

COMMON MISTAKES
Do not confuse this with the circular-street variant. Replacing one_back too early corrupts two_back. Returning max(nums) ignores valid nonadjacent combinations.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    two_back = one_back = 0
    for amount in nums:
        two_back, one_back = one_back, max(one_back, two_back + amount)
    return one_back


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([7]) == 7
    assert solve([1, 9]) == 9
    assert solve([2, 7, 9, 3, 1]) == 12
    assert solve([2, 1, 1, 2]) == 4
    assert solve([0, 0, 0]) == 0
    assert solve([6, 10, 6]) == 12
    from itertools import product
    for n in range(6):
        for values in product(range(3), repeat=n):
            expected = max((sum(values[i] for i in range(n) if mask & (1 << i))
                            for mask in range(1 << n) if not (mask & (mask << 1))),
                           default=0)
            assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 086 — House Robber")
