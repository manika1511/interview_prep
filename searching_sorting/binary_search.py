def binary_search(arr, start, end, val): #O(logn)
    while start<=end:
        mid = start + (end-start)//2

        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def binary_search_rec(arr, start, end, val):
    if start <= end:
        mid = start + (end-start)//2

        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            return binary_search_rec(arr, start, mid-1, val)
        else:
            return binary_search_rec(arr, mid+1, end, val)

    return -1


if __name__ == "__main__":
    arr = [1,3,5,7]
    print(binary_search(arr, 0, len(arr)-1, 3))
    print(binary_search_rec(arr, 0, len(arr) - 1, 3))
