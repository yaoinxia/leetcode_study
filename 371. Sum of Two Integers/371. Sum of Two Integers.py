class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            #c表示与操作
            c = a & b
            #与的操作左移，与下一个异或结果，再进行异或操作
            a = (a ^ b) % 0x100000000
            print(a)
            #进位不断进行左移
            b = (c << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)

if __name__ == "__main__":
    #print(-2 | ~111+1)
    print(Solution().getSum(-1, 1))