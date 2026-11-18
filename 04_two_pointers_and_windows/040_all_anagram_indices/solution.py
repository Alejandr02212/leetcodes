# Explained reference solution — 040. Find All Anagram Start Indices
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

SOLUTION EXPLANATION
A width-sized substring is an anagram exactly when its 26 letter counts
equal pattern's counts. The rolling updates maintain those counts for each
successive window in constant alphabet-size work. Every possible start
appears once as a full window's right endpoint is processed. Appending its
corresponding start records all and only matches; scanning right endpoints
in order also returns starts in increasing order. Moving just one step at
a time preserves overlapping matches.

COMPLEXITY
Time O(m+n), auxiliary space O(1) for fixed alphabet, plus O(r) output; m = len(pattern), n = len(text), r = number of matches.

COMMON MISTAKES
Do not skip ahead by pattern length after a match: overlapping answers would be lost. Empty pattern includes the boundary after the final character.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str, pattern: str) -> list[int]:
    width = len(pattern)
    if width == 0:
        return list(range(len(text) + 1))
    if width > len(text):
        return []
    needed = [0] * 26
    window = [0] * 26
    for char in pattern:
        needed[ord(char) - ord('a')] += 1
    answer = []
    for right, char in enumerate(text):
        window[ord(char) - ord('a')] += 1
        if right >= width:
            window[ord(text[right - width]) - ord('a')] -= 1
        if right >= width - 1 and window == needed:
            answer.append(right - width + 1)
    return answer


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
