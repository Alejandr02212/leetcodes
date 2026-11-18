# Your practice file — 061. Reverse a Linked List
"""
061. Reverse a Linked List
Difficulty: Easy | Pattern: Pointer rewiring with previous/current/next
Prerequisites: Variables, loops, and the supplied ListNode class

TASK
Reverse a finite acyclic singly linked list in place and return its new
head. Reuse the original nodes: do not allocate replacement data nodes or
convert the list to an array to reverse it. None represents an empty list.
The supplied from_list and to_list helpers are only for building test data.

EXAMPLES
to_list(solve(from_list([1, 2, 3]))) -> [3, 2, 1].
solve(None) -> None.
A one-node list returns the same node object.

CONSTRAINTS AND CONTRACT
0 <= node count <= 100000. Node values are integers; the input has no cycle. Mutation of next pointers is required.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Keep a reversed prefix and an untouched suffix.
2. Save current.next before redirecting it to the previous node.
3. Advance previous to current and current to the saved successor.

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
    one = ListNode(7)
    assert solve(one) is one and one.next is None
    assert to_list(solve(from_list([1, 2]))) == [2, 1]
    assert to_list(solve(from_list([1, 2, 3, 4]))) == [4, 3, 2, 1]
    assert to_list(solve(from_list([2, 2, -1]))) == [-1, 2, 2]
    first, second, third = ListNode(1), ListNode(2), ListNode(3)
    first.next, second.next = second, third
    result = solve(first)
    assert result is third and third.next is second and second.next is first and first.next is None
    original = from_list([8, 9, 10])
    assert solve(solve(original)) is original and to_list(original) == [8, 9, 10]


if __name__ == "__main__":
    run_tests()
    print("PASS: 061 — Reverse a Linked List")
