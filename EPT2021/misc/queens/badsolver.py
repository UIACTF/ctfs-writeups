import sys
import numpy as np
from ortools.constraint_solver import pywrapcp


def main(board_size):
    # Creates the solver.
    solver = pywrapcp.Solver('n-queens')

    # Creates the variables.
    # The array index is the column, and the value is the row.
    queens = [solver.IntVar(0, board_size - 1, f'x{i}') for i in range(board_size)]

    # Creates the constraints.
    # All rows must be different.
    solver.Add(solver.AllDifferent(queens))

    # All columns must be different because the indices of queens are all different.
    # No two queens can be on the same diagonal.
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))

    db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_MIN_VALUE)
    mal = np.zeros((board_size, board_size))
    array1 = mal.copy()
#Queens	  ,y  ,x
    array1[10][0] = 1
    array1[5][4] = 1
    array1[2][10] = 1
    array1[7][11] = 1

    array2 = mal.copy()
    checker = 0
    increment = 1
    # Iterates through the solutions, displaying each.
    num_solutions = 0
    solver.NewSearch(db)
    while solver.NextSolution():
        # Displays the solution just computed.
        for i in range(board_size):
            for j in range(board_size):
                if queens[j].Value() == i:
                    # There is a queen in column j, row i.
                    array2[j][i] = 1
                else:
                    array2[j][i] = 0
        num_solutions += 1
        for a in range(board_size):
            for b in range(board_size):
                if array1[b][a] == 1:
                    if array2[b][a] != 1:
                        checker = 1
        if checker == 0:
            # Prints the syntax that the challenge accepts
            for i in range(board_size):
                increment = 1
                for j in range(board_size):
                    if array2[i][j] == 1:
                        print(increment, end=',')
                    increment += 1
            exit()
        checker = 0
    solver.EndSearch()



if __name__ == '__main__':
    board_size = 13
    main(board_size)