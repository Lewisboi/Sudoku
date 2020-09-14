from Sudoku import Sudoku
from copy import deepcopy


def sudoku_solve(sudoku):
    if sudoku.is_solved():
        return sudoku

    if not sudoku.is_valid():
        return False

    else:
        y, x = sudoku.encontrar_espacio()
        for num in range(1, 10):
            prueba_sudoku = deepcopy(sudoku)
            prueba_sudoku.insert(num, y, x)
            if (resuelto := sudoku_solve(prueba_sudoku)):
                return resuelto


if __name__ == '__main__':
    sudoku_prueba_1 = [[8, 2, 7, 1, 5, 4, 3, 9, 0],
                       [9, 6, 5, 3, 2, 7, 1, 4, 0],
                       [3, 4, 1, 6, 8, 9, 7, 5, 0],
                       [5, 9, 3, 4, 6, 8, 2, 7, 0],
                       [4, 7, 2, 5, 1, 3, 6, 8, 0],
                       [6, 1, 8, 9, 7, 2, 4, 3, 0],
                       [7, 8, 6, 2, 3, 5, 9, 1, 0],
                       [1, 5, 4, 7, 9, 6, 8, 2, 0],
                       [2, 3, 9, 8, 4, 1, 5, 6, 0]]

    sudoku_prueba_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sudoku_prueba = Sudoku(sudoku_prueba_1)
    nuevo_sudoku = sudoku_solve(sudoku_prueba)
    print('   --- Sudoku 1 ---')
    print(nuevo_sudoku)

    sudoku_prueba = Sudoku(sudoku_prueba_2)
    nuevo_sudoku = sudoku_solve(sudoku_prueba)
    print('   --- Sudoku 2 ---')
    print(nuevo_sudoku)
