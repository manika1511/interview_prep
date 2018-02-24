def max_sum_subarray(arr):
    max_sum = arr[0]
    running_sum = arr[0]

    for i in range(1, len(arr)):
        running_sum = running_sum + arr[i]
        if running_sum < arr[i]:
            running_sum = arr[i]
        max_sum = max(max_sum, running_sum)
    return max_sum

def main():
    arr = [3,-6,2,4,-3,7,4]
    print (max_sum_subarray(arr))

if __name__ == "__main__":
    main()