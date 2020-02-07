class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        i = 0
        j = i + 1
        result = []

        if not nums:
            if lower != upper:
                item = "{0}->{1}".format(lower, upper)
                result.append(item)
            else:
                result.append(str(lower))
            return result

        if nums[i] != lower:
            if nums[i] - lower > 1:
                item = "{0}->{1}".format(lower, nums[i] - 1)
                result.append(item)
            elif nums[i] - lower == 1:
                result.append(str(lower))
        if len(nums) == 1:
            if upper - nums[0] > 1:
                result.append("{0}->{1}".format(nums[0] + 1, upper))
            elif upper - nums[0] == 1:
                result.append(str(upper))
            return result

        while j < len(nums):
            if nums[j] - nums[i] == 2:
                result.append(str(nums[i] + 1))
            elif nums[j] - nums[i] > 2:
                item = "{0}->{1}".format(nums[i] + 1, nums[j] - 1)
                result.append(item)
            j = j + 1
            i = i + 1

        if nums[i] != upper:
            if upper - nums[i] == 1:
                result.append(str(nums[i] + 1))
            else:
                item = "{0}->{1}".format(nums[i] + 1, upper)
                result.append(item)
        return result

