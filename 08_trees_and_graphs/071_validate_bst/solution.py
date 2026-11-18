# Explained reference solution — 071. Validate a Binary Search Tree
"""
071. Validate a Binary Search Tree
Difficulty: Medium | Pattern: DFS carrying exclusive ancestor bounds
Prerequisites: Problem 067 DFS state; comparison with inherited constraints

TASK
Return whether a binary tree is a strict binary search tree: every value
in a node's left subtree is smaller than that node, every value in its right
subtree is larger, and both subtrees obey the same rule. Duplicates are
invalid. An empty tree is valid. Preserve the tree.

EXAMPLES
solve(tree([2, 1, 3])) -> True.
solve(tree([5, 1, 6, None, None, 3, 7])) -> False: 3 is in the right subtree of 5.
solve(tree([2, 2, 3])) -> False: equality violates strict ordering.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are arbitrary Python integers, with no fixed finite lower or upper bound. Input is a finite ordinary tree.

SOLUTION EXPLANATION
A node must satisfy every ordering constraint imposed by its ancestors.
Those constraints compress into an interval: its strongest lower bound and
strongest upper bound. The stack stores that permitted open interval. If
the node lies outside it, the BST condition fails for some ancestor. If it
lies inside, its left subtree can only contain smaller values and its right
subtree larger values, so tighten the relevant bound when scheduling each
child. Inductively, every accepted node satisfies all ancestors, which is
exactly the global BST rule.

None represents an absent bound and supports arbitrary integer magnitudes.

COMPLEXITY
Time O(n), auxiliary stack O(h), worst-case O(n), for n nodes and height h. Returned bool uses O(1) space.

COMMON MISTAKES
Local parent-child comparisons do not establish a BST. Bounds are exclusive, so duplicate values fail. Use absent bounds rather than an arbitrary finite sentinel.

Run this file with python3 solution.py to check the reference implementation.
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


def solve(root: TreeNode | None) -> bool:
    stack = [(root, None, None)]
    while stack:
        node, lower, upper = stack.pop()
        if node is None:
            continue
        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False
        stack.append((node.left, lower, node.val))
        stack.append((node.right, node.val, upper))
    return True


def run_tests() -> None:
    assert solve(None) is True
    assert solve(TreeNode(0)) is True
    assert solve(tree([2, 1, 3])) is True
    assert solve(tree([5, 1, 6, None, None, 3, 7])) is False
    assert solve(tree([2, 2, 3])) is False
    assert solve(tree([2, 1, 2])) is False
    huge = 10**100
    assert solve(TreeNode(huge, TreeNode(-huge), TreeNode(huge + 1))) is True
    root = tree([10, 5, 15, None, None, 6, 20])
    assert solve(root) is False and to_level(root) == [10, 5, 15, None, None, 6, 20]


if __name__ == "__main__":
    run_tests()
    print("PASS: 071 — Validate a Binary Search Tree")
