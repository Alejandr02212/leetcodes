# Your practice file — 066. Binary Tree Inorder Traversal
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Walk left while saving ancestors on a stack.
2. When no left child remains, pop the next node to visit.
3. After recording it, start the same leftward process in its right subtree.

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


def solve(root: TreeNode | None) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
