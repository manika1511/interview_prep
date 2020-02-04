class Solution(object): #O(n) time and O(n) space
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        result = []
        carry = 0

        for i in reversed(range(n)):
            if i == n - 1:
                s = digits[i] + carry + 1
            else:
                s = digits[i] + carry

            carry = int(s / 10)
            quo = int(s % 10)
            result.insert(0, quo)
        if carry != 0:
            result.insert(0, carry)
        return result