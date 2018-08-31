Given a singly linked list, determine if it is a palindrome.
给出一个单链表，确定它是否是回文。

__Example 1:__

Input: 1->2

Output: false

__Example 2:__

Input: 1->2->2->1
Output: true

__Follow up:__

Could you do it in O(n) time and O(1) space?

- 思路
把链表转化成数组，然后分别从数组的头部和尾部开始比较

- 用时
30分钟

~~~
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
~~~




