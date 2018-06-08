Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

给定两个排序的整数数组nums1和nums2，将nums2合并为nums1作为一个排序数组。

注意：

在nums1和nums2中初始化的元素数量分别是m和n。
你可以假设nums1有足够的空间（大小大于或等于m + n）来保存nums2中的其他元素。
例：

输入：
Nums1 = [1,2,3,0,0,0]，m = 3
Nums2 = [2,5,6]，n = 3


输出：[1,2,2,3,5,6]

思路：
依次比较num1中和num2中各元素吗，当num2中的元素大于num1中某元素，并且小于等于其后面的元素，插入
关键掌握列表的插入
nums1.insert(i+1, nums2[j])

疑问：如何处理插入相应数组后，数组大小的变化

参考网址：https://blog.csdn.net/coder_orz/article/details/51681144