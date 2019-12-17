class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        flag = 0
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] = d[char] + 1
        print(d)
        for v in d.values():
            if v % 2 == 0:
                result = result + v
            else:
                flag = 1
                result = result + 2 * int(v / 2)

        if flag == 1:
            result = result + 1

        return result