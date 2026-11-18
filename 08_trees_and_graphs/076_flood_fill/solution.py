# Explained reference solution — 076. Flood Fill
"""
076. Flood Fill
Difficulty: Easy | Pattern: Grid traversal with an explicit stack
Prerequisites: 075 Number of Islands; coordinate bounds; sets or marking visited cells.

TASK
Given a rectangular integer image and a valid starting coordinate (sr, sc),
change every pixel in its four-directionally connected component to color. The
component contains only pixels equal to the starting pixel's ORIGINAL color.
Return the image. Mutating the supplied image in place is allowed and expected;
do not cross diagonally or repaint a disconnected region.

EXAMPLES
image=[[1,1,0],[1,0,0]], sr=0, sc=0, color=7 -> [[7,7,0],[7,0,0]].
image=[[2,0],[0,2]], sr=0, sc=0, color=3 -> [[3,0],[0,2]]: diagonals do not connect.
image=[[4]], sr=0, sc=0, color=4 -> [[4]].

CONSTRAINTS AND CONTRACT
1 <= rows, cols <= 200. The image is rectangular; sr/sc are valid. Pixel values and color are integers.

SOLUTION EXPLANATION
A flood fill is graph traversal: pixels are vertices and four-directional
adjacency supplies edges. Save the old color, paint the starting pixel, then
repeatedly paint and push each eligible neighbor. Every painted pixel was reached
through a path of old-colored pixels, so no unrelated component changes.
Conversely, following any such path from the start eventually visits its next
pixel; therefore the entire component is painted. Painting BEFORE pushing is
our visited marker. The old==color guard is essential because otherwise painting
would not distinguish discovered pixels. An explicit stack avoids Python's
recursion-depth limit on large connected images.

COMPLEXITY
Let R and C be image dimensions. Time O(R*C) worst case; auxiliary stack space O(R*C). The returned image is the original object, so there is no output copy.

COMMON MISTAKES
Checking image[sr][sc] after repainting loses the old color. Marking only on pop creates duplicate work. Recursive DFS can overflow on a long component.

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    old = image[sr][sc]
    if old == color:
        return image
    rows, cols = len(image), len(image[0])
    image[sr][sc] = color
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old:
                image[nr][nc] = color
                stack.append((nr, nc))
    return image


def run_tests() -> None:
    image = [[1, 1, 0], [1, 0, 0]]
    assert solve(image, 0, 0, 7) == [[7, 7, 0], [7, 0, 0]]
    assert image == [[7, 7, 0], [7, 0, 0]]
    assert solve([[2, 0], [0, 2]], 0, 0, 3) == [[3, 0], [0, 2]]
    assert solve([[4]], 0, 0, 4) == [[4]]
    assert solve([[1]], 0, 0, -2) == [[-2]]
    assert solve([[0, 1, 1, 0]], 0, 2, 8) == [[0, 8, 8, 0]]
    assert solve([[3], [3], [0], [3]], 1, 0, 9) == [[9], [9], [0], [3]]
    assert solve([[1, 1], [1, 1]], 1, 1, 0) == [[0, 0], [0, 0]]


if __name__ == "__main__":
    run_tests()
    print("PASS: 076 — Flood Fill")
