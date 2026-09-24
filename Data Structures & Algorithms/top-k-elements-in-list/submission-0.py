class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        lookup = Counter(nums)
        for key,val in lookup.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        ans = []
        for f,a in heap:
            ans.append(a)
        return ans