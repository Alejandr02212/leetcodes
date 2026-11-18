# Explained reference solution — 078. Can You Finish Every Course?
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

SOLUTION EXPLANATION
Keep indegree equal to the number of incoming prerequisite edges from
courses that have not yet been processed. A zero value therefore means a course
can safely be taken next. Processing that course removes all its outgoing edges,
possibly unlocking dependents. If every course is processed, their processing
order is a valid schedule. Otherwise every remaining course has an incoming edge
from another remaining course. Following such edges in a finite graph eventually
repeats a node, proving a cycle and making a complete schedule impossible.
Duplicate edges are counted and removed equally, so they do not affect correctness.
The queue-based approach also avoids recursion-depth issues on long chains.

COMPLEXITY
Let V=num_courses and E=len(prerequisites). Time O(V+E); auxiliary adjacency, indegree, and queue space O(V+E).

COMMON MISTAKES
Reversing only the indegree convention breaks unlocking. A single cyclic component invalidates the entire schedule, even when other courses are available.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    from collections import deque
    following = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        following[prerequisite].append(course)
        indegree[course] += 1
    ready = deque(i for i in range(num_courses) if indegree[i] == 0)
    completed = 0
    while ready:
        course = ready.popleft()
        completed += 1
        for dependent in following[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)
    return completed == num_courses


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
