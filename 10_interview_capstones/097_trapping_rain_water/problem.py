# Your practice file — 097. Trapping Rain Water
"""
097. Trapping Rain Water
Difficulty: Hard | Pattern: Two pointers with certified boundary maxima
Prerequisites: 033 Container With Most Water; prefix/suffix maxima; two-pointer proof.

TASK
heights describes unit-width bars placed next to each other. Return the
total number of unit squares of water that would remain trapped after rain.
Water cannot be retained beyond the outer boundaries. Heights are nonnegative
integers. An empty list or fewer than three bars traps zero. Do not modify it.

EXAMPLES
heights=[0,1,0,2,1,0,1,3,2,1,2,1] -> 6.
heights=[3,0,3] -> 3.
heights=[1,2,3] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(heights) <= 100_000; 0 <= height <= 10_000.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Water over i equals min(max_left[i], max_right[i])-heights[i].
2. A prefix/suffix-array solution uses O(n) memory and is a useful first version.
3. With two pointers, finalize the side whose known maximum is smaller: the opposite boundary is already high enough.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(heights: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([4]) == 0
    assert solve([1, 2]) == 0
    assert solve([3, 0, 3]) == 3
    assert solve([1, 2, 3]) == 0
    assert solve([3, 2, 1]) == 0
    assert solve([2, 0, 2, 0, 2]) == 4
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    from itertools import product
    for n in range(7):
        for values in product(range(3), repeat=n):
            expected = sum(min(max(values[:i + 1]), max(values[i:])) - value
                           for i, value in enumerate(values))
            assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 097 — Trapping Rain Water")
