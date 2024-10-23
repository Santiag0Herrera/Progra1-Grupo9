def generarMatriz(columnas, filas):
  matriz = []
  for i in range(filas):
    matriz.append([0]*columnas)
  return matriz

def buscar_en_matriz(matriz, valor):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] == valor:
        return True
  return False

def buscar_en_lista(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1