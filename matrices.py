import numpy as np

def create_matrix(blocks,n=4,m=4):
    matrix = np.zeros((n, m))
    for item in blocks:
        matrix[item[0]][item[1]] = 1
    return matrix

#check whether the point is inbounds
def isValid(mat, point):
    if point[0] < len(mat) and point[1] < len(mat[0]) and point[0] >=0 and point[1] >=0:
        return True
    return False

#function to find if a path exists
def hasPath(mat, start, end):
    if start == end:
        return True

    mat[start[0]][start[1]] = 1

    a = [(0,1),(1,0),(-1,0), (0,-1)]
    for item in a:
        new_start = [start[0]+item[0], start[1]+item[1]]
        if isValid(mat, new_start):
            if mat[new_start[0]][new_start[1]] != 1:
                if hasPath(mat, new_start, end):
                    return True

    mat[start[0]][start[1]] = 0
    return False

#return the path
def returnPath(mat, start, end, path):
    if start == end:
        return True

    mat[start[0]][start[1]] = 1

    a = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for item in a:
        new_start = [start[0] + item[0], start[1] + item[1]]
        if isValid(mat, new_start):
            if mat[new_start[0]][new_start[1]] != 1:
                if hasPath(mat, new_start, end, path):
                    path.append(new_start)
                    # return True

    mat[start[0]][start[1]] = 0
    # return False
    return path

def main():
    n = 5
    m = 5

    blocks = [(0,3),(0,4),(1,0),(1,1),(1,3),(1,4),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4)]

    mat = create_matrix(blocks,n,m)
    print (mat)

    start = [0,0]
    end = [n-1,m-1]
    print (hasPath(mat, start, end))

    print(returnPath(mat, start, end, [start]))




if __name__ == "__main__":
    main()
