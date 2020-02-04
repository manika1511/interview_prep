class Solution(object): #O(n2) , O(n) space
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = [False]*len(nums)
        check[-1] = True
        n = len(nums)
        for i in reversed(range(n-1)):
            if True in check[i+1:i+nums[i]+1]:
                check[i] = True
            else:
                check[i] = False
        if check[0] == True:
            return True
        else:
            return False


class Solution(object): #O(n) time and O(1) space
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # check = [False]*len(nums)
        # check[-1] = True
        n = len(nums)
        leftmost_good = n - 1
        for i in reversed(range(n - 1)):
            if i + nums[i] >= leftmost_good:
                leftmost_good = i

        if leftmost_good == 0:
            return True
        else:
            return False