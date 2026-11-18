# Explained reference solution — 092. Decode a Digit String
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

SOLUTION EXPLANATION
Classify decodings by their final token. A valid one-digit token is 1..9
and leaves any decoding of the previous prefix. A valid two-digit token is
10..26 and leaves a decoding two positions earlier. These disjoint categories
sum to the transition. dp[0]=1 represents the one way to finish after consuming
all digits, which is necessary for a leading valid token to contribute. The
external empty-input convention is handled separately. Comparing exactly two
ASCII digits lexicographically with '10' and '26' is equivalent to numeric
comparison here. Invalid prefixes naturally have count zero and cannot revive
unless a valid transition comes from an earlier valid prefix.

COMPLEXITY
For n digits, O(n) DP operations and O(n) integer slots. Counts can have O(n) bits; a conservative exact-arithmetic bound is O(n^2) bit work and O(n^2) bits for the full table. Rolling state can reduce storage.

COMMON MISTAKES
Do not count '0' alone or accept '06' as six. A prefix count of zero is not always an early-stop signal before considering a two-digit token (for example '10').

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(s: str) -> int:
    if not s:
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if i >= 2 and '10' <= s[i - 2:i] <= '26':
            dp[i] += dp[i - 2]
    return dp[-1]


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
