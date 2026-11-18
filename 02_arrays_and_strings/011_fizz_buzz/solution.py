# Explained reference solution — 011. Fizz Buzz
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

SOLUTION EXPLANATION
Check the most specific condition first: a multiple of both 3 and 5 is a multiple of 15. The mutually exclusive elif chain then maps each number to exactly one output. Iterating in increasing order preserves the required position of every result.

COMPLEXITY
Time O(n), auxiliary working space O(1) beyond O(n) output under the stated bound.

COMMON MISTAKES
Checking divisibility by 3 first would label 15 as Fizz. range(1, n) omits n.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(n: int) -> list[str]:
    result = []
    for value in range(1, n + 1):
        if value % 15 == 0:
            result.append('FizzBuzz')
        elif value % 3 == 0:
            result.append('Fizz')
        elif value % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(value))
    return result


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
