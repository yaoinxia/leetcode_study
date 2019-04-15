#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

def find_num(li):
    # 使用桶排序的思想
    # 定义长度为n+1长度的列表，初始都初始化为0
    init_l = [0]*(li[0]+1)
    # 遍历给定数组，如果存在就设置为1
    for i in range(1, len(li)):
        init_l[li[i]] = 1
    for j in range(0, li[0]+1):
        if init_l[j] == 0:
            print(j)

# 小招喵跑步
def cat_run(x):
    # 有三种走法
    x = abs(x)
    if x<=3:
        return x
    else:
        if x%2 == 0:
            return cat_run(x//2)+1
        else:
            return cat_run(x//2)+2 if cat_run(x//2)<cat_run(x//2+1) else cat_run(x//2+1) + 2

# 年会抢玩偶
"""
某公司年会上，组织人员安排了一个小游戏来调节气氛。游戏规则如下：
N个人参与游戏，站成一排来抢工作人抛来的M个小玩偶。为了增加游戏的趣味和难度，规则规定，
参与游戏的人抢到的礼物不能比左右两边的人多两个或以上，否则会受到一定的惩罚。游戏结束时拥有玩偶最多的人将获得一份大奖。
假设大家都想赢得这份大奖，请问站在第K个位置的小招在赢得游戏时，最多能拥有几个玩偶？

输入为用空格分隔的3个正整数，依次为：参与游戏人数N、玩偶数M、小招所在位置K
"""
def catch_doll():
    N, M, K = [int(num) for num in input().split()]
    if K < 1 or K > N:
        print(0)
        exit()
    if N == 1:
        print(M)
        exit()
    cnt = 0
    i = j = K
    need = j - i + 1
    while M >= need:
        cnt == 1
        M -= need
        i = max(1, j-1)
        j = min(N, j+1)
        need = j - i + 1
    print(cnt)


def Huaxue(x, value):
    # 先排序
    # print(sorted(value))
    v_s = sorted(value)
    min_v = min(v_s)
    max_v = max(v_s)
    for i in range(0, x):
        if v_s[i] % 2 == 0:
            continue
        else:
            break
    if i == x-1:
        print(int(max_v//min_v/2))





if __name__ == '__main__':
    # line = sys.stdin.readline().strip()
    # # 把每一行的数字分隔后转化成int列表
    # values = list(map(int, line.split()))
    # li = [3, 3, 0, 1]
    # find_num(values)

    x = int(sys.stdin.readline().strip())
    # print(cat_run(x))
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    Huaxue(x, values)
