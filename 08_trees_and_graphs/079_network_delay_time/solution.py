# Explained reference solution — 079. Network Delay Time
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

SOLUTION EXPLANATION
Distance estimates describe the best discovered route to each node. The
heap chooses the smallest pending estimate. With nonnegative edge weights, no
route through a later, more distant node can improve the node being expanded:
that expansion has its final shortest distance. Relax each outgoing edge by
trying elapsed+weight. We push a new heap entry on improvement rather than
editing an existing entry, so stale entries must be skipped. After traversal,
infinity identifies unreachable nodes. Otherwise the last node receives the
signal at the maximum shortest distance. Ordinary BFS would minimize edge count,
which is insufficient when edge weights differ.

COMPLEXITY
For V=n and E edges, time O(V + E*log(E+1)) and auxiliary space O(V+E), including possible stale heap entries. Parallel edges make log(E+1) the general heap bound.

COMMON MISTAKES
Do not mark nodes final when first pushed. Do not sum shortest distances. Treat edges as directed; the reverse route may not exist.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(times: list[list[int]], n: int, start: int) -> int:
    from heapq import heappop, heappush
    adjacency = [[] for _ in range(n + 1)]
    for source, destination, weight in times:
        adjacency[source].append((destination, weight))
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        elapsed, node = heappop(heap)
        if elapsed != distance[node]:
            continue
        for neighbor, weight in adjacency[node]:
            candidate = elapsed + weight
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                heappush(heap, (candidate, neighbor))
    answer = max(distance[1:])
    return -1 if answer == float('inf') else answer


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
