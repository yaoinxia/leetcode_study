# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        length0 = int(length/2)
        #print(length0)
        root = TreeNode(nums[length0])
        root.left = self.sortedArrayToBST(nums[:length0])
        root.right = self.sortedArrayToBST(nums[length0+1:])
        return root


if __name__ == "__main__":
    nodes = [-10, -3, 0, 5, 9]
    nodes1 = [1]
    print(Solution().sortedArrayToBST(nodes))




