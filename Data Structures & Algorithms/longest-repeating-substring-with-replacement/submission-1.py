class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        ans = 0
        l = 0 

        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]]=0
            lookup[s[i]]+=1

            w = i-l+1 # current spread of str

            if w - max(lookup.values())<=k:
                ans = max(ans,w)
            else:
                lookup[s[l]]-=1
                l+=1
        return ans