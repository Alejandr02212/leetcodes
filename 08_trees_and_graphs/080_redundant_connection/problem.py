# Your practice file — 080. Find the Redundant Connection
"""
080. Find the Redundant Connection
Difficulty: Medium | Pattern: Disjoint-set union with path compression and union by size
Prerequisites: Undirected cycles; parent arrays; component identity.

TASK
An undirected simple graph was made from a tree on nodes 1 through n by
adding one extra edge between distinct nodes. You receive its n edges in input
order. Return the edge whose removal restores a tree; if several work, choose
the one appearing LAST in the input. Return it as [u, v] in its supplied order.
The input is guaranteed to meet the tree-plus-one-edge contract.

EXAMPLES
edges=[[1,2],[1,3],[2,3]] -> [2,3].
edges=[[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4].

CONSTRAINTS AND CONTRACT
3 <= n=len(edges) <= 10_000. Labels are 1..n; no self-loops or duplicate undirected edges. Input unchanged.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Before adding an edge, ask whether its endpoints are already connected.
2. A disjoint-set union structure can answer that efficiently.
3. The first edge whose endpoints already share a root closes the unique cycle.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(edges: list[list[int]]) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert solve([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    assert solve([[2, 3], [3, 1], [1, 2]]) == [1, 2]
    assert solve([[1, 2], [2, 3], [3, 4], [4, 1]]) == [4, 1]
    assert solve([[1, 2], [3, 4], [2, 3], [1, 4]]) == [1, 4]
    assert solve([[3, 4], [1, 2], [2, 3], [4, 1], [4, 5]]) == [4, 1]
    assert solve([[1, 2], [2, 3], [1, 3], [3, 4], [4, 5]]) == [1, 3]


if __name__ == "__main__":
    run_tests()
    print("PASS: 080 — Find the Redundant Connection")
