"""Write code to remove duplicates from an unsorted li nked list.How would you solve this problem if a 
temporary buffer is not allowed?"""

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

    #method to remove duplicate nodes USING BUFFER
    def remove_dups(self):
        current = self.head #start with head

        buffer = {current.data: True} #store the value of head in  the buffer

        while current.next != None:   #while th elast element is not reached
            next_node = current.next  #pointer to the second element

            if next_node.data not in buffer:    #check if the value already in buffer
                buffer[next_node.data] = True   #if not, store in the buffer
                current = current.next
            else:
                current.next = next_node.next   #else delete it

    #method to remove duplicates W/O USING BUFFER
    def remove_dups_no_buf(self):
        start = self.head

        while start != None:
            prev = start
            check = start.next

            while check != None:
                if check.data == start.data:
                    prev.next = check.next
                    check = check.next
                else:
                    prev = check
                    check = check.next

            start = start.next

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
    print ("--------")
    l.remove_dups_no_buf()
    l.print_list()

if __name__ == "__main__":
    main()


