# Explained reference solution — 017. Valid Anagram
"""
017. Valid Anagram
Difficulty: Easy | Pattern: Frequency map
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
Return whether strings first and second contain exactly the same characters with the same multiplicities. Order does not matter; spaces and case do matter.

EXAMPLES
solve('listen', 'silent') -> True
solve('aab', 'abb') -> False

CONSTRAINTS AND CONTRACT
0 <= lengths <= 10000. Strings may contain any Python characters.

SOLUTION EXPLANATION
Count each character in the first string, then spend one occurrence for every character in the second. At every point counts records the unspent supply. A missing occurrence makes an anagram impossible. Equal lengths ensure that if every requested occurrence is available, the full supply is consumed and the multisets are equal.

COMPLEXITY
For lengths n and m: expected time O(n+m), auxiliary space O(u) for u distinct characters in first. Dictionary operations have expected O(1) cost.

COMMON MISTAKES
A set loses multiplicity: aab and abb have the same set. Do not lowercase unless the specification asks for it.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    counts = {}
    for character in first:
        counts[character] = counts.get(character, 0) + 1
    for character in second:
        if counts.get(character, 0) == 0:
            return False
        counts[character] -= 1
    return True


def run_tests() -> None:
    assert solve('listen', 'silent') is True
    assert solve('aab', 'abb') is False
    assert solve('', '') is True
    assert solve('a', '') is False
    assert solve('Aa', 'aa') is False
    assert solve('a b', 'b a') is True
    assert solve('ééx', 'xéé') is True


if __name__ == "__main__":
    run_tests()
    print("PASS: 017 — Valid Anagram")
