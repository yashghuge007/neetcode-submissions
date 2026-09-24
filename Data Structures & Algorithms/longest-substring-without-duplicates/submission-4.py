class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l=0
        
        for r,c in enumerate(s):
            # if c in seen:
            while c in seen:
                seen.remove(s[l])
                l+=1
            # else:
            ans = max(ans,r-l+1)
            seen.add(c)
        
        return ans
