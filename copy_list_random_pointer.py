"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head): #O(n) space and O(n) time
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        initial_node = head
        new_node = Node(head.val, None, None)
        self.visited[initial_node] = new_node

        while initial_node != None:
            new_node.random = self.get_node_copy(initial_node.random)
            new_node.next = self.get_node_copy(initial_node.next)

            initial_node = initial_node.next
            new_node = new_node.next
        return self.visited[head]

    def get_node_copy(self, node):
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val, None, None)

            return self.visited[node]
        return None

    def copyRandomList2(self, head): #O(n) time and O(1) space
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        curr = head

        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        curr = head
        clone = head.next

        while curr.next:
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp
        return clone





