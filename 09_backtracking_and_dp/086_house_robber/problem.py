# Your practice file — 086. House Robber
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. At a house, either skip it or take it and exclude the previous house.
2. best(i)=max(best(i-1), best(i-2)+nums[i]).
3. Track the best totals for the previous two prefixes, initially both zero.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
