class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for i in range(1,numRows):
            print("==================================")
            print(i)
            l.append([])
            for j in range(i+1):
                print("++++++++++++++++++++++++")
                print(j)
                l[i].append((l[i - 1][j - 1] if j > 0 else 0) + (l[i - 1][j] if j < i else 0))
        return l

if __name__ == "__main__":
    print(Solution().generate(5))