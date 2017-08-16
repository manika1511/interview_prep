"""Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O. 
Time complexity: O(nxm)+ O(n)"""

def zero_matrix(matrix):
    index = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                index.append((i,j))
    for item in index:
        for l in matrix:
            l[item[1]] = 0
        matrix[item[0]] = [0] * len(matrix[item[0]])

    return matrix

def main():
    assert zero_matrix([
        [1, 2, 3],
        [4, 5, 0],
        [5, 6, 7],
    ]) == [
        [1,2,0],
        [0,0,0],
        [5,6,0]]

    assert zero_matrix([
        [1, 0, 3],
        [4, 5, 0],
        [5, 6, 7],
    ]) == [
        [0, 0, 0],
        [0, 0, 0],
        [5, 0, 0]]

if __name__ == '__main__':
    main()