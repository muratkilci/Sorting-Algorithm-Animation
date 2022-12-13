def quick_sort(arr, start_index, last_index):
    if last_index > start_index and len(arr) != 1:
        pivot = arr[last_index]
        j = start_index - 1
        for i in range(start_index, last_index):
            if arr[i] < pivot:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[j + 1], arr[last_index] = arr[last_index], arr[j + 1]

        quick_sort(arr, start_index, j)
        quick_sort(arr, j + 2, last_index)

    return arr
