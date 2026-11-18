# Your practice file — 063. Merge Two Sorted Linked Lists
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Repeatedly append the smaller current node to an output tail.
2. A dummy head removes the special case for the first appended node.
3. When one list ends, attach the entire remaining suffix of the other.

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


def solve(first: ListNode | None, second: ListNode | None) -> ListNode | None:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
