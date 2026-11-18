# Your practice file — 022. Group Anagrams
"""
022. Group Anagrams
Difficulty: Medium | Pattern: Canonical key and buckets
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Group words that are anagrams of one another. Return groups in order of first appearance of their anagram class; preserve input order within each group. Comparison is case-sensitive.

EXAMPLES
solve(['eat','tea','tan','ate','nat','bat']) -> [['eat','tea','ate'],['tan','nat'],['bat']]
solve(['','']) -> [['','']]

CONSTRAINTS AND CONTRACT
0 <= len(words) <= 1000; 0 <= word lengths <= 100; arbitrary characters. Do not mutate words.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Give every anagram class the same key.
2. Sorted characters are such a key.
3. Map each key to an append-only list.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(words: list[str]) -> list[list[str]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert solve([]) == []
    assert solve(['', '']) == [['', '']]
    assert solve(['aab', 'abb', 'baa']) == [['aab', 'baa'], ['abb']]
    assert solve(['a', 'A']) == [['a'], ['A']]
    assert solve(['x', 'x']) == [['x', 'x']]
    assert solve(['ab', 'z', 'ba']) == [['ab', 'ba'], ['z']]


if __name__ == "__main__":
    run_tests()
    print("PASS: 022 — Group Anagrams")
