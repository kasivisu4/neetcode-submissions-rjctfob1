class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def find_freq(s):
            counter = [0] * 26
            for ch in s:
                pos = ord(ch) - ord('a')
                counter[pos] += 1
            return tuple(counter)
        
        res = collections.defaultdict(list)
        for s in strs:
            freq = find_freq(s)
            res[freq].append(s)
        return list(res.values())