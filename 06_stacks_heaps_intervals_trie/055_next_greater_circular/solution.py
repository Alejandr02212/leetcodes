# Explained reference solution — 055. Next Greater Element in a Circular Array
"""
055. Next Greater Element in a Circular Array
Difficulty: Medium | Pattern: Monotonic stack plus virtual circular traversal
Prerequisites: Problem 054 monotonic stacks; modulo indexing

TASK
For each value, return the first strictly greater value encountered while
walking forward circularly through at most the other n-1 positions. Return
-1 if none exists. The result contains values, not indices or distances.
The input is unchanged.

EXAMPLES
solve([1, 2, 1]) -> [2, -1, 2]: the last 1 wraps to the 2.
solve([3, 2, 1]) -> [-1, 3, 3].
solve([]) -> [].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100000. Values are arbitrary integers; -1 may be a real next-greater value as well as the required missing-value sentinel.

SOLUTION EXPLANATION
Imagine two copies of the array placed side by side. Every original
position can see all later positions and then all earlier positions within
that doubled traversal. Keep unresolved original indices in a nonincreasing
stack of values. A greater value resolves the top immediately, so the first
one encountered is its circular next-greater value. An index cannot be
incorrectly resolved by itself because the comparison is strict. If it has
no greater value in a whole cycle, it remains unresolved with -1.

Only first-pass indices are pushed. That bounds total pushes and pops by n
and avoids recording duplicate work in the second pass.

COMPLEXITY
Time O(n), auxiliary space O(n), output O(n), for n = len(nums).

COMMON MISTAKES
Push only during the first pass. Greater means strict >, so equal values do not resolve each other. Return values here; Daily Temperatures returned distances.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [-1] * n
    waiting = []
    for step in range(2 * n):
        index = step % n
        while waiting and nums[waiting[-1]] < nums[index]:
            answer[waiting.pop()] = nums[index]
        if step < n:
            waiting.append(index)
    return answer


def run_tests() -> None:
    assert solve([]) == []
    assert solve([9]) == [-1]
    assert solve([1, 2, 1]) == [2, -1, 2]
    assert solve([3, 2, 1]) == [-1, 3, 3]
    assert solve([2, 2, 2]) == [-1, -1, -1]
    assert solve([-3, -2, -1]) == [-2, -1, -1]
    from itertools import product
    for values in product(range(3), repeat=5):
        expected = [next((values[(i+d) % len(values)] for d in range(1, len(values)) if values[(i+d) % len(values)] > values[i]), -1) for i in range(len(values))]
        assert solve(list(values)) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 055 — Next Greater Element in a Circular Array")
