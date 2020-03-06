class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, val):
        self.items.append(val)

    def pop(self):
        val = self.items[-1]
        self.items = self.items[0:-1]
        return val

    def peek(self):
        return self.items[-1]

    def print_stack(self):
        print (self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(5)
    stack.push(3)
    stack.push(6)
    stack.print_stack()
    # print(stack.peek())
    # print(stack.isEmpty())
    print(stack.pop())
    stack.print_stack()

