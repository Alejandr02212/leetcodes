# Your practice file — 059. Kth Largest Element
"""
059. Kth Largest Element
Difficulty: Medium | Pattern: Bounded min-heap: retain the best k candidates
Prerequisites: Lists, sorting, and the heapq standard library

TASK
Return the kth largest element of nums, counting duplicates as separate
elements. For example, the second largest of [5, 5, 2] is 5. Use a heap of at
most k elements and leave nums unchanged.

EXAMPLES
solve([3, 2, 1, 5, 6, 4], 2) -> 5.
solve([5, 5, 2], 2) -> 5.
solve([-4, -1, -7], 3) -> -7.

CONSTRAINTS AND CONTRACT
1 <= k <= len(nums) <= 100000. Values are arbitrary integers. The valid-k precondition is guaranteed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep only the k largest values seen so far.
2. A min-heap makes the weakest of those candidates easy to remove.
3. Push every value and pop the minimum whenever the heap size exceeds k; its final root is the answer.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

from heapq import heappush, heappop


def solve(nums: list[int], k: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([3, 2, 1, 5, 6, 4], 2) == 5
    assert solve([5, 5, 2], 2) == 5
    assert solve([-4, -1, -7], 3) == -7
    assert solve([8], 1) == 8
    assert solve([4, 1, 4, 2], 1) == 4
    assert solve([4, 1, 4, 2], 4) == 1
    data = [9, 1, 7]
    assert solve(data, 2) == 7 and data == [9, 1, 7]
    from itertools import product
    for values in product(range(-1, 2), repeat=5):
        for k in range(1, 6):
            assert solve(list(values), k) == sorted(values, reverse=True)[k-1]


if __name__ == "__main__":
    run_tests()
    print("PASS: 059 — Kth Largest Element")
