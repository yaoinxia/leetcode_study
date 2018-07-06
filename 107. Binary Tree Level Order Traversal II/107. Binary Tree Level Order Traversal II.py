# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        



if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.left.left = TreeNode("null")
    t.left.right = TreeNode("null")
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print(Solution().levelOrderBottom(t))

