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
        self.item.append(data)
