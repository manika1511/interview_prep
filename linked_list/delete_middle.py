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

    #method to delete middle node.. take two pointers: slow and fast(2 steps)..when fast reaches the end, then the
    #slow is pointing at the middle
    def delete_middle(self):
        slow = self.head
        fast = self.head
        prev = self.head

        while fast.next != None:
            prev = slow
            slow=slow.next
            fast=fast.next
            fast=fast.next

        prev.next = slow.next

def main():
    l= LinkedList()
    l.push(15)
    l.push(14)
    l.push(16)
    l.push(15)
    l.push(15)
    l.push(14)
    l.push(18)
    l.print_list()
    print ("-----")
    l.delete_middle()
    l.print_list()

if __name__ == '__main__':
    main()