# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n): #in two passes O(n)
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len_list = 0
        p = head
        while p:
            len_list = len_list + 1
            p = p.next

        if len_list == 0:
            return head

        from_front = len_list - n + 1
        if from_front == 1:
            return head.next

        curr = head
        prev = head
        x = 1
        while x != from_front:
            prev = curr
            curr = curr.next
            x = x + 1

        prev.next = curr.next
        return head

    def removeNthFromEnd2(self, head, n): #Single pass O(n)
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result_head = ListNode(0)
        result_head.next = head
        first = result_head
        second = result_head
        x = 0
        while x < n:
            second = second.next
            x = x + 1

        prev = first
        while second:
            prev = first
            first = first.next
            second = second.next

        prev.next = first.next
        return result_head.next

