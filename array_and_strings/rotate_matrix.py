import numpy as np
import random

def rotate_matrix(arr):
    #if matrix has no element or it is not a square matrix
    if (len(arr) == 0 or len(arr) != len(arr[0])):
        return
    for layer in range(0,int(len(arr)/2)):
        arr = rotate(arr, layer, len(arr)-1-layer)
    return arr

def rotate(arr, start, end):
    cur = 0
    while start+cur < end:
        top = arr[start][start + cur] #save in a temp variable
        arr[start][start + cur] = arr[end - cur][start] #copy from left to top
        arr[end - cur][start] = arr[end][end - cur] #copy from bottom to left
        arr[end][end - cur] = arr[start + cur][end] #copy from right to bottom
        arr[start + cur][end] = top #copy from top
        cur = cur + 1
    return arr

def main():
    random.seed(10)
    matrix = np.random.random_integers(20, size=(4,4))
    print (matrix)
    print (rotate_matrix(matrix))

if __name__ == "__main__":
    main()