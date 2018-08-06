# Definition for singly-linked list.
from datashape import null


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length