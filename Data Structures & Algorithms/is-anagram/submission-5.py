class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c]=0
            m[c]+=1
        
        for c in t:
            if c not in m:
                return False
            m[c]-=1
        

        return True if all(p == 0 for p in m.values()) else False