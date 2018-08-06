class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            print(i)
            if i in map:
                #print(map([i]))
                return True
            map[i] = True
        return False

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    b = Solution().containsDuplicate(nums)
    print(b)
