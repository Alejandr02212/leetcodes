# Explained reference solution — 093. Word Break
"""
093. Word Break
Difficulty: Medium | Pattern: Prefix DP over a dictionary
Prerequisites: Sets; substring boundaries; boolean reachability DP.

TASK
Return whether s can be segmented into zero or more words from word_dict.
Words may be reused. Dictionary entries are nonempty, and duplicates are allowed.
Matching is case-sensitive. An empty string returns True using zero words.
Do not modify word_dict.

EXAMPLES
s='applepenapple', word_dict=['apple','pen'] -> True.
s='catsandog', word_dict=['cats','dog','sand','and','cat'] -> False.
s='', word_dict=[] -> True.

CONSTRAINTS AND CONTRACT
0 <= len(s) <= 300; at most 1000 dictionary entries; 1 <= word length <= 30.

SOLUTION EXPLANATION
Define reachable[i] to mean the prefix ending just before i admits a
complete segmentation. The empty prefix is reachable. Any nonempty valid
segmentation ends with some dictionary word s[start:end], preceded by a
reachable prefix. Trying every permitted start therefore finds every valid
segmentation and creates no invalid ones. Process end in ascending order so
all shorter prefixes are known. A set makes word lookup efficient, and the
maximum dictionary word length limits how far back a final word can begin.
This is boolean DP: many segmentations of the same prefix share one useful
state, avoiding the repeated work of naive recursive splitting.

COMPLEXITY
Let n=len(s), D be total dictionary characters, and L=min(n, maximum word length). Expected time O(D + n*(L+1)^2), accounting for Python substring copying/hashing and an empty dictionary; auxiliary O(n + number of distinct dictionary words) references, plus O(L) temporary substring characters. Dictionary word strings are reused.

COMMON MISTAKES
Substring lookup alone is insufficient: the prefix before it must be reachable. Python slices cost time; O(n*L) ignores that copying and hashing. Do not reject the empty string.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    max_length = max((len(word) for word in words), default=0)
    reachable = [False] * (len(s) + 1)
    reachable[0] = True
    for end in range(1, len(s) + 1):
        for start in range(max(0, end - max_length), end):
            if reachable[start] and s[start:end] in words:
                reachable[end] = True
                break
    return reachable[-1]


def run_tests() -> None:
    assert solve('', []) is True
    assert solve('a', []) is False
    assert solve('applepenapple', ['apple', 'pen']) is True
    assert solve('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) is False
    assert solve('aaaaaaa', ['aaaa', 'aaa']) is True
    assert solve('aaaaab', ['a', 'aa', 'aaa']) is False
    assert solve('ab', ['a', 'b', 'a']) is True
    assert solve('Ab', ['ab']) is False
    assert solve('carpet', ['car', 'carpet', 'pet']) is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 093 — Word Break")
