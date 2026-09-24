class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stk =[]
        for c in s:
            if c in pairs.values():
                stk.append(c)
            elif not stk or stk.pop() != pairs[c]:
                return False
        return len(stk)==0