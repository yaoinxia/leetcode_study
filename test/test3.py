#!/usr/bin/env python
# _*_ coding:utf-8 _*_

if __name__ == '__main__':
    l1 = [1, 2, 4, 6, 10, 11]
    d = {1: 1, 2: 5, 4: 8, 6: 4, 10: 3, 11: 2}
    l = []
    maxS = 0
    for i in range(0, len(l1)):
        for j in range(i, len(l1)):
            sum0 = int(d.get(i) + d.get(j))
            if sum0 > maxS:
                maxS = sum0
    # d.values()[0]
    print(maxS)
    # for c in d.values():
    #     l.append(c)
    #     print(c)
    #
    # print(d.get(d.keys()))
    # print(d.get(0))
    # d.get(1)+d.get(2)