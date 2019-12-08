class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reverse_word(x):
            return x[::-1]

        prev_blank = -1
        curr_blank = 0
        result = ""

        if len(s) == 0:
            return ""

        for i in range(len(s)):
            if s[i] == " ":
                curr_blank = i
            elif i == len(s) - 1:
                curr_blank = len(s)
            if curr_blank != 0:
                if result != "":
                    result = result + " "
                result = result + reverse_word(s[prev_blank + 1:curr_blank])
                # j = curr_blank-1
                # while j > prev_blank:
                #     result = result + s[j]
                #     j = j - 1
                prev_blank = curr_blank
                curr_blank = 0

        return result