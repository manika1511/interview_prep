from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return float(self.window_sum) / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)