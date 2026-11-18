# Your practice file — 064. Remove the Nth Node From the End
"""
064. Remove the Nth Node From the End
Difficulty: Medium | Pattern: Fixed-gap pointers with a dummy head
Prerequisites: Problems 062 and 063 fast pointers and dummy heads

TASK
Remove the nth node counting from the end of a nonempty acyclic linked
list, and return the resulting head. n=1 removes the last node. Reuse all
retained nodes and rewire links in place. The valid n precondition is
guaranteed; the removed node does not need its own next pointer cleared.

EXAMPLES
to_list(solve(from_list([1, 2, 3, 4, 5]), 2)) -> [1, 2, 3, 5].
to_list(solve(from_list([1, 2]), 2)) -> [2].
solve(from_list([7]), 1) -> None.

CONSTRAINTS AND CONTRACT
1 <= n <= node count <= 100000. The input contains integer values and has no cycle. Mutation is required; replacement data nodes are not allowed.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. To delete a singly linked node, find its predecessor.
2. Use a dummy predecessor before the real head, so removing the head is ordinary.
3. Separate fast and slow by n+1 edges; when fast reaches None, slow precedes the target.

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


def solve(head: ListNode, n: int) -> ListNode | None:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(ListNode(7), 1) is None
    assert to_list(solve(from_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(solve(from_list([1, 2]), 2)) == [2]
    assert to_list(solve(from_list([1, 2]), 1)) == [1]
    assert to_list(solve(from_list([4, 4, 4]), 2)) == [4, 4]
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next, b.next = b, c
    result = solve(a, 2)
    assert result is a and a.next is c and c.next is None
    a, b = ListNode(5), ListNode(6)
    a.next = b
    assert solve(a, 2) is b


if __name__ == "__main__":
    run_tests()
    print("PASS: 064 — Remove the Nth Node From the End")
