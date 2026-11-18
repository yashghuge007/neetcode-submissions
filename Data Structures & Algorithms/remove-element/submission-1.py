class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        traverse till val
        then till end until non val is found
        k+=1
        swap val and non val
        '''
        i=0
        n= len(nums)
        while i < n:
            if nums[i]==val:
                n-=1
                nums[i]=nums[n]
            else:
                i+=1
            
        return n