#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def divisorGame(self, N):
        return N % 2 == 0


if __name__ == '__main__':
    t = Solution().divisorGame(21)
    print(t)