#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Definition for singly-linked list.
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
        n_a = 0
        n_b = 0
        while headA:
            while headB:
                if headA.val == headB.val:
                    print(headA.val)
                    return headA.val
                    break
                else:
                    headB = headB.next
            headA = headA.next
        if headA == None:
            print("null")
            return "null"



if __name__ == '__main__':
    a1 = ListNode(4)
    print(a1.val)
    a1.next = ListNode(1)
    print(a1.next.val)
    # num = 0
    # while a1:
    #     num += 1
    #     a1 = a1.next
    # print(num)
    a2 = ListNode(1)
    print(a2.val)
    a2.next = ListNode(5)
    print(a2.next.val)
    Solution().getIntersectionNode(a1, a2)


