class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []

        for char in S:
            if char != "#":
                stack_s.append(char)
            else:
                if stack_s:
                    stack_s.pop()

        for char in T:
            if char != "#":
                stack_t.append(char)
            else:
                if stack_t:
                    stack_t.pop()

        if stack_s == stack_t:
            return True
        else:
            return False