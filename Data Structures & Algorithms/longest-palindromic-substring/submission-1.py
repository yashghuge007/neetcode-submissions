class Solution:
    def helper(self,s,l,r):
        ans = ''
        while l>=0 and r<len(s) and s[l]==s[r]:
            ans=s[l:r+1] #if l==r else s[l]+ans+s[r]
            l-=1
            r+=1
        return ans
        
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            odd = self.helper(s,i,i)
            if len(odd) > len(ans):
                ans = odd
            
            even = self.helper(s,i,i+1)
            if len(even) > len(ans):
                ans = even
        
        return ans