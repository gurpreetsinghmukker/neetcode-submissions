from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s)%2== 0:
            return False
        o_set = {
            '(':')', 
            '{':'}' ,
            '[':']'
        }
        c_set = {
            ')':'(', 
            '}':'{', 
            ']':'['
        }
        d = deque()
        for c in s:
            if c in o_set:
                d.append(c)
            if c in c_set:
                if len(d) == 0:
                    return False
                if not o_set[d.pop()] == c:
                    return False
        if len(d)>0:
            return False
        return True
