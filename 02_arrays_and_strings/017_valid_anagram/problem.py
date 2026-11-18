# Your practice file — 017. Valid Anagram
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Order can be ignored, counts cannot.
2. Count characters from the first string in a dictionary.
3. Decrement while scanning the second; reject any missing supply.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(first: str, second: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
