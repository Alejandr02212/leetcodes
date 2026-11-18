# Your practice file — 067. Maximum Depth of a Binary Tree
"""
067. Maximum Depth of a Binary Tree
Difficulty: Easy | Pattern: Tree DFS carrying depth state
Prerequisites: Problem 066 explicit tree traversal

TASK
Return the maximum number of nodes on a path from the root to a leaf.
An empty tree has depth 0 and a single node has depth 1. Use an iterative
traversal and preserve the input tree.

EXAMPLES
solve(tree([3, 9, 20, None, None, 15, 7])) -> 3.
solve(TreeNode(5)) -> 1.
solve(None) -> 0.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are integers. The input is a finite ordinary tree without cycles or shared children.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A root-to-node depth can travel alongside each node.
2. Put (root, 1) on a stack and each child at depth + 1.
3. Keep the largest depth seen; use 0 for an empty root.

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
    assert solve(TreeNode(5)) == 1
    assert solve(tree([1, 2])) == 2
    assert solve(tree([3, 9, 20, None, None, 15, 7])) == 3
    assert solve(tree([1, 2, 3, 4, 5, 6, 7])) == 3
    assert solve(tree([0, None, 0, None, 0, None, 0])) == 4
    root = tree([5, 4, 6])
    assert solve(root) == 2 and to_level(root) == [5, 4, 6]
    chain = None
    for value in range(2000):
        chain = TreeNode(value, None, chain)
    assert solve(chain) == 2000


if __name__ == "__main__":
    run_tests()
    print("PASS: 067 — Maximum Depth of a Binary Tree")
