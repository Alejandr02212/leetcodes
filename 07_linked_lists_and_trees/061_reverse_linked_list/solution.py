# Explained reference solution — 061. Reverse a Linked List
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

SOLUTION EXPLANATION
Before each iteration, previous heads the reversed processed prefix and
current heads the original unprocessed suffix. Save the suffix's next node,
then redirect current.next toward the reversed prefix. This adds exactly one
original node to that prefix without losing the remaining suffix. Advancing
both variables restores the invariant. When current becomes None, every
original node is in the reversed prefix, whose head is previous.

Pointer problems become safer when you name what each reference owns and
save any link that a mutation would overwrite.

COMPLEXITY
Time O(n) and auxiliary space O(1), where n is the number of nodes. The result reuses existing nodes; no new output nodes are allocated.

COMMON MISTAKES
Save the successor before overwriting next. Return previous rather than the old head. A node's value is not its identity; repeated values are allowed.

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
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


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
