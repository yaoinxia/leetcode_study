# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        p.val = p.next.val
        p.next = p.next.next

if __name__ == "__main__":
    l = ListNode(4)
    l.next = ListNode(5)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(9)
    Solution().deleteNode(ListNode(5))