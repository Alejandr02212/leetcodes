# Your practice file — 053. Evaluate Reverse Polish Notation
"""
053. Evaluate Reverse Polish Notation
Difficulty: Medium | Pattern: Stack: evaluate an expression from completed operands
Prerequisites: Problem 051; integer arithmetic and operand order

TASK
Evaluate a valid postfix expression represented by tokens. An integer
token pushes an operand; each of '+', '-', '*', '/' consumes the previous
two results and pushes the result. Division truncates toward zero. Return
the final integer. Use integer arithmetic even for very large operands.

EXAMPLES
solve(["2", "1", "+", "3", "*"]) -> 9, meaning (2 + 1) * 3.
solve(["7", "-3", "/"]) -> -2, because truncation is toward zero.
solve(["5"]) -> 5.

CONSTRAINTS AND CONTRACT
The expression is valid and leaves exactly one result. Tokens are integer strings or + - * /. No divisor is zero. Python integers may be arbitrarily large.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. A stack holds results of completed subexpressions.
2. Pop right operand first, then left operand; subtraction and division care about order.
3. Compute abs(left) // abs(right), then choose the division sign; avoid float conversion.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(tokens: list[str]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(["2", "1", "+", "3", "*"]) == 9
    assert solve(["7", "-3", "/"]) == -2
    assert solve(["-7", "3", "/"]) == -2
    assert solve(["-7", "-3", "/"]) == 2
    assert solve(["5"]) == 5
    assert solve(["8", "3", "-"]) == 5
    assert solve(["4", "13", "5", "/", "+"]) == 6
    assert solve([str(10**80 + 2), "3", "/"]) == (10**80 + 2) // 3
    assert solve(["0", "8", "/"]) == 0


if __name__ == "__main__":
    run_tests()
    print("PASS: 053 — Evaluate Reverse Polish Notation")
