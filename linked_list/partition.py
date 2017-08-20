"""Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes 
greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements 
less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to
 appear between the left and right partitions."""

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

    #method to partition list
    def partition(self, k):
        head= self.head     #head of new list
        tail=self.head      #tail of new list
        start = self.head   #iterator for the given list
        while start != None:
            temp=start.next     #store the address of the next node
            if start.data < k:  #insert at head if smaller than k
                start.next=head
                head=start
            else:
                tail.next=start #insert at tail if larger than k
                tail=start
            start = temp
        tail.next=None          #last node points to Null
        new_list = LinkedList()
        new_list.head=head
        return new_list         #return new list

def main():
    l= LinkedList()
    result=LinkedList()
    l.push(15)
    l.push(14)
    l.push(16)
    l.push(15)
    l.push(15)
    l.push(14)
    l.push(18)
    l.print_list()
    print("--------")
    result=l.partition(15)
    result.print_list()

if __name__ == "__main__":
    main()


