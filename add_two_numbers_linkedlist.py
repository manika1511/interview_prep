# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        curr = result
        p = l1
        q = l2
        carry = 0

        while p or q or carry:
            v1 = (p.val if p else 0)
            v2 = (q.val if q else 0)

            sum_s = v1 + v2 + carry
            carry = sum_s / 10
            rem = sum_s % 10
            curr.next = ListNode(rem)
            curr = curr.next

            p = (p.next if p else None)
            q = (q.next if q else None)

        return result.next
