# Explained reference solution — 050. Ship Packages Within D Days
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

SOLUTION EXPLANATION
For a fixed capacity, greedily ship the longest fitting prefix each day.
After any number of days this greedy schedule has shipped at least as many
packages as any other valid schedule: assuming the claim for yesterday,
another schedule starts no farther ahead today, so it cannot finish farther
ahead than the greedy longest fitting prefix. Thus greedy minimizes the
required day count and gives an exact feasibility test. Larger capacities
can reuse any smaller-capacity schedule, so feasibility is monotone. The
heaviest package is a necessary lower bound; the total weight is a feasible
upper bound. Lower-bound binary search returns the first feasible capacity.

COMPLEXITY
Time O(n log(S-M+2)), auxiliary space O(1), where n = len(weights), S = sum(weights), M = max(weights).

COMMON MISTAKES
The lower bound must fit every individual package. Packages cannot be sorted. Exactly filling capacity does not require starting a new day until another package arrives.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(weights: list[int], days: int) -> int:
    def feasible(capacity: int) -> bool:
        used_days = 1
        load = 0
        for weight in weights:
            if load + weight > capacity:
                used_days += 1
                load = 0
            load += weight
        return used_days <= days

    left, right = max(weights), sum(weights)
    while left < right:
        capacity = (left + right) // 2
        if feasible(capacity):
            right = capacity
        else:
            left = capacity + 1
    return left


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
