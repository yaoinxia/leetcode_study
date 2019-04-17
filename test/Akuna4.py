def minKBitFlips(A, k):
    n = len(A)
    future_switch_order = [0 for i in range(n)]
    print(future_switch_order)
    switch = 0
    ans = 0
    for i in range(n):
        switch ^= future_switch_order[i]
        if A[i] ^ switch == 0:
            ans += 1
            switch ^= 1
            if i + k < n:
                future_switch_order[i + k] = 1
            elif i + k > n:
                    return -1
    return ans

if __name__ == '__main__':
    # s = "+--"
    # s_l = list(s)
    # for i in range(len(s_l)):
    #     if s_l[i]=="+":
    #         s_l[i] = 1
    #     else:
    #         s_l[i] = 0
    # print(s_l)
    print(minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
    # print(minKBitFlips([1, 1, 1, 1, 1], 4))
    # print(minKBitFlips([0, 1, 0, 1, 0], 4))
