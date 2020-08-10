import re

def nums_match(l):
    # 白名单
    d = {}
    # # 通配符
    tmp = []
    for action, number in l:
        if action == "M":
            if "*" in number:
                n0 = number.split("*")[0]
                tmp.append(n0)
            elif number not in tmp:
                tmp.append(number)
            else:
                continue

        if action == "C":
            for a in tmp:
                if a == number:
                    if number in d:
                        d[number][0] += 1
                    else:
                        d[number] = [1,0]
                else:
                    if len(a)<len(number):
                        print(number[:len(a)] == a)
                        if number[:len(a)] == a:
                            if number in d:
                                d[number][0] += 1
                            else:
                                d[number] = [1, 0]
                        else:
                            if number in d:
                                d[number][1] += 1
                            else:
                                d[number] = [0, 1]
                    else:
                        if number in d:
                            d[number][1] += 1
                        else:
                            d[number] = [0, 1]


            # for a in tmp:
            #     ret = re.match(a, number)
            #     if ret: #如果通配符能匹配，相应位置+1，否则，继续
            #         if number not in d:
            #             d[number] = [1, 0]
            #         else:
            #             d[number][0] += 1

            # if number not in d:
            #     d[number] = [0, 1]
    print(d)

def nums_match2(l):
    # 白名单
    m = []
    c = {}
    for action, number in l:
        if action == "M":
            m.append(number)
        elif action == "C":
            c[number] = []

if __name__ == '__main__':
    n = 6
    l = [("M", "18820986931"),
         ("C", "18820986931"),
         ("M", "1882097*"),
         ("C", "18820977931"),
         ("C", "18820976932"),
         ("C", "18820976944"),]

    nums_match(l)