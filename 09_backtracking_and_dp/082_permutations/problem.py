# Your practice file — 082. Generate All Permutations
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A permutation makes a choice of an unused element for its next position.
2. Track used input positions separately from path.
3. After recursion, undo both the used flag and the path append.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(nums: list[int]) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
