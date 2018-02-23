def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def move_zeros(arr):
    e = len(arr) - 1
    w = e

    while e>=0:
        if arr[e] == 0:
            arr = swap(arr, e,w)
            w = w - 1
        e = e - 1

    return arr

def main():
    arr = [1,2,3,4,0,5,6,0,0,9,1,1,1]
    print (move_zeros(arr))

if __name__== "__main__":
    main()