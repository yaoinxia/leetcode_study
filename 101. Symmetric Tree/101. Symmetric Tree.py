# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return root.left == root.right and self.isSameTree(root.right) and self.isSymmetric(root.left)
        else:
            return root

if __name__=="__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(3)

    print(Solution().isSymmetric(t))




