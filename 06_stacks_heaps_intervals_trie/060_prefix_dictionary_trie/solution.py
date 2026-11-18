# Explained reference solution — 060. Build a Prefix Dictionary
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

SOLUTION EXPLANATION
A trie represents each distinct prefix once. Starting at the root, one
edge consumes one character, so reaching a node means exactly that the
traversed prefix was created by an insertion. The terminal marker records
complete words independently of children: a node can terminate 'app' and
still lead to 'apple'. Insertion creates missing edges and marks the final
node. Search follows the path and checks that marker. Prefix lookup only
needs a path, plus the dictionary's nonempty flag for the empty prefix.

The marker '#' cannot collide with an edge because words use only a-z.
has_words makes the stated empty-dictionary behavior explicit.

COMPLEXITY
Expected time O(C + q) for q operations and C characters examined, using hash dictionaries. Trie auxiliary space O(S) for total inserted characters S; result space O(q). Each individual operation is O(length + 1).

COMMON MISTAKES
A prefix path does not imply a complete word. Empty words terminate at the root. Define empty-prefix behavior explicitly; this exercise returns False when no word has been inserted.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(operations: list[list[str]]) -> list[bool | None]:
    class Trie:
        def __init__(self):
            self.root = {}
            self.has_words = False

        def insert(self, word):
            node = self.root
            for character in word:
                if character not in node:
                    node[character] = {}
                node = node[character]
            node['#'] = True
            self.has_words = True

        def lookup(self, word, complete):
            node = self.root
            for character in word:
                if character not in node:
                    return False
                node = node[character]
            return '#' in node if complete else self.has_words

    trie = Trie()
    answer = []
    for command, word in operations:
        if command == 'insert':
            trie.insert(word)
            answer.append(None)
        else:
            answer.append(trie.lookup(word, command == 'search'))
    return answer


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
