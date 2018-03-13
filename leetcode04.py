class Solution(object):
    def getKth(self, A, B, k):
        lenA = len(A);
        lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k / 2, lenA);
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, A, B ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB) / 2 + 1)
        else:
<<<<<<< HEAD
            return (self.getKth(A, B, (lenA + lenB) / 2) + self.getKth(A, B, (lenA + lenB) / 2 + 1)) * 0.5




=======
            for i in nums1:


                
>>>>>>> 8cd90e0ade96e1fae0a1cef2001ebfbd0abd789e
