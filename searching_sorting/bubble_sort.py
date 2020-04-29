def bubble_sort(arr): #O(n2)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort([1,2,3,4,5]))