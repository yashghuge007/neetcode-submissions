class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs)==1:
        #     return [strs]

        temp = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')]+=1
            
            temp[tuple(key)].append(s)
        
        return list(temp.values())
