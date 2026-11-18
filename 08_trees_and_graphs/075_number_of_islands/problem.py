# Your practice file — 075. Count Islands in a Grid
"""
075. Count Islands in a Grid
Difficulty: Medium | Pattern: Flood fill: one traversal per connected component
Prerequisites: Problem 067 iterative DFS; sets of coordinate tuples

TASK
A rectangular grid contains '1' for land and '0' for water. Count the
islands, where land cells connect only vertically and horizontally, never
diagonally. Preserve the grid. An empty grid, including zero columns,
contains zero islands.

EXAMPLES
solve([["1", "1", "0"], ["0", "1", "0"], ["1", "0", "1"]]) -> 3.
solve([["1", "0"], ["0", "1"]]) -> 2: diagonal land is separate.
solve([]) -> 0.

CONSTRAINTS AND CONTRACT
0 <= rows, columns <= 300. Every row has the same length. Cells are strings '0' or '1', not integers. The input must remain unchanged.

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Scan for a land cell not visited before; it begins a new island.
2. Use a stack to visit all land reachable from it.
3. Mark a cell visited when adding it to the stack so several neighbors cannot schedule it repeatedly.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(grid: list[list[str]]) -> int:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


def run_tests() -> None:
    assert solve([]) == 0
    assert solve([[], []]) == 0
    assert solve([["0", "0"]]) == 0
    assert solve([["1"]]) == 1
    assert solve([["1", "0"], ["0", "1"]]) == 2
    assert solve([["1", "1", "0"], ["0", "1", "0"], ["1", "0", "1"]]) == 3
    assert solve([["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]]) == 1
    grid = [["1", "0", "1"], ["1", "0", "1"]]
    before = [row[:] for row in grid]
    assert solve(grid) == 2 and grid == before
    assert solve([["1"] * 100 for _ in range(100)]) == 1


if __name__ == "__main__":
    run_tests()
    print("PASS: 075 — Count Islands in a Grid")
