class Queue(object):
    def __init__(self):
        self.w = []
        self.r = []

    def dequeue(self):
        if len(self.r) == 0:
            if len(self.w) == 0:
                return False
            i = len(self.w) - 1
            while i >= 0:
                self.r.append(self.w[i])
                del self.w[i]
                i = i - 1
        return self.r[-1]


    def enqueue(self, val):
        self.w.append(val)
        print (self.w)


def main():
    q = Queue()
    q.enqueue(10)
    print (q.dequeue())

if __name__=="__main__":
    main()
