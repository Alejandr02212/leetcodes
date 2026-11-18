# Explained reference solution — 024. Product Except Self
"""
024. Product Except Self
Difficulty: Medium | Pattern: Prefix and suffix accumulators
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return a list whose ith value is the product of all nums values except nums[i]. Do not use division. For a singleton, the empty product is 1; for an empty input, return [].

EXAMPLES
solve([1,2,3,4]) -> [24,12,8,6]
solve([0,2,3]) -> [6,0,0]

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 10000; -10 <= values <= 10. Assume fixed-width arithmetic for the usual interview complexity; Python supports larger integers. Do not mutate nums.

SOLUTION EXPLANATION
Everything except index i splits into the part before i and the part after i. In the forward pass prefix is the product strictly before the current index, and that is stored in result. In the backward pass suffix is the product strictly after the index; multiplying combines the two disjoint parts. Update accumulators after using them to exclude the current value. Zeros work without any special case.

COMPLEXITY
For n values: O(n) arithmetic operations and O(1) auxiliary variables beyond O(n) output, under unit-cost arithmetic. With Python arbitrary-precision integers, actual time and byte space also depend on product bit lengths.

COMMON MISTAKES
Division fails with zeros and violates the task. Multiplying the current number into prefix or suffix too early includes the excluded value.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    for index in range(len(nums)):
        result[index] = prefix
        prefix *= nums[index]
    suffix = 1
    for index in range(len(nums) - 1, -1, -1):
        result[index] *= suffix
        suffix *= nums[index]
    return result


def run_tests() -> None:
    assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solve([]) == []
    assert solve([8]) == [1]
    assert solve([0, 2, 3]) == [6, 0, 0]
    assert solve([0, 2, 0]) == [0, 0, 0]
    assert solve([-1, 2, -3]) == [-6, 3, -2]
    assert solve([2, 5]) == [5, 2]


if __name__ == "__main__":
    run_tests()
    print("PASS: 024 — Product Except Self")
