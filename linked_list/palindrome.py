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

    # method to detect if a linked list is a palindrome
    def palindrome(self):
        slow=self.head
        fast=self.head
        stack = []                           #stack to fill with first half of the elements

        size=self.size()

        while fast.next and fast.next.next:
            stack.append(slow.data)          #append to the list
            slow = slow.next
            fast = fast.next.next

        stack.append(slow.data)             #append the middle element

        if size%2 != 0:                     #if odd size, middle element need not be compared, so remove it from stack
            stack.pop()
        slow=slow.next

        while slow != None:                 #check the elements in stack to the end elements of the list
            check=stack.pop()
            if check == slow.data:
                slow=slow.next
            else:
                return False

        if len(stack) != 0:
            return False
        return True

def main():
    l1= LinkedList()
    l1.push("m")
    l1.push("a")
    l1.push("a")
    l1.push("m")

    print (l1.palindrome())

if __name__ == "__main__":
    main()





