# Your practice file — 073. Diameter of a Binary Tree
"""
073. Diameter of a Binary Tree
Difficulty: Medium | Pattern: Bottom-up tree DP using iterative postorder
Prerequisites: Problem 067 depth; dictionaries keyed by node identity

TASK
Return the number of edges in the longest path between any two nodes in
a binary tree. The path may pass through any node, not necessarily the root.
An empty tree or single node has diameter 0. Preserve the tree and support
deep chains without recursion.

EXAMPLES
solve(tree([1, 2, 3, 4, 5])) -> 3, via 4 -> 2 -> 1 -> 3.
solve(TreeNode(7)) -> 0.
solve(tree([1, 2, None, 3, 4, 5, None, None, 6])) -> 4, via 5 -> 3 -> 2 -> 4 -> 6.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are arbitrary integers and need not be unique. Input is a finite ordinary tree. Diameter counts edges, while subtree heights below count nodes.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. At any node, a path joining its left and right descendants has length left_height + right_height.
2. You need child heights before the parent: process in postorder.
3. Store (node, ready) stack states; a ready node has already scheduled both children.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def tree(values: list[int | None]) -> TreeNode | None:
    """Build from level order: absent children are None; trailing None is optional."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    position = 1
    while queue and position < len(values):
        node = queue.popleft()
        if position < len(values) and values[position] is not None:
            node.left = TreeNode(values[position])
            queue.append(node.left)
        position += 1
        if position < len(values) and values[position] is not None:
            node.right = TreeNode(values[position])
            queue.append(node.right)
        position += 1
    return root


def to_level(root: TreeNode | None) -> list[int | None]:
    """Convert an ordinary finite tree to level order for assertions."""
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.extend([node.left, node.right])
    while values and values[-1] is None:
        values.pop()
    return values


def solve(root: TreeNode | None) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(None) == 0
    assert solve(TreeNode(7)) == 0
    assert solve(tree([1, 2])) == 1
    assert solve(tree([1, 2, 3, 4, 5])) == 3
    assert solve(tree([1, 2, None, 3, 4, 5, None, None, 6])) == 4
    assert solve(tree([1, 2, 3, 4, None, None, 5])) == 4
    root = tree([2, 2, 2])
    assert solve(root) == 2 and to_level(root) == [2, 2, 2]
    chain = None
    for value in range(2000):
        chain = TreeNode(value, chain)
    assert solve(chain) == 1999


if __name__ == "__main__":
    run_tests()
    print("PASS: 073 — Diameter of a Binary Tree")
