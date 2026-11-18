# Your practice file — 034. Three Sum
"""
034. Three Sum
Difficulty: Medium | Pattern: Sorting + fixed anchor + two pointers
Prerequisites: Two Sum in a Sorted Array (031).

TASK
Return all distinct value triplets [a, b, c] with a <= b <= c and a+b+c = 0,
using three different input indices. Return triplets in lexicographic order.
Duplicate input values may be used when enough occurrences exist. Do not change nums.

EXAMPLES
solve([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]].
solve([0, 0, 0, 0]) -> [[0, 0, 0]].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 3000; values are integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Sort a copy, then fix the smallest value of each candidate triplet.
2. Search the remaining suffix using two pointers.
3. Skip repeated anchors and repeated endpoint values after recording a match.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solve([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solve([]) == []
    assert solve([0, 0]) == []
    assert solve([1, 2, 3]) == []
    assert solve([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    assert solve([-2, -1, 0, 1, 2]) == [[-2, 0, 2], [-1, 0, 1]]
    from itertools import combinations, product
    for size in range(6):
        for values in product((-1, 0, 1), repeat=size):
            expected = sorted({tuple(sorted(triplet)) for triplet in combinations(values, 3)
                               if sum(triplet) == 0})
            original = list(values)
            assert solve(original) == [list(t) for t in expected]
            assert original == list(values)


if __name__ == "__main__":
    run_tests()
    print("PASS: 034 — Three Sum")
