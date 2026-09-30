class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l = 0
        r = 0
        ans = 0

        while r<len(s):
            freq[s[r]]+=1

            while 0<=(r-l+1)-max(freq.values())>k:
                freq[s[l]]-=1
                l+=1
            
            ans = max(ans,r-l+1)
            r+=1
        
        return ans