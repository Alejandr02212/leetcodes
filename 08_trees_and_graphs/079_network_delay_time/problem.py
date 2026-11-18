# Your practice file — 079. Network Delay Time
"""
079. Network Delay Time
Difficulty: Medium | Pattern: Dijkstra's shortest paths with a min-heap
Prerequisites: Graph adjacency lists; heapq; weighted paths.

TASK
times contains directed edges [source, destination, weight] among nodes
1 through n. A signal starts at node start at time zero. Return the earliest
time when every node can have received it, or -1 if some node is unreachable.
Travel times are positive integers. Parallel edges may occur. Receiving a signal
along several paths uses the earliest arrival, not the sum of arrivals.

EXAMPLES
times=[[1,2,3],[2,3,4],[1,3,9]], n=3, start=1 -> 7.
times=[[1,2,1]], n=2, start=2 -> -1.
times=[], n=1, start=1 -> 0.

CONSTRAINTS AND CONTRACT
1 <= n <= 3000; 0 <= len(times) <= 15_000. Valid node labels and start. All weights >= 1. Input unchanged.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Find the shortest distance from start to EVERY node.
2. Repeatedly expand the pending smallest distance, updating better neighbor distances.
3. A heap can hold obsolete distances; skip an entry if it no longer matches dist[node].

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(times: list[list[int]], n: int, start: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([], 1, 1) == 0
    assert solve([], 2, 1) == -1
    assert solve([[1, 2, 1]], 2, 2) == -1
    assert solve([[1, 2, 3], [2, 3, 4], [1, 3, 9]], 3, 1) == 7
    assert solve([[1, 2, 10], [1, 3, 1], [3, 2, 1], [2, 4, 1]], 4, 1) == 3
    assert solve([[1, 2, 9], [1, 2, 2]], 2, 1) == 2
    assert solve([[1, 2, 1], [2, 1, 1], [2, 3, 8]], 3, 1) == 9
    assert solve([[2, 1, 2], [2, 3, 1], [3, 4, 5]], 4, 2) == 6


if __name__ == "__main__":
    run_tests()
    print("PASS: 079 — Network Delay Time")
