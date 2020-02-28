from heapq import heappop, heappush
class Solution(object):
    def findKthLargest1(self, nums, k): #o(nlogn) time
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums, reverse=True)
        return nums[k - 1]

    def findKthLargest2(self, nums, k): #O(nlogk) time and O(k) space
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heappop(heap)
