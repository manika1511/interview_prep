class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def set_data(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node=new_next