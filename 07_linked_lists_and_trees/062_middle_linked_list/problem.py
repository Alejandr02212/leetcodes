# Your practice file — 062. Middle of a Linked List
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. One pointer can move one step while another moves two.
2. When the fast pointer runs out, how far has the slow pointer traveled?
3. Continue while fast and fast.next exist; starting both at head naturally chooses the second middle.

The adjacent solution.py contains the explanation and reference code.
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
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
