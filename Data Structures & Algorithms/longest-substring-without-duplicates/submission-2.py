class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        ans = 0
        j = 0
        for i in range(n):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[j])
                    j+=1
            else:
                ans = max(ans, i-j+1)
            seen.add(s[i])
        return ans