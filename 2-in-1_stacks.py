class twoStacks(object):
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.start1 = 0
        self.start2 = n-1

    def push1(self, val):
        if self.start1 <= self.start2:
            self.arr[self.start1] = val
            self.start1 = self.start1 + 1

        else:
            print("Stack overflow")

    def push2(self, val):
        if self.start2 >= self.start1:
            self.arr[self.start2] = val
            self.start2 = self.start2-1

        else:
            print("Stack overflow")

    def pop1(self):
        if self.start1 >=0:
            val = self.arr[self.start1-1]
            self.start1 = self.start1 - 1
            return val
        else:
            print("Stack Overflow")

    def pop2(self):
        if self.start2 >=0 and self.start2 < self.size:
            val = self.arr[self.start2+1]
            self.start2 = self.start2 - 1
            return val
        else:
            print("Stack Overflow")

    def p_print(self):
        print(self.arr)

if __name__ == "__main__":
    ts = twoStacks(5)
    ts.push1(10)
    ts.push2(3)
    ts.p_print()
    ts.push1(11)
    ts.push2(1)
    ts.p_print()
    ts.push1(2)
    ts.p_print()
    print(ts.pop1())
    print(ts.pop1())
    print(ts.pop1())
    print(ts.pop2())
    print(ts.pop2())
    # print(ts.pop2())
    # print(ts.pop1())