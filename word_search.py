class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def search(board, i, j, count, word):
            if count == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
                return False

            temp = board[i][j]
            board[i][j] = ' '

            found = search(board, i - 1, j, count + 1, word) or search(board, i + 1, j, count + 1, word) or search(
                board, i, j - 1, count + 1, word) or search(board, i, j + 1, count + 1, word)
            board[i][j] = temp

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and search(board, i, j, 0, word):
                    return True

        return False





