def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def partition(arr, k):
    e = 0
    w_low = 0
    w_high = len(arr) - 1

    while e <= w_high:
        if arr[e] < k:
            arr = swap(arr, e,w_low)
            w_low = w_low + 1

        elif arr[e] > k:
            arr = swap(arr, e, w_high)
            w_high = w_high - 1
            e = e - 1

        e = e + 1
    return arr

def main():
    # arr = [2,1,0,2,2,1,1,0,1,2]
    arr = [2,2,3,9,3,0,1,0,1,0,3,4]
    print (partition(arr, 1))

if __name__=="__main__":
    main()

