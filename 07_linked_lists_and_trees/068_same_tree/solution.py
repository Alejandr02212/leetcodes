# Explained reference solution — 068. Are Two Binary Trees the Same?
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

SOLUTION EXPLANATION
A pair on the stack represents a claim that two corresponding subtrees
must match. Two empty subtrees satisfy it. If only one is empty or their root
values differ, the whole-tree claim is false. Otherwise the pair matches if
and only if its left-child pair and right-child pair match, so replace it
with those two smaller claims. All claims eventually terminate at missing
children. If none fails, every position has matching presence and value,
which proves both shape and values are equal.

COMPLEXITY
Time O(n+m) in the worst case for trees with n and m nodes (often it stops earlier). Auxiliary stack O(h1+h2), worst-case O(n+m); returned bool O(1).

COMMON MISTAKES
Equal inorder values alone do not prove equal shape. Do not treat matching values as matching identities. Check missing nodes before accessing .val.

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


def solve(first: TreeNode | None, second: TreeNode | None) -> bool:
    stack = [(first, second)]
    while stack:
        left, right = stack.pop()
        if left is None or right is None:
            if left is not right:
                return False
            continue
        if left.val != right.val:
            return False
        stack.append((left.left, right.left))
        stack.append((left.right, right.right))
    return True


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
