# Node class to define linked list nodes
class Node(object):
    # constructor to initialise node
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

