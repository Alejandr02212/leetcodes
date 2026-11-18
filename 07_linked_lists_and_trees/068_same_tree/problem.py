# Your practice file — 068. Are Two Binary Trees the Same?
"""
068. Are Two Binary Trees the Same?
Difficulty: Easy | Pattern: Traverse paired states to compare structure and values
Prerequisites: Problem 066 tree traversal and None handling

TASK
Return whether two trees have exactly the same shape and equal values at
corresponding nodes. The trees may be different objects; object identity is
not required for equality here. Preserve both trees and handle empty trees.

EXAMPLES
solve(tree([1, 2, 3]), tree([1, 2, 3])) -> True.
solve(tree([1, 2]), tree([1, None, 2])) -> False: same values, different shape.
solve(None, None) -> True.

CONSTRAINTS AND CONTRACT
Each tree has at most 100000 nodes; values are integers and may repeat. Trees are finite without cycles or shared children. Use an iterative traversal.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Compare pairs of corresponding nodes, not independent traversal lists.
2. Two missing nodes match; exactly one missing node does not.
3. For two real equal-valued nodes, schedule corresponding left and right pairs.

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


def solve(first: TreeNode | None, second: TreeNode | None) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(None, None) is True
    assert solve(TreeNode(1), None) is False
    assert solve(None, TreeNode(1)) is False
    assert solve(tree([1, 2, 3]), tree([1, 2, 3])) is True
    assert solve(tree([1, 2]), tree([1, None, 2])) is False
    assert solve(tree([1, 2, 3]), tree([1, 2, 4])) is False
    assert solve(tree([7, 7]), tree([7, 7])) is True
    root = tree([4, 2, 5])
    assert solve(root, root) is True and to_level(root) == [4, 2, 5]


if __name__ == "__main__":
    run_tests()
    print("PASS: 068 — Are Two Binary Trees the Same?")
