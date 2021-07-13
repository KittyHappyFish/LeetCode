'''
    使用dp方式尝试解题
'''

# import numpy as np


class Solution:
    # def find_ans(self, s):
    #     if s =='0': return 0
        
    #     if (len(s)>1):
    #         if (int(s[:2]) in range(1,27)): 
    #             return self + self.find_ans(s[2:])
        
    #     if len(s)>=1:
    #         ans = find_ans(s[1:])
        
    #     return   
    
    def numDecodings(self, s: str) -> int:
        if s[0] =='0' : return 0
        if len(s) == 1: return 1

        legal = set( str(i) for i in range(1,27,1))
        # print(legal)
        d = [0] * len(s)
        d[0] = 1
        if s[1] not in legal:
            if s[:2] in legal:
                d[1] = 1
            else:
                d[1] = 0
        else:
            if s[:2] in legal:
                d[1] = 2
            else:
                d[1] = 1

        for i in range(2,len(s)):
            if s[i] not in legal:
                if s[i-1:i+1] not in legal:
                    return 0
                else:
                    d[i] = d[i-2]
            else:
                if s[i-1:i+1] not in legal:
                    d[i] = d[i-1]
                else:
                    d[i] = d[i-1] + d[i-2]
        return d[-1]

if __name__ == '__main__':

    s = '226'

    t = Solution()
    print('s=', t.numDecodings(s))