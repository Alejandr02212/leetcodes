# Your practice file — 087. Minimum Coin Change
"""
087. Minimum Coin Change
Difficulty: Medium | Pattern: Unbounded knapsack: minimum-cost one-dimensional DP
Prerequisites: DP state/transition/base cases; infinity as an impossible sentinel.

TASK
Given positive integer coin denominations and a nonnegative amount,
return the fewest coins needed to form amount exactly. Each denomination may
be used unlimited times. Return -1 if impossible. Repeated denominations are
allowed and do not affect the answer. Do not modify coins.

EXAMPLES
coins=[1,3,4], amount=6 -> 2 (3+3, better than greedy 4+1+1).
coins=[2], amount=3 -> -1.
coins=[], amount=0 -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(coins) <= 100; 1 <= denomination <= 10_000; 0 <= amount <= 10_000.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Let dp[x] be the fewest coins that total exactly x.
2. The last coin c leaves the subproblem x-c, so try dp[x-c]+1.
3. Start dp[0]=0; keep unreachable states at amount+1.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(coins: list[int], amount: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 3, 4], 6) == 2
    assert solve([2], 3) == -1
    assert solve([], 0) == 0
    assert solve([], 7) == -1
    assert solve([5], 10) == 2
    assert solve([2, 2, 3], 7) == 3
    assert solve([9, 6, 5, 1], 11) == 2
    assert solve([8, 10], 6) == -1
    assert solve([1], 99) == 99


if __name__ == "__main__":
    run_tests()
    print("PASS: 087 — Minimum Coin Change")
