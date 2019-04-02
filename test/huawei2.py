#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

def split(input):
    tmp = int(input[0])
    s = input[1:]
    if tmp == 0:
        return "".join(list(reversed(s)))
    else:
        return s

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    i = 0
    re = []
    while i < num:
        input = s[i*9: (i+1)*9]
        t = split(input)
        re.append(t)
        i += 1
    # print(re)
    total = ''
    for i in range(num):
        st = re[i]
        # print(st)
        if i == num - 1:
            total = total + st
        else:
            total = total + st + ' '
        # if i != len(re) - 1:
        #     total = st + total
    print(total)


