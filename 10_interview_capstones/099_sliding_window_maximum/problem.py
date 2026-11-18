# Your practice file — 099. Sliding Window Maximum
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Store candidate INDICES so you can remove values that leave the window.
2. A newer value >= an older candidate makes that older candidate permanently useless.
3. Keep indices increasing and their values decreasing; the front is the current maximum.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int], k: int) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
