class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = []
        count = 1
        for i in range(len(chars)):
            if i < len(chars)-1:
                if chars[i] == chars[i+1]:
                    count = count + 1
                else:
                    result.append(str(chars[i]))
                    if count > 1:
                        result.append(str(count))
                    count = 1
            else:
                result.append(str(chars[i]))
                if count > 1:
                    result.append(str(count))
        return result


def main():
    l = ["a","b","c"]
    obj = Solution()
    print (obj.compress(l))



if __name__ == '__main__':
    main()