class Solution(object): #O(n)
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while (i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1
        if i >= 0:

            j = n - 1
            while (j > i and nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]
        return




