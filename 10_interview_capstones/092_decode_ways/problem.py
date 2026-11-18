# Your practice file — 092. Decode a Digit String
"""
092. Decode a Digit String
Difficulty: Medium | Pattern: DP with validity checks on one- and two-character tokens
Prerequisites: Climbing stairs; strings; base cases with forbidden transitions.

TASK
Map '1' through '26' to letters A through Z. Return the number of ways
to split s into valid mapped tokens. Tokens cannot have leading zeros: '0' and
'06' are invalid, but '10' and '20' are valid. s contains only decimal digits.
By this problem's interface, an empty input string returns 0.

EXAMPLES
s='226' -> 3: '2|2|6', '22|6', '2|26'.
s='06' -> 0.
s='10' -> 1.

CONSTRAINTS AND CONTRACT
0 <= len(s) <= 500. ASCII digits '0' through '9' only.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Let dp[i] count valid decodings of the first i digits.
2. A nonzero last digit can extend dp[i-1].
3. A two-digit value in 10..26 can extend dp[i-2]; zero contributes only within valid pairs.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(s: str) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('') == 0
    assert solve('0') == 0
    assert solve('06') == 0
    assert solve('10') == 1
    assert solve('20') == 1
    assert solve('30') == 0
    assert solve('226') == 3
    assert solve('11106') == 2
    assert solve('100') == 0
    assert solve('27') == 1
    assert solve('1111') == 5


if __name__ == "__main__":
    run_tests()
    print("PASS: 092 — Decode a Digit String")
