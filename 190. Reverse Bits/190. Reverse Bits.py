class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nb = bin(n)[:1:-1]
        print(nb)
        return int(nb + '0'*(32-len(nb)), 2)

if __name__ == "__main__":
    print(Solution().reverseBits(6))