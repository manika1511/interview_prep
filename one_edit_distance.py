class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False

        if s == t:
            return False

        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count = count + 1
                    if count > 1:
                        return False
            return True

        elif len(s) > len(t):
            count = 0
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    count = count + 1
                    if count > 1:
                        return False
                    if s[i + 1] != t[j]:
                        return False
                    else:
                        i = i + 2
                        j = j + 1
                else:
                    i = i + 1
                    j = j + 1
            return True

        else:
            count = 0
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    count = count + 1
                    if count > 1:
                        return False
                    if s[i] != t[j + 1]:
                        return False
                    else:
                        i = i + 1
                        j = j + 2
                else:
                    i = i + 1
                    j = j + 1
            return True


