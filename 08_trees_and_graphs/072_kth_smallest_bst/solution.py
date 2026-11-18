# Explained reference solution — 072. Kth Smallest Value in a BST
"""
072. Kth Smallest Value in a BST
Difficulty: Medium | Pattern: Ordered traversal with an early stop
Prerequisites: Problems 066 inorder and 071 strict BSTs

TASK
Given a nonempty strict BST and a valid 1-based k, return its kth smallest
value. Traverse incrementally and stop once the answer is known. Do not
convert the whole tree into a sorted list, and preserve all child links.

EXAMPLES
solve(tree([3, 1, 4, None, 2]), 1) -> 1.
solve(tree([3, 1, 4, None, 2]), 3) -> 3.
solve(TreeNode(-5), 1) -> -5.

CONSTRAINTS AND CONTRACT
1 <= k <= node count <= 100000. All values are distinct integers and the input satisfies the strict BST rule. Input is a finite ordinary tree.

SOLUTION EXPLANATION
For each BST node, all left values are smaller and all right values are
larger. Inorder recursively visits the left subtree, the node, and then the
right subtree, so its visitation sequence is strictly ascending. The stack
simulates that sequence without building an output array. Decrementing k
only when a node is actually visited counts the sorted ranks correctly.
The visit that changes k to zero is the requested rank, so later nodes are
unnecessary. The final error is defensive; the stated valid-k precondition
guarantees that the loop returns earlier.

COMPLEXITY
Time O(h+k), at most O(n), and auxiliary stack O(h), where h is height and n is node count. The returned integer takes O(1) space.

COMMON MISTAKES
k is 1-based. A node pushed on the path has not been visited yet. The BST guarantee is essential; inorder on an arbitrary tree is not sorted.

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


def solve(root: TreeNode, k: int) -> int:
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right
    raise ValueError('k must be within the tree size')


def run_tests() -> None:
    assert solve(TreeNode(-5), 1) == -5
    assert solve(tree([3, 1, 4, None, 2]), 1) == 1
    assert solve(tree([3, 1, 4, None, 2]), 3) == 3
    assert solve(tree([3, 1, 4, None, 2]), 4) == 4
    assert solve(tree([0, -2, 2, -3, -1, 1, 3]), 4) == 0
    root = tree([5, 3, 6, 2, 4, None, None, 1])
    assert [solve(root, k) for k in range(1, 7)] == [1, 2, 3, 4, 5, 6]
    assert to_level(root) == [5, 3, 6, 2, 4, None, None, 1]


if __name__ == "__main__":
    run_tests()
    print("PASS: 072 — Kth Smallest Value in a BST")
