# Explained reference solution — 080. Find the Redundant Connection
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

SOLUTION EXPLANATION
Initially every node forms its own connected component. For each edge,
find both component roots. Different roots can be joined without creating a
cycle; the same root means an existing path already joins the endpoints, so
this edge closes a cycle. A tree plus one edge has exactly one cycle. Its last
input edge is precisely the edge that first closes that cycle during this scan,
so returning it satisfies the requested tie rule. Union by size keeps the
shallower structure under the larger root; path compression shortens future
searches by making visited nodes skip ancestors. This template is useful for
incremental connectivity and Kruskal's minimum spanning tree algorithm too.

COMPLEXITY
For n edges/n nodes: O(n*alpha(n)) amortized time, where alpha is the inverse Ackermann function; O(n) auxiliary space.

COMMON MISTAKES
Union roots, not arbitrary endpoints. Without the tree-plus-one-edge guarantee, returning the first detected cycle edge does not solve every deletion variant.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))
    size = [1] * (len(edges) + 1)
    def find(node):
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return [u, v]
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
    raise ValueError('Expected a tree plus one extra edge')


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
