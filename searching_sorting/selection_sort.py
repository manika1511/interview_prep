def selection_sort(arr): #O(n2) time, O(1) space
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort([1]))