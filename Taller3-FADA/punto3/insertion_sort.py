""""
Punto 3 correspondiente al taller 3
29 de noviembre del 2023
Miguel Angel Rueda Colonia - 2159896
Leider Santiago Cortes Hernandez - (2159879)
InsertionSort
"""


import random
import time


def insertionSort(arr):
    n = len(arr)  # Ve el numero de posiciones que tenga el arreglo.

    if n <= 1:
        return  # Si el arreglo esta entre 0 o 1,  para retornar la lista, ya que esta ordenada.

    for i in range(1, n):  # Recorre desde el segundo elemento hasta el ultimo del arreglo.
        k = arr[i]  # La variable k almacena el elemento actual del arreglo que se va a insertar en la posición
        # correcta en la parte ya ordenada del arreglo.(k=llave)
        j = i - 1  # Es un elemento menor a i que se mueve hacia la izquierda.
        while j >= 0 and k < arr[j]:  # Este es un bucle que se ejecuta mientras j sea mayor o igual a 0 y el
            # elemento key sea menor que el elemento en la posición j del arreglo.
            arr[j + 1] = arr[j]  # Si el elemento guardado en k es menor queel guardado en j, se intercambian
            j -= 1  # Se decrementa para ir atras en el arreglo
        arr[j + 1] = k  # Aqui se acomoda a k en el arreglo

arr = []
# n = 0 # Tamaño del arreglo
# n = 10
n = 50
# n = 100
# n = 500
# n = 1000
# n = 2000
# #n = 5000
# n = 10000
for i in range(n):  # Darle valores aleatorios al arreglo.
    arr.append(random.randint(0, 100))

inicio = time.time()

insertionSort(arr)

fin = time.time()

tiempoEjecucion = (fin - inicio) * 1000

print({tiempoEjecucion})


print(arr)
