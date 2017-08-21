"""Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop."""

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

    #method to calculate size of list
    def size(self):
        start=self.head
        size=0
        while start!=None:
            size=size+1
            start=start.next
        return size

    #methid to detect a loop in a linked list
    def loop_detection(self):
        slow=self.head
        fast=self.head

        #use runner method to find first collision point
        while slow != fast:
            slow=slow.next
            fast=fast.next.next

        #after finding the first collision point, set slow to head
        slow=self.head

        #move slow and fast 1 step at a time, this time the collision point is the start of loop
        while slow != fast:
            slow=slow.next
            fast=fast.next
        return slow




