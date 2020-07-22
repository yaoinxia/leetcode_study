class Solution:
    def reverseBits(self, n: int) -> int:
        s_n = str(n)
        print(s_n)
        print(int(s_n))
        s_r_n = s_n[::-1]
        print(int(s_r_n))
if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    Solution().reverseBits(n)

