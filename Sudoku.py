from random import randint
from time import time
class Sudoku:
    def __init__(self, lista):
        self.lista = lista

    def get_filas(self):
        filas = self.lista.copy()
        return filas

    def get_columnas(self):
        columnas = []
        for i in range(9):
            columna = []
            for j in range(9):
                columna.append(self.get_filas()[j][i])
            columnas.append(columna)
        return columnas

    def get_cuadrantes(self):
        cuadrantes = []
        for fila in [(0, 3), (3, 6), (6, 9)]:
            paquete = self.get_filas()[fila[0]:fila[1]]  #  Hace un 'paquete' de los elementos (a, b) de la lista
            for columna in [(0, 3), (3, 6), (6, 9)]:
                cuadrante = paquete[0][columna[0]:columna[1]] + \
                            paquete[1][columna[0]:columna[1]] + \
                            paquete[2][columna[0]:columna[1]]

                cuadrantes.append(cuadrante)
        return cuadrantes

    def encontrar_espacio(self):
        for fila in range(9):
            for elem in range(9):
                if self.get_filas()[fila][elem] not in {i for i in range(1, 10)}:
                    espacio_encontrado = (fila, elem)
                    return espacio_encontrado
        #return False

    def is_valid(self):
        def se_repite(lista):
            lista_sin_ceros = [i for i in lista if i != 0]
            set_lista = set(lista)
            set_lista.discard(0)
            return (len(set_lista) != len(lista_sin_ceros))
        columnas_validas = True
        for col in self.get_columnas():
            if se_repite(col):
                columnas_validas = False
                break
        filas_validas = True
        for fila in self.get_filas():
            if se_repite(fila):
                filas_validas = False
                break
        cuadrantes_validos = True
        for cuad in self.get_cuadrantes():
            if se_repite(cuad):
                cuadrantes_validos = False
                break

        return (columnas_validas and filas_validas and cuadrantes_validos)
            
    def insert(self, num, fila, columna):
        self.lista[fila][columna] = num

    def is_solved(self):
        comparacion = {i for i in range(1, 10)}
        columnas_resueltas = True
        for columna in self.get_columnas():
            numeros_en_columna = set(columna)
            if numeros_en_columna != comparacion:
                columnas_resueltas = False
                break

        filas_resueltas = True
        for fila in self.get_filas():
            numeros_en_fila = set(fila)
            if numeros_en_fila != comparacion:
                filas_resueltas = False
                break

        cuadrantes_resueltos = True
        for cuadrante in self.get_cuadrantes():
            numeros_en_cuadrante = set(cuadrante)
            if numeros_en_cuadrante != comparacion:
                cuadrantes_resueltos = False
                break

        solved = (columnas_resueltas and filas_resueltas and cuadrantes_resueltos)
        return solved

    def __repr__(self):
        representacion = ''
        for fila in self.get_filas():
            string_fila =  str(fila)[1:-1]
            representacion += string_fila + '\n'
        return representacion


'''lista_resuelto = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                   [9, 6, 5, 3, 2, 7, 1, 4, 8],
                   [3, 4, 1, 6, 8, 9, 7, 5, 2],
                   [5, 9, 3, 4, 6, 8, 2, 7, 1],
                   [4, 7, 2, 5, 1, 3, 6, 8, 9],
                   [6, 1, 8, 9, 7, 2, 4, 3, 5],
                   [7, 8, 6, 2, 3, 5, 9, 1, 4],
                   [1, 5, 4, 7, 9, 6, 8, 2, 3],
                   [2, 3, 9, 8, 4, 1, 5, 6, 7]]'''