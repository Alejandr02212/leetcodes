# Your practice file — 055. Next Greater Element in a Circular Array
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Traverse the array twice to expose possible wrapped answers.
2. Use the same unresolved-index stack as Daily Temperatures.
3. Push indices only on the first pass, and use modulo to read values on both passes.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
