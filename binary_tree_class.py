class Node(object):
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val



class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.value):
            if (node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if (node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    #inorder traversal
    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print (str(node.data) + ' ')
            self._printTree(node.right)


def main():
    tree = BinaryTree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    print (tree)

if __name__ == "__main__":
    main()