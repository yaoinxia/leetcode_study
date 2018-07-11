from math import fmod

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n+1):
            if fmod(i, 3) == 0:
                if fmod(i,15) == 0:
                    l.append("FizzBuzz")
                else:
                    l.append("Fizz")
            elif fmod(i, 5) == 0 and fmod(i, 15) != 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l

if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))
