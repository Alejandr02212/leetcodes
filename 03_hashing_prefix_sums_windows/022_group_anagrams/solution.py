# Explained reference solution — 022. Group Anagrams
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

SOLUTION EXPLANATION
Sorting a word creates a canonical representation of its character multiset. Two words have the same sorted characters exactly when they are anagrams. A dictionary maps that key to a bucket. Python dictionaries retain insertion order, so creating a bucket at its first word preserves class order; appending preserves order inside each class.

COMPLEXITY
For w words of maximum length L: time O(w*(1 + L log(max(2,L)))). Auxiliary space O(w*(L+1)) for stored distinct keys and bucket references in the worst case, including O(w) output references; input strings are reused. The +1 accounts for empty words.

COMMON MISTAKES
A set of letters is not a valid anagram key because multiplicities matter. Preserve repeated words. Dictionary insertion order is defined in Python 3.7+.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


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
