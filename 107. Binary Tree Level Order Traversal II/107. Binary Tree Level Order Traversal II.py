# Definition for a binary tree node.
from datashape import null


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
        #存放最终结果
        res = []
        #如果为空，返回结果列表
        if not root:
            return res
        curr_root = [root]
        while curr_root:
            level_result = []
            next_root = []
            for temp in curr_root:
                level_result.append(temp.val)
                if temp.left:
                    next_root.append(temp.left)
                if temp.right:
                    next_root.append(temp.right)
            res.append(level_result)
            curr_root = next_root
        res.reverse()
        return res

if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.left.left = TreeNode("null")
    t.left.right = TreeNode("null")
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print(Solution().levelOrderBottom(t))
    #print(Solution().levelOrderBottom(t))

