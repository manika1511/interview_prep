#find the sub-array, sorting which sorts the entire array (O(n))
def sort_sub(arr):
    start = 0
    end = 0
    count = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1] and count == 0:
            start = i
            break

    # for i in range(start+1,len(arr)-1):
    #     if arr[i] > arr[i+1]:
    #         end = i + 1
    #         break
    j = len(arr) - 1
    while j > start:
        if arr[j] < arr[j - 1]:
            end = j
            break
        j = j - 1

    if start == end:
        return "Already sorted"
    return arr[start:end+1]

def main():
    arr = [1,2,4,3,2,7,6,8,9]

    print(sort_sub(arr))

if __name__ == "__main__":
    main()



