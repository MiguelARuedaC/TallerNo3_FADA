import random
import time


def merge_sort(lst):
    if len(lst) <= 1:  # caso base: el subarray es solo de un elemento, o es vacio
        return lst

    else: #caso recursivo

        mid = len(lst)//2  # Dividir a la mitad hasta que quedan arreglos de 1 posicion, el caso base, conquistamos.
        left = merge_sort(lst[:mid])  # La mitad iquierda
        right = merge_sort(lst[mid:])  # La mitad derecha

        return merge(left, right)  # Combinar

def merge(left, right):  # Combinar.

    result = []
    i = 0  # indice para el subarray de la izquierda.
    j = 0  # indice para el sub array de la derecha.
    while i < len(left) and j < len(right): # El bucle que se encarga de ordenar las pequeñas soluciones.
        if left[i] < right[j]:  # Si el de la izquierda es menor que el de la derecha, pone prmero el de la izquierda
            result.append(left[i])
            i += 1
        else:  # Si el de la izquierda es menor que el de la derecha, pone prmero el de la izquierda
            result.append(right[j])
            j += 1


    while i < len(left):  # Si aún quedan elementos en el subarray de la izquierda.
        result.append(left[i])
        i += 1

    while j < len(right):  # Si aún quedan elementos en el subarray de la izquierda
        result.append(right[j])
        j += 1

    return result # regresa la lista ya combinada y ordenada

arr = []
# n = 0 # Tamaño del arreglo
n = 10
# n = 50
# n = 100
# n = 500
# n = 1000
# n = 2000
# n = 5000
# n = 10000
for i in range(n):  # Darle valores aleatorios al arreglo.
    arr.append(random.randint(0, 100))

inicio = time.time()

merge_sort(arr)

fin = time.time()

tiempoEjecucion = (fin - inicio) * 1000

print({tiempoEjecucion})

print(merge_sort(arr))
