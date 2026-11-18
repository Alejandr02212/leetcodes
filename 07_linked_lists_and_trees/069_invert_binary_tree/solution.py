# Explained reference solution — 069. Invert a Binary Tree
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

SOLUTION EXPLANATION
A mirror reverses the left/right choice at each edge along every path.
Swapping each node's two child references performs exactly that reversal.
The stack visits every original node once because swapping preserves the
parent-child set and the input has no shared children or cycles. Thus every
node gets one swap and every descendant is mirrored too. No new tree nodes
are needed, so the returned root has the same identity.

Inverting a second time restores the original structure because swapping the
same two references twice is an identity operation.

COMPLEXITY
Time O(n), auxiliary stack O(h), worst-case O(n), where n is node count and h is height. The returned tree reuses all existing nodes.

COMMON MISTAKES
Do not swap values: shape must change too. Schedule both nonempty children after swapping. Return root rather than the last visited node.

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


def solve(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return root


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
