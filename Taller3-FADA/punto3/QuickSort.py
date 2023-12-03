""""
Punto 3 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - 2159879
QuickSort
"""
import random
import time
import timeit
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

#Generar arrays de tamaño n aleatorios.
arr = []
#n = 0 # Tamaño del arreglo
# n = 10
n = 50
#n = 100
#n = 500
#n = 1000
#n = 2000
#n = 5000
#n = 10000
for i in range(n):  # Darle valores aleatorios al arreglo.
    arr.append(random.randint(0, 100))
#print(quicksort(arr))
print(timeit.timeit(lambda: quicksort(arr), number=1000))
