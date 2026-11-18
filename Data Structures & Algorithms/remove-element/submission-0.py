class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        traverse till val
        then till end until non val is found
        k+=1
        swap val and non val
        '''
        k=0
        n= len(nums)
        for i in range(n):
            if nums[i]!=val:
                k+=1
                continue
            j=i+1
            while j<n:
                if nums[j]!=val:
                    k+=1
                    nums[i],nums[j]=nums[j],nums[i]
                    break
                j+=1
            
        return k