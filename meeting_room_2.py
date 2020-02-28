from heapq import heappop, heappush


class Solution(object):
    def minMeetingRooms(self, intervals): #(O(nlogn) time and O(n) space
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        if not intervals:
            return 0

        heappush(heap, intervals[0][1])

        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heappop(heap)

            heappush(heap, interval[1])

        return len(heap)