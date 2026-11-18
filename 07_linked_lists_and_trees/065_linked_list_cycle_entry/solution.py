# Explained reference solution — 065. Find a Linked List's Cycle Entry
"""
065. Find a Linked List's Cycle Entry
Difficulty: Medium | Pattern: Floyd's fast/slow pointers and reset phase
Prerequisites: Problem 062 fast and slow pointers; object identity

TASK
Given a singly linked list that may contain a cycle, return the existing
node where the cycle begins, or None if the list is acyclic. Do not modify
any next pointer and do not use a visited-node set. Compare node identity,
not values. The returned node must be the actual entry object.

EXAMPLES
For 3 -> 2 -> 0 -> -4 with -4.next pointing to the node containing 2,
return that node containing 2.
A node whose next points to itself is its own cycle entry.
An ordinary list 1 -> 2 -> None returns None.

CONSTRAINTS AND CONTRACT
0 <= number of distinct reachable nodes <= 100000. Values are integers and may repeat. Each node has at most one successor; preserve the structure.

SOLUTION EXPLANATION
If there is no cycle, fast eventually reaches None. Inside a cycle, fast
gains one position per iteration relative to slow, so they must meet within
one cycle length after both enter it.

Let mu be the distance from head to entry, lambda the cycle length, and t
the number of slow steps at a meeting. Fast has taken 2t steps, so their
distance difference t is a multiple of lambda. A pointer starting at the
meeting and moving mu further steps reaches cycle offset t, modulo lambda,
which is 0: the entry. A pointer reset to head also reaches entry after mu
steps. Before then the reset pointer is outside the cycle, so they cannot
meet earlier. This proves the reset phase finds the actual entry.

COMPLEXITY
Time O(mu + lambda), auxiliary space O(1). For an acyclic list, time O(n); no nodes or result structure are allocated.

COMMON MISTAKES
A meeting proves a cycle but is not generally the entry. Use 'is' for node identity, especially when values repeat. Never run to_list on a cyclic list.

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
        if slow is fast:
            entry = head
            while entry is not slow:
                entry = entry.next
                slow = slow.next
            return entry
    return None


def run_tests() -> None:
    assert solve(None) is None
    assert solve(from_list([1])) is None
    assert solve(from_list([2, 2, 2, 2])) is None
    one = ListNode(8)
    one.next = one
    assert solve(one) is one and one.next is one
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    a.next, b.next, c.next, d.next = b, c, d, b
    assert solve(a) is b
    assert a.next is b and b.next is c and c.next is d and d.next is b
    a, b = ListNode(1), ListNode(1)
    a.next, b.next = b, a
    assert solve(a) is a
    a, b, c = ListNode(5), ListNode(5), ListNode(5)
    a.next, b.next, c.next = b, c, c
    assert solve(a) is c


if __name__ == "__main__":
    run_tests()
    print("PASS: 065 — Find a Linked List's Cycle Entry")
