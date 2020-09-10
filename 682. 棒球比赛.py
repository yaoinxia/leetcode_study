class Solution:
    def calPoints(self, ops) -> int:
        # 操作列表
        op = ["+", "D", "C"]
        # 考虑长度为1的情况
        if len(ops) == 1:
            if ops[0] in op:
                return 0
            else:
                return int(ops[0])
        # 存放轮数
        n = 0
        # 总数和
        sum = 0
        l = []
        # 具体操作，会对1， 2， 产生影响
        i = 0
        while i < len(ops):
            if ops[i] not in op:
                l.append(int(ops[i]))
            if ops[i] == "D" and len(l)>=1:
                t = l[-1] * 2
                l.append(t)
            if ops[i] == "+" and len(l)>=2:
                t1 = l[-1]+l[-2]
                l.append(t1)
            if ops[i] == "C" and len(l)>=1:
                del l[-1]
            i += 1
        for c in l:
            sum += c

        return sum


print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))

