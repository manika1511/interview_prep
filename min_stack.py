class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min[-1]:
            self.min.append(x)
        self.items.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.items:
            val = self.items.pop()
            if val == self.min[-1]:
                self.min.pop()
            return val

    def top(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()