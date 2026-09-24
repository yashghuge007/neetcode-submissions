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
            elif len(stk) == 0 or stk.pop() != pairs[c]:
                return False
        return True if len(stk)==0 else False