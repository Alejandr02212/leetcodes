# Your practice file — 070. Binary Tree Level Order Traversal
"""
070. Binary Tree Level Order Traversal
Difficulty: Medium | Pattern: Breadth-first search with a fixed layer size
Prerequisites: Problem 066 trees; collections.deque

TASK
Return the values of a binary tree grouped by depth, from root level to
deepest level, and left to right within each level. An empty tree returns
an empty list. Preserve the input tree.

EXAMPLES
solve(tree([3, 9, 20, None, None, 15, 7])) -> [[3], [9, 20], [15, 7]].
solve(TreeNode(1)) -> [[1]].
solve(None) -> [].

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are integers, including duplicates. The input is a finite ordinary tree.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A queue processes nodes in the order they were discovered.
2. At the start of a level, save len(queue).
3. Remove exactly that many nodes, appending their children for the next level.

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


def solve(root: TreeNode | None) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(None) == []
    assert solve(TreeNode(1)) == [[1]]
    assert solve(tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert solve(tree([1, 2, 3, 4, 5, 6, 7])) == [[1], [2, 3], [4, 5, 6, 7]]
    assert solve(tree([1, None, 2, None, 3])) == [[1], [2], [3]]
    assert solve(tree([4, 4, 4])) == [[4], [4, 4]]
    root = tree([7, 3, 9, None, 5])
    assert solve(root) == [[7], [3, 9], [5]] and to_level(root) == [7, 3, 9, None, 5]


if __name__ == "__main__":
    run_tests()
    print("PASS: 070 — Binary Tree Level Order Traversal")
