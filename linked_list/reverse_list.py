"""Implement a function to check if a linked list is a palindrome."""

# Node class to define linked list nodes
class Node(object):
    # constructor to initialise node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Linkedlist class

class LinkedList(object):
    #method to initialise head
    def __init__(self, head=None):
        self.head=head

    #method to add data into the list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head=new_node

    #method to print the list nodes
    def print_list(self):
        start=self.head
        while start != None:
            print (start.data)
            start=start.next

    #method to find size of the linked list
    def size(self):
        start=self.head
        size=0
        while start!=None:
            size=size+1
            start=start.next
        return size

    def reverse_list(self):
        if self.head is None:
            return

        # reverse second half
        p, last = self.head, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        self.head = last

def main():
    l1= LinkedList()
    l1.push("m")
    l1.push("a")
    l1.push("n")
    l1.push("i")
    l1.push("k")
    l1.push("a")

    l1.reverse_list()
    l1.print_list()
    l1.reverse_list()
    l1.print_list()

if __name__ == "__main__":
    main()





