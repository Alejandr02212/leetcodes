# Explained reference solution — 063. Merge Two Sorted Linked Lists
"""
063. Merge Two Sorted Linked Lists
Difficulty: Easy | Pattern: Dummy head and a moving tail
Prerequisites: Problem 061 pointers; merging sorted arrays

TASK
Merge two ascending sorted, finite acyclic linked lists into one ascending
sorted list. Reuse and rewire the original data nodes, and return the merged
head. The input lists share no nodes. If values tie, take a node from the
first list first. A temporary dummy node is allowed.

EXAMPLES
to_list(solve(from_list([1, 2, 4]), from_list([1, 3, 4]))) -> [1, 1, 2, 3, 4, 4].
solve(None, None) -> None.
Merging an empty first list returns the second list's original head.

CONSTRAINTS AND CONTRACT
0 <= total node count <= 100000. Both input lists are sorted nondecreasingly, contain integers, and are disjoint by identity. Original links may change.

SOLUTION EXPLANATION
The smaller current head is the smallest unconsumed value because both
remaining lists are sorted. Appending that node therefore extends the sorted
result correctly. Maintain the invariant that the result prefix contains
exactly the consumed nodes in sorted order, and tail is its last node.
Advance only the list whose head was consumed. When one becomes empty, all
remaining nodes in the other already form a sorted suffix and can be attached
in one operation. The dummy is never part of the returned data list.

This dummy-head pattern is useful whenever the first output node would
otherwise need a separate branch.

COMPLEXITY
Time O(m+n), auxiliary space O(1), where m and n are input lengths. Existing nodes become the result; the temporary dummy uses constant space.

COMMON MISTAKES
Advance the chosen input pointer and the output tail. Return dummy.next, not dummy. Tests must use fresh lists because this algorithm consumes and rewires their links.

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


def solve(first: ListNode | None, second: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    while first is not None and second is not None:
        if first.val <= second.val:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next
    tail.next = first if first is not None else second
    return dummy.next


def run_tests() -> None:
    assert solve(None, None) is None
    second = from_list([2, 3])
    assert solve(None, second) is second
    first = from_list([1])
    assert solve(first, None) is first
    assert to_list(solve(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(solve(from_list([-5, -1]), from_list([-4, 0, 8]))) == [-5, -4, -1, 0, 8]
    a, b = ListNode(1), ListNode(1)
    result = solve(a, b)
    assert result is a and result.next is b and b.next is None
    a1, a2, b1 = ListNode(2), ListNode(6), ListNode(4)
    a1.next = a2
    result = solve(a1, b1)
    assert result is a1 and a1.next is b1 and b1.next is a2 and a2.next is None


if __name__ == "__main__":
    run_tests()
    print("PASS: 063 — Merge Two Sorted Linked Lists")
