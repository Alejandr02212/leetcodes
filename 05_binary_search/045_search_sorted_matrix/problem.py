# Your practice file — 045. Search a Sorted Matrix
"""
045. Search a Sorted Matrix
Difficulty: Medium | Pattern: Virtual flattened array + binary search
Prerequisites: Binary Search (041); row and column indexing.

TASK
Return whether target appears in a rectangular matrix. Each row is strictly
increasing, and the first number of each row is greater than the last number
of the previous row. Use O(log(rows*cols)) time without flattening the matrix.

EXAMPLES
solve([[1, 3, 5], [7, 9, 11]], 9) -> True.
solve([[1, 3, 5], [7, 9, 11]], 6) -> False.

CONSTRAINTS AND CONTRACT
0 <= rows, cols <= 1000; all rows have equal length; [] and [[], ...] are empty matrices. Values and target are integers.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Reading row by row gives one sorted sequence.
2. Convert a virtual index mid to row = mid // cols and column = mid % cols.
3. Run ordinary binary search over virtual indices.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(matrix: list[list[int]], target: int) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([[1, 3, 5], [7, 9, 11]], 9) is True
    assert solve([[1, 3, 5], [7, 9, 11]], 6) is False
    assert solve([], 1) is False
    assert solve([[], []], 1) is False
    assert solve([[4]], 4) is True
    assert solve([[4]], 3) is False
    assert solve([[1], [3], [5]], 3) is True
    assert solve([[1, 3, 5]], 5) is True
    assert solve([[1, 3, 5], [7, 9, 11]], 1) is True
    assert solve([[1, 3, 5], [7, 9, 11]], 12) is False


if __name__ == "__main__":
    run_tests()
    print("PASS: 045 — Search a Sorted Matrix")
