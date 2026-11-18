# Your practice file — 037. Longest Repeating Character Replacement
"""
037. Longest Repeating Character Replacement
Difficulty: Medium | Pattern: Variable window + frequency constraint
Prerequisites: Variable windows (029–030); character counts.

TASK
Return the longest substring that can become one repeated letter by
replacing at most k of its characters. You may choose the repeated letter.
Replacements affect only the chosen substring; return its length.

EXAMPLES
solve('AABABBA', 1) -> 4: 'AABA' can become 'AAAA'.
solve('ABAB', 2) -> 4.

CONSTRAINTS AND CONTRACT
0 <= len(text) <= 100000; uppercase English letters only; k >= 0.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A window needs length minus its largest character frequency replacements.
2. Shrink while that number exceeds k.
3. With 26 letters, recomputing max(counts) is constant-size work and keeps the invariant explicit.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(text: str, k: int) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve('AABABBA', 1) == 4
    assert solve('ABAB', 2) == 4
    assert solve('', 0) == 0
    assert solve('AAAA', 0) == 4
    assert solve('ABCDE', 0) == 1
    assert solve('ABCDE', 10) == 5
    assert solve('ABBB', 1) == 4
    from itertools import product
    for size in range(6):
        for letters in product('AB', repeat=size):
            text = ''.join(letters)
            for k in range(3):
                expected = 0
                for i in range(size):
                    for j in range(i + 1, size + 1):
                        segment = text[i:j]
                        if len(segment) - max(segment.count(c) for c in set(segment)) <= k:
                            expected = max(expected, len(segment))
                assert solve(text, k) == expected


if __name__ == "__main__":
    run_tests()
    print("PASS: 037 — Longest Repeating Character Replacement")
