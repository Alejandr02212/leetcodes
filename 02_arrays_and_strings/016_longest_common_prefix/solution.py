# Explained reference solution — 016. Longest Common Prefix
"""
016. Longest Common Prefix
Difficulty: Easy | Pattern: Column-wise scan and early exit
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return the longest string prefix shared by every word in words. If there are no words, return an empty string. Comparison is case-sensitive.

EXAMPLES
solve(['flower','flow','flight']) -> 'fl'
solve(['dog','cat']) -> ''

CONSTRAINTS AND CONTRACT
0 <= len(words) <= 200; 0 <= length of each word <= 200.

SOLUTION EXPLANATION
A shared prefix must match the first word at every included position. Scan its characters from left to right and check all other words. The first missing or mismatching position cannot be part of any common prefix; all earlier positions matched, so slicing there gives the longest possible answer. If no mismatch occurs, the entire first word is common.

COMPLEXITY
For w words and L characters in the first word: worst-case O(w*L) time, O(1) auxiliary working space, and up to O(L) space for the returned prefix.

COMMON MISTAKES
Check a word is long enough before indexing it. Empty words force an empty prefix. Avoid repeatedly concatenating single characters.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(words: list[str]) -> str:
    if not words:
        return ''
    first = words[0]
    for index, character in enumerate(first):
        for word_index in range(1, len(words)):
            word = words[word_index]
            if index >= len(word) or word[index] != character:
                return first[:index]
    return first


def run_tests() -> None:
    assert solve(['flower', 'flow', 'flight']) == 'fl'
    assert solve(['dog', 'cat']) == ''
    assert solve([]) == ''
    assert solve(['']) == ''
    assert solve(['abc', '']) == ''
    assert solve(['same', 'same']) == 'same'
    assert solve(['alone']) == 'alone'
    assert solve(['a', 'A']) == ''


if __name__ == "__main__":
    run_tests()
    print("PASS: 016 — Longest Common Prefix")
