class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        
        temp = []
        for c in s:
            if c=='0':
                temp[-1]=temp[-1]+c
                if int(temp[-1])>26:
                    return 0
            else:
                temp.append(c)
        
        tn = len(temp)
        if tn<2:
            return 1
        
        dp = dp2 = 1
        dp1 = 2 if 1<=int(temp[0]+temp[1])<=26 else 1
        for i in range(2,tn):
            if 1<=int(temp[i-1]+temp[i])<=26:
                dp = dp1+dp2
            else:
                dp = dp1
            dp2 = dp1
            dp1 = dp
        return dp1