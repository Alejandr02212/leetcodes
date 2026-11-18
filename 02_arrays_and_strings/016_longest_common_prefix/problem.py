# Your practice file — 016. Longest Common Prefix
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. The answer must be a prefix of the first word.
2. Check one character position across all words.
3. Stop at the first mismatch or ended word.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(words: list[str]) -> str:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
