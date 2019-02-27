#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# input:输入是行数
# output:输出是一个列表，该行的数值
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 首先初始化一个列表l,里面所有的元素都是1,列表长度为row+1
        l = [1]*(rowIndex+1)
        print(l)
        if (rowIndex <= 1):
            return l
        last = 1
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                temp = l[j]
                l[j] = last + l[j]
                last = temp
        print(l)
        return l

if __name__ == '__main__':
    Solution().getRow(4)

