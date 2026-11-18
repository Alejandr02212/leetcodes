# Explained reference solution — 087. Minimum Coin Change
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

SOLUTION EXPLANATION
Any nonempty solution for total x ends with some available coin c.
Removing it leaves a solution for x-c; using an optimal such solution minimizes
the number of coins for that choice of c. Taking the minimum over all possible
last coins covers every solution. Positive denominations ensure x-c<x, so the
ascending total loop has already solved every dependency. dp[0]=0 starts the
construction. The sentinel amount+1 exceeds any possible valid coin count,
because every coin is at least one; an unreachable state therefore stays
recognizable. Unlike a greedy largest-coin choice, this transition works for
arbitrary denominations.

COMPLEXITY
Let A=amount and C=len(coins). O(A*C+A+1) time and O(A+1) auxiliary space, including empty coin lists and amount zero.

COMMON MISTAKES
Greedy is not valid for arbitrary coin sets. dp initialized to zero would treat impossible sums as free. This task counts coins, not combinations.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(coins: list[int], amount: int) -> int:
    unreachable = amount + 1
    dp = [0] + [unreachable] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] == unreachable else dp[amount]


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
