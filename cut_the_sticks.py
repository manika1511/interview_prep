def computeSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print (len(arr))
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    computeSticks(arr)