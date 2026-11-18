# Explained reference solution — 082. Generate All Permutations
"""
082. Generate All Permutations
Difficulty: Medium | Pattern: Backtracking with used positions
Prerequisites: 081 Subsets; recursive search state; factorial growth.

TASK
Return every ordering of the distinct integers in nums. Each ordering
must use every input integer exactly once. The order of the returned permutations
does not matter. Leave nums unchanged. The empty list has one permutation: [].

EXAMPLES
nums=[1,2] -> [[1,2],[2,1]].
nums=[] -> [[]].
nums=[7] -> [[7]].

CONSTRAINTS AND CONTRACT
0 <= len(nums) <= 8. Values are distinct integers.

SOLUTION EXPLANATION
The path is a valid partial permutation and used marks exactly the
indices it already contains. Try every unused index as the next choice, recurse,
and restore both pieces of state. This includes every valid next element, so
inductively every complete permutation is reached. Distinct choices at the first
position where two paths differ ensure different outputs; no permutation is
repeated. At length n, all input positions have been used exactly once, so save
a copy. Notice how this differs from subsets: each depth selects ANY unused
index instead of deciding only about a fixed next index. Recursion is safe under
the small n<=8 limit; factorial output is the real constraint.

COMPLEXITY
For n>=1: O(n*n!) time and output storage; O(n) auxiliary path/used/recursion space. The n=0 case takes constant time and returns [[]].

COMMON MISTAKES
A set of chosen values works only with distinct inputs. Not clearing used loses branches. Results must be copies of path.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    result = []
    path = []
    used = [False] * len(nums)
    def visit():
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for index, value in enumerate(nums):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            visit()
            path.pop()
            used[index] = False
    visit()
    return result


def run_tests() -> None:
    from itertools import permutations
    assert solve([]) == [[]]
    assert solve([7]) == [[7]]
    assert {tuple(x) for x in solve([1, 2])} == {(1, 2), (2, 1)}
    assert len(solve([1, 2, 3])) == 6
    for values in ([0, -4, 2], [8, 3, 5, 1]):
        result = solve(list(values))
        assert {tuple(x) for x in result} == set(permutations(values))
        assert len(result) == len(set(tuple(x) for x in result))
    values = [2, 9]
    result = solve(values)
    assert values == [2, 9]
    result[0].append(100)
    assert all(100 not in item for item in result[1:])


if __name__ == "__main__":
    run_tests()
    print("PASS: 082 — Generate All Permutations")
