#reverse array
def reverse_array(arr, start, end):
    if len(arr) == 0:
        return None

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start = start + 1
        end = end - 1

    return arr

#rotate array
def rotate_array(arr, n):
    if n > len(arr):
        return arr

    l = len(arr)
    rev_arr = reverse_array(arr, 0, l-1)
    first = reverse_array(rev_arr, 0, l-n-1)
    final = reverse_array(first, l-n, l-1)

    return final


def main():
    arr = [1,2,3,4,5]
    print (rotate_array(arr, 5))

if __name__ == "__main__":
    main()
