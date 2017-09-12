"""Three in One: Describe how you could use a single array to implement three stacks."""

class ThreeStacks:
    def __init__(self, size):
        self.size = size
        self.lst = [None] * 3 * size
        self.top = [0, 0, 0]

    def push(data, stackNum):
        if stackNum < 3 and stackNum >= 0:
            lst[stackNum * size + top[stackNum]] = data
            top[stackNum] + +

    def pop(stackNum):
        if stackNum < 3 & & stackNum >= 0:
            temp = lst[top[stackNum]]
            lst[top[stackNum]] = None
            top[stackNum] - -
            return temp

    def size(stackNum):
        return top[stackNum]