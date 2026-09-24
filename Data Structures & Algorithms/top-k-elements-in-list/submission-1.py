class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n not in res:
                res[n]=0
            res[n]+=1
        
        heap = []
        for key,val in res.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        
        return [a for f,a in heap]