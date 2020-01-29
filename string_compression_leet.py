class Solution1(object): #O(n) time and O(n) space
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = ""
        count = 1
        for i in range(len(chars)):
            if i == len(chars)-1:
                result = result + chars[i]
                if count > 1:
                    result = result + str(count)
                return list(result)
            if chars[i] == chars[i+1]:
                count = count + 1
            else:
                result = result + chars[i]
                if count > 1:
                    result = result + str(count)
                count = 1
        return list(result)

class Solution(object): #O(n) time and O(1) space
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

def main():
    s1 = ["a","a","b","b","c","c","c"]
    obj = Solution()

    print (obj.compress(s1))



if __name__ == '__main__':
    main()