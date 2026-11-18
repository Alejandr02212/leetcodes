# Explained reference solution — 099. Sliding Window Maximum
"""
099. Sliding Window Maximum
Difficulty: Hard | Pattern: Monotonic deque of still-useful candidates
Prerequisites: Fixed windows; queues/deques; monotonic stack reasoning.

TASK
Return the maximum in each contiguous window of exactly k elements in
nums, in left-to-right order. The output length is len(nums)-k+1. Do not modify
nums. Raise ValueError if k<1 or k>len(nums), including every k for an empty list.
Target linear time rather than rescanning or sorting every window.

EXAMPLES
nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7].
nums=[4,4,2], k=2 -> [4,4].
nums=[3,-2], k=1 -> [3,-2].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100_000; k is an integer; values are integers. Invalid k must raise ValueError.

SOLUTION EXPLANATION
An older candidate whose value is no greater than a newer value can
never become a future maximum while both matter: the newer value is at least
as good and expires later. Remove such dominated candidates from the back.
Expired indices leave from the front. The remaining indices increase while
their values decrease, so the front always contains the largest undominated
value in the current window. Every discarded value is either expired or
covered by a newer candidate, preserving the true maximum. Emit an answer only
after k values have arrived. Although there are nested while loops, each index
enters once and leaves at most once, giving linear total work. This is the
monotonic DEQUE template, distinct from a stack because both ends are used.

COMPLEXITY
For n=len(nums), O(n) time, O(k) auxiliary deque space, and O(n-k+1) output space for valid k. Invalid k is rejected in O(1).

COMMON MISTAKES
Storing only values makes expiration ambiguous. Remove index <= current-k. Emit no result for incomplete windows. A heap with lazy deletion needs additional care and can retain stale entries.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> list[int]:
    from collections import deque
    if not 1 <= k <= len(nums):
        raise ValueError('k must satisfy 1 <= k <= len(nums)')
    candidates = deque()
    result = []
    for index, value in enumerate(nums):
        while candidates and candidates[0] <= index - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= k - 1:
            result.append(nums[candidates[0]])
    return result


def run_tests() -> None:
    assert solve([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solve([4, 4, 2], 2) == [4, 4]
    assert solve([3, -2], 1) == [3, -2]
    assert solve([3, -2], 2) == [3]
    assert solve([-5, -2, -7], 2) == [-2, -2]
    assert solve([9], 1) == [9]
    for values, k in (([], 1), ([1], 0), ([1], 2), ([1], -1)):
        try:
            solve(values, k)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid window size must raise ValueError')
    from itertools import product
    for n in range(1, 6):
        for values in product(range(3), repeat=n):
            for k in range(1, n + 1):
                expected = [max(values[i:i + k]) for i in range(n - k + 1)]
                assert solve(list(values), k) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 099 — Sliding Window Maximum")
