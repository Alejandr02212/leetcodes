# Explained reference solution — 075. Count Islands in a Grid
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

SOLUTION EXPLANATION
Think of land cells as graph vertices and orthogonal adjacency as edges.
A DFS starting from unvisited land reaches exactly its connected component:
every scheduled cell is land connected by a discovered path, and every
reachable neighbor is eventually scheduled. Marking on insertion ensures
each cell is processed once. After the traversal, that whole island is
visited, so later scanning cannot count it again. Conversely, every island
has a first cell encountered by the scan, which starts one traversal and
increments the count once. Thus the count equals the number of components.

A separate visited set preserves the input. Replacing visited land with '0'
is another common approach only when mutation is allowed.

COMPLEXITY
Time O(R*C) for R rows and C columns: each cell is scanned and each land cell's four neighbors are checked once. Auxiliary space O(R*C) for visited and DFS stack; returned integer O(1).

COMMON MISTAKES
Use four neighbors, not eight. Compare string '1', not integer 1. Mark when pushing rather than popping. An iterative traversal avoids recursion overflow on large connected land.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, columns = len(grid), len(grid[0])
    visited = set()
    islands = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] != '1' or (row, column) in visited:
                continue
            islands += 1
            visited.add((row, column))
            stack = [(row, column)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (0 <= nr < rows and 0 <= nc < columns
                            and grid[nr][nc] == '1' and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        stack.append((nr, nc))
    return islands


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
