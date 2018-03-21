#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = len(l1)
        len2 = len(l2)
        total = []
        i = 0
        j = 0
        z = 0
        if l1 != None and l2 !=None:
            while i<len1 and j <len2:
                if l1[i] <= l2[j]:
                    total[z] = l1[i]
                    z+=1
                    i+=1
                elif l1[i] > l2[j]:
                    total[z] = l2[j]
                    z+=1
                    j+=1
        return total


s = Solution()
print(s.mergeTwoLists([1,2,3],[2,3,4]))

