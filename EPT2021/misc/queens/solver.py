import numpy as np

N = 18


def printSolution(board):
    np.set_printoptions(threshold=np.inf)
    print(board)
    for i in range(N):
        increment = 1
        for j in range(N):
            if board[i][j] == 1:
                print(increment, end=',')
            increment += 1


def isSafe(board, row, col):
    for i in range(col):  # Check this row on left side
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1),  # Check upper diagonal on left side
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1),  # Check lower diagonal on left side
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, predefined):
    if col >= N:  # If all queens are placed then return true
        return True

    if predefined[col] is not None:
        if not isSafe(board, predefined[col], col):
            return False

        board[predefined[col]][col] = 1

        if solveNQUtil(board, col + 1, predefined):
            return True

        board[predefined[col]][col] = 0
    else:
        for i in range(N):

            if isSafe(board, i, col):

                board[i][col] = 1  # Place this queen in board[i][col]

                if solveNQUtil(board, col + 1, predefined):  # recur to place rest of the queens
                    return True

                board[i][col] = 0  # backtracking

    return False


# Predefined Queens in Columns x
predefinedQueens = [0, 2, None, None, None, None, 1, None, 14, 5, 7, None, None, 12, 6, None, None, 10]


def solveNQ():
    board = np.zeros((N, N))

    if not solveNQUtil(board, 0, predefinedQueens):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()
