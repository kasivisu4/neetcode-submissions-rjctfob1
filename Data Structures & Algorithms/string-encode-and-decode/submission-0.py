class Solution:

    def encode(self, strs: List[str]) -> str:
        # Pattern : len(s) + "#" + s
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # 5#abcde
        # start = 2
        # end = 7
        decoded_strs = []
        i = 0
        while i < len(s):
            delim = s.find("#", i)
            str_length =  int(s[i:delim])
            str_start = delim + 1
            str_end = str_start + str_length
            decoded_strs.append(s[str_start: str_end])
            i = str_end
        return decoded_strs