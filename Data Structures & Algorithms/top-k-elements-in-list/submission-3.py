class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n]+=1
        
        heap = []
        for i,v in dic.items():
            heapq.heappush(heap,(v,i))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            v,i = heapq.heappop(heap)
            res.append(i)
        return res
