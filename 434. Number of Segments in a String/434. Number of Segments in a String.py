class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        print(len(s.split()))
        return len(s.split())

    def countSegments2(self, s):
        if s.isspace():
            return 0
        s1 = s.strip()
        if len(s1) == 0:
            return 0
        m = list(s1)
        d = [0]
        while m:
            if m[0] != '':
                d[-1] += 1
            else:
                d.append(0)
            m.pop(0)
        print(d)
        print(m)
        print(len(d) - d.count(0))

if __name__ == '__main__':
    s = "    23 1 23"
    Solution().countSegments2(s)