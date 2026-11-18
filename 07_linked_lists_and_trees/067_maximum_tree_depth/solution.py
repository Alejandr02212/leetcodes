# Explained reference solution — 067. Maximum Depth of a Binary Tree
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

SOLUTION EXPLANATION
The stack pairs each scheduled node with its exact root-to-node depth.
The root's depth is 1; every child is one edge farther away, so adding 1
preserves this invariant. The traversal schedules each child once and visits
every node. The maximum recorded depth is therefore the maximum over all
root-to-node paths. Any deepest node is a leaf, since a child would be deeper,
so this is also the requested root-to-leaf maximum.

Carrying a small piece of path state in each stack entry is a general DFS
technique, useful for sums, bounds, and distances too.

COMPLEXITY
Time O(n), auxiliary DFS stack O(h), worst-case O(n), for n nodes and tree height h. The returned integer uses O(1) space.

COMMON MISTAKES
This exercise counts nodes, whereas tree diameter later counts edges. Return 0 for None. Recursion is concise but can exceed Python's depth limit on a chain.

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


def solve(root: TreeNode | None) -> int:
    if root is None:
        return 0
    deepest = 0
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        deepest = max(deepest, depth)
        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth + 1))
    return deepest


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
