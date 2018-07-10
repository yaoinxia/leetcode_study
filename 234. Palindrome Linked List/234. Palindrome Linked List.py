# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #num:记录链表长度
        num = 0
        node = []
        p = head
        while p:
            node.append(p.val)
            p = p.next
            num += 1
        print(num)
        print(node)
        i = 0
        j = num-1
        while i <= j:
            if node[i] == node[j]:
                i += 1
                j -= 1
            else:
                return False
        return True



if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)
    print(Solution().isPalindrome(l))


