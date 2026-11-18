# Your practice file — 098. Largest Rectangle in a Histogram
"""
098. Largest Rectangle in a Histogram
Difficulty: Hard | Pattern: Monotonic increasing stack of unresolved boundaries
Prerequisites: 054 Daily Temperatures; monotonic stacks; interval widths.

TASK
Each nonnegative integer in heights is the height of a unit-width
histogram bar. Return the largest rectangle area entirely covered by adjacent
bars. A rectangle may span any contiguous interval and its height cannot exceed
that interval's shortest bar. Empty input returns zero. Leave heights unchanged.

EXAMPLES
heights=[2,1,5,6,2,3] -> 10 (height 5 across bars 5 and 6).
heights=[2,2,2] -> 6.
heights=[] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(heights) <= 100_000; 0 <= height <= 10_000.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. For a chosen bar height, extend left and right until a shorter bar blocks it.
2. An increasing stack keeps bars whose right boundary has not appeared yet.
3. When a shorter bar arrives, pop taller bars and compute their full possible width. A final zero flushes the stack.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(heights: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([4]) == 4
    assert solve([0, 0]) == 0
    assert solve([2, 2, 2]) == 6
    assert solve([2, 1, 5, 6, 2, 3]) == 10
    assert solve([1, 2, 3, 4]) == 6
    assert solve([4, 3, 2, 1]) == 6
    assert solve([2, 0, 2]) == 2
    from itertools import product
    for n in range(7):
        for values in product(range(3), repeat=n):
            expected = max((min(values[left:right]) * (right - left)
                            for left in range(n) for right in range(left + 1, n + 1)),
                           default=0)
            assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 098 — Largest Rectangle in a Histogram")
