#!/usr/bin/python3
"""Solves the N-queens puzzle.
"""
import sys


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def chessboard_mtn(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chessboard]
    return chessboard


def chessboard_oop(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(chessboard_oop, chessboard))
    return chessboard


def solve_nqueens(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    """
    if queens == len(chessboard):
        solutions.append(get_solution(chessboard))
        return solutions

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_chessboard = chessboard_oop(chessboard)
            tmp_chessboard[row][c] = "Q"
            mark_positions(tmp_chessboard, row, c)
            solutions = solve_nqueens(tmp_chessboard, row + 1,
                                      queens + 1, solutions)

    return solutions


def mark_positions(chessboard, row, xcolx):
    """Mark out spots on a chessboard.
    """
    for c in range(xcolx + 1, len(chessboard)):
        chessboard[row][c] = "x"
    for c in range(xcolx - 1, -1, -1):
        chessboard[row][c] = "x"
    for r in range(row + 1, len(chessboard)):
        chessboard[r][xcolx] = "x"
    for r in range(row - 1, -1, -1):
        chessboard[r][xcolx] = "x"
    c = xcolx + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    c = xcolx + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = xcolx - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = chessboard_mtn(int(sys.argv[1]))
    solutions = solve_nqueens(chessboard, 0, 0, [])
    for xx in solutions:
        print(xx)
