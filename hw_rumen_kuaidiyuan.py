class Solution:
    def find_minMans(self, points):
        man_num = 0
        i = 0
        while i < len(points):
            if points[i] == 1:
                man_num += 1
                i = i + 3
            else:
                i += 1
        return man_num

if __name__ == '__main__':
    points = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1]
    obj = Solution()
    print(obj.find_minMans(points))
