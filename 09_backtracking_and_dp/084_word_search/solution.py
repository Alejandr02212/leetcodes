# Explained reference solution — 084. Word Search
"""
084. Word Search
Difficulty: Medium | Pattern: Grid backtracking with path-local visited state
Prerequisites: Flood fill; backtracking; difference between global and path-local visitation.

TASK
Return whether word can be spelled by a path through a rectangular board
of single-character strings. Consecutive letters must be horizontally or
vertically adjacent. A board cell can be used at most once within a path, but
different attempted paths may reuse it. Leave the board unchanged. The empty
word always exists, including on an empty board.

EXAMPLES
board=[['A','B'],['C','D']], word='ABD' -> True.
board=[['A','B'],['C','D']], word='ABA' -> False (would reuse A).
board=[], word='' -> True.

CONSTRAINTS AND CONTRACT
0 <= rows, cols <= 6; rectangular board; 0 <= len(word) <= 12. Characters are case-sensitive.

SOLUTION EXPLANATION
A state matches word[index] at one coordinate while used contains exactly
the cells occupied by earlier letters of this candidate path. Reject invalid
coordinates, wrong letters, and reused cells. If this is the final matching
letter, the path proves success. Otherwise mark the cell, explore four possible
next letters, and unmark before returning. This restoration lets sibling paths
try the same cell in different contexts. Every valid path starts at some cell
and uses one of these four moves at every step, so the exhaustive search finds
it. A global visited set would incorrectly discard alternate paths. The word
length bound limits recursion depth to 12; the board itself is never edited.

COMPLEXITY
Let R,C be board dimensions and L=len(word). For L>0, O(R*C*4^L) time is a simple upper bound, and O(L) auxiliary recursion/visited space. Empty word takes O(1).

COMMON MISTAKES
Do not retain visits across independent paths. Matching a cell is not enough unless every letter matches. Empty-word handling must come before reading word[0].

Run this file with python3 solution.py to check the reference implementation.
"""

from __future__ import annotations

def solve(board: list[list[str]], word: str) -> bool:
    if not word:
        return True
    if not board or not board[0]:
        return False
    rows, cols = len(board), len(board[0])
    if len(word) > rows * cols:
        return False
    used = set()
    def visit(r, c, index):
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if (r, c) in used or board[r][c] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        used.add((r, c))
        found = any(visit(r + dr, c + dc, index + 1)
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        used.remove((r, c))
        return found
    return any(visit(r, c, 0) for r in range(rows) for c in range(cols))


def run_tests() -> None:
    assert solve([], '') is True
    assert solve([], 'A') is False
    assert solve([[]], 'A') is False
    assert solve([['A']], 'A') is True
    assert solve([['A']], 'AA') is False
    board = [['A', 'B'], ['C', 'D']]
    assert solve(board, 'ABD') is True
    assert solve(board, 'ABA') is False
    assert solve(board, 'AD') is False
    assert board == [['A', 'B'], ['C', 'D']]
    board = [list('ABCE'), list('SFCS'), list('ADEE')]
    assert solve(board, 'ABCCED') is True
    assert solve(board, 'SEE') is True
    assert solve(board, 'ABCB') is False


if __name__ == "__main__":
    run_tests()
    print("PASS: 084 — Word Search")
