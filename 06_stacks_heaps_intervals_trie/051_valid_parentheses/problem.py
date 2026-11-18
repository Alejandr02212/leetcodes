# Your practice file — 051. Valid Parentheses
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. The last opening bracket must be the first one closed.
2. Store opening brackets in a list used as a stack.
3. On a closer, reject an empty stack or a mismatched top; finally require an empty stack.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
