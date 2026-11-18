# Your practice file — 069. Invert a Binary Tree
"""
069. Invert a Binary Tree
Difficulty: Easy | Pattern: Visit every node and apply a local transformation
Prerequisites: Problem 067 iterative DFS; swapping Python references

TASK
Mirror a binary tree in place by swapping the left and right child of
every node. Return the original root object, whose descendants are now
mirrored. An empty root returns None. Reuse every existing node.

EXAMPLES
to_level(solve(tree([4, 2, 7, 1, 3, 6, 9]))) -> [4, 7, 2, 9, 6, 3, 1].
to_level(solve(tree([1, 2]))) -> [1, None, 2].
solve(None) -> None.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are integers. Input is a finite ordinary tree with no cycles or shared children. Child-link mutation is required.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Mirroring means swapping children at every node, not reversing a value list.
2. Use a stack to visit all nodes.
3. Swap once, then schedule each existing child; return root.

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


def solve(root: TreeNode | None) -> TreeNode | None:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(None) is None
    one = TreeNode(5)
    assert solve(one) is one and one.left is None and one.right is None
    assert to_level(solve(tree([1, 2]))) == [1, None, 2]
    assert to_level(solve(tree([1, None, 2]))) == [1, 2]
    assert to_level(solve(tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    root = tree([1, 2, 3, None, 4])
    original = to_level(root)
    assert solve(solve(root)) is root and to_level(root) == original
    child = TreeNode(2)
    root = TreeNode(1, child)
    assert solve(root) is root and root.right is child and root.left is None


if __name__ == "__main__":
    run_tests()
    print("PASS: 069 — Invert a Binary Tree")
