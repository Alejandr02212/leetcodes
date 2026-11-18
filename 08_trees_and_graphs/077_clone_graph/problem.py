# Your practice file — 077. Clone an Undirected Graph
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A visited set is insufficient: you also need each original node's copy.
2. Create and register a node's copy before exploring its neighbors.
3. For every original edge u -> v, append copies[v] to copies[u].neighbors.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

class Node:
    def __init__(self, val: int, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = [] if neighbors is None else list(neighbors)


def solve(node: Node | None) -> Node | None:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
