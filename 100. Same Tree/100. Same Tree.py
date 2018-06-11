# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pl = p.left
        pr = p.right
        ql = q.left
        qr = q.right
        if p.val == q.val and pl.val == pr.val and ql.val == qr.val:
            return True
        else:
            return False

t1 = TreeNode(5)
t2 = TreeNode(4)
t3 = TreeNode(1)



s = Solution()
s2 = s.isSameTree(3)


