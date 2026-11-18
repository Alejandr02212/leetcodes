# Explained reference solution — 053. Evaluate Reverse Polish Notation
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

SOLUTION EXPLANATION
Postfix notation places an operator after its two already completed
operands. At every step, the stack stores the values of completed
subexpressions that still await an operator. A number creates a new completed
expression. An operator combines the two most recent expressions into one,
preserving the invariant. Validity guarantees that exactly the full
expression remains at the end.

Python's // rounds negative answers down, while this problem truncates toward
zero. Divide nonnegative magnitudes and then restore the sign. This also
avoids losing precision through float conversion.

COMPLEXITY
O(t) arithmetic operations and O(t) stack space for t tokens, under the usual unit-cost integer model. With unbounded integers, arithmetic time also depends on operand bit lengths.

COMMON MISTAKES
The first pop is the right operand. -7 // 3 is -3 but truncation requires -2. int(left / right) can lose precision or overflow through floating point.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token not in ('+', '-', '*', '/'):
            stack.append(int(token))
            continue
        right = stack.pop()
        left = stack.pop()
        if token == '+':
            value = left + right
        elif token == '-':
            value = left - right
        elif token == '*':
            value = left * right
        else:
            value = abs(left) // abs(right)
            if (left < 0) != (right < 0):
                value = -value
        stack.append(value)
    return stack[0]


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
