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
        if p and q:
            return p.val==q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left)
        else:
            return p == q

if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)

    print(Solution().isSameTree(t1, t2))


