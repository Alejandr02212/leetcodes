# Explained reference solution — 083. Combination Sum
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

SOLUTION EXPLANATION
Without a start index, choices [2,3] and [3,2] would be produced as
different search paths. Sorting and permitting only nondecreasing indices gives
every combination exactly one path. Recursing with index rather than index+1
allows unlimited reuse. All candidates are positive, so remaining strictly
decreases; reaching zero proves the chosen values form a valid combination.
For any valid combination in sorted order, its next value is allowed by start
and does not exceed remaining, so that combination cannot be pruned away.
Undo the append after exploring each choice. Positivity is essential: zero would
prevent progress, and negative values invalidate the stopping rule.

COMPLEXITY
Let c be candidate count, T the target, and d=floor(T/min(candidates)) for nonempty input. A conservative bound is O(c log c + (c+1)^(d+1) + L) time, with L output integers; O(c+d+1) auxiliary space plus O(L+Z) output for Z combinations. Empty candidates take constant work.

COMMON MISTAKES
Advancing to index+1 accidentally forbids reuse. Starting from zero on every call repeats combinations. Sort a copy to preserve the input.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(candidates: list[int], target: int) -> list[list[int]]:
    values = sorted(candidates)
    result = []
    path = []
    def visit(start, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for index in range(start, len(values)):
            value = values[index]
            if value > remaining:
                break
            path.append(value)
            visit(index, remaining - value)
            path.pop()
    visit(0, target)
    return result


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
