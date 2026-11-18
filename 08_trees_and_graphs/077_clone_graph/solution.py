# Explained reference solution — 077. Clone an Undirected Graph
"""
077. Clone an Undirected Graph
Difficulty: Medium | Pattern: Graph traversal with an original-to-copy map
Prerequisites: Grid BFS/DFS; dictionaries keyed by objects; object identity.

TASK
Given a Node in a finite undirected graph, return the corresponding node
of a deep graph copy. Every reachable original node must have a distinct new
Node with the same val and a neighbors list matching the original neighbor
order. Copied edges must point only to copied nodes. Values need NOT be unique.
The input may contain cycles, self-loops, and repeated neighbor references.
Return None for None. Leave the original graph unchanged.

EXAMPLES
A(val=1) <-> B(val=2) -> a fresh A' <-> B', with neither node shared.
A.neighbors=[A] -> A'.neighbors=[A']; the self-loop remains.
None -> None.

CONSTRAINTS AND CONTRACT
At most 300 reachable nodes and 2000 neighbor entries. Values are arbitrary integers; each edge is represented in the corresponding neighbors lists.

SOLUTION EXPLANATION
The dictionary is both a visited structure and a translation table between
original and copied identities. Register the first copy immediately. When an
edge leads to a new node, register its empty copy before scheduling exploration;
this breaks cycles without recursion. Append one translated neighbor for every
original neighbor entry, preserving order and multiplicity. Each original node
is expanded once. Every reachable node consequently has exactly one copy, and
every original edge is reproduced between its endpoint copies. Key by the Node
object itself, not by val: different vertices may store the same value.

COMPLEXITY
For V reachable nodes and E neighbor entries: time O(V+E), auxiliary map/stack O(V), plus O(V+E) output graph storage.

COMMON MISTAKES
Copying only the first node shares old neighbors. Keying by val merges different vertices. Registering after recursion never terminates on cycles.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

class Node:
    def __init__(self, val: int, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = [] if neighbors is None else list(neighbors)


def solve(node: Node | None) -> Node | None:
    if node is None:
        return None
    copies = {node: Node(node.val)}
    stack = [node]
    while stack:
        original = stack.pop()
        for neighbor in original.neighbors:
            if neighbor not in copies:
                copies[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            copies[original].neighbors.append(copies[neighbor])
    return copies[node]


def run_tests() -> None:
    def check(original):
        clone = solve(original)
        if original is None:
            assert clone is None
            return
        originals = set()
        pending = [original]
        while pending:
            item = pending.pop()
            if item in originals:
                continue
            originals.add(item)
            pending.extend(item.neighbors)
        mapping = {original: clone}
        pending = [original]
        while pending:
            item = pending.pop()
            copy = mapping[item]
            assert copy not in originals
            assert copy.val == item.val
            assert len(copy.neighbors) == len(item.neighbors)
            for neighbor, copied_neighbor in zip(item.neighbors, copy.neighbors):
                if neighbor in mapping:
                    assert mapping[neighbor] is copied_neighbor
                else:
                    mapping[neighbor] = copied_neighbor
                    pending.append(neighbor)
        assert len(set(mapping.values())) == len(mapping)

    check(None)
    check(Node(7))
    a = Node(1)
    a.neighbors = [a]
    check(a)
    a, b = Node(4), Node(4)
    a.neighbors, b.neighbors = [b], [a]
    check(a)
    a, b, c = Node(1), Node(2), Node(3)
    a.neighbors, b.neighbors, c.neighbors = [b, c], [a, c], [a, b]
    check(a)
    a, b = Node(-2), Node(9)
    a.neighbors, b.neighbors = [b, b], [a, a]
    check(a)
    copy = solve(a)
    copy.val = 100
    copy.neighbors.clear()
    assert a.val == -2 and len(a.neighbors) == 2


if __name__ == "__main__":
    run_tests()
    print("PASS: 077 — Clone an Undirected Graph")
