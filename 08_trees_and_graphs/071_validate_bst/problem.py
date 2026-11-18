# Your practice file — 071. Validate a Binary Search Tree
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Checking only the immediate children misses violations from distant ancestors.
2. Carry a lower and upper exclusive bound with each DFS state.
3. A left child inherits the old lower bound and uses parent.val as its upper bound; reverse that for a right child.

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


def solve(root: TreeNode | None) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
