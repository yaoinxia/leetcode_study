# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        newList = []
        while p:
            newList.insert(0, p.val)
            p = p.next

        p = head
        for v in newList:
            p.val = v
            print(p.val)
            p = p.next
        return head



if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(3)
    L1.next.next.next = ListNode(4)
    L1.next.next.next.next = ListNode(5)
    print(Solution().reverseList(L1))
