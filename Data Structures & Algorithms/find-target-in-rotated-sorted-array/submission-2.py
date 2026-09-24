class Solution:
    def getRotationIndex(self, nums: List[int]):
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=nums[0]:
                l = mid+1
            else:
                r = mid
        return l
    
    def search(self, nums: List[int], target: int) -> int:
        idx = self.getRotationIndex(nums)
        print(idx)
        l,r = 0,len(nums)-1
        # if idx!=0:
        if target>=nums[0]:
            r = idx
        else:
            l = idx
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1
