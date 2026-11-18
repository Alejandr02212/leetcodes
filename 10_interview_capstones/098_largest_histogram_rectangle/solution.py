# Explained reference solution — 098. Largest Rectangle in a Histogram
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

SOLUTION EXPLANATION
Store increasing heights together with the earliest index where each
height can start. When a lower height arrives at index i, every taller stack
height has found its first shorter bar to the right. Its maximal rectangle ends
at i-1, and its stored start provides the left boundary, giving width i-start.
After popping, the current shorter height inherits the earliest popped start
because it can span all those taller bars too. Equal heights keep only the
older, earlier-start entry. A virtual zero at the end settles all positive
remaining heights without modifying the input. Any optimal rectangle has a
minimum-height bar; that height's maximal span is considered when it is popped,
so at least one considered rectangle achieves the optimum.

COMPLEXITY
For n bars, O(n) time: each stack entry is pushed and popped at most once. O(n) auxiliary stack space.

COMMON MISTAKES
Width is index-start, not index-start+1, because the current shorter bar is excluded. Carry the earliest popped start forward. Do not forget to flush the stack after the last real bar.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(heights: list[int]) -> int:
    stack = []  # (earliest_start, height), with strictly increasing heights
    best = 0
    for index in range(len(heights) + 1):
        height = heights[index] if index < len(heights) else 0
        start = index
        while stack and stack[-1][1] > height:
            earlier_start, earlier_height = stack.pop()
            best = max(best, earlier_height * (index - earlier_start))
            start = earlier_start
        if not stack or stack[-1][1] < height:
            stack.append((start, height))
    return best


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
