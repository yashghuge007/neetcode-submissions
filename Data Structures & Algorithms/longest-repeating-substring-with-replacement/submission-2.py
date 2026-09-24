class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        seen = {}
        l=0

        for r,c in enumerate(s):
            if c not in seen:
                seen[c]=0
            seen[c]+=1

            w = r-l+1

            if w-max(seen.values())<=k:
                ans = max(ans,w)
            else:
                seen[s[l]]-=1
                l+=1
        
        return ans