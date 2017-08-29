"""Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

#Stack implementation
class Stack(object):
    #constructor
    def __init__(self):
        self.minValue=None      #initiate the minValue to None
        self.items=[]

    #method to check if stack is empty
    def isEmpty(self):
        return len(self.items)==0

    #method to push data onto stack
    def push(self, data):
        if self.isEmpty():              #if the first element, push it as it is
            self.items.append(data)
            self.minValue=data          #set min to the first value
        else:
            self.items.append(2*data-self.minValue) #else add 2*data-min
            if self.minValue > data:
                self.minValue = data            #set the min value if the data inserted is less than min

    #method to remove data from top of stack
    def pop(self):
        temp=self.items.pop()
        if temp < self.minValue:            #while removing check if it is less than min..
            self.minValue=2*self.minValue - temp #if yes, set min to 2*min-removed
        return (temp+self.minValue)/2       #return the actual data

    #method to peek the value on top of stack
    def peek(self):
        if len(self.items) > 1:
            return int((self.items[len(self.items)-1]+self.minValue)/2)
        elif len(self.items) == 1:
            return self.items[len(self.items)-1]

    #method to return stack size
    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.minValue

    def printStack(self):
        print (self.items)

def main():
    s = Stack()
    s.push(3)
    s.push(5)
    # print (s.getMin())
    s.push(2)
    s.push(1)
    s.printStack()
    # print (s.getMin())
    s.pop()
    s.pop()
    # print(s.getMin())
    print (s.peek())
    s.pop()
    print (s.peek())

if __name__=="__main__":
    main()
