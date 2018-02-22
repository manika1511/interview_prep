#sort method will not work as the index is lost
def two_sum_sort(arr, sum):
    arr.sort()
    result = []
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start] + arr[end]
        if temp == sum:
            result.append((start,end))
            start = start + 1
            end = end - 1
        if temp < sum:
            start = start + 1
        if temp > sum:
            end = end - 1
    return result

#using dict
def two_sum_map(arr, sum):
    d = {}
    result = []
    for i in range(0, len(arr)):
        diff = sum - arr[i]
        d[diff] = i

    for i in range(0, len(arr)):
        if arr[i] in d.keys() and i != d[arr[i]]:
            if (d[arr[i]], i) not in result:
                result.append((i, d[arr[i]]))
    return result

def main():
    arr = [1,2,5,4,6,8,9]
    sum = 13
    print (two_sum_map(arr,sum))
    # print (two_sum_sort(arr,sum))

if __name__ == "__main__":
    main()
