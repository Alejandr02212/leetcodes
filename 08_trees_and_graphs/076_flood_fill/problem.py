# Your practice file — 076. Flood Fill
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Remember the starting color before changing any pixel.
2. Mark a pixel when putting it on your stack, so another neighbor cannot add it again.
3. If the old and new colors match, return immediately: repainting cannot mark visits.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
