class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = nums1.length
        len2 = nums2.length
        median = 0
        if nums1[len1-1] < nums2[0]:
            median = nums1[len1-1]+nums2[0]
        #插入排序
        else:
            for i in nums1:
                
