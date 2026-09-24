class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n  = len(s)
        sett = set()
        j = 0
        res = 0
        for i in range(n):
            if s[i] in sett:
                while s[i] in sett:
                    sett.remove(s[j])
                    j+=1
            else:
                res = max(res, i-j+1)
            sett.add(s[i])
        return res