class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s): #O(n) time, O(1) space
        """
        :type s: str
        :rtype: int
        """
        hash_dict = dict()
        size_dict = 0
        left = 0
        right = 0
        max_len = 0

        while left <= right and right < len(s):
            if s[right] in hash_dict:
                hash_dict[s[right]] = hash_dict[s[right]] + 1
            else:
                hash_dict[s[right]] = 1
            if len(hash_dict) > 2:
                max_len = max(max_len, right - left)
                hash_dict[s[left]] = hash_dict[s[left]] - 1
                if hash_dict[s[left]] == 0:
                    del hash_dict[s[left]]
                left = left + 1
            else:
                max_len = max(max_len, right - left + 1)

            right = right + 1
            return max_len