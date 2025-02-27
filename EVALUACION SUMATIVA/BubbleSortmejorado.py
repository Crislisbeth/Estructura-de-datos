def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Si no hubo intercambios, el arreglo ya esta ordenado
    return arr

# un ejemplo de como se utiliza el codigo
arr = [5, 3, 8, 1, 2, 7]
print(bubble_sort(arr))
