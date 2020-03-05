# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        end = k - 1

        while end != 0:
            i = 0
            j = end

            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i = i + 1
                j = j - 1

                if i >= j:
                    end = j

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return None

        head_pointer = ListNode(-1)
        prev = head_pointer
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l2 is None else l2

        return head_pointer.next


