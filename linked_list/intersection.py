"""Program to find point of intersection of two linked lists"""
import random

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

    #method to find out intersection point of two linked lists
    def intersection(self, other):
        head1=self.head
        head2=other.head
        len1=0
        len2=0

        while head1 != None:
            len1 = len1 + 1
            head1=head1.next

        while head2 != None:
            len2 = len2 + 1
            head2=head2.next
            """if at this point, when both the pointers are at end, the both nodes are same by reference, then the 
            lists intersect"""

        head1=self.head
        head2=other.head
        if len1 < len2:                 #move the difference ahead
            for i in range(len2-len1):
                head2=head2.next
        else:
            for i in range(len1-len2):
                head1=head1.next
        while head1 != head2:
            head1=head1.next
            head2=head2.next
        return head1

def merge(self, other):
    head1 = self.head
    head2 = other.head

    while head1 != None or head2 != None:
        head1 = head1.next
        head2 = head2.next

    if head1 == None:
        head1 = other.head
        while head2 != None:
            head2 = head2.next
            head1 = head1.next
        head2 = other.head
    else:
        head2 = self.head
        while head1 != None:
            head1 = head1.next
            head2 = head2.next
        head1 = self.head

    while head1.next != head2.next:
        head1 = head1.next
        head2 = head2.next

    return head2.data

def main():
    l1 = LinkedList()
    for i in range(10):
        l1.push(random.randint(1, 100))
    l1.print_list()

    l2 = LinkedList()
    for i in range(5):
        l2.push(random.randint(1, 100))
    l2.print_list()

if __name__ == '__main__':
    main()







