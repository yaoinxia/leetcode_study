#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
    print(array)

def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    # array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    # Solution().findKthLargest2(nums, k)
    quick_sort(nums, 0, 8)