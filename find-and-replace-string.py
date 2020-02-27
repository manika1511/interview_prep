class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        result = []
        cursor = 0

        l_zip = zip(indexes, sources, targets)
        l_zip.sort()
        sorted_lists = zip(*l_zip)
        indexes, sources, targets = sorted_lists[0], sorted_lists[1], sorted_lists[2]

        for index, source, target in zip(indexes, sources, targets):
            if S.find(source, index) == index:
                result.append(S[cursor:index])
                cursor = index
                result.append(target)
                cursor += len(source)

        result.append(S[cursor:])
        return "".join(result)