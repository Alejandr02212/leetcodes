# Your practice file — 060. Build a Prefix Dictionary
"""
060. Build a Prefix Dictionary
Difficulty: Medium | Pattern: Trie: share common prefixes in a character tree
Prerequisites: Dictionaries, nested structures, and classes

TASK
Process operations of the form [command, word] in order. Commands are
'insert', 'search', and 'starts_with'. Insert stores a word and returns None;
search returns whether the complete word has been inserted; starts_with
returns whether any stored word begins with the prefix. Return one result
per operation. Duplicate insertions have no effect. The empty string is a
valid word; empty-prefix lookup is True only if at least one word is stored.
Implement a trie rather than scanning all stored words.

EXAMPLES
solve([["insert", "apple"], ["search", "app"], ["starts_with", "app"], ["insert", "app"], ["search", "app"]]) -> [None, False, True, None, True].
solve([["starts_with", ""], ["insert", ""], ["search", ""]]) -> [False, None, True].
solve([]) -> [].

CONSTRAINTS AND CONTRACT
At most 10000 operations; words contain lowercase English letters and may be empty. Total characters across operations <= 100000. Commands are valid. Preserve the input operations.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Each node maps a next character to another node.
2. Mark a terminal node separately: reaching 'app' in 'apple' does not mean 'app' was inserted.
3. Traversal failure means False; a completed search checks the terminal flag, while a prefix query only needs an existing path and a nonempty dictionary.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(operations: list[list[str]]) -> list[bool | None]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == []
    assert solve([["search", "a"], ["starts_with", ""]]) == [False, False]
    assert solve([["insert", "apple"], ["search", "app"], ["starts_with", "app"], ["insert", "app"], ["search", "app"]]) == [None, False, True, None, True]
    assert solve([["insert", "a"], ["insert", "a"], ["search", "a"], ["search", "ab"]]) == [None, None, True, False]
    assert solve([["insert", ""], ["search", ""], ["starts_with", ""], ["starts_with", "a"]]) == [None, True, True, False]
    assert solve([["insert", "cat"], ["insert", "car"], ["starts_with", "ca"], ["search", "ca"], ["search", "car"]]) == [None, None, True, False, True]
    assert solve([["insert", "abc"], ["starts_with", ""], ["search", ""], ["starts_with", "abcd"]]) == [None, True, False, False]


if __name__ == "__main__":
    run_tests()
    print("PASS: 060 — Build a Prefix Dictionary")
