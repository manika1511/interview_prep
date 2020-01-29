class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):  #check if lengths are same
            return False
        if A in B*2:          #if rotation, then must be substring of twice the string
            return True
        else:
            return False