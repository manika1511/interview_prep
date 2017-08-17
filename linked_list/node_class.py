# Node class to define linked list nodes
class Node(object):
    # constructor to initialise node
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # method to get the data in a particular node
    def get_data(self):
        return self.data

    # method to get the next_node
    def get_next(self):
        return self.next_node

    # method to get set the next_node
    def set_next(self, new_next):
        self.next_node = new_next

