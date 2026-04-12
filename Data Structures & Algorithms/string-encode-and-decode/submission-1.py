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
        curr_i = 0
        while curr_i < len(s):
            length = ""
            while s[curr_i] != "#":
                length += s[curr_i]
                curr_i += 1
            length = int(length)
            curr_i += 1
            part = ""
            while length > 0:
                part += s[curr_i]
                curr_i += 1
                length -= 1
            res.append(part)
        return res