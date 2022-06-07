def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1  # a.k.a. the position
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]  # array position + 1 is equal to the array position
            j = j - 1

        arr[j + 1] = temp

    return arr
