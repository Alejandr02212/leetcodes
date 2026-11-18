# Your practice file — 093. Word Break
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. reachable[end] means s[:end] can already be segmented.
2. Try a final dictionary word s[start:end] after a reachable prefix.
3. No final word is longer than the longest dictionary entry; bound the inner loop.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(s: str, word_dict: list[str]) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
