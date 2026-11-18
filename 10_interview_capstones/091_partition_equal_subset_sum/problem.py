# Your practice file — 091. Partition Into Equal-Sum Subsets
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Equal parts require an even total; one part must sum to total//2.
2. reachable[s] records whether a subset of processed positions totals s.
3. Update sums downward, so the current value cannot be reused in the same pass.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
