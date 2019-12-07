class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        result = ""
        if l1 == 0 and l2 == 0:
            return "0"
        if l1 == 0 and l2 != 0:
            return num2
        if l1 != 0 and l2 == 0:
            return num1

        l1 = l1 - 1
        l2 = l2 - 1
        carry = 0
        while l1 >= 0 or l2 >= 0:
            if l1 >= 0 and l2 >= 0:
                s = int(num1[l1]) + int(num2[l2]) + carry
            elif l1 >= 0 and l2 < 0:
                s = int(num1[l1]) + carry
            elif l1 < 0 and l2 >= 0:
                s = int(num2[l2]) + carry
            s_rem = int(s % 10)
            carry = int(s / 10)
            result = str(s_rem) + result
            l1 = l1 - 1
            l2 = l2 - 1

        if carry != 0:
            result = str(carry) + result
        return result

