class Solution(object): #O(N) time and O(N) space
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = dict()
        for char in s:
            if char in d:
                d[char] = d[char] + 1
            else:
                d[char] = 1

        dict_values = d.values()
        check_list = [x % 2 for x in dict_values]
        if sum(check_list) > 1:
            return False
        else:
            return True

    class Solution(object): #O(N) time and O(1) space
        def canPermutePalindrome2(self, s):
            """
            :type s: str
            :rtype: bool
            """
            check = [0] * 128
            for char in s:
                ascii_char = ord(char)
                check[ascii_char] = check[ascii_char] + 1

            check_list = [x % 2 for x in check]
            if sum(check_list) > 1:
                return False
            else:
                return True


