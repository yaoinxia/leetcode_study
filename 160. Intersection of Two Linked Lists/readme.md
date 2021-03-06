---
layout: post
title: "160. Intersection of Two Linked Lists"
tag: leetcode刷题笔记
---

Write a program to find the node at which the intersection of two singly linked lists begins.
编写程序以找到两个单链表开头的节点。


For example, the following two linked lists:
~~~
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
~~~

begin to intersect at node c1.
开始在节点c1处相交。

**Notes:**

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
如果两个链接列表根本没有交集，则返回null。
函数返回后，链接列表必须保留其原始结构。
您可以假设整个链接结构中没有任何循环。
您的代码最好在O（n）时间内运行，并且只使用O（1）内存。
积分：
特别感谢@stellari添加此问题并创建所有测试用例。

**网上思路：**
<https://blog.csdn.net/coder_orz/article/details/51615444>

~~~python
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
~~~
        