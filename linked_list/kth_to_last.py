"""Implement an algorithm to find the kth to last element of a singly linked list."""
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

    # method to print kth to last element (simplest): k-n+1 from the start
    def kth_to_last(self, k):
        start = self.head
        length = 0

        #calculate the length
        while start!= None:
            length = length + 1
            start = start.next

        #if length is less than k then no such kth from last exists
        if length < k:
            return

        temp = self.head

        #iterate to the length-k+1 element
        for i in range(1, length-k+1):
            temp = temp.next
        return temp.data #return the data

def main():
    l= LinkedList()
    l.push(15)
    l.push(14)
    l.push(16)
    l.push(15)
    l.push(15)
    l.push(14)
    l.push(18)
    print (l.kth_to_last(3))


if __name__ == "__main__":
    main()



