class Solution:
    # 采用异或的方法
    def findTheDifference(self, s: str, t: str) -> str:
        tmp = s + t
        # 返回对应ASCII码值
        res = ord(tmp[0])
        # print(res)
        for t in tmp[1:]:
            res ^= ord(t)
        return chr(res)

if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))

