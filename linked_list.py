import random

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    #insert node at head
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert node in middle
    def push_middle(self, data):
        start = self.head
        for i in range(0,2):
            start=start.next
        new_node = Node(data)
        new_node.next = start.next
        start.next = new_node

    #get the tail
    def get_tail(self):
        start = self.head
        while start.next != None:
            start = start.next
        return start

    #print list
    def print_list(self):
        start = self.head
        while start != None:
            print(str(start.data) + "->", end="")
            start = start.next
        print ("\n")

    #get the intersection point of the list
    def intersection(self, other):
        head1 = self.head
        head2 = other.head

        while head1 != None and head2 != None:
            head1 = head1.next
            head2 = head2.next

        if head1 == None:
            head1 = other.head
            while head2 != None:
                head2 = head2.next
                head1 = head1.next
            head2 = self.head
        else:
            head2 = self.head
            while head1 != None:
                head1 = head1.next
                head2 = head2.next
            head1 = other.head

        while head1.next != head2.next:
            head1 = head1.next
            head2 = head2.next

        return head2.next.data

    #move the iterator to number of nodes
    def move(self, number):
        start = self.head
        for i in range(number):
            start = start.next
        return start

    #Rearrange a linked list such that all even and odd positioned nodes are together
    # f = LinkedList()
    # f.head = l1.even_odd()
    # f.print_list()
    def even_odd(self):
        if self.head == None:
            return None

        odd = self.head
        even = self.head.next
        ef = even

        while(1):
            if odd == None or even == None or even.next == None:
                odd.next = ef
                break

            odd.next = even.next
            odd = even.next

            if odd.next == None:
                odd.next = ef
                even.next = None
                break

            even.next = odd.next
            even = odd.next

        return self.head

    def create_merged_list(self, other):
        random.seed(10)
        l1 = LinkedList()
        for i in range(10):
            l1.push(random.randint(1, 100))
        l1.print_list()

        l2 = LinkedList()
        for i in range(5):
            l2.push(random.randint(1, 100))
        l2.print_list()

        tail = Node()
        tail = l2.get_tail()

        m = Node()
        m = l1.move(4)
        tail.next = m
        l1.print_list()
        l2.print_list()
        print (l1.intersection(l2))

    #partition a linked list with first half having more than second if odd number of elements else same
    # p1 = LinkedList()
    # p2 = LinkedList()
    #
    # p1.head, p2.head = l1.partition_list()
    #
    # p1.print_list()
    # p2.print_list()
    def partition_list(self):
        if self.head == None:
            return None

        s = self.head
        f = self.head

        while f != None:
            if f.next != None:
                f = f.next
                if f != None:
                    f = f.next
                else:
                    break
            else:
                break
            if f != None:
                s = s.next
        h2 = s.next
        s.next = None
        h1 = self.head

        return h1, h2

    #rotate the list by k elements
    def rotate(self,k):
        if self.head == None:
            return None

        if self.head.next == None:
            return self.head

        start = self.head
        for i in range(k):
            start = start.next

        sec = self.head
        prev = self.head
        temp = start
        while start != None:
            prev = sec
            sec = sec.next
            temp = start
            start = start.next

        temp.next = self.head
        prev.next = None

        return sec

    #reverse the list iteratively O(n)
    def reverse_iter(self):
        start = self.head
        tail = None

        while start:
            next = start.next
            start.next = tail
            tail = start
            start = next

        # self.head = tail
        return tail

    # reverse the list recurssively O(n)
    def reverse_rec(self):
        if self.head == None or self.head.next == None:
            return self.head

        first = self.head
        rest = first.next
        rem = LinkedList(rest)
        rem.reverse_rec()
        first.next.next = first
        first.next = None
        self.head = rem.head

    def palindrome(self):
        rev = LinkedList()
        rev.head = self.reverse_iter()
        h1 = self.head
        h2 = rev.head
        while h1 != None:
            if h1.data != h2.data:
                return False
            h1 = h1.next
            h2 = h2.next
        return True

    #calculate sum of the list with least significant digit on head
    def sum_number(self, other):
        h1 = self.head
        h2 = other.head
        s = LinkedList()
        carry = 0
        while h1 != None or h2 != None:
            sum = h1.data + h2.data + carry
            carry = int(sum/10)
            val = int(sum % 10)
            n = Node(val)
            if s.head == None:
                s.head = n
            else:
                n.next = s.head
                s.head = n
            h1 = h1.next
            h2 = h2.next

        if h1 == None:
            while h2 != None:
                sum = h2.data + carry
                carry = int(sum/10)
                val = int(sum % 10)
                n = Node(val)
                if s.head == None:
                    s.head = n
                else:
                    n.next = s.head
                    s.head = n
        elif h2 == None:
            while h1 != None:
                sum = h1.data + carry
                carry = int(sum/10)
                val = int(sum % 10)
                n = Node(val)
                if s.head == None:
                    s.head = n
                else:
                    n.next = s.head
                    s.head = n

        if carry != 0:
            n = Node(carry)
            n.next = s.head
            s.head = n
        return s.head

    #sum of numbers with most significant digit at the head
    def sum2(self, other):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.head = self.reverse_iter()
        l2.head = other.reverse_iter()

        return l1.sum_number(l2)

    #partition the list and then zip it
    def zip_list(self):
        if self.head == None or self.head.next == None:
            return self.head

        l1 = LinkedList()
        l2 = LinkedList()
        l1.head, l2.head = self.partition_list()
        l1.print_list()
        l2.print_list()
        h1 = l1.head
        h2 = l2.head

        while h1 != None and h2 != None:
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2
            h2.next = temp1
            h1 = temp1
            h2 = temp2

        return l1.head

    def create_list_with_loop(self, k):
        x = self.move(k)
        t = self.get_tail()
        t.next = x

    #detect loop with the loop start
    def loop_detection(self):
        if self.head == None or self.head.next == None:
            return None

        loopStart = Node()
        slow = self.head
        fast = self.head

        while slow != None and fast != None:
            slow = slow.next
            if fast.next == None:
                loopStart.next = None
                break

            fast = fast.next.next

            if slow == fast:
                slow = self.head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                loopStart = slow
                break


        return loopStart

    #detect if the loop exists
    def detect_loop(self):
        slow = self.head
        fast = self.head

        # use runner method to find first collision point
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            print ("True")
            return

def main():
    l1 = LinkedList()
    for i in range(8):
        l1.push(random.randint(0, 10))
    l1.print_list()

    l1.create_list_with_loop(4)

    x = Node()
    x = l1.loop_detection()
    if x.next == None:
        print ("No loop")
    else:
        print (x.data)

if __name__ == '__main__':
    main()