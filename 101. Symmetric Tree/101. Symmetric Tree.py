# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def compare(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val == right.val:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.compare(root.left, root.right)

if __name__=="__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(3)

    print(Solution().isSymmetric(t))




