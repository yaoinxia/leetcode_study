class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sn = len(s)
        tn = len(t)
        lists = []
        listt = []
        if sn != tn:
            return False
        for i in range(0, sn):
            lists.append(s[i])
        #print(lists)
        #print("-----------------------------------")
        for j in range(0, tn):
            listt.append(t[j])
        #print(listt)
        listt.sort()
        #print(listt)
        lists.sort()
        #print(lists)
        if lists == listt:
            return True
        else:
            return False
        # letters = {}
        # letters2 = {}
        # for c in s:
        #     letters[c] = letters[c] + 1 if c in letters else 1
        #     #print(letters[c])
        #     print(letters)
        # print("=======================================")
        # for d in s:
        #     letters2[d] = letters2[d] + 1 if d in letters2 else 1
        #     #print(letters2[c])
        #     print(letters2)
        # if letters == letters2:
        #     return True
        # else:
        #     return False
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        思路：定义一个26长度的列表，每个元素都是0，在s中进行扫描，扫描到，对应列表元素位置加一
        在t中扫描，相应元素再减一。
        """
        a = [0] * 26
        for c in s:
            a[ord(c)-ord('a')] += 1
        for c in t:
            a[ord(c)-ord('a')] -= 1
        for sc in a:
            if sc != 0:
                return False
        return True


if __name__ == "__main__":
    a = "anagram"
    b = "nagaram"
    print(Solution().isAnagram(a, b))