class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            val = self.items[0]
            self.items = self.items[1:]
            return val

    def peek(self):
        return self.items[0]

    def print_q(self):
        print(self.items)


if __name__== "__main__":
    queue = Queue()
    queue.add(10)
    queue.add(12)
    queue.add(7)
    queue.add(6)
    queue.print_q()
    print(queue.peek())
    print(queue.remove())
    queue.print_q()
    print(queue.isEmpty())