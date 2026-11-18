# Explained reference solution — 045. Search a Sorted Matrix
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

SOLUTION EXPLANATION
The cross-row ordering guarantee makes the row-major sequence globally
sorted, not merely sorted within each row. Every virtual index maps uniquely
to a real cell through quotient and remainder by the column count. Binary
search can therefore access the middle value without creating a flattened
copy. Its usual invariant applies: if target exists, it lies within the
remaining virtual index interval. Empty matrices return False before any
indexing or division occurs.

COMPLEXITY
Time O(log(rows*cols+1)), auxiliary space O(1); no flattened matrix is allocated.

COMMON MISTAKES
Divide by the number of columns, not rows. This method fails if columns are sorted but the row-major sequence is not globally sorted.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


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
