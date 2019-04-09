#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import math
def xiecheng2(n, str, list):

# 高斯概率密度
def calc_gaosi(x, mean, std):
    ex = math.exp(-(math.pow(x-mean,2)/(2*math.pow(std, 2))))
    return (1/(math.sqrt(2*math.pi)*std))*ex


if __name__ == "__main__":
    # 读取第一行的n
    num = int(sys.stdin.readline().strip())
    str = sys.stdin.readline().strip().split(" ")
    l_s = list(str)
    print(l_s)
    l_v = []
    for i in range(num):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        l_v.append(values)
        # print(values)
    xiecheng2(num, l_s, l_v)