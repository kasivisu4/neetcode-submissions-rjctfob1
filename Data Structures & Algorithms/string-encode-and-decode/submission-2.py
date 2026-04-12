import struct
class Solution:

    def encode(self, strs: List[str]) -> str:
        # Pattern : len(s) + "#" + s
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        # 5#abcde
        res = []
        i = 0
        while i < len(s):
            curr_i = i
            while curr_i < len(s) and s[curr_i] != "#":
                curr_i += 1
            
            length = int(s[i:curr_i])

            res.append(s[curr_i + 1: curr_i + 1 + length])
            i = curr_i + 1 + length
        return res