class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r= len(people)-1
        ans = 0
        
        while l<=r:
            if people[r]+people[l]<=limit:
                l+=1
                r-=1
            else:
                r-=1
            ans+=1
        return ans