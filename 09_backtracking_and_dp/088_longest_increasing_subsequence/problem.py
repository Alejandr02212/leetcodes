# Your practice file — 088. Longest Increasing Subsequence
"""
088. Longest Increasing Subsequence
Difficulty: Medium | Pattern: Binary search on optimal tail values
Prerequisites: Search insert position; DP dominance; subsequence versus substring.

TASK
Return the length of the longest STRICTLY increasing subsequence of nums.
A subsequence preserves relative order but may skip elements. Equal consecutive
values do not extend an increasing subsequence. Return 0 for an empty list.
Do not modify nums. Aim for O(n log n) time after first considering O(n^2) DP.

EXAMPLES
nums=[10,9,2,5,3,7,101,18] -> 4, for example [2,3,7,18].
nums=[2,2,2] -> 1.
nums=[] -> 0.

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 100_000; values are integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Smaller ending values make a subsequence easier to extend later.
2. tails[length-1] stores the smallest known ending value for that length.
3. Replace the first tail >= value, using bisect_left; append if none exists.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([4]) == 1
    assert solve([2, 2, 2]) == 1
    assert solve([5, 4, 3, 2]) == 1
    assert solve([1, 2, 3, 4]) == 4
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solve([-2, -1, -1, 0]) == 3
    from itertools import product
    for n in range(6):
        for values in product(range(3), repeat=n):
            dp = [1] * n
            for i in range(n):
                for j in range(i):
                    if values[j] < values[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            assert solve(list(values)) == max(dp, default=0)


if __name__ == "__main__":
    run_tests()
    print("PASS: 088 — Longest Increasing Subsequence")
