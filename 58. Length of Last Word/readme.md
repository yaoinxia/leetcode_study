Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

给定一个字符串s由大写/小写字母和空白字符''组成，返回字符串中最后一个单词的长度。

如果最后一个字不存在，则返回0。

注意：单词被定义为只包含非空格字符的字符序列。


学习笔记：
s = "abced aa bb cc "
print(s[3])
print(s.split(" "))
print(s.split(" ").__len__())
print(s.split(" ")[3])
output:
['abced', 'aa', 'bb', 'cc', '']
5
cc

学习心得：
学会使用python自带的一些字符串的操作
比如怎么分割字符串，然后会将分割的字符串作为词典进行存储
然后就可以使用词典的方法来进行操作


别人做法：
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s.split()
        if len(s) > 0:
            return len(s[-1])
        return 0

split()和split(" ")是有区别的，使用split直接就返回非空字符了。


