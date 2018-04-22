Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
给定一个表示非负整数的非空数字数组，加上一个整数。
数字被存储为使得最高有效数字位于列表的头部，并且数组中的每个元素都包含单个数字。
您可以假定整数不包含任何前导零，除****了数字0本身。

例1：

输入：[1,2,3]
输出：[1,2,4]
说明：数组表示整数123。
例2：

输入：[4,3,2,1]
输出：[4,3,2,2]
说明：数组表示整数4321。

初步思路：
1.直接用数组来做
2.先转化为整数，加上一，然后再转化为数组
3.有没有直接可以数组转化为整数的，以及整数转化为数组的函数或者方法

出现错误：
IndexError: list assignment index out of range
解决：
在如上代码中，l[]一开始就是个空数组，后面又对该空数组进行赋值，必然会越界。最好的解决办法是用append方法或者insert方法插入新元素。
例：
l.append('test')

心得：
使用的是基于第2种思路，先转化为整数
很多地方使用到了强制类型转换
h = 5 

h ** 2               #h的二次方 25

h ** 3               #h的三次方 125

网上其他人思路：
从后向前扫描数组，每位加一，有进位则变成0且保留进位。最高位如果是9且有进位则要在数组前面多加一个元素1。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(xrange(0, len(digits))):
            digit = (digits[i] + carry) % 10
            carry = 1 if digit < digits[i] else 0
            digits[i] = digit
        if carry == 1:
            return [1] + digits
        return digits