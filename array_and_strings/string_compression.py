"""Implement a method to perform basic string compression using the counts of repeated characters. Traversing a string 
wil take O(n) time and all other operations are O(1). So, the entire algorithm has O(n) time complexity. """
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        write = 0
        for i in range(len(chars)):
            if i == len(chars)-1:
                chars[write] = chars[i]
                write = write + 1
                if count > 1:
                    count = list(str(count))
                    for ch in count:
                        chars[write] = ch
                        write = write + 1
                return len(chars[0:write])
            if chars[i] == chars[i+1]:
                count = count + 1
            else:
                chars[write] = chars[i]
                write = write + 1
                if count > 1:
                    count = list(str(count))
                    for ch in count:
                        chars[write] = ch
                        write = write + 1
                count = 1




