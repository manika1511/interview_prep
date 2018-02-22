# Linkedlist class
class LinkedList(object):
    #method to initialise head
    def __init__(self, head=None):
        self.head=head

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head=new_node

    def print_list(self):
        start=self.head
        while start != None:
            print (start.data)
            start=start.next_node
