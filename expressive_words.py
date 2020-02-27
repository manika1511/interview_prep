class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def char_count(S):
            char_list = []
            count_list = []
            char_list.append(S[0])
            c_c = 1
            for char in S[1:]:
                if char == char_list[-1]:
                    c_c = c_c + 1
                else:
                    count_list.append(c_c)
                    char_list.append(char)
                    c_c = 1
            count_list.append(c_c)
            return char_list, count_list

        count = 0
        char_list_S, count_list_S = char_count(S)

        for word in words:
            char_list_w, count_list_w = char_count(word)
            if char_list_w == char_list_S:
                count = count + all(c_s >= max(c_w, 3) or c_s == c_w
                                    for c_s, c_w in zip(count_list_S, count_list_w))

        return count

