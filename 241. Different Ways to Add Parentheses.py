#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        # print(input[1])
        # print(input[0:])
        # print(input[:2])
        # print(len(input))
        length = len(input)
        ch = ['*', '-', '+']
        for i in range(length):
            if input[i] in ['*', '-', '+']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == "+":
                            result.append(l+r)
                        elif input[i] == "*":
                            result.append(l*r)
                        elif input[i] == "-":
                            result.append(l-r)
        if not result:
            result.append(int(input))
        print(result)
        return result



if __name__ == '__main__':
    input = "2*3-4*5"
    Solution().diffWaysToCompute(input)

