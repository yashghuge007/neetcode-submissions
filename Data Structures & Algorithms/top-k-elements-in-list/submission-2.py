class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n]+=1
        
        heap = []
        for n, f in m.items():
            heapq.heappush(heap,(f,n))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
