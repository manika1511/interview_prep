class Solution(object): #O(n) time and O(1) space
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j])*(j-i)
            max_val = max(area, max_val)
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1
        return max_val