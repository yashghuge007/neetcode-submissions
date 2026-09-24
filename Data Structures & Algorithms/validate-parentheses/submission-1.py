class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stk = []
        for c in s:
            if c in pairs.values():
                stk.append(c)
            else:
                if not stk or stk[-1]!=pairs[c]:
                    return False
                stk.pop()
        return len(stk)==0