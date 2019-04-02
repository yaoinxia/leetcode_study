"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        """
        i=0
        j=0
        len = m
        while i<m and j<n:
            if nums1[i]<=nums2[j] and nums2[j]<nums1[i+1]:
                nums1.insert(i+1, nums2[j])
                j+=1
                i+=2
                len +=1
            elif i==len-1 and nums2[j] > nums1[i]:
                while j < n:
                    nums1.insert(i+1,nums2[j])
                    i+=1
                    j+=1
            else:
                i+=1

        return nums1
"""
        p, q, k = m - 1, n - 1, m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[k] = nums1[p]
                p, k = p - 1, k - 1
            else:
                nums1[k] = nums2[q]
                q, k = q - 1, k - 1
        nums1[:q + 1] = nums2[:q + 1]
        return nums1

s = Solution()
s2 = s.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(s2)


