"""
The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that
adds the two numbers and returns the sum as a linked list.
"""

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

    #method to sum numbers is list if least significant is at head
    def sum_list(self, list2):
        head1=self.head
        head2=list2.head
        sum_list=LinkedList()
        carry = 0
        while head1 != None or head2 != None:
            if head1 != None:
                carry=carry+head1.data
                head1=head1.next

            if head2 != None:
                carry = carry + head2.data
                head2=head2.next
            sum_list.push(int (carry%10))
            carry=carry/10

            if carry == 1:
                sum_list.push(1)
        return sum_list

def main():
    l1= LinkedList()
    l2 = LinkedList()
    l1.push(6)
    l1.push(1)
    l1.push(7)
    l2.push(2)
    l2.push(9)
    l2.push(5)
    result= l1.sum_list(l2)
    result.print_list()

if __name__ == "__main__":
    main()


