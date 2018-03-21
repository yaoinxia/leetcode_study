#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        if l1==None and l2==None :
            return None
        if l1==None :
            return l2
        if l2==None :
            return  l1
        if l1.val>=l2.val :
            result=l2
            result.next=self.mergeTwoLists(l1,l2.next)
        else :
            result=l1
            result.next=self.mergeTwoLists(l2,l1.next)
        return result

s = Solution()
print(s.mergeTwoLists([1,2,3],[2,3,4]))