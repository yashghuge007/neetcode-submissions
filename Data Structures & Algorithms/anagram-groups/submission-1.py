class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in res:
                res[temp].append(s)
            else:
                res[temp] = [s]
        return [x for x in res.values()]