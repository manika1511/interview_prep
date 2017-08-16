"""write a method to rotate the image by 90 degrees. 
Time complexity: reversed is O(n), zip is O(nxm)"""

def rotate_matrix(matrix):
    rev_matrix = list(reversed(matrix))             #reverse the matrix
    new_rows = zip(*rev_matrix)                     #zip the list of lists
    rotated_matrix = [list(i) for i in new_rows]    #convert tuples to rows
    return rotated_matrix

def main():
    assert rotate_matrix([
        [1, 2, 3],
        [4, 5, 0],
        [5, 6, 7],
    ]) == [
        [5,4,1],
        [6,5,2],
        [7,0,3]
    ]

if __name__ == '__main__':
    main()