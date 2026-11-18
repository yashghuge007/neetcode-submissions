class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = strs[0]
        for w in strs:
            j = 0
            while j < min(len(ans),len(w)):
                if ans[j]!=w[j]:
                    break
                j+=1
            ans = ans[:j]
        return ans