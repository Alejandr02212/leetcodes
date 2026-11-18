# Explained reference solution — 062. Middle of a Linked List
"""
062. Middle of a Linked List
Difficulty: Easy | Pattern: Fast and slow pointers
Prerequisites: Problem 061 linked-list traversal

TASK
Return the middle node of a finite acyclic singly linked list without
changing it. For an even number of nodes, return the second middle node.
Return None for an empty list. Return an existing node object, not its value
or a copied suffix.

EXAMPLES
For nodes 1 -> 2 -> 3 -> 4 -> 5, return the node containing 3.
For 1 -> 2 -> 3 -> 4, return the node containing 3 (second middle).
solve(None) -> None.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Values are integers and may repeat. The list has no cycle; preserve all links.

SOLUTION EXPLANATION
After t iterations, slow has advanced t edges and fast has advanced 2t
edges, whenever those positions exist. With n nodes the loop runs floor(n/2)
times. Therefore slow ends at zero-based index floor(n/2): the unique middle
for odd n and the second middle for even n. Reading next links without
assigning them preserves the input.

The reusable idea is to turn a positional relationship into a speed ratio,
avoiding a separate counting pass.

COMPLEXITY
Time O(n), auxiliary space O(1), and no new result nodes, where n is the node count.

COMMON MISTAKES
Check fast before accessing fast.next. Changing the initial fast position changes which middle an even list returns. Return the actual node so identity is preserved.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

class ListNode:
    """A node is identified by its object identity, even if values repeat."""
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def from_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    """For acyclic test lists only."""
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def solve(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def run_tests() -> None:
    assert solve(None) is None
    one = ListNode(9)
    assert solve(one) is one
    two = from_list([4, 5])
    assert solve(two) is two.next
    odd = from_list([1, 2, 3, 4, 5])
    assert solve(odd) is odd.next.next
    even = from_list([1, 2, 3, 4, 5, 6])
    assert solve(even) is even.next.next.next
    repeated = from_list([7, 7, 7, 7])
    assert solve(repeated) is repeated.next.next
    assert to_list(even) == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    run_tests()
    print("PASS: 062 — Middle of a Linked List")
