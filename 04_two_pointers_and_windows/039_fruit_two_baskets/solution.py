# Explained reference solution — 039. Fruit Into Two Baskets
"""
039. Fruit Into Two Baskets
Difficulty: Medium | Pattern: Variable window with at most K distinct values
Prerequisites: Frequency maps; variable windows (029, 038).

TASK
Each integer in fruits identifies a fruit type at that position. Choose
one contiguous segment containing at most two distinct types, and return
its maximum possible length. Do not change fruits.

EXAMPLES
solve([1, 2, 1]) -> 3.
solve([0, 1, 2, 2]) -> 3: choose [1, 2, 2].

CONSTRAINTS AND CONTRACT
0 <= len(fruits) <= 100000; type identifiers are arbitrary integers.

SOLUTION EXPLANATION
The map counts exactly the types currently between left and right.
After extension, shrink until at most two counts remain positive. For a
fixed start, adding future positions cannot reduce the number of distinct
types, so any discarded start stays invalid. This makes the retained window
the longest valid window ending at the current right endpoint. Taking the
largest such length solves the problem. This generalizes directly to at
most K distinct values by replacing the budget 2 with K.

COMPLEXITY
Expected time O(n), auxiliary space O(1) here: the map holds at most 3 types before shrinking; n = len(fruits).

COMMON MISTAKES
Leaving zero-count keys makes len(counts) incorrect. You must choose a contiguous segment, not all occurrences of two favorite types.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(fruits: list[int]) -> int:
    counts = {}
    left = 0
    best = 0
    for right, fruit in enumerate(fruits):
        counts[fruit] = counts.get(fruit, 0) + 1
        while len(counts) > 2:
            outgoing = fruits[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        best = max(best, right - left + 1)
    return best


def run_tests() -> None:
    assert solve([1, 2, 1]) == 3
    assert solve([0, 1, 2, 2]) == 3
    assert solve([]) == 0
    assert solve([9]) == 1
    assert solve([3, 3, 3, 3]) == 4
    assert solve([1, 2, 3, 2, 2]) == 4
    assert solve([1, 2, 3, 4, 5]) == 2
    assert solve([-1, -2, -1, -3, -3]) == 3


if __name__ == "__main__":
    run_tests()
    print("PASS: 039 — Fruit Into Two Baskets")
