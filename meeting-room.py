class Solution(object):
    def canAttendMeetings(self, intervals): #(O(nlogn)
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])

        curr = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < curr[1]:
                return False
            curr = interval

        return True