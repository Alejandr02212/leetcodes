# Your practice file — 011. Fizz Buzz
"""
011. Fizz Buzz
Difficulty: Easy | Pattern: Ordered conditions and mapping a range
Prerequisites: Earlier exercises in this stage; basic Python expressions.

TASK
For each integer from 1 through n, return a string: FizzBuzz if divisible by both 3 and 5, Fizz if only by 3, Buzz if only by 5, otherwise its decimal representation.

EXAMPLES
solve(5) -> ['1', '2', 'Fizz', '4', 'Buzz']
solve(0) -> []

CONSTRAINTS AND CONTRACT
0 <= n <= 10000.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Build one string per number.
2. Check the combined case before the individual cases.
3. Divisibility by both means remainder zero modulo 15.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(n: int) -> list[str]:
    # Write your solution here.
    sol = []
    for i in range(1,n + 1):
        if i % 15 == 0:
            sol.append("FizzBuzz")
        elif i % 3 == 0:
            sol.append("Fizz")
        elif i % 5 == 0:
            sol.append("Buzz")
        else:
            sol.append(str(i))

    return sol
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve(0) == []
    assert solve(1) == ['1']
    assert solve(3) == ['1', '2', 'Fizz']
    assert solve(5)[-1] == 'Buzz'
    assert solve(15)[-1] == 'FizzBuzz'
    assert solve(30)[-1] == 'FizzBuzz'
    assert solve(16)[-1] == '16'


if __name__ == "__main__":
    run_tests()
    print("PASS: 011 — Fizz Buzz")
