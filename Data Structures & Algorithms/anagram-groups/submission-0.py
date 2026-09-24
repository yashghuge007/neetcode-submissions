class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup =defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            lookup[temp].append(s)
        ans = []
        for val in lookup.values():
            ans.append(val)
        return ans