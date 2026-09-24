class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left=[0]*(n)
        right=[0]*(n)

        left[0] = heights[0]
        right[n-1] = heights[n-1]
        
        for i in range(1,n):
            left[i]=max(left[i-1],heights[i])
            right[n-1-i]=max(right[n-i],heights[n-1-i])
        
        ans = 0

        for i in range(n):
            ans+= min(left[i],right[i])-heights[i]
        
        return ans