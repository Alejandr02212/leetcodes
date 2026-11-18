# Your practice file — 074. Lowest Common Ancestor in a Binary Tree
"""
074. Lowest Common Ancestor in a Binary Tree
Difficulty: Medium | Pattern: Parent map plus ancestor-set intersection
Prerequisites: Problem 067 tree traversal; sets and object identity

TASK
Given a nonempty binary tree and two node objects p and q that both occur
in it, return their lowest common ancestor (LCA) as an existing node object.
A node is its own ancestor, so p == q has LCA p, and an ancestor-descendant
pair has the ancestor as LCA. Values may repeat; use identity. Do not assume
a BST or change the tree.

EXAMPLES
For root 3 with children 5 and 1, LCA(root, node5, node1) is root.
If node5 has descendant node4, LCA(root, node5, node4) is node5.
solve(root, p, p) is p.

CONSTRAINTS AND CONTRACT
1 <= node count <= 100000. p and q are actual node references in a finite ordinary tree; both are guaranteed to exist. Values are arbitrary integers, possibly duplicates.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A parent dictionary lets you walk from a node back to root.
2. Record every ancestor of p, including p.
3. Walk upward from q; the first node in that set is the lowest shared ancestor.

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


def solve(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    root = tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert solve(root, root.left, root.right) is root
    assert solve(root, root.left, root.left.right.right) is root.left
    assert solve(root, root.left.right.left, root.left.right.right) is root.left.right
    assert solve(root, root, root.right.right) is root
    assert solve(root, root.left, root.left) is root.left
    single = TreeNode(9)
    assert solve(single, single, single) is single
    duplicate = TreeNode(1, TreeNode(1), TreeNode(1))
    assert solve(duplicate, duplicate.left, duplicate.right) is duplicate
    assert to_level(root) == [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]


if __name__ == "__main__":
    run_tests()
    print("PASS: 074 — Lowest Common Ancestor in a Binary Tree")
