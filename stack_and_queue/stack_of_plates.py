#Stack implementation
class Stack(object):
    #constructor
    def __init__(self):
        self.items=[]

    #method to check if stack is empty
    def isEmpty(self):
        return len(self.items)==0

    #method to push data onto stack
    def push(self, data):
        self.items.append(data)

    #method to remove data from top of stack
    def pop(self):
        return self.items.pop()

    #method to peek the value on top of stack
    def peek(self):
        return self.items[len(self.items)-1]

    #method to return stack size
    def size(self):
        return len(self.items)

class SetOfStacks(object):
    def __init__(self, capacity):
        self.capacity=capacity
        self.stacks=[]

    def push(self, data):
        if (len(self.stacks) == 0 or len(self.stack[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(data)






