# Your practice file — 083. Combination Sum
"""
083. Combination Sum
Difficulty: Medium | Pattern: Backtracking with a start index and pruning
Prerequisites: 081 Subsets; recursion; combination versus permutation.

TASK
Given distinct positive candidate integers and a nonnegative target,
return all unique combinations whose sum is target. A candidate may be reused
any number of times. Return each combination in nondecreasing order; the outer
order does not matter. Different orders of the same values are one combination.
Do not mutate candidates. When target=0, return [[]].

EXAMPLES
candidates=[2,3,6,7], target=7 -> [[2,2,3],[7]].
candidates=[4,6], target=5 -> [].
candidates=[], target=0 -> [[]].

CONSTRAINTS AND CONTRACT
0 <= len(candidates) <= 10; distinct integers in 1..30; 0 <= target <= 30. These bounds keep recursion depth <=30.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Sort a copy so each combination can be built in one canonical order.
2. Pass a start index; choosing index i permits i again but forbids earlier indices.
3. If the next candidate exceeds the remainder, later candidates do too.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(candidates: list[int], target: int) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    def normalized(items):
        return {tuple(item) for item in items}
    assert normalized(solve([2, 3, 6, 7], 7)) == {(2, 2, 3), (7,)}
    assert solve([4, 6], 5) == []
    assert solve([], 0) == [[]]
    assert solve([], 3) == []
    assert solve([3], 9) == [[3, 3, 3]]
    assert normalized(solve([2, 3, 5], 8)) == {(2, 2, 2, 2), (2, 3, 3), (3, 5)}
    assert solve([9], 4) == []
    values = [7, 2, 3]
    result = solve(values, 7)
    assert values == [7, 2, 3]
    assert len(result) == len(normalized(result))
    assert all(item == sorted(item) for item in result)


if __name__ == "__main__":
    run_tests()
    print("PASS: 083 — Combination Sum")
