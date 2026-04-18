
class Solution:
    def isValid(self, s: str) -> bool:
        char_mappings = {
        '(':')',
        '{':'}', 
        '[':']'
        }
        keys = set(char_mappings)
        deq = deque()
        for ch in s:
            if ch in keys:
                deq.append(ch)
            else:
                if not deq:
                    return False
                last_elem = deq.pop()
                if ch != char_mappings[last_elem]:
                    return False     
        return True if not deq else False