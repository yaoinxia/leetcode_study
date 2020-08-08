# Definition for singly-linked list.
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
1->2->4: p 
1->3->4: q
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # print(l1.val, l2.val)
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2
        # print(prehead.next.val)
        return prehead.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    Solution().mergeTwoLists(l1, l2)


