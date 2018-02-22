def remove_duplicates(arr):
    arr.sort()
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] == arr[j]:
            j = j + 1
        else:
            arr[i+1] = arr[j]
            i = i + 1

    return arr[0:i+1]

def main():
    arr = [1,3,4,1,2,4,5]
    print (remove_duplicates(arr))

if __name__ == "__main__":
    main()