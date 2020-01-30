class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        check = set()
        max_val = 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in check:
                check.add(s[j])
                j = j + 1
                max_val = max(len(check), max_val)
            else:
                check.remove(s[i])
                i = i + 1
        return max_val