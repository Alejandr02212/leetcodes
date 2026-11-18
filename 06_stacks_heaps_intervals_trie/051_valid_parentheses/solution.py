# Explained reference solution — 051. Valid Parentheses
"""
051. Valid Parentheses
Difficulty: Easy | Pattern: Stack: match the latest unfinished opener
Prerequisites: Functions, dictionaries, loops; problem 010 palindrome warmup

TASK
Given a string containing only (), [] and {}, return whether every closing
bracket matches the most recent unmatched opening bracket and all brackets
are eventually closed. The empty string is valid.

EXAMPLES
solve("([]{})") -> True: every inner pair closes before its outer pair.
solve("([)]") -> False: ')' tries to close '['.
solve("") -> True.

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 10000. Characters belong to ()[]{}. Do not modify the input.

SOLUTION EXPLANATION
A stack records the unfinished work. After each processed character, its
contents are exactly the opening brackets whose closing partners have not
appeared, in nesting order. An opener extends that unfinished suffix. A
closer must consume the latest opener; any other match would cross pairs.
Reject immediately when that requirement fails. At the end, an empty stack
means every required partner was consumed, which proves validity.

Template: push items that wait for a future event; when that event arrives,
inspect or remove the latest pending item.

COMPLEXITY
Time O(n), space O(n) in the deepest nesting, where n = len(text). The returned bool is O(1).

COMMON MISTAKES
Counting brackets is insufficient: '([)]' has balanced counts but invalid nesting. Check the stack before popping. Reject leftover openers.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for character in text:
        if character in '([{':
            stack.append(character)
        elif not stack or stack.pop() != pairs[character]:
            return False
    return not stack


def run_tests() -> None:
    assert solve("") is True
    assert solve("()[]{}") is True
    assert solve("{[()]}") is True
    assert solve("([)]") is False
    assert solve(")") is False
    assert solve("((") is False
    assert solve("([]){()}") is True
    assert solve("[(])") is False


if __name__ == "__main__":
    run_tests()
    print("PASS: 051 — Valid Parentheses")
