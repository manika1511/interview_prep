# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is not None:
            stack = list()
            stack.append(root)

            while len(stack) > 0:
                node = stack.pop()
                if node is not None:
                    result.append(node.val)
                    if node.right is not None:
                        stack.append(node.right)
                    if node.left is not None:
                        stack.append(node.left)

        return result

