""""
Punto 3 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - 2159879
QuickSort
"""

def quicksort(arr):
    # Caso base: si el arreglo tiene 0 o 1 elementos, está ordenado
    if len(arr) <= 1:
        return arr

    # Elegir un pivote (en este caso, simplemente el primer elemento)
    pivote = arr[0]

    # Separar los elementos menores, iguales y mayores que el pivote
    menores = [x for x in arr[1:] if x <= pivote]
    mayores = [x for x in arr[1:] if x > pivote]

    # Recursivamente ordenar los elementos menores y mayores
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
arreglo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
arreglo_ordenado = quicksort(arreglo)
print("Arreglo Original:", arreglo)
print("Arreglo Ordenado:", arreglo_ordenado)
