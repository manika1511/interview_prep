from .node_class import Node

# Linkedlist class

class LinkedList(object):
    #method to initialise head
    def __init__(self, head=None):
        self.head=head

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head=new_node

    



