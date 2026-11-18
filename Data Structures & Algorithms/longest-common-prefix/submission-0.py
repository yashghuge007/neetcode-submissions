class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for i,w in enumerate(strs):
            j = 0
            while j < min(len(ans),len(w)):
                if ans[j]!=w[j]:
                    break
                j+=1
            ans = ans[:j]
        return ans