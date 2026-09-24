class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        r = len(heights)-1

        while l<r:
            w = r-l
            h = 0

            if heights[l] < heights[r]:
                h=heights[l]
                l+=1
            else:
                h=heights[r]
                r-=1
            ans = max(ans,w*h)
        return ans