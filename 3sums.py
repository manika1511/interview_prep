class Solution(object): #O(n3)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_req = 0
        result = set()
        n = len(nums)
        for i in range(0, n-1):
            s = set()
            curr_sum = sum_req - nums[i]
            for j in range(i + 1, n):
                if (curr_sum - nums[j]) in s:
                    l = sorted([nums[i], nums[j], curr_sum-nums[j]])
                    result.add(tuple(l))
                s.add(nums[j])
        return result


class Solution(object):  #O(n2)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        n = len(nums)
        nums = sorted(nums)
        for i in range(0, n-2):
            start = i + 1
            end = n-1
            while start < end:
                check = nums[i]+nums[start]+nums[end]
                if check == 0:
                    result.add(tuple([nums[i], nums[start], nums[end]]))
                    start = start + 1
                elif check < 0:
                    start = start + 1
                else:
                    end = end - 1
        return result