#find the sub-array, sorting which sorts the entire array
def sort_sub(arr):
    start = 0
    end = 0
    count = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1] and count == 0:
            start = i
            break

    for i in range(start+1,len(arr)-1):
        if arr[i] > arr[i+1]:
            end = i + 1
            break
    if start == end:
        return "Already sorted"
    return arr[start:end+1]

def main():
    arr = [1,2,3,4,5,6]

    print(sort_sub(arr))

if __name__ == "__main__":
    main()



