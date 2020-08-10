"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
class Solution:
    def plusOne(self, digits):
        sum = 0
        for i in range(len(digits)):
            print(digits[i])
            sum += digits[i] * (10 ** (len(digits) - i - 1))
        sum0 = sum + 1
        l = []
        while sum0 > 0:
            tmp = sum0 % 10
            l.insert(0, tmp)
            sum0 = sum0 // 10
        # print(l)
        return l

    def plus1(self, digits):
        # 定义进位标志位, 默认为False，即不进位
        temp = True
        for i in range(len(digits)-1, -1, -1):
            # print(digits[i])
            # 不进位，直接末尾加一，eg: 1234
            if temp :
                digits[i] += 1
                if digits[i] <10 :
                    temp = False
                else :
                    digits[i] = 0
            else :
                break

        if digits[0] == 0 :
            digits.insert(0, 1)
            # digits = []*(len(digits)+1)
            # digits[0] = 1

        return digits


if __name__ == '__main__':
    digits = [9,9]
    print(Solution().plus1(digits))