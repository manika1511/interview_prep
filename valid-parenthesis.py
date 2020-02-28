class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_dict = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        stack = []
        for char in s:
            if char in brackets_dict:
                stack.append(char)
            else:
                if not stack or brackets_dict[stack.pop()] != char:
                    return False

        if not stack:
            return True
        return False
