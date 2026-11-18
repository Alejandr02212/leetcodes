# Your practice file — 048. Find a Peak Element
"""
048. Find a Peak Element
Difficulty: Medium | Pattern: Binary search on a slope
Prerequisites: Boundary-preserving binary search (047).

TASK
Return an index i whose value is strictly greater than its immediate
neighbors. Treat values beyond either end as negative infinity. Adjacent
input values are never equal. Any peak index is accepted; use O(log n) time.

EXAMPLES
solve([1, 2, 3, 1]) -> 2.
solve([1, 2, 1, 3, 5, 6, 4]) -> 1 or 5.

CONSTRAINTS AND CONTRACT
1 <= len(nums) <= 1000000; integers; nums[i] != nums[i+1]. Nonadjacent values may repeat.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare nums[mid] and nums[mid+1].
2. An uphill slope guarantees a peak somewhere to the right.
3. A downhill slope guarantees a peak at mid or to the left.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    def check(nums):
        index = solve(nums)
        assert 0 <= index < len(nums)
        assert index == 0 or nums[index] > nums[index - 1]
        assert index == len(nums) - 1 or nums[index] > nums[index + 1]
    check([1, 2, 3, 1])
    check([1, 2, 1, 3, 5, 6, 4])
    check([8])
    check([1, 2])
    check([2, 1])
    check([1, 3, 2, 4, 1])
    check([-4, -3, -2])
    from itertools import product
    for size in range(1, 7):
        for values in product((0, 1, 2), repeat=size):
            if all(values[i] != values[i + 1] for i in range(size - 1)):
                check(list(values))


if __name__ == "__main__":
    run_tests()
    print("PASS: 048 — Find a Peak Element")
