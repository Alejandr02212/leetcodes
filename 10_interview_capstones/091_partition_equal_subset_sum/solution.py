# Explained reference solution — 091. Partition Into Equal-Sum Subsets
"""
091. Partition Into Equal-Sum Subsets
Difficulty: Medium | Pattern: 0/1 knapsack with descending updates
Prerequisites: Coin change; boolean DP; using each item once versus unlimited times.

TASK
Return whether nums can be split into two disjoint subsets whose union
uses every element and whose sums are equal. Values are nonnegative and each
position can be used once, even if values repeat. Empty subsets are allowed,
so an empty list returns True. Leave nums unchanged.

EXAMPLES
nums=[1,5,11,5] -> True ([11] and [1,5,5]).
nums=[1,2,5] -> False.
nums=[] -> True.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 200; 0 <= nums[i] <= 100.

SOLUTION EXPLANATION
If two sums are equal, each must be half the total; an odd total is
impossible. It is enough to find one subset with that half-sum, because all
remaining positions form the other half. Before each item, reachable[s] means
some subset of earlier positions totals s. The next state can either omit the
item or include it using an earlier state at s-value. Updating s downward
preserves that earlier state until it is read, ensuring each position is used
at most once. Upward updates would allow the same item repeatedly, accidentally
solving unbounded knapsack. Zero values leave reachable unchanged, and the
empty subset initializes reachable[0]=True.

COMPLEXITY
Let n=len(nums) and S=sum(nums)//2. O(n*(S+1)) time and O(S+1) auxiliary space; odd-total inputs return after O(n) summation.

COMMON MISTAKES
Descending versus ascending sum order changes the problem. Checking only total parity is insufficient. Treat repeated values as separate selectable positions.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    reachable = [False] * (target + 1)
    reachable[0] = True
    for value in nums:
        for subtotal in range(target, value - 1, -1):
            reachable[subtotal] = reachable[subtotal] or reachable[subtotal - value]
    return reachable[target]


def run_tests() -> None:
    assert solve([]) is True
    assert solve([0]) is True
    assert solve([1]) is False
    assert solve([1, 5, 11, 5]) is True
    assert solve([1, 2, 5]) is False
    assert solve([2, 2, 3, 5]) is False
    assert solve([0, 0, 2, 2]) is True
    from itertools import product
    for n in range(6):
        for values in product(range(3), repeat=n):
            total = sum(values)
            possible = total % 2 == 0 and any(
                sum(values[i] for i in range(n) if mask & (1 << i)) == total // 2
                for mask in range(1 << n))
            assert solve(list(values)) is possible


if __name__ == "__main__":
    run_tests()
    print("PASS: 091 — Partition Into Equal-Sum Subsets")
