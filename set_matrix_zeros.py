class Solution(object):
    def setZeroes(self, matrix): #O(mn) time, O(m+n) space
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        for row in zero_rows:
            matrix[row] = [0] * len(matrix[row])
        for col in zero_columns:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return matrix


class Solution2(object):
    def setZeroes(self, matrix): #O(mn) time, O(1) space
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col_zero = False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][0] == 0:
                col_zero = True

            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0

        if col_zero:
            for i in range(r):
                matrix[i][0] = 0

        return matrix