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
        stack = []
        i = 0
        p = head
        while p:
            stack.append(p.val)
            #print(p.val)
            p = p.next
            i += 1
        #print(stack)
        q = head
        l = []
        for j in range(len(stack)-1, -1, -1):
            #print(j)
            #q.val = stack[j]
            l.append(stack[j])
            #print(q.val)
            #q = q.next
        #print(l)
        return l


if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(3)
    L1.next.next.next = ListNode(4)
    L1.next.next.next.next = ListNode(5)
    Solution().reverseList(L1)
