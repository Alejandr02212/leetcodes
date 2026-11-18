# Explained reference solution — 049. Minimum Banana Eating Speed
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

SOLUTION EXPLANATION
For a proposed speed, integer ceiling division computes the hours required
by each pile. Their sum is an exact feasibility check because each pile
consumes its own hours. Increasing speed can only decrease these ceilings,
so feasibility changes once from False to True. Speed max(piles) is feasible
because every pile then takes one hour and h is at least the pile count.
Binary search maintains the minimum feasible speed inside [left, right]:
keep speed if feasible, or discard all speeds through it if infeasible.
The final single candidate is therefore the minimum feasible speed.

COMPLEXITY
Time O(n log(M+1)), auxiliary space O(1), where n = len(piles), M = max(piles); ceiling arithmetic uses integers.

COMMON MISTAKES
ceil(sum(piles)/k) is wrong: hours cannot be shared between piles. Avoid floating-point ceiling division.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    while left < right:
        speed = (left + right) // 2
        hours = sum((pile + speed - 1) // speed for pile in piles)
        if hours <= h:
            right = speed
        else:
            left = speed + 1
    return left


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
