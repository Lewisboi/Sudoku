from Sudoku import Sudoku
def sudoku_solve(sudoku):
    if sudoku.is_solved():
            return sudoku
    else:
        y, x = sudoku.encontrar_espacio()
        for num in range(1, 10):
            sudoku.insert(num, y, x)
            if sudoku.is_valid():
                return sudoku_solve(sudoku)


sudoku_prueba = [[8, 2, 0, 1, 5, 0, 3, 9, 0],
                 [9, 6, 5, 3, 0, 7, 1, 4, 8],  #  (1, 1) es un 0
                 [3, 4, 0, 6, 8, 9, 0, 0, 2],
                 [5, 9, 3, 4, 6, 8, 0, 7, 1],
                 [4, 7, 2, 5, 1, 0, 6, 0, 9],
                 [6, 0, 8, 0, 7, 2, 4, 3, 5],
                 [7, 0, 0, 2, 3, 5, 0, 1, 4],
                 [1, 5, 4, 0, 9, 6, 0, 2, 3],
                 [2, 3, 0, 8, 4, 1, 5, 6, 0]]


sudoku_prueba = Sudoku(sudoku_prueba)
print(sudoku_prueba)
sudoku_solve(sudoku_prueba)
print(sudoku_prueba)