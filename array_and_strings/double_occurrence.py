def double_occurrence(arr):
    count = 0
    digits = 0
    for i in range(len(arr)):
        if arr[i] != None:
            if arr[i] % 2 == 0:
                count = count + 1
                digits = digits + 1
            else:
                digits = digits + 1

    last_index = digits + count
    i = last_index-1
    j = digits-1
    while i >= 0:
        arr[i] = arr[j]
        i = i - 1
        if arr[i+1] % 2 == 0:
            arr[i] = arr[j]
            i = i - 1
        j = j-1
    return arr


def main():
    arr = [1,2,5,6,8,10, None,None,None,None,None,None]
    print (double_occurrence(arr))

if __name__=="__main__":
    main()