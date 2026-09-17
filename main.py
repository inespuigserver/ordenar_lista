def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] #i indica la pposicion en la que se encuenra el elemento
        j = i - 1 #j es la variable que recorre la lista
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] #para recorrer el siguiente elemento de la lista
            j -= 1
        arr[j + 1] = key
    return arr
print(insertion_sort([12, 11, 13, 5, 6, 2, 4, 3, 1, 10, 9, 8, 7]))