# Your practice file — 049. Minimum Banana Eating Speed
"""
049. Minimum Banana Eating Speed
Difficulty: Medium | Pattern: Binary search on minimum feasible answer
Prerequisites: Integer Square Root (044); lower bound (042).

TASK
Each positive pile size is a number of bananas. At integer speed k, one
hour is spent on one pile and removes up to k bananas from it; leftover time
in that hour cannot be used on another pile. Return the minimum positive k
that finishes all piles within h hours. Do not change piles.

EXAMPLES
solve([3, 6, 7, 11], 8) -> 4: required hours are 1+2+2+3 = 8.
solve([30, 11, 23, 4, 20], 5) -> 30.

CONSTRAINTS AND CONTRACT
1 <= len(piles) <= 100000; every pile > 0; h >= len(piles), so a feasible speed exists.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. At speed k a pile needs ceil(pile/k) hours.
2. Total required hours never increases when speed increases.
3. Binary-search speeds 1 through max(piles) for the first feasible one.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(piles: list[int], h: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([3, 6, 7, 11], 8) == 4
    assert solve([30, 11, 23, 4, 20], 5) == 30
    assert solve([30, 11, 23, 4, 20], 6) == 23
    assert solve([1], 1) == 1
    assert solve([9], 4) == 3
    assert solve([2, 2], 100) == 1
    assert solve([10**9], 2) == 500000000
    from itertools import product
    for size in range(1, 5):
        for piles in product((1, 2, 5), repeat=size):
            for h in range(size, size + 4):
                expected = next(k for k in range(1, max(piles) + 1)
                                if sum((p + k - 1) // k for p in piles) <= h)
                assert solve(list(piles), h) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 049 — Minimum Banana Eating Speed")
