# Your practice file — 084. Word Search
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

YOUR TURN
Implement solve below. Helper structures are supplied where needed.
Run: python3 problem.py
Read the tests for extra examples. They are local checks, not a proof of correctness.

HINTS (read one at a time when needed)
1. Try every board cell as a possible first letter.
2. The visited set belongs to the current search path, not the whole search.
3. Remove the current cell from visited when returning, whether a branch succeeds or fails.

The adjacent solution.py contains the explanation and reference code.
"""

from __future__ import annotations

def solve(board: list[list[str]], word: str) -> bool:
    # Write your solution here.
    raise NotImplementedError("Your turn: implement solve, then run this file again.")


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
