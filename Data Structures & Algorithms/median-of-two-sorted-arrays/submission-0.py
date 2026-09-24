class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        def findTarget(target):
            l,r = 0,0
            curr = 0

            while l<m and r<n:
                if curr == target:
                    return nums1[l] if nums1[l]<=nums2[r] else nums2[r]
                if nums1[l]<=nums2[r]:
                    l+=1
                else:
                    r+=1
                curr+=1
            
            while l<m:
                if curr == target:
                    return nums1[l]
                l+=1
                curr+=1
            
            while r<n:
                if curr == target:
                    return nums2[r]
                curr+=1
                r+=1

        def odd():
            target = (m+n)//2
            return findTarget(target)

        def even():
            t1 = (m+n)//2-1
            print(t1)
            n1 = findTarget(t1)
            n2 = findTarget(t1+1)
            print(n1,n2)
            return (n1+n2)/2

        return even() if (m+n)%2==0 else odd()
            

