class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # if matrix has no element or it is not a square matrix
        if (len(matrix) == 0 or len(matrix) != len(matrix[0])):
            return
        for layer in range(0, int(len(matrix) / 2)):
            matrix = self.rotate_layer(matrix, layer, len(matrix) - 1 - layer)
        return matrix

    def rotate_layer(self, arr, start, end):
        cur = 0
        while start + cur < end:
            top = arr[start][start + cur]  # save in a temp variable
            arr[start][start + cur] = arr[end - cur][start]  # copy from left to top
            arr[end - cur][start] = arr[end][end - cur]  # copy from bottom to left
            arr[end][end - cur] = arr[start + cur][end]  # copy from right to bottom
            arr[start + cur][end] = top  # copy from top
            cur = cur + 1
        return arr