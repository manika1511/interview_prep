# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object): #O(n) time complexity, O(n) space .. avg o(log n)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.caller_function(root, result)
        return result

    def caller_function(self, node, result):
        if node != None:
            self.caller_function(node.left, result)
            result.append(node.val)
            self.caller_function(node.right, result)

    def inorder_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

