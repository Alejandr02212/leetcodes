# Your practice file — 050. Ship Packages Within D Days
"""
050. Ship Packages Within D Days
Difficulty: Medium | Pattern: Binary search on answer + greedy feasibility
Prerequisites: Minimum feasible answer (049); greedy scans.

TASK
Packages must be shipped in the given order, each package entirely on one
day. Each day can carry a prefix of the remaining packages with total weight
at most a fixed capacity. Return the minimum integer capacity needed to
finish within days days. Do not reorder or change weights.

EXAMPLES
solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) -> 15.
solve([3, 2, 2, 4, 1, 4], 3) -> 6: [3,2], [2,4], [1,4].

CONSTRAINTS AND CONTRACT
1 <= len(weights) <= 100000; all weights are positive integers; days >= 1. Unused days are allowed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Capacity lies between the heaviest package and the total weight.
2. For a capacity, greedily pack each day until the next package would overflow.
3. The required day count cannot increase as capacity grows; find the first feasible capacity.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(weights: list[int], days: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert solve([3, 2, 2, 4, 1, 4], 3) == 6
    assert solve([1, 2, 3, 1, 1], 4) == 3
    assert solve([7], 1) == 7
    assert solve([2, 3, 4], 1) == 9
    assert solve([2, 3, 4], 100) == 4
    assert solve([5, 5, 5], 3) == 5
    from itertools import combinations, product
    for size in range(1, 6):
        for weights in product((1, 3), repeat=size):
            for days in range(1, size + 2):
                # Independent oracle: enumerate every contiguous partition.
                best = sum(weights)
                for cuts_count in range(min(days, size)):
                    for cuts in combinations(range(1, size), cuts_count):
                        boundaries = (0,) + cuts + (size,)
                        capacity = max(sum(weights[a:b])
                                       for a, b in zip(boundaries, boundaries[1:]))
                        best = min(best, capacity)
                assert solve(list(weights), days) == best


if __name__ == "__main__":
    run_tests()
    print("PASS: 050 — Ship Packages Within D Days")
