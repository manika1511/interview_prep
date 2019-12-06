class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        j = i + 1
        result = 0

        while i < len(s) and j < len(s):
            if roman_dict[s[i]] >= roman_dict[s[j]]:
                result = result + roman_dict[s[i]]
                i = i + 1
                j = j + 1
            else:
                result = result + roman_dict[s[j]] - roman_dict[s[i]]
                i = j + 1
                j = i + 1
        if i == len(s) - 1:
            result = result + roman_dict[s[i]]
        return result


