class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = ""
        S = S.replace("-", "")

        rem = len(S) % K
        parts = []
        start = 0
        if rem != 0:
            parts.append(S[start: start + rem].upper())
            start = start + rem
        while start < len(S):
            parts.append(S[start:start + K].upper())
            start = start + K

        return ("-").join(parts)