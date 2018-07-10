from jieba import xrange


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for k in nums1:
            index = -1
            for j in xrange(0, len(nums2)):
                if nums2[j] == k:
                    index = j
                    break
            if index != -1:
                res.append(k)
                del nums2[index]
        return res

 if __name__ == "__main__":
     n1 = [1, 2, 2, 0, 3]
     n2 = [0, 2]
     print(Solution().intersect(n1, n2))

