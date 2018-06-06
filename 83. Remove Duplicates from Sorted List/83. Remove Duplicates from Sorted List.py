# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{}->{}".format(self.val,self.next)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head

        while p != None and p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

if __name__=="__main__":
    l1=ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(2)
    l1.next.next.next=ListNode(3)
    print(l1)
    s = Solution()
    s2 = s.deleteDuplicates(l1)
    print(s2)
