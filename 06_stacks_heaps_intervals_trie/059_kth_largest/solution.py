# Explained reference solution — 059. Kth Largest Element
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

SOLUTION EXPLANATION
Maintain a heap containing the largest min(k, processed_count) values of
the processed prefix. Pushing the next value creates the candidate set; if
it is too large, removing its smallest member leaves exactly the best k.
This proves the invariant by induction. At completion, the smallest of the
k largest values is precisely the kth largest. A min-heap is useful even
though the question asks for a largest value: it exposes the retained
candidate that should be discarded first.

This pattern supports streams as well: retain a bounded candidate set rather
than sorting or storing the entire history.

COMPLEXITY
Time O(n log(k+1)), auxiliary space O(k), returned output O(1), where n = len(nums).

COMMON MISTAKES
Duplicates count; do not turn nums into a set. Heap entries are not fully sorted. A min-heap of size k exposes the kth largest at index 0.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

from heapq import heappush, heappop


def solve(nums: list[int], k: int) -> int:
    heap = []
    for value in nums:
        heappush(heap, value)
        if len(heap) > k:
            heappop(heap)
    return heap[0]


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
