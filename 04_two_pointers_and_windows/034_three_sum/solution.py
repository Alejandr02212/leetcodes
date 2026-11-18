# Explained reference solution — 034. Three Sum
"""
034. Three Sum
Difficulty: Medium | Pattern: Sorting + fixed anchor + two pointers
Prerequisites: Two Sum in a Sorted Array (031).

TASK
Return all distinct value triplets [a, b, c] with a <= b <= c and a+b+c = 0,
using three different input indices. Return triplets in lexicographic order.
Duplicate input values may be used when enough occurrences exist. Do not change nums.

EXAMPLES
solve([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]].
solve([0, 0, 0, 0]) -> [[0, 0, 0]].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 3000; values are integers.

SOLUTION EXPLANATION
After sorting, every valid triplet has a smallest element at some anchor i.
For that anchor the remaining problem is two-sum on its suffix, with target
-values[i]. A sum too small safely discards left; a sum too large safely
discards right, just as in 031. Equal anchors would generate the same value
triplets, so only the first is processed. After a match, repeated left or
right values produce duplicates and can be skipped. Anchors increase, and
matching left values increase within each anchor, yielding lexicographic order.
Distinct indices follow from i < left < right.

COMPLEXITY
Time O(n^2), auxiliary space O(n) for the sorted copy and sorting workspace, plus O(t) output for t triplets.

COMMON MISTAKES
Deduplicate values, not all input occurrences: [-1, -1, 2] needs both -1 values. Sorting nums in place violates this contract.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    values = sorted(nums)
    answer = []
    for i in range(len(values) - 2):
        if i > 0 and values[i] == values[i - 1]:
            continue
        if values[i] > 0:
            break
        left, right = i + 1, len(values) - 1
        while left < right:
            total = values[i] + values[left] + values[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                answer.append([values[i], values[left], values[right]])
                left += 1
                right -= 1
                while left < right and values[left] == values[left - 1]:
                    left += 1
                while left < right and values[right] == values[right + 1]:
                    right -= 1
    return answer


def run_tests() -> None:
    assert solve([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solve([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solve([]) == []
    assert solve([0, 0]) == []
    assert solve([1, 2, 3]) == []
    assert solve([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    assert solve([-2, -1, 0, 1, 2]) == [[-2, 0, 2], [-1, 0, 1]]
    from itertools import combinations, product
    for size in range(6):
        for values in product((-1, 0, 1), repeat=size):
            expected = sorted({tuple(sorted(triplet)) for triplet in combinations(values, 3)
                               if sum(triplet) == 0})
            original = list(values)
            assert solve(original) == [list(t) for t in expected]
            assert original == list(values)


if __name__ == "__main__":
    run_tests()
    print("PASS: 034 — Three Sum")
