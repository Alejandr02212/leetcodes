# Explained reference solution — 073. Diameter of a Binary Tree
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

SOLUTION EXPLANATION
Any simple path in a tree has one highest node. At that node the path
takes at most one downward branch in each child subtree, so its best possible
length is left_height + right_height: a child height in nodes equals the
number of edges from the parent down that branch. Taking the maximum of this
quantity over all nodes therefore considers every possible longest path.

Heights obey height(node) = 1 + max(height(left), height(right)), with missing
children height 0. An explicit postorder stack processes children before the
ready version of their parent, so each cached height is already correct when
used. This is tree dynamic programming: return useful summaries upward and
update a larger answer while combining children.

COMPLEXITY
Time O(n). Auxiliary space O(n) for cached heights plus O(h) traversal stack; total O(n). Returned diameter uses O(1) space.

COMMON MISTAKES
The longest path need not go through root. Distinguish height in nodes from diameter in edges. Combine both child heights, but pass only the larger one upward.

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
    heights = {}
    longest = 0
    stack = [(root, False)]
    while stack:
        node, ready = stack.pop()
        if not ready:
            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))
        else:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            longest = max(longest, left_height + right_height)
            heights[node] = 1 + max(left_height, right_height)
    return longest


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
