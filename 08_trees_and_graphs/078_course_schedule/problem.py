# Your practice file — 078. Can You Finish Every Course?
"""
078. Can You Finish Every Course?
Difficulty: Medium | Pattern: Topological sorting with indegrees (Kahn's algorithm)
Prerequisites: Queues; adjacency lists; directed graphs.

TASK
There are num_courses courses labeled 0 through num_courses-1.
Each pair [course, prerequisite] means you must take prerequisite before course.
Return whether an ordering exists that completes all courses. Courses without
prerequisites are available immediately. Duplicate pairs are allowed and do not
change the answer. A course requiring itself makes completion impossible.

EXAMPLES
num_courses=3, prerequisites=[[1,0],[2,1]] -> True (0,1,2).
num_courses=2, prerequisites=[[1,0],[0,1]] -> False.
num_courses=0, prerequisites=[] -> True.

CONSTRAINTS AND CONTRACT
0 <= num_courses <= 10_000. All labels are valid; at most 50_000 prerequisite pairs. No input mutation.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Think of prerequisites as arrows from an earlier course to a later one.
2. Track how many prerequisites remain for each course.
3. Repeatedly remove zero-indegree courses; a cycle leaves some courses unremoved.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(0, []) is True
    assert solve(1, []) is True
    assert solve(1, [[0, 0]]) is False
    assert solve(3, [[1, 0], [2, 1]]) is True
    assert solve(2, [[1, 0], [0, 1]]) is False
    assert solve(4, [[1, 0], [3, 2]]) is True
    assert solve(5, [[1, 0], [3, 2], [2, 3]]) is False
    assert solve(2, [[1, 0], [1, 0]]) is True
    assert solve(1500, [[i, i - 1] for i in range(1, 1500)]) is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 078 — Can You Finish Every Course?")
