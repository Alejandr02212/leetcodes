# Explained reference solution — 066. Binary Tree Inorder Traversal
"""
066. Binary Tree Inorder Traversal
Difficulty: Easy | Pattern: Iterative DFS: stack simulates recursive calls
Prerequisites: Problem 051 stacks; supplied TreeNode helpers

TASK
Return the node values of a binary tree in inorder: visit the left
subtree, then the node, then its right subtree. Use an explicit stack to
avoid Python recursion-depth limits on a long chain. Do not change links.
The supplied tree helper reads level-order values, with None for missing
children.

EXAMPLES
solve(tree([1, None, 2, 3])) -> [1, 3, 2].
solve(tree([2, 1, 3])) -> [1, 2, 3].
solve(None) -> [].

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are integers and may repeat. The input is a finite tree with no cycles or shared child nodes.

SOLUTION EXPLANATION
Each stacked node represents a paused recursive call waiting for its
left subtree to finish. Walking left pushes those calls. When current is
None, the top node has no unvisited left work and is the next inorder value.
Pop and record it, then explore its right subtree using the same procedure.
Every node is pushed and popped once, and a node is recorded only after its
left subtree and before its right subtree. That is exactly the inorder rule.

This is an explicit version of recursion: stack entries record the work to
resume after descending into a child.

COMPLEXITY
Time O(n); auxiliary stack O(h) for height h, worst-case O(n). Returned traversal uses O(n) space. Empty-tree height is 0.

COMMON MISTAKES
Continue while current exists OR the stack is nonempty. Inorder is sorted only for a BST, not for an arbitrary binary tree. Avoid mutating links while traversing.

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


def solve(root: TreeNode | None) -> list[int]:
    answer = []
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        answer.append(current.val)
        current = current.right
    return answer


def run_tests() -> None:
    assert solve(None) == []
    assert solve(TreeNode(4)) == [4]
    assert solve(tree([1, None, 2, 3])) == [1, 3, 2]
    assert solve(tree([2, 1, 3])) == [1, 2, 3]
    assert solve(tree([1, 2, 3, 4, 5])) == [4, 2, 5, 1, 3]
    assert solve(tree([7, 7, 7])) == [7, 7, 7]
    root = tree([3, 1, 4, None, 2])
    before = to_level(root)
    assert solve(root) == [1, 2, 3, 4] and to_level(root) == before
    chain = None
    for value in range(2000):
        chain = TreeNode(value, chain)
    assert solve(chain) == list(range(2000))


if __name__ == "__main__":
    run_tests()
    print("PASS: 066 — Binary Tree Inorder Traversal")
