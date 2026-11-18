# Your practice file — 081. Generate All Subsets
"""
081. Generate All Subsets
Difficulty: Medium | Pattern: Backtracking: choose, explore, undo
Prerequisites: Functions; recursion; copying lists; binary choices.

TASK
Given distinct integers nums, return every subset, including the empty
subset and the full set. Each input element may be chosen once. The order of
subsets does not matter, but preserve input order within each subset. Do not
modify nums. A subset is a choice of positions, not a contiguous slice.

EXAMPLES
nums=[2,5] -> [[],[2],[5],[2,5]] in any outer order.
nums=[] -> [[]].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 12. Integers are distinct.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. At each index, either exclude that element or include it.
2. Keep one mutable path and undo appends after recursive exploration.
3. At a leaf, append path.copy(), not path itself.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    def normalized(items):
        return {tuple(item) for item in items}
    assert solve([]) == [[]]
    assert normalized(solve([9])) == {(), (9,)}
    assert normalized(solve([2, 5])) == {(), (2,), (5,), (2, 5)}
    assert normalized(solve([-1, 0])) == {(), (-1,), (0,), (-1, 0)}
    assert len(solve([4, 1, 8])) == 8
    values = [3, 7, -2, 5]
    expected = {tuple(values[i] for i in range(len(values)) if mask & (1 << i))
                for mask in range(1 << len(values))}
    result = solve(values)
    assert normalized(result) == expected and len(result) == 16
    assert values == [3, 7, -2, 5]
    result[0].append(999)
    assert all(999 not in item for item in result[1:])


if __name__ == "__main__":
    run_tests()
    print("PASS: 081 — Generate All Subsets")
