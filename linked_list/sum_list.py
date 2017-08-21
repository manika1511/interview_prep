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

    def size(self):
        start=self.head
        size=0
        while start!=None:
            size=size+1
            start=start.next
        return size

    #method to sum numbers in list if least significant is at head
    def sum_list_reverse_digits(self, list2):
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

    # method to sum numbers in list if most significant is at head
    def sum_list_forward_digits(self, list2):
        size1=self.size()
        size2=list2.size()
        if size1 > size2:
            count=size1-size2
            while count > 0:
                size2.push(0)
                count=count-1
        else:
            count = size2 - size1
            while count > 0:
                size1.push(0)
                count=count-1

        head1=self.head
        head2=list2.head
        print (head2.data)
        sum_list=LinkedList()
        sum_list_prev=sum_list.head
        carry=0

        while head1 is not None or head2 is not None:
            if head1 is not None:
                digit1 = head1.data
            else:
                digit1 = 0
            if head2 is not None:
                digit2 = head2.data
            else:
                digit2 = 0

            sum = carry + digit1 + digit2
            carry = round (sum / 10)

            if sum_list.head == None:
                sum_list.push(sum)
                sum_list_prev=sum_list.head
            else:
                if sum_list_prev!=None:
                    if carry > 0 and sum_list_prev!=None:
                        sum_list_prev.data=sum_list_prev.data + carry
                    sum_list.push(sum%10)
                    sum_list_prev=sum_list_prev.next

            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next
        return sum_list


def main():
    l1= LinkedList()
    l2 = LinkedList()
    l1.push(7)
    l1.push(1)
    l1.push(6)
    l2.push(5)
    l2.push(9)
    l2.push(2)
    result=l1.sum_list_forward_digits(l2)
    result.print_list()

if __name__ == "__main__":
    main()


