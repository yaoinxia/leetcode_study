def findFlips(str, n):

    last = ''
    res = 0

    for i in range( n) :

    # If last character is not equal
    # to str[i] increase res
        if (last != str[i]):
            res += 1
            last = str[i]

    # To return min flips
    return res // 2


    # Driver Code
if __name__ == '__main__':

    str = "00011110001110"

    n = 4

    print(findFlips(str, n))