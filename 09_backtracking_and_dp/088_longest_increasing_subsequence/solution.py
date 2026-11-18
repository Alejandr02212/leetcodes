# Explained reference solution — 088. Longest Increasing Subsequence
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

SOLUTION EXPLANATION
An O(n^2) starting point stores the best increasing length ending at each
index. We compress that information differently: tails[k] is the smallest last
value achievable by a length-(k+1) increasing subsequence in the processed
prefix. Smaller is always at least as useful for future extensions. tails is
strictly increasing. For a new value x, binary search its first tail >=x. The
preceding tail, if any, is smaller than x, so x can end a subsequence of this
length. Replacing the found tail improves that length without changing other
possible lengths; appending establishes one new longer length. The number of
tails is therefore the optimum length. tails itself need not be a subsequence
of the original array; it summarizes different candidate subsequences.

COMPLEXITY
For n elements and LIS length L, O(n log(L+1)) time and O(L) auxiliary space, bounded by O(n log n) and O(n).

COMMON MISTAKES
bisect_right would compute a nondecreasing variant. Sorting the input loses order. Return len(tails), not tails as an alleged actual subsequence.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    from bisect import bisect_left
    tails = []
    for value in nums:
        index = bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    return len(tails)


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
