# Your practice file — 040. Find All Anagram Start Indices
"""
040. Find All Anagram Start Indices
Difficulty: Medium | Pattern: Fixed window + character frequencies
Prerequisites: Permutation in a String (036).

TASK
Return the increasing list of every 0-based index where an anagram of
pattern begins in text. Matches may overlap. The empty pattern matches
every boundary, giving list(range(len(text) + 1)).

EXAMPLES
solve('cbaebabacd', 'abc') -> [0, 6].
solve('abab', 'ab') -> [0, 1, 2].

CONSTRAINTS AND CONTRACT
0 <= len(text), len(pattern) <= 100000; lowercase English letters only.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Reuse the count-window idea from 036.
2. On a match ending at right, the start is right - len(pattern) + 1.
3. Collect every match instead of returning on the first.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str, pattern: str) -> list[int]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('cbaebabacd', 'abc') == [0, 6]
    assert solve('abab', 'ab') == [0, 1, 2]
    assert solve('', '') == [0]
    assert solve('abc', '') == [0, 1, 2, 3]
    assert solve('', 'a') == []
    assert solve('ab', 'abc') == []
    assert solve('aaaa', 'aa') == [0, 1, 2]
    assert solve('aabb', 'ab') == [1]
    from itertools import product
    for size in range(5):
        for letters in product('ab', repeat=size):
            text = ''.join(letters)
            for pattern in ('', 'a', 'ab', 'aa', 'aab'):
                expected = [i for i in range(size - len(pattern) + 1)
                            if sorted(text[i:i + len(pattern)]) == sorted(pattern)]
                assert solve(text, pattern) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 040 — Find All Anagram Start Indices")
