class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1
        temp = s.lower()

        while l<r:
            if not temp[l].isalnum():
                l+=1
            elif not temp[r].isalnum():
                r-=1
            elif temp[l]!=temp[r]:
                return False
            else:
                l+=1
                r-=1
        return True