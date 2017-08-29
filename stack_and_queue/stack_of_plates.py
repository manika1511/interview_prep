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
        if (len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(data)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        data=self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data

    def popAt(self, index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index - 1]) == 0:
            return None
        else:
            return self.stacks[index - 1].pop()

def main():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print (i)
    print ("")

    for i in range(5):
        print ("Poped", setofstacks.pop())

    print ("Test for popAt")
    for i in range(5):
        for i in range(3):
            print ("Poped", setofstacks.popAt(i+1))


if __name__ == "__main__":
    main()








