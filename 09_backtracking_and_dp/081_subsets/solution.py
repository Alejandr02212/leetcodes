# Explained reference solution — 081. Generate All Subsets
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

SOLUTION EXPLANATION
A recursion state means: choices for indices before index are fixed in
path; all later positions remain undecided. Branching into exclude and include
covers the two possible decisions for the current position. These branches are
disjoint, so no subset appears twice. When index reaches n, every input position
has exactly one decision and path is a complete subset. Copy it because the
shared path will be changed while exploring siblings. The final pop restores
precisely the state the caller supplied. This choose/explore/undo discipline is
the basic backtracking template reused by permutations, combinations, and board
search. Recursion depth is n, bounded here by 12.

COMPLEXITY
For n elements: O(n*2^n) time and output storage, because copying all subsets writes n*2^(n-1) elements for n>0. Auxiliary recursion/path space O(n).

COMMON MISTAKES
Appending the same path object aliases every result. Forgetting pop contaminates sibling branches. [] is an input; its only subset is [].

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    result = []
    path = []
    def visit(index):
        if index == len(nums):
            result.append(path.copy())
            return
        visit(index + 1)
        path.append(nums[index])
        visit(index + 1)
        path.pop()
    visit(0)
    return result


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
