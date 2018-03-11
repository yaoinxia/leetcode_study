class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        '''
        num = 0
        for i in J:
            for j in S:
                if J[i] == S[j]:
                    num=num+1
                else:
                    continue
        
        return  num
        '''
        return sum(map(J.count, S))

