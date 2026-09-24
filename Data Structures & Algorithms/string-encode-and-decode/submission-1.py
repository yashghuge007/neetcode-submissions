class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            m = len(s)
            msg = str(m)+"~"+s
            res+=msg
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        n = len(s)
        ans = []
        while l<n:
            c = 0
            while s[l]!='~':
                c= c*10+int(s[l])
                l+=1
            msg = ''
            l+=1
            while c>0:
                msg+=s[l]
                l+=1
                c-=1
            ans.append(msg)
        return ans

